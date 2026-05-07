"""HDR data visualization for the browser, from numpy arrays.

Renders 2D numpy arrays as PQ Rec2020-tagged PNGs that HDR-capable browsers
composite in extended dynamic range. Includes a small library of HDR-aware
colormaps and an ``imshow``-style helper.

Tested in Chromium-based browsers (Chrome, Brave, Edge) on macOS with HDR
displays. On non-HDR displays the PNG renders correctly in standard range.

Quick start::

    import numpy as np
    from hdrviz import imshow

    data = np.random.RandomState(0).rand(400, 600)
    widget = imshow(data, cmap="inferno-hdr", peak_nits=4000)
    widget   # display in Jupyter / marimo

To toggle HDR rendering on or off (same pixels), set CSS
``dynamic-range-limit: standard`` on the ``<img>`` element. The :class:`HDRImage`
widget exposes a ``clamp_to_sdr`` traitlet for this.
"""

# MIT License
#
# Copyright (c) 2026 Konstantin Taletskiy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

from __future__ import annotations

import base64
import io
import struct
import zlib

import anywidget
import colour
import numpy as np
import traitlets
from PIL import Image

__version__ = "0.2.1"
__all__ = [
    "DEFAULT_PQ_REC2020_ICC",
    "COLORMAP_LIBRARY",
    "extract_icc_from_png",
    "linear_nits_to_pq",
    "encode_hdr_png",
    "to_data_url",
    "hdr_colormap",
    "imshow",
    "hdr_imshow",  # deprecated alias for imshow, removed in 0.2.0
    "HDRImage",
]


