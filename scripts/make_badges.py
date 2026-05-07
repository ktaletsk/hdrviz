# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "hdrviz",
#     "numpy",
#     "pillow",
# ]
# ///
"""Pre-render the HDR/SDR metal badges shown in the notebook's HeadroomDetector.

Run from the project root:

    uv run scripts/make_badges.py

Writes ``assets/hdr_badge.png`` and ``assets/sdr_badge.png``. The notebook
fetches them via ``fetch_asset()`` so they're portable to molab and other
sandboxes that don't have macOS/Windows system fonts available.

Background: the badges use a metallic gradient + bold text rendered through
hdrviz's PQ Rec2020 pipeline (mode='gold' pushes the top of the gradient above
SDR white at ~5000 nits so the plate genuinely glows on HDR displays;
mode='silver' stays within SDR). Pre-rendering once on a machine with good
fonts is more reliable than generating on every notebook load.
"""

from __future__ import annotations

import pathlib
import sys

import numpy as np
from hdrviz import encode_hdr_png
from PIL import Image, ImageDraw, ImageFont


def make_metal_badge_png(
    text: str = "HDR",
    *,
    width: int = 480,
    height: int = 130,
    peak_nits: float = 5000.0,
    mode: str = "gold",
) -> bytes:
    """Render a metallic plate badge with bold text as a PQ Rec2020 PNG.

    ``mode='gold'`` boosts the top of the gradient above SDR white (~peak_nits
    = 5000) so the plate genuinely glows on HDR displays. ``mode='silver'``
    stays within SDR.
    """
    H, W = height, width

    if mode == "gold":
        pts   = np.array([0.00, 0.20, 0.55, 1.00])
        R_pts = np.array([1.65, 1.30, 0.85, 0.42])
        G_pts = np.array([1.05, 0.72, 0.38, 0.18])
        B_pts = np.array([0.35, 0.12, 0.02, 0.01])
    else:  # silver / chrome — capped below SDR white so it doesn't glow
        pts   = np.array([0.00, 0.20, 0.55, 1.00])
        R_pts = np.array([0.78, 0.55, 0.32, 0.18])
        G_pts = np.array([0.78, 0.55, 0.32, 0.18])
        B_pts = np.array([0.80, 0.57, 0.34, 0.20])

    y = np.linspace(0.0, 1.0, H)
    R = np.interp(y, pts, R_pts) * peak_nits
    G = np.interp(y, pts, G_pts) * peak_nits
    B = np.interp(y, pts, B_pts) * peak_nits

    rgb = np.stack([
        np.broadcast_to(R[:, None], (H, W)),
        np.broadcast_to(G[:, None], (H, W)),
        np.broadcast_to(B[:, None], (H, W)),
    ], axis=-1).astype(np.float64).copy()

    x = np.linspace(0.0, 1.0, W)
    sheen = 1.0 - 0.06 * np.abs(x - 0.5) * 2
    rgb *= sheen[None, :, None]

    text_img = Image.new("L", (W, H), 0)
    draw = ImageDraw.Draw(text_img)
    font = None
    # First try font names - fontconfig resolves on Linux, system font lookup on macOS/Windows.
    for name in ("Arial Black", "Arial-Bold", "Arial Bold", "DejaVu Sans Bold",
                 "DejaVuSans-Bold", "Helvetica-Bold"):
        try:
            font = ImageFont.truetype(name, int(H * 0.62))
            break
        except (OSError, IOError):
            continue
    # Then try absolute paths (covers macOS + common Linux distros).
    if font is None:
        for fp in [
            "/System/Library/Fonts/Supplemental/Arial Black.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
        ]:
            try:
                font = ImageFont.truetype(fp, int(H * 0.62))
                break
            except (OSError, IOError):
                continue
    # Final fallback: Pillow's bundled TTF, sized (Pillow 10+).
    if font is None:
        try:
            font = ImageFont.load_default(size=int(H * 0.62))
        except TypeError:
            font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (W - tw) // 2 - bbox[0]
    ty = (H - th) // 2 - bbox[1]
    draw.text((tx, ty), text, fill=255, font=font)
    text_mask = np.asarray(text_img, dtype=np.float64) / 255.0

    text_dark = np.array([5.0, 4.0, 3.0])
    rgb = rgb * (1.0 - text_mask[..., None]) + text_dark[None, None, :] * text_mask[..., None]

    return encode_hdr_png(rgb)


def main(out_dir: pathlib.Path = pathlib.Path("assets")) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    hdr_path = out_dir / "hdr_badge.png"
    sdr_path = out_dir / "sdr_badge.png"

    hdr_bytes = make_metal_badge_png("HDR", mode="gold",   peak_nits=5000.0)
    sdr_bytes = make_metal_badge_png("SDR", mode="silver", peak_nits=200.0)

    hdr_path.write_bytes(hdr_bytes)
    sdr_path.write_bytes(sdr_bytes)

    print(f"wrote {hdr_path} ({len(hdr_bytes):,} bytes)")
    print(f"wrote {sdr_path} ({len(sdr_bytes):,} bytes)")


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("assets")
    main(out)
