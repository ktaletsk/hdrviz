"""Smoke tests for hdrviz."""
import base64
import warnings

import numpy as np
import pytest

from hdrviz import (
    COLORMAP_LIBRARY,
    DEFAULT_PQ_REC2020_ICC,
    HDRImage,
    encode_hdr_png,
    extract_icc_from_png,
    hdr_colormap,
    hdr_imshow,
    imshow,
    linear_nits_to_pq,
    to_data_url,
)


def test_imports():
    """All public symbols are importable and of expected types."""
    assert callable(imshow)
    assert callable(hdr_imshow)  # deprecated alias
    assert callable(encode_hdr_png)
    assert callable(linear_nits_to_pq)
    assert callable(to_data_url)
    assert callable(extract_icc_from_png)
    assert callable(hdr_colormap)
    assert isinstance(DEFAULT_PQ_REC2020_ICC, bytes)
    assert len(DEFAULT_PQ_REC2020_ICC) > 1000
    assert isinstance(COLORMAP_LIBRARY, dict)
    assert "fire-purple" in COLORMAP_LIBRARY
    assert "inferno-hdr" in COLORMAP_LIBRARY


def test_pq_encoding_monotonic_and_bounded():
    nits = np.array([0.0, 100.0, 1000.0, 4000.0, 10000.0])
    pq = linear_nits_to_pq(nits)
    assert pq.shape == nits.shape
    assert (pq >= 0.0).all() and (pq <= 1.0).all()
    assert (np.diff(pq) > 0).all()
    # 100 nits is roughly SDR diffuse white -> ~half of PQ range
    assert 0.4 < pq[1] < 0.6
    assert pq[-1] == pytest.approx(1.0, abs=1e-6)


def test_imshow_returns_widget_with_data_url():
    arr = np.random.RandomState(0).rand(50, 80)
    widget = imshow(arr, cmap="inferno-hdr", peak_nits=4000)
    assert isinstance(widget, HDRImage)
    assert widget.image_data_url.startswith("data:image/png;base64,")
    png_bytes = base64.b64decode(widget.image_data_url.split(",", 1)[1])
    assert png_bytes.startswith(b"\x89PNG\r\n\x1a\n")


def test_display_width_and_image_rendering_traits():
    """v0.2.0: HDRImage exposes display_width + image_rendering, plumbed through imshow."""
    # Defaults
    bare = HDRImage()
    assert bare.display_width == "100%"
    assert bare.image_rendering == "auto"

    # imshow forwards the kwargs
    arr = np.zeros((20, 30))
    w = imshow(arr, display_width="600px", image_rendering="pixelated")
    assert w.display_width == "600px"
    assert w.image_rendering == "pixelated"


def test_imshow_validates_inputs():
    with pytest.raises(ValueError, match="2D array"):
        imshow(np.zeros(10))
    with pytest.raises(ValueError, match="unknown cmap"):
        imshow(np.zeros((10, 10)), cmap="not-a-real-cmap")


def test_extract_icc_roundtrip():
    """encode_hdr_png embeds DEFAULT_PQ_REC2020_ICC; extract_icc_from_png recovers it."""
    arr = np.full((10, 10, 3), 100.0)
    png = encode_hdr_png(arr)
    recovered = extract_icc_from_png(png)
    assert recovered == DEFAULT_PQ_REC2020_ICC


def test_hdr_colormap_shape_and_units():
    """hdr_colormap produces an (..., 3) array in nits."""
    norm = np.linspace(0, 1, 100)
    rgb = hdr_colormap(norm, cmap_name="ember", peak_nits=4000.0)
    assert rgb.shape == (100, 3)
    # Top of colormap should exceed peak_nits in at least one channel (HDR boost)
    assert rgb.max() > 4000.0
    # Bottom should be near zero
    assert rgb[0].max() < 200.0


def test_hdr_imshow_alias_emits_deprecation_warning():
    """hdr_imshow still works but emits DeprecationWarning."""
    arr = np.zeros((10, 10))
    with warnings.catch_warnings(record=True) as recorded:
        warnings.simplefilter("always")
        widget = hdr_imshow(arr)
    assert isinstance(widget, HDRImage)
    assert any(
        issubclass(w.category, DeprecationWarning)
        and "hdr_imshow is deprecated" in str(w.message)
        for w in recorded
    )