# Bundled ICC profile: "Rec2020 Gamut with PQ Transfer", 9176 bytes raw.
# This is the standard color space for HDR10 / HDR PNG / UltraHDR carriers.
# Pass icc_profile=... to encode_hdr_png to use a different one (e.g. HLG).
_DEFAULT_ICC_B64 = (
    "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"
    "EzlzMy5EEC+AAEzNKvcAAEzNKvcIfkzNKvcSSkzNKvcdq0zNKvcq90zNKvc6jkzNKvdMzUWKJjlZ"
    "mj2tIUZmZjWyHHBzMy5EGBeAAEzNOo4AAEzNOo4IfkzNOo4SSkzNOo4dq0zNOo4q90zNOo46jkzN"
    "Oo5MzUWKNIVZmj2tLhxmZjWyJ75zMy5EIe2AAEzNTM0AAEzNTM0IfkzNTM0SSkzNTM0dq0zNTM0q"
    "90zNTM06jkzNTM1MzUWKRYpZmj2tPa1mZjWyNbJzMy5ELkSAAEWKWZoAAEWKWZoHa0WKWZoQD0WK"
    "WZoaNkWKWZomOUWKWZo0hUWKWZpFikWKWZpZmj2tUGhmZjWyRtlzMy5EPb2AAD2tZmYAAD2tZmYG"
    "Vz2tZmYNyz2tZmYWpz2tZmYhRj2tZmYuHD2tZmY9rT2tZmZQaD2tZmZmZjWyW31zMy5EUMqAADWy"
    "czMAADWyczMFUzWyczMLpDWyczMTOTWyczMccDWyczMnvjWyczM1sjWyczNG2TWyczNbfTWyczNz"
    "My5EZz6AAC5EgAAAAC5EgAAEcC5EgAAJwC5EgAAQLy5EgAAYFy5EgAAh7S5EgAAuRC5EgAA9vS5E"
    "gABQyi5EgABnPi5EgACAAFmaAAAAAFmaAAAHa1maAAAQD1maAAAaNlmaAAAmOVmaAAA0hVmaAABF"
    "ilmaAABZmlBoAABmZkbZAABzMz29AACAAFmaB2sAAFmaB2sHa1maB2sQD1maB2saNlmaB2smOVma"
    "B2s0hVmaB2tFilmaB2tZmlBoBldmZkbZBVNzMz29BHCAAFmaEA8AAFmaEA8Ha1maEA8QD1maEA8a"
    "NlmaEA8mOVmaEA80hVmaEA9FilmaEA9ZmlBoDctmZkbZC6RzMz29CcCAAFmaGjYAAFmaGjYHa1ma"
    "GjYQD1maGjYaNlmaGjYmOVmaGjY0hVmaGjZFilmaGjZZmlBoFqdmZkbZEzlzMz29EC+AAFmaJjkA"
    "AFmaJjkHa1maJjkQD1maJjkaNlmaJjkmOVmaJjk0hVmaJjlFilmaJjlZmlBoIUZmZkbZHHBzMz29"
    "GBeAAFmaNIUAAFmaNIUHa1maNIUQD1maNIUaNlmaNIUmOVmaNIU0hVmaNIVFilmaNIVZmlBoLhxm"
    "ZkbZJ75zMz29Ie2AAFmaRYoAAFmaRYoHa1maRYoQD1maRYoaNlmaRYomOVmaRYo0hVmaRYpFilma"
    "RYpZmlBoPa1mZkbZNbJzMz29LkSAAFmaWZoAAFmaWZoHa1maWZoQD1maWZoaNlmaWZomOVmaWZo0"
    "hVmaWZpFilmaWZpZmlBoUGhmZkbZRtlzMz29Pb2AAFBoZmYAAFBoZmYGV1BoZmYNy1BoZmYWp1Bo"
    "ZmYhRlBoZmYuHFBoZmY9rVBoZmZQaFBoZmZmZkbZW31zMz29UMqAAEbZczMAAEbZczMFU0bZczML"
    "pEbZczMTOUbZczMccEbZczMnvkbZczM1skbZczNG2UbZczNbfUbZczNzMz29Zz6AAD29gAAAAD29"
    "gAAEcD29gAAJwD29gAAQLz29gAAYFz29gAAh7T29gAAuRD29gAA9vT29gABQyj29gABnPj29gACA"
    "AGZmAAAAAGZmAAAGV2ZmAAANy2ZmAAAWp2ZmAAAhRmZmAAAuHGZmAAA9rWZmAABQaGZmAABmZlt9"
    "AABzM1DKAACAAGZmBlcAAGZmBlcGV2ZmBlcNy2ZmBlcWp2ZmBlchRmZmBlcuHGZmBlc9rWZmBldQ"
    "aGZmBldmZlt9BVNzM1DKBHCAAGZmDcsAAGZmDcsGV2ZmDcsNy2ZmDcsWp2ZmDcshRmZmDcsuHGZm"
    "Dcs9rWZmDctQaGZmDctmZlt9C6RzM1DKCcCAAGZmFqcAAGZmFqcGV2ZmFqcNy2ZmFqcWp2ZmFqch"
    "RmZmFqcuHGZmFqc9rWZmFqdQaGZmFqdmZlt9EzlzM1DKEC+AAGZmIUYAAGZmIUYGV2ZmIUYNy2Zm"
    "IUYWp2ZmIUYhRmZmIUYuHGZmIUY9rWZmIUZQaGZmIUZmZlt9HHBzM1DKGBeAAGZmLhwAAGZmLhwG"
    "V2ZmLhwNy2ZmLhwWp2ZmLhwhRmZmLhwuHGZmLhw9rWZmLhxQaGZmLhxmZlt9J75zM1DKIe2AAGZm"
    "Pa0AAGZmPa0GV2ZmPa0Ny2ZmPa0Wp2ZmPa0hRmZmPa0uHGZmPa09rWZmPa1QaGZmPa1mZlt9NbJz"
    "M1DKLkSAAGZmUGgAAGZmUGgGV2ZmUGgNy2ZmUGgWp2ZmUGghRmZmUGguHGZmUGg9rWZmUGhQaGZm"
    "UGhmZlt9RtlzM1DKPb2AAGZmZmYAAGZmZmYGV2ZmZmYNy2ZmZmYWp2ZmZmYhRmZmZmYuHGZmZmY9"
    "rWZmZmZQaGZmZmZmZlt9W31zM1DKUMqAAFt9czMAAFt9czMFU1t9czMLpFt9czMTOVt9czMccFt9"
    "czMnvlt9czM1slt9czNG2Vt9czNbfVt9czNzM1DKZz6AAFDKgAAAAFDKgAAEcFDKgAAJwFDKgAAQ"
    "L1DKgAAYF1DKgAAh7VDKgAAuRFDKgAA9vVDKgABQylDKgABnPlDKgACAAHMzAAAAAHMzAAAFU3Mz"
    "AAALpHMzAAATOXMzAAAccHMzAAAnvnMzAAA1snMzAABG2XMzAABbfXMzAABzM2c+AACAAHMzBVMA"
    "AHMzBVMFU3MzBVMLpHMzBVMTOXMzBVMccHMzBVMnvnMzBVM1snMzBVNG2XMzBVNbfXMzBVNzM2c+"
    "BHCAAHMzC6QAAHMzC6QFU3MzC6QLpHMzC6QTOXMzC6QccHMzC6QnvnMzC6Q1snMzC6RG2XMzC6Rb"
    "fXMzC6RzM2c+CcCAAHMzEzkAAHMzEzkFU3MzEzkLpHMzEzkTOXMzEzkccHMzEzknvnMzEzk1snMz"
    "EzlG2XMzEzlbfXMzEzlzM2c+EC+AAHMzHHAAAHMzHHAFU3MzHHALpHMzHHATOXMzHHAccHMzHHAn"
    "vnMzHHA1snMzHHBG2XMzHHBbfXMzHHBzM2c+GBeAAHMzJ74AAHMzJ74FU3MzJ74LpHMzJ74TOXMz"
    "J74ccHMzJ74nvnMzJ741snMzJ75G2XMzJ75bfXMzJ75zM2c+Ie2AAHMzNbIAAHMzNbIFU3MzNbIL"
    "pHMzNbITOXMzNbIccHMzNbInvnMzNbI1snMzNbJG2XMzNbJbfXMzNbJzM2c+LkSAAHMzRtkAAHMz"
    "RtkFU3MzRtkLpHMzRtkTOXMzRtkccHMzRtknvnMzRtk1snMzRtlG2XMzRtlbfXMzRtlzM2c+Pb2A"
    "AHMzW30AAHMzW30FU3MzW30LpHMzW30TOXMzW30ccHMzW30nvnMzW301snMzW31G2XMzW31bfXMz"
    "W31zM2c+UMqAAHMzczMAAHMzczMFU3MzczMLpHMzczMTOXMzczMccHMzczMnvnMzczM1snMzczNG"
    "2XMzczNbfXMzczNzM2c+Zz6AAGc+gAAAAGc+gAAEcGc+gAAJwGc+gAAQL2c+gAAYF2c+gAAh7Wc+"
    "gAAuRGc+gAA9vWc+gABQymc+gABnPmc+gACAAIAAAAAAAIAAAAAEcIAAAAAJwIAAAAAQL4AAAAAY"
    "F4AAAAAh7YAAAAAuRIAAAAA9vYAAAABQyoAAAABnPoAAAACAAIAABHAAAIAABHAEcIAABHAJwIAA"
    "BHAQL4AABHAYF4AABHAh7YAABHAuRIAABHA9vYAABHBQyoAABHBnPoAABHCAAIAACcAAAIAACcAE"
    "cIAACcAJwIAACcAQL4AACcAYF4AACcAh7YAACcAuRIAACcA9vYAACcBQyoAACcBnPoAACcCAAIAA"
    "EC8AAIAAEC8EcIAAEC8JwIAAEC8QL4AAEC8YF4AAEC8h7YAAEC8uRIAAEC89vYAAEC9QyoAAEC9n"
    "PoAAEC+AAIAAGBcAAIAAGBcEcIAAGBcJwIAAGBcQL4AAGBcYF4AAGBch7YAAGBcuRIAAGBc9vYAA"
    "GBdQyoAAGBdnPoAAGBeAAIAAIe0AAIAAIe0EcIAAIe0JwIAAIe0QL4AAIe0YF4AAIe0h7YAAIe0u"
    "RIAAIe09vYAAIe1QyoAAIe1nPoAAIe2AAIAALkQAAIAALkQEcIAALkQJwIAALkQQL4AALkQYF4AA"
    "LkQh7YAALkQuRIAALkQ9vYAALkRQyoAALkRnPoAALkSAAIAAPb0AAIAAPb0EcIAAPb0JwIAAPb0Q"
    "L4AAPb0YF4AAPb0h7YAAPb0uRIAAPb09vYAAPb1QyoAAPb1nPoAAPb2AAIAAUMoAAIAAUMoEcIAA"
    "UMoJwIAAUMoQL4AAUMoYF4AAUMoh7YAAUMouRIAAUMo9vYAAUMpQyoAAUMpnPoAAUMqAAIAAZz4A"
    "AIAAZz4EcIAAZz4JwIAAZz4QL4AAZz4YF4AAZz4h7YAAZz4uRIAAZz49vYAAZz5QyoAAZz5nPoAA"
    "Zz6AAIAAgAAAAIAAgAAEcIAAgAAJwIAAgAAQL4AAgAAYF4AAgAAh7YAAgAAuRIAAgAA9vYAAgABQ"
    "yoAAgABnPoAAgACAAAAAY3VydgAAAAAAAABBAAAAAgAHABEAIAA4AFgAhAC/AQoBaQHhAnYDLQQK"
    "BRUGVAfPCY8LnA4DEMQT+hefG8UgZSWeK3cx5DjQQIRItlF+WrdkfG56eNuDio5UmUOkSK8yukPF"
    "VNBn27HnHPK9/t7//////////////////////////////////////////wAAY3VydgAAAAAAAABB"
    "AAAAAgAHABEAIAA4AFgAhAC/AQoBaQHhAnYDLQQKBRUGVAfPCY8LnA4DEMQT+hefG8UgZSWeK3cx"
    "5DjQQIRItlF+WrdkfG56eNuDio5UmUOkSK8yukPFVNBn27HnHPK9/t7/////////////////////"
    "/////////////////////wAAY3VydgAAAAAAAABBAAAAAgAHABEAIAA4AFgAhAC/AQoBaQHhAnYD"
    "LQQKBRUGVAfPCY8LnA4DEMQT+hefG8UgZSWeK3cx5DjQQIRItlF+WrdkfG56eNuDio5UmUOkSK8y"
    "ukPFVNBn27HnHPK9/t7//////////////////////////////////////////wAAAACsaAAAKmkA"
    "ACAHAABHbwAArOMAAAuu////gQAAB60AAMwTAAAAAAAAAAAAAAAAcGFyYQAAAAAAAAAAAAEAAHBh"
    "cmEAAAAAAAAAAAABAABwYXJhAAAAAAAAAAAAAQAAbUJBIAAAAAADAwAAAAAAIAAAAAAAAAAAAAAA"
    "AAAAAABwYXJhAAAAAAAAAAAAAQAAcGFyYQAAAAAAAAAAAAEAAHBhcmEAAAAAAAAAAAABAABtbHVj"
    "AAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADY="
)
DEFAULT_PQ_REC2020_ICC: bytes = base64.b64decode("".join(_DEFAULT_ICC_B64))


def extract_icc_from_png(png_bytes: bytes) -> bytes | None:
    """Return the decompressed ICC profile from a PNG's iCCP chunk, or ``None``."""
    if png_bytes[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    i = 8
    while i < len(png_bytes):
        length = struct.unpack(">I", png_bytes[i : i + 4])[0]
        ctype = png_bytes[i + 4 : i + 8]
        payload = png_bytes[i + 8 : i + 8 + length]
        if ctype == b"iCCP":
            nul = payload.index(b"\x00")
            return zlib.decompress(payload[nul + 2 :])
        if ctype == b"IEND":
            return None
        i += 8 + length + 4
    return None


def linear_nits_to_pq(rgb_nits: np.ndarray) -> np.ndarray:
    """Inverse PQ EOTF (SMPTE ST 2084).

    Args:
        rgb_nits: Linear luminance in cd/m^2 (nits). Any shape; clipped to [0, 10000].

    Returns:
        PQ-encoded code values in [0, 1], same shape as input.
    """
    return colour.models.eotf_inverse_ST2084(np.clip(rgb_nits, 0.0, 10000.0))


def encode_hdr_png(
    rgb_nits: np.ndarray,
    icc_profile: bytes = DEFAULT_PQ_REC2020_ICC,
) -> bytes:
    """Encode a (H, W, 3) array of linear-light RGB nits as a PQ-tagged PNG.

    The returned bytes are an 8-bit RGB PNG with an embedded ICC profile (Rec2020
    primaries, PQ transfer by default). HDR-capable browsers will composite this
    in extended dynamic range; SDR browsers render it tone-mapped.
    """
    pq = linear_nits_to_pq(rgb_nits)
    pq8 = np.clip(pq * 255.0 + 0.5, 0, 255).astype(np.uint8)
    img = Image.fromarray(pq8, mode="RGB")
    buf = io.BytesIO()
    img.save(buf, format="PNG", icc_profile=icc_profile)
    return buf.getvalue()


def to_data_url(png_bytes: bytes) -> str:
    """Wrap PNG bytes in a ``data:`` URL suitable for an ``<img src=...>``."""
    return "data:image/png;base64," + base64.b64encode(png_bytes).decode("ascii")


# HDR-aware colormaps. (norm, R, G, B) control points; channel values can
# exceed 1.0 to push above ``peak_nits`` — that is how the visible glow happens.
COLORMAP_LIBRARY: dict[str, np.ndarray] = {
    "fire-purple": np.array([
        [0.00, 0.000, 0.000, 0.000],
        [0.05, 0.020, 0.000, 0.060],
        [0.20, 0.080, 0.000, 0.180],
        [0.40, 0.350, 0.020, 0.280],
        [0.55, 0.700, 0.150, 0.150],
        [0.70, 0.950, 0.450, 0.080],
        [0.85, 1.000, 0.850, 0.250],
        [0.95, 1.000, 1.000, 0.700],
        [1.00, 1.000, 1.000, 0.950],
    ]),
    "ice": np.array([
        [0.00, 0.000, 0.000, 0.000],
        [0.10, 0.000, 0.020, 0.080],
        [0.30, 0.020, 0.150, 0.400],
        [0.55, 0.100, 0.500, 0.900],
        [0.75, 0.500, 0.900, 1.000],
        [0.90, 1.000, 1.100, 1.150],
        [1.00, 1.300, 1.300, 1.250],
    ]),
    "twilight-burst": np.array([
        [0.00, 0.000, 0.000, 0.000],
        [0.10, 0.080, 0.000, 0.150],
        [0.30, 0.400, 0.040, 0.500],
        [0.55, 0.900, 0.300, 0.300],
        [0.75, 1.100, 0.700, 0.150],
        [0.90, 1.250, 1.100, 0.450],
        [1.00, 1.300, 1.300, 1.000],
    ]),
    "matrix-green": np.array([
        [0.00, 0.000, 0.000, 0.000],
        [0.20, 0.000, 0.080, 0.020],
        [0.50, 0.040, 0.500, 0.080],
        [0.75, 0.150, 1.000, 0.250],
        [0.90, 0.500, 1.300, 0.500],
        [1.00, 1.000, 1.500, 1.000],
    ]),
    "ember": np.array([
        [0.00, 0.000, 0.000, 0.000],
        [0.30, 0.300, 0.020, 0.000],
        [0.55, 0.700, 0.080, 0.000],
        [0.75, 1.000, 0.350, 0.020],
        [0.88, 1.150, 0.700, 0.150],
        [0.97, 1.250, 1.100, 0.500],
        [1.00, 1.300, 1.250, 0.900],
    ]),
    "viridis-hdr": np.array([
        [0.00, 0.267, 0.005, 0.329],
        [0.20, 0.281, 0.165, 0.476],
        [0.40, 0.254, 0.265, 0.530],
        [0.60, 0.207, 0.372, 0.553],
        [0.80, 0.435, 0.643, 0.422],
        [0.90, 0.770, 0.902, 0.245],
        [0.97, 1.050, 1.150, 0.450],
        [1.00, 1.250, 1.350, 0.700],
    ]),
    "inferno-hdr": np.array([
        [0.00, 0.001, 0.000, 0.014],
        [0.20, 0.218, 0.041, 0.378],
        [0.40, 0.580, 0.149, 0.404],
        [0.60, 0.866, 0.317, 0.226],
        [0.75, 0.988, 0.557, 0.094],
        [0.88, 1.000, 0.860, 0.250],
        [0.97, 1.150, 1.150, 0.620],
        [1.00, 1.300, 1.300, 0.950],
    ]),
}


def hdr_colormap(
    norm: np.ndarray,
    cmap_name: str = "fire-purple",
    peak_nits: float = 4000.0,
) -> np.ndarray:
    """Map normalized [0, 1] values to RGB linear nits via a named colormap.

    Args:
        norm: Array of values in [0, 1]. Any shape.
        cmap_name: Key from :data:`COLORMAP_LIBRARY`.
        peak_nits: Linear-light scale. A colormap channel value of 1.0 maps to
            this many nits; values above 1.0 push proportionally higher.

    Returns:
        An array shaped ``norm.shape + (3,)`` in linear cd/m^2 (nits).
    """
    pts = COLORMAP_LIBRARY[cmap_name]
    R = np.interp(norm, pts[:, 0], pts[:, 1]) * peak_nits
    G = np.interp(norm, pts[:, 0], pts[:, 2]) * peak_nits
    B = np.interp(norm, pts[:, 0], pts[:, 3]) * peak_nits
    return np.stack([R, G, B], axis=-1)


def imshow(
    arr: np.ndarray,
    cmap: str = "fire-purple",
    peak_nits: float = 4000.0,
    normalize: str = "linear",
    vmin: float | None = None,
    vmax: float | None = None,
    clip_percentile: tuple[float, float] | None = None,
    interior_mask: np.ndarray | None = None,
    label: str = "",
    display_width: str = "100%",
    max_height_px: int = 360,
    image_rendering: str = "auto",
) -> "HDRImage":
    """Render a 2D numpy array as an HDR image. Returns an :class:`HDRImage` widget.

    Conceptually a tiny ``matplotlib.imshow`` analogue, but pixels are PQ Rec2020-
    encoded so a capable browser composites them in extended dynamic range.

    Args:
        arr: ``(H, W)`` float-like array. ``NaN``/``Inf`` values are treated as
            interior (rendered black).
        cmap: Key from :data:`COLORMAP_LIBRARY`.
        peak_nits: Luminance scale; cmap channel value 1.0 maps to this.
        normalize: How to map values to [0, 1]:

            - ``"linear"``: ``(v - vmin) / (vmax - vmin)``
            - ``"log"``: ``log1p((v - vmin) + tiny) / log1p((vmax - vmin) + tiny)``
            - ``"sqrt"``: square root of linear

            Default is linear; for HDR data viz, prefer linear or pre-stretch your
            data with ``np.log1p``/``np.sqrt`` rather than reaching for log here.
        vmin, vmax: Explicit data range. If unset, derived from data.
        clip_percentile: Optional ``(lo, hi)`` percentile pair to derive
            ``vmin``/``vmax`` robustly (e.g. ``(0.5, 99.5)`` to ignore outliers).
        interior_mask: Optional bool array same shape as ``arr``; ``True`` pixels
            render as black. Useful for fractal interiors, NaN regions, etc.
        label: Caption shown above the rendered image in the widget.
        display_width: CSS ``width`` for the rendered ``<img>``. Default ``"100%"``
            (fills the parent column, browser scales the PNG to fit). Use
            ``"auto"`` to render at intrinsic pixel size, or e.g. ``"600px"`` /
            ``"50vw"`` for an explicit size.
        max_height_px: Cap on rendered height in pixels. Default 360 keeps
            tall outputs from triggering the host notebook's internal scrollbar.
            Set to ``0`` to disable the cap.
        image_rendering: CSS ``image-rendering`` value, controlling how the
            browser interpolates when scaling. Default ``"auto"`` (smooth /
            bilinear). Use ``"pixelated"`` to preserve hard pixel edges (good
            when each pixel is meaningful, e.g. raw scientific imagery), or
            ``"crisp-edges"`` for a middle ground.
    """
    if arr.ndim != 2:
        raise ValueError(f"hdr_imshow expects a 2D array, got shape {arr.shape}")
    if cmap not in COLORMAP_LIBRARY:
        raise ValueError(
            f"unknown cmap {cmap!r}; choose from {list(COLORMAP_LIBRARY)}"
        )

    A = np.asarray(arr, dtype=np.float64).copy()
    finite = np.isfinite(A)
    if interior_mask is None:
        interior_mask = np.zeros_like(A, dtype=bool)
    else:
        interior_mask = np.asarray(interior_mask, dtype=bool)
        if interior_mask.shape != A.shape:
            raise ValueError("interior_mask must match arr shape")

    treat_as_interior = interior_mask | ~finite
    A[~finite] = 0.0

    sample = A[finite & ~interior_mask]
    if sample.size == 0:
        vmin_eff = 0.0 if vmin is None else float(vmin)
        vmax_eff = 1.0 if vmax is None else float(vmax)
    elif clip_percentile is not None:
        lo, hi = clip_percentile
        vmin_eff = float(np.percentile(sample, lo)) if vmin is None else float(vmin)
        vmax_eff = float(np.percentile(sample, hi)) if vmax is None else float(vmax)
    else:
        vmin_eff = float(sample.min()) if vmin is None else float(vmin)
        vmax_eff = float(sample.max()) if vmax is None else float(vmax)

    if not np.isfinite(vmin_eff) or not np.isfinite(vmax_eff) or vmax_eff <= vmin_eff:
        vmin_eff, vmax_eff = 0.0, 1.0

    A_clipped = np.clip(A, vmin_eff, vmax_eff)
    span = vmax_eff - vmin_eff

    if normalize == "linear":
        norm = (A_clipped - vmin_eff) / span
    elif normalize == "log":
        eps = 1e-9 * span
        norm = np.log1p(A_clipped - vmin_eff + eps) / np.log1p(span + eps)
    elif normalize == "sqrt":
        norm = np.sqrt((A_clipped - vmin_eff) / span)
    else:
        raise ValueError(f"unknown normalize={normalize!r}")

    norm = np.clip(norm, 0.0, 1.0)
    norm[treat_as_interior] = 0.0

    rgb_nits = hdr_colormap(norm, cmap_name=cmap, peak_nits=peak_nits)
    rgb_nits[treat_as_interior] = 0.0

    png = encode_hdr_png(rgb_nits)
    return HDRImage(
        image_data_url=to_data_url(png),
        label=label,
        display_width=display_width,
        max_height_px=max_height_px,
        image_rendering=image_rendering,
    )



def hdr_imshow(*args, **kwargs):
    """Deprecated alias for :func:`imshow`. Will be removed in 0.2.0.

    Emits :class:`DeprecationWarning` (silent by default in CPython; surface
    via ``python -W error::DeprecationWarning`` or pytest).
    """
    import warnings
    warnings.warn(
        "hdr_imshow is deprecated, use imshow instead. "
        "This alias will be removed in v0.2.0.",
        DeprecationWarning,
        stacklevel=2,
    )
    return imshow(*args, **kwargs)


class HDRImage(anywidget.AnyWidget):
    """Anywidget that displays an HDR-encoded image with a CSS-clamp toggle.

    Setting ``clamp_to_sdr=True`` applies ``dynamic-range-limit: standard`` to
    the ``<img>``, making the same pixels render in SDR. This is the cleanest
    A/B for showing HDR's contribution: same image, same display, one CSS
    property apart.

    Sizing is controlled by three traits: ``display_width`` (any CSS width
    value; default ``"100%"`` fills the parent column), ``max_height_px``
    (caps the rendered image height; default 360 px keeps tall outputs from
    triggering the host notebook's internal scrollbar; set to ``0`` to disable
    the cap), and ``image_rendering`` (CSS ``image-rendering``; default
    ``"auto"`` smooth, ``"pixelated"`` for raw scientific data where hard
    pixel edges should be preserved).
    """

    image_data_url = traitlets.Unicode("").tag(sync=True)
    label = traitlets.Unicode("").tag(sync=True)
    clamp_to_sdr = traitlets.Bool(False).tag(sync=True)
    display_width = traitlets.Unicode("100%").tag(sync=True)
    max_height_px = traitlets.Int(360).tag(sync=True)
    image_rendering = traitlets.Unicode("auto").tag(sync=True)

    _esm = r'''
    function render({ model, el }) {
      function rebuild() {
        const url = model.get("image_data_url");
        const label = model.get("label");
        const clamp = model.get("clamp_to_sdr");
        const dw = model.get("display_width") || "100%";
        const ir = model.get("image_rendering") || "auto";
        const mh = Number(model.get("max_height_px")) || 0;
        const imgStyle = [
          `width:${dw}`,
          "height:auto",
          mh > 0 ? `max-height:${mh}px` : "",
          mh > 0 ? "object-fit:contain" : "",
          `image-rendering:${ir}`,
          clamp ? "dynamic-range-limit:standard" : "",
        ].filter(Boolean).join("; ");
        el.innerHTML = `
          <style>
            .hi-card { font-family: system-ui, -apple-system, sans-serif; color: inherit;
              border: 1px solid color-mix(in srgb, currentColor 20%, transparent);
              border-radius: 12px; padding: 12px; display: grid; gap: 8px; }
            .hi-label { font-size: 12px; opacity: 0.8; display:flex; gap:8px; align-items:center; }
            .hi-label .tag { font-family: ui-monospace, SFMono-Regular, monospace; font-size: 11px;
              padding: 2px 6px; border-radius: 4px;
              background: color-mix(in srgb, currentColor 10%, transparent); }
            .hi-img-wrap { background:#000; border-radius:8px; overflow:hidden; display:flex;
              justify-content:center; align-items:center; }
            .hi-img-wrap img { max-width:100%; display:block; }
          </style>
          <div class="hi-card">
            <div class="hi-label">${label}
              <span class="tag">dynamic-range-limit: ${clamp ? "standard" : "no-limit"}</span>
            </div>
            <div class="hi-img-wrap">
              <img src="${url}" alt="${label}" style="${imgStyle}">
            </div>
          </div>
        `;
      }
      rebuild();
      model.on("change:clamp_to_sdr", rebuild);
      model.on("change:image_data_url", rebuild);
      model.on("change:label", rebuild);
      model.on("change:display_width", rebuild);
      model.on("change:max_height_px", rebuild);
      model.on("change:image_rendering", rebuild);
    }
    export default { render };
    '''
