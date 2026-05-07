# /// script
# dependencies = [
#     "anywidget==0.11.0",
#     "astropy==7.2.0",
#     "colour-science==0.4.7",
#     "hdrviz==0.2.1",
#     "marimo",
#     "matplotlib==3.10.9",
#     "numpy==2.4.4",
#     "pillow==12.2.0",
#     "scipy==1.17.1",
#     "tifffile==2026.5.2",
#     "traitlets==5.14.3",
# ]
# requires-python = ">=3.13"
#
# [tool.marimo.display]
# theme = "dark"
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import anywidget
    import traitlets

    return anywidget, mo, traitlets


@app.cell(hide_code=True)
def _(GLOW_HDR_DATA_URL, LOGO_DATA_URL, mo):
    banner = f"""
    <style>
      .hdr-hero {{
        margin: 0 0 24px;
        overflow: hidden;
        position: relative;
        border-radius: 14px;
        background:
          radial-gradient(ellipse at 18% 20%, rgba(251, 146, 60, 0.18) 0%, transparent 55%),
          radial-gradient(ellipse at 90% 80%, rgba(99, 102, 241, 0.18) 0%, transparent 60%),
          linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0f172a 100%);
        color: #e2e8f0;
        border: 1px solid rgba(148, 163, 184, 0.18);
      }}
      .hdr-hero__grid {{
        align-items: stretch;
        display: grid;
        gap: 22px;
        grid-template-columns: minmax(0, 1.25fr) minmax(260px, 0.75fr);
        padding: 30px 28px;
      }}
      @media (max-width: 760px) {{
        .hdr-hero__grid {{
          grid-template-columns: 1fr;
          padding: 24px 18px;
        }}
        .hdr-hero h1 {{ font-size: 1.9rem !important; }}
      }}
      .hdr-hero h1 {{
        margin: 14px 0 10px;
        color: #f8fafc;
        font-size: 2.55rem;
        line-height: 1.04;
        font-weight: 850;
        letter-spacing: -0.01em;
      }}
      .hdr-hero h1 .glow {{
        background: linear-gradient(120deg, #fde047 0%, #fb923c 40%, #f97316 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 22px rgba(251, 146, 60, 0.55);
        transition: text-shadow 260ms ease, filter 260ms ease;
        cursor: default;
      }}
      .hdr-hero h1 .glow:hover {{
        background-image: url({GLOW_HDR_DATA_URL});
        background-size: 100% 100%;
        background-repeat: no-repeat;
        -webkit-background-clip: text;
        background-clip: text;
        text-shadow: 0 0 42px rgba(253, 186, 116, 0.95);
        filter: saturate(1.1);
      }}
      .hdr-hero__pill {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        border: 1px solid rgba(253, 186, 116, 0.45);
        background: rgba(251, 146, 60, 0.08);
        border-radius: 999px;
        color: #fdba74;
        font-size: 0.74rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        text-decoration: none;
        transition: background 120ms, border-color 120ms;
      }}
      a.hdr-hero__pill:hover {{
        background: rgba(251, 146, 60, 0.15);
        border-color: rgba(253, 186, 116, 0.75);
      }}
      .hdr-hero__viewing {{
        margin-top: 16px;
        padding: 10px 14px;
        border-left: 3px solid rgba(251, 146, 60, 0.5);
        background: rgba(251, 146, 60, 0.05);
        border-radius: 0 8px 8px 0;
        color: #cbd5e1;
        font-size: 0.95rem;
        line-height: 1.55;
        max-width: 650px;
      }}
      .hdr-hero__todo {{
        display: block;
        margin-top: 14px;
        padding: 10px 12px;
        border: 1px dashed rgba(251, 146, 60, 0.55);
        border-radius: 8px;
        background: rgba(251, 146, 60, 0.04);
        color: #fdba74;
        font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
        font-size: 0.82rem;
        font-style: normal;
        line-height: 1.45;
        max-width: 650px;
      }}
      .hdr-hero__todo b {{
        color: #fed7aa;
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        font-size: 0.7rem;
        display: block;
        margin-bottom: 4px;
      }}
      .hdr-hero__lede {{
        margin: 0 0 14px;
        color: #cbd5e1;
        font-size: 1.05rem;
        line-height: 1.55;
        max-width: 650px;
      }}
      .hdr-hero__byline {{
        margin: 14px 0 0;
        color: #94a3b8;
        font-size: 0.9rem;
      }}
      .hdr-hero__byline a {{
        color: #fdba74;
        text-decoration: none;
      }}
      .hdr-hero__byline a:hover {{ text-decoration: underline; }}
      .hdr-hero__side {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}
      .hdr-hero__side img {{
        max-width: 250px;
        width: 100%;
        height: auto;
        display: block;
        align-self: center;
        border-radius: 6%;
      }}
    </style>
    <div class="hdr-hero">
      <div class="hdr-hero__grid">
        <div>
          <a class="hdr-hero__pill" href="https://github.com/ktaletsk/hdrviz">HDR Dataviz</a>
          <h1>Let your data <span class="glow">GLOW</span></h1>

          <p class="hdr-hero__lede">Scientific data has more dynamic range than your viewer libraries show. This notebook introduces a new Python library <code>hdrviz</code>. Watch the data come to life on an HDR display.</p>

          <div class="hdr-hero__viewing">
            We recommend setting a dark theme, maximum screen brightness, and ideally
            getting the room dark as well. Works best in Chromium-based browsers (Chrome, Brave, Edge). Enjoy the show!
          </div>

          <p class="hdr-hero__byline"><a href="https://www.linkedin.com/in/taletskiy">Konstantin Taletskiy</a> &middot; <a href="https://github.com/ktaletsk/hdrviz">Repo</a></p>
        </div>
        <div class="hdr-hero__side">
    <img src="{LOGO_DATA_URL}" alt="hdrviz logo">
        </div>
      </div>
    </div>
    """
    mo.Html(banner)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Intro

    The story alternates between micro-demos and longer explorations (fractals, astronomy and biological data). You can read it linearly, but every demo is independent — feel free to skip to whichever one calls to you. The accompanying library [`hdrviz`](https://github.com/ktaletsk/hdrviz) is MIT-licensed and avilable on PyPI; everything else in this notebook either consumes it or surrounds it with explanation.

    ## Before we start, let's check what display capabilities you have.
    Browser API can report it and we can check it in our widget. Please, re-run the cell if you move the notebook window between displays
    """)
    return


@app.cell(hide_code=True)
def _(
    HDR_BADGE_DATA_URL,
    SDR_BADGE_DATA_URL,
    XDR_FRAME_DATA_URL,
    anywidget,
    traitlets,
):
    class HeadroomDetector(anywidget.AnyWidget):
        """Browser HDR capability detector, rendered as a Pro Display XDR with the info on its screen.
        Click the HDR/SDR badge for a DVD-screensaver bounce inside the monitor; click again to reset.
        Hits a corner perfectly? Celebration."""

        dynamic_range_high = traitlets.Bool(False).tag(sync=True)
        color_gamut_p3 = traitlets.Bool(False).tag(sync=True)
        color_gamut_rec2020 = traitlets.Bool(False).tag(sync=True)
        peak_luminance_nits = traitlets.Float(0.0).tag(sync=True)
        detection_complete = traitlets.Bool(False).tag(sync=True)
        frame_data_url = traitlets.Unicode("").tag(sync=True)
        hdr_badge_data_url = traitlets.Unicode("").tag(sync=True)
        sdr_badge_data_url = traitlets.Unicode("").tag(sync=True)

        def __init__(
            self,
            frame_data_url=XDR_FRAME_DATA_URL,
            hdr_badge_data_url=HDR_BADGE_DATA_URL,
            sdr_badge_data_url=SDR_BADGE_DATA_URL,
            **kw,
        ):
            super().__init__(
                frame_data_url=frame_data_url,
                hdr_badge_data_url=hdr_badge_data_url,
                sdr_badge_data_url=sdr_badge_data_url,
                **kw,
            )

        _esm = r"""
        function render({ model, el }) {
          const dynRangeHigh = window.matchMedia("(dynamic-range: high)").matches;
          const gamutP3 = window.matchMedia("(color-gamut: p3)").matches;
          const gamutRec2020 = window.matchMedia("(color-gamut: rec2020)").matches;
          let peakNits = 0;
          try {
            if (window.screen && "luminance" in window.screen && window.screen.luminance) {
              peakNits = Number(window.screen.luminance.max) || 0;
            }
          } catch (_) {}

          model.set("dynamic_range_high", dynRangeHigh);
          model.set("color_gamut_p3", gamutP3);
          model.set("color_gamut_rec2020", gamutRec2020);
          model.set("peak_luminance_nits", peakNits);
          model.set("detection_complete", true);
          model.save_changes();

          const frameUrl = model.get("frame_data_url");
          const badgeUrl = dynRangeHigh
            ? model.get("hdr_badge_data_url")
            : model.get("sdr_badge_data_url");

          el.innerHTML = `
            <style>
              .xdr-wrap {
                position: relative;
                width: 100%;
                max-width: 1040px;
                margin: 0 auto;
                aspect-ratio: 1200 / 630;
                font-family: system-ui, -apple-system, sans-serif;
                container-type: inline-size;
              }
              .xdr-wrap > img.frame {
                position: absolute;
                inset: 0;
                width: 100%;
                height: 100%;
                display: block;
                user-select: none;
                pointer-events: none;
              }
              .xdr-screen {
                position: absolute;
                top: 17.46%;
                left: 25.92%;
                width: 48.17%;
                height: 52.70%;
                color: #e2e8f0;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 4% 5%;
                box-sizing: border-box;
                background:
                  radial-gradient(ellipse at 50% 0%, rgba(99, 102, 241, 0.10) 0%, transparent 60%),
                  radial-gradient(ellipse at 50% 100%, rgba(251, 146, 60, 0.08) 0%, transparent 60%);
                overflow: hidden;
              }
              .xdr-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
              }
              .xdr-header .title {
                font-weight: 700;
                color: #f8fafc;
                letter-spacing: 0.02em;
                font-size: clamp(11px, 1.8cqi, 18px);
              }
              .xdr-badge {
                display: block;
                height: clamp(18px, 3.4cqi, 34px);
                width: auto;
                border-radius: 6px;
                user-select: none;
                cursor: pointer;
                box-shadow:
                  0 2px 8px rgba(0, 0, 0, 0.5),
                  0 0 22px rgba(255, 200, 80, 0.15);
              }
              .xdr-badge.bouncing {
                position: absolute;
                z-index: 10;
                transition: none;
              }
              .xdr-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 6px;
                font-size: clamp(8px, 1.3cqi, 13px);
              }
              .xdr-pill {
                border: 1px solid rgba(148, 163, 184, 0.3);
                border-radius: 5px;
                padding: 5px 9px;
                display: flex;
                justify-content: space-between;
                gap: 8px;
                line-height: 1.25;
                background: rgba(15, 23, 42, 0.4);
              }
              .xdr-pill .v {
                font-weight: 700;
                font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
              }
              .xdr-yes { color: #4ade80; }
              .xdr-no  { color: #94a3b8; opacity: 0.7; }

              /* corner-hit celebration */
              .xdr-corner-burst {
                position: absolute;
                width: clamp(80px, 30cqi, 280px);
                height: clamp(80px, 30cqi, 280px);
                border-radius: 50%;
                background: radial-gradient(circle,
                  rgba(255, 240, 160, 0.85) 0%,
                  rgba(251, 191, 36, 0.6) 25%,
                  rgba(251, 146, 60, 0.3) 55%,
                  transparent 75%);
                pointer-events: none;
                opacity: 0;
                transform: translate(-50%, -50%) scale(0.2);
                animation: xdr-burst 1100ms forwards;
                z-index: 5;
              }
              @keyframes xdr-burst {
                0%   { opacity: 0;   transform: translate(-50%, -50%) scale(0.2); }
                18%  { opacity: 1;   transform: translate(-50%, -50%) scale(0.9); }
                100% { opacity: 0;   transform: translate(-50%, -50%) scale(1.7); }
              }
              .xdr-corner-text {
                position: absolute;
                top: 50%;
                left: 50%;
                font-weight: 900;
                font-size: clamp(18px, 6cqi, 56px);
                letter-spacing: 0.08em;
                background: linear-gradient(180deg, #fff5b8 0%, #fde047 35%, #f59e0b 70%, #b45309 100%);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                text-shadow: 0 0 28px rgba(251, 191, 36, 0.55);
                pointer-events: none;
                opacity: 0;
                transform: translate(-50%, -50%) scale(0.3);
                animation: xdr-corner-text 1300ms forwards;
                z-index: 6;
              }
              @keyframes xdr-corner-text {
                0%   { opacity: 0; transform: translate(-50%, -50%) scale(0.3); }
                18%  { opacity: 1; transform: translate(-50%, -50%) scale(1.15); }
                55%  { opacity: 1; transform: translate(-50%, -50%) scale(1.0);  }
                100% { opacity: 0; transform: translate(-50%, -50%) scale(1.4);  }
              }
            </style>
            <div class="xdr-wrap">
              <img class="frame" src="${frameUrl}" alt="Pro Display XDR">
              <div class="xdr-screen">
                <div class="xdr-header">
                  <span class="title">Display capability check</span>
                  <img class="xdr-badge" src="${badgeUrl}" alt="${dynRangeHigh ? "HDR" : "SDR"}"
                       title="click for DVD bounce; click again to reset">
                </div>
                <div class="xdr-grid">
                  <div class="xdr-pill"><span>HDR (dynamic-range)</span>
                    <span class="v ${dynRangeHigh ? "xdr-yes" : "xdr-no"}">${dynRangeHigh ? "high" : "standard"}</span></div>
                  <div class="xdr-pill"><span>color-gamut: P3</span>
                    <span class="v ${gamutP3 ? "xdr-yes" : "xdr-no"}">${gamutP3 ? "yes" : "no"}</span></div>
                  <div class="xdr-pill"><span>color-gamut: rec2020</span>
                    <span class="v ${gamutRec2020 ? "xdr-yes" : "xdr-no"}">${gamutRec2020 ? "yes" : "no"}</span></div>
                  <div class="xdr-pill"><span>peak luminance API</span>
                    <span class="v ${peakNits > 0 ? "xdr-yes" : "xdr-no"}">${peakNits > 0 ? peakNits + " nits" : "n/a"}</span></div>
                </div>
              </div>
            </div>
          `;

          // ----- DVD bounce + corner celebration -----
          const screenEl = el.querySelector(".xdr-screen");
          const headerEl = el.querySelector(".xdr-header");
          const badgeEl = el.querySelector(".xdr-badge");

          let bouncing = false;
          let raf = null;
          let lastCornerCelebration = 0;

          function celebrateCorner(cx, cy) {
            const now = performance.now();
            if (now - lastCornerCelebration < 600) return;  // cooldown
            lastCornerCelebration = now;

            const burst = document.createElement("div");
            burst.className = "xdr-corner-burst";
            burst.style.left = cx + "px";
            burst.style.top  = cy + "px";
            screenEl.appendChild(burst);

            const text = document.createElement("div");
            text.className = "xdr-corner-text";
            text.textContent = "CORNER!";
            screenEl.appendChild(text);

            setTimeout(() => { burst.remove(); text.remove(); }, 1400);
          }

          function startBounce() {
            if (bouncing) return;
            bouncing = true;
            const sRect = screenEl.getBoundingClientRect();
            const bRect = badgeEl.getBoundingClientRect();
            const startX = bRect.left - sRect.left;
            const startY = bRect.top  - sRect.top;
            screenEl.appendChild(badgeEl);
            badgeEl.classList.add("bouncing");
            badgeEl.style.left = startX + "px";
            badgeEl.style.top  = startY + "px";

            const speed = Math.max(1.0, sRect.width / 320);
            const angle = (Math.random() * 0.6 + 0.2) * Math.PI;
            const dir = Math.random() > 0.5 ? 1 : -1;
            let vx = Math.cos(angle) * speed * dir;
            let vy = Math.sin(angle) * speed;
            let x = startX, y = startY;

            function step() {
              if (!bouncing) return;
              const sRect2 = screenEl.getBoundingClientRect();
              const maxX = sRect2.width  - badgeEl.offsetWidth;
              const maxY = sRect2.height - badgeEl.offsetHeight;
              x += vx;
              y += vy;
              let xBounced = false, yBounced = false;
              if (x <= 0)    { x = 0;    vx = -vx; xBounced = true; }
              else if (x >= maxX) { x = maxX; vx = -vx; xBounced = true; }
              if (y <= 0)    { y = 0;    vy = -vy; yBounced = true; }
              else if (y >= maxY) { y = maxY; vy = -vy; yBounced = true; }

              if (xBounced && yBounced) {
                // Center the celebration on the corner the badge actually hit
                const cornerX = (x <= 0) ? 0 : maxX + badgeEl.offsetWidth;
                const cornerY = (y <= 0) ? 0 : maxY + badgeEl.offsetHeight;
                celebrateCorner(cornerX, cornerY);
              }

              badgeEl.style.left = x + "px";
              badgeEl.style.top  = y + "px";
              raf = requestAnimationFrame(step);
            }
            raf = requestAnimationFrame(step);
          }

          function stopBounce() {
            if (!bouncing) return;
            bouncing = false;
            cancelAnimationFrame(raf);
            badgeEl.classList.remove("bouncing");
            badgeEl.style.left = "";
            badgeEl.style.top  = "";
            // Clear any in-flight celebration overlays so reset is clean
            screenEl.querySelectorAll(".xdr-corner-burst, .xdr-corner-text").forEach(n => n.remove());
            // Reparent back to header → resets to original spot
            headerEl.appendChild(badgeEl);
          }

          badgeEl.addEventListener("click", () => {
            if (bouncing) stopBounce();
            else startBounce();
          });
        }
        export default { render };
        """


    return (HeadroomDetector,)


@app.cell(hide_code=True)
def _(HeadroomDetector):
    detector = HeadroomDetector()
    detector
    return


@app.cell(hide_code=True)
def _():
    import base64, pathlib, urllib.request

    # Public URLs the notebook can fall back to when running in molab / nbviewer
    # / any sandbox that strips the local assets/ directory. Local files take
    # precedence so the notebook is fast on the author's machine.
    ASSET_URLS = {
        "orbrx-glowing.png":     "https://raw.githubusercontent.com/ktaletsk/hdrviz/main/assets/orbrx-glowing.png",
        "xdr_display_frame.png": "https://raw.githubusercontent.com/ktaletsk/hdrviz/main/assets/xdr_display_frame.png",
        "logo.svg":              "https://raw.githubusercontent.com/ktaletsk/hdrviz/main/assets/logo.svg",
        "HorseHead.fits":        "https://www.astropy.org/astropy-data/tutorials/FITS-images/HorseHead.fits",
        "cells3d.tif":           "https://gitlab.com/scikit-image/data/-/raw/2cdc5ce89b334d28f06a58c9f0ca21aa6992a5ba/cells3d.tif",
        "hdr_badge.png":         "https://raw.githubusercontent.com/ktaletsk/hdrviz/main/assets/hdr_badge.png",
        "sdr_badge.png":         "https://raw.githubusercontent.com/ktaletsk/hdrviz/main/assets/sdr_badge.png",
    }
    _ASSET_BYTES_CACHE: dict = {}


    def fetch_asset(name: str) -> bytes:
        """Load an asset by name. Tries assets/<name> first; falls back to the
        URL in ASSET_URLS. Cached in-memory for the kernel session."""
        if name in _ASSET_BYTES_CACHE:
            return _ASSET_BYTES_CACHE[name]
        local = pathlib.Path("assets") / name
        if local.exists():
            data = local.read_bytes()
        else:
            url = ASSET_URLS.get(name)
            if not url:
                raise FileNotFoundError(
                    f"asset {name!r} not found at assets/{name} and no fallback URL configured"
                )
            with urllib.request.urlopen(url, timeout=60) as r:
                data = r.read()
        _ASSET_BYTES_CACHE[name] = data
        return data


    PNG_BYTES = fetch_asset("orbrx-glowing.png")
    PNG_DATA_URL = "data:image/png;base64," + base64.b64encode(PNG_BYTES).decode("ascii")
    PNG_LABEL = "orbrx-glowing.png"

    XDR_FRAME_BYTES = fetch_asset("xdr_display_frame.png")
    XDR_FRAME_DATA_URL = "data:image/png;base64," + base64.b64encode(XDR_FRAME_BYTES).decode("ascii")

    LOGO_SVG_BYTES = fetch_asset("logo.svg")
    LOGO_DATA_URL = "data:image/svg+xml;base64," + base64.b64encode(LOGO_SVG_BYTES).decode("ascii")
    return (
        LOGO_DATA_URL,
        PNG_DATA_URL,
        PNG_LABEL,
        XDR_FRAME_DATA_URL,
        fetch_asset,
    )


@app.cell
def _(encode_hdr_png, to_data_url):
    import numpy as _np

    # Horizontal HDR gradient that mirrors the orbrx logo's golden-yellow glow.
    # Channel values >= 1.0 push above peak_nits for the brightest pixels.
    _W, _H = 800, 140
    _peak_nits = 4000.0
    _pts = _np.array([
        [0.00, 1.00, 1.00, 0.55],   # bright yellow (almost white-yellow)
        [0.50, 1.00, 0.95, 0.35],   # rich yellow
        [1.00, 1.00, 0.85, 0.22],   # warm gold (still yellow-dominant)
    ])
    _x = _np.linspace(0.0, 1.0, _W)
    _R = _np.interp(_x, _pts[:, 0], _pts[:, 1]) * _peak_nits
    _G = _np.interp(_x, _pts[:, 0], _pts[:, 2]) * _peak_nits
    _B = _np.interp(_x, _pts[:, 0], _pts[:, 3]) * _peak_nits
    _rgb_strip = _np.stack([_R, _G, _B], axis=-1)
    _rgb_nits  = _np.broadcast_to(_rgb_strip, (_H, _W, 3)).copy()
    GLOW_HDR_DATA_URL = to_data_url(encode_hdr_png(_rgb_nits))
    return (GLOW_HDR_DATA_URL,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What is Dynamic Range?
    Dynamic range is the ratio between the brightest and darkest meaningful values in a signal. Your eye can distinguish a candle on a dark beach (~10⁻³ nits) and a sunlit beach (~10⁵ nits) — roughly 10⁸ across — except your eye doesn't see both at once; it adapts. A camera, a display, a JPEG file have *fixed* dynamic ranges, no adaptation, and they vary wildly.

    ### How to measure dynamic range

    For an array of data:

    $$\mathrm{DR} = \frac{\max(x)}{\min_{x>0}(x)} \qquad \text{stops} = \log_2(\mathrm{DR}) \qquad \log_{10}(\mathrm{DR})$$

    Notice that zero pixels (background, masked regions) are ignored in the calculation.

    ### Dynamic range at a glance

    | Where data comes from | max / min | stops |
    |---|---:|---:|
    | Human eye, instantaneous (no adaptation) | ~16,000 : 1 | ~14 |
    | Human eye, with adaptation (night ↔ noon) | ~10⁹ : 1 | ~30 |
    | 8-bit JPEG | 256 : 1 | 8 |
    | 10-bit HDR PNG (PQ Rec2020) | ~10⁵ : 1 effective | ~17 |
    | 16-bit scientific CMOS sensor | ~30,000 : 1 | ~15 |
    | 32-bit float FITS image | numerical: ~10⁷⁰ : 1 | (unbounded) |

    | Where data is shown | max / min | stops |
    |---|---:|---:|
    | SDR display (sRGB, ~100 nits peak) | 100 : 1 | ~7 |
    | HDR display (PQ, ~1000 nits peak) | ~1,000 : 1 | ~10 |
    | Apple Pro Display XDR / MacBook Pro (sustained 1000 / peak 1600) | ~10,000 : 1 | ~13 |

    The display is usually the bottleneck. Most scientific data carries more information than your screen has been showing you — but only if you bother to render it that way.
    """)
    return


@app.cell(hide_code=True)
def _(PNG_DATA_URL, PNG_LABEL, anywidget, traitlets):
    class HeadroomMixer(anywidget.AnyWidget):
        """Slider over CSS dynamic-range-limit, smoothly mixing standard <-> no-limit.
        Live readout reports the effective dynamic range and total stops, matching
        the same metric used in the introductory table."""

        image_data_url = traitlets.Unicode("").tag(sync=True)
        image_label = traitlets.Unicode("").tag(sync=True)
        mix_percent = traitlets.Int(100).tag(sync=True)

        # Endpoints. SDR follows CSS reference (100 nits diffuse white, ~100:1
        # display contrast). HDR defaults to a "typical PQ display" spec; bump
        # display_peak_nits to 1600 and display_floor_nits to 0.16 to match the
        # Apple Pro Display XDR / MacBook Pro Liquid Retina XDR (10,000:1).
        sdr_peak_nits = traitlets.Float(100.0).tag(sync=True)
        sdr_floor_nits = traitlets.Float(1.0).tag(sync=True)
        display_peak_nits = traitlets.Float(1000.0).tag(sync=True)
        display_floor_nits = traitlets.Float(1.0).tag(sync=True)

        def __init__(self, image_data_url=PNG_DATA_URL, image_label=PNG_LABEL, **kw):
            super().__init__(image_data_url=image_data_url, image_label=image_label, **kw)

        _esm = r"""
        function render({ model, el }) {
          const url = model.get("image_data_url");
          const label = model.get("image_label");

          el.innerHTML = `
            <style>
              .hm-card { font-family: system-ui, -apple-system, sans-serif; color: inherit;
                border: 1px solid color-mix(in srgb, currentColor 20%, transparent);
                border-radius: 12px; padding: 14px; display: grid; gap: 12px; }
              .hm-img-wrap { background:#000; border-radius:10px;
                border:1px solid color-mix(in srgb, currentColor 12%, transparent);
                display:flex; justify-content:center; align-items:center;
                min-height:180px; max-height:280px; overflow:hidden; }
              .hm-img-wrap img { max-width:100%; max-height:280px; display:block; }
              .hm-row { display:flex; gap:12px; align-items:center; font-size:13px; }
              .hm-row .lo, .hm-row .hi {
                font-family: ui-monospace, SFMono-Regular, monospace; font-size:11px;
                opacity:0.75; min-width:64px;
              }
              .hm-row .hi { text-align:right; }
              .hm-slider { flex:1; }
              .hm-readout { font-family: ui-monospace, SFMono-Regular, monospace;
                font-size:11px; opacity:0.7; min-width:48px; text-align:right;
                font-variant-numeric: tabular-nums; }
              .hm-metrics {
                display:flex; gap:8px; flex-wrap:wrap; align-items:center;
                font-family: ui-monospace, SFMono-Regular, monospace; font-size:11px;
              }
              .hm-pill {
                padding:4px 10px; border-radius:999px;
                background: color-mix(in srgb, currentColor 7%, transparent);
                border: 1px solid color-mix(in srgb, currentColor 14%, transparent);
                white-space: nowrap;
              }
              .hm-pill .k { opacity:0.65; margin-right:4px; }
              .hm-pill .v { font-weight:600; font-variant-numeric: tabular-nums; }
            </style>
            <div class="hm-card">
              <div class="hm-img-wrap"><img id="hm-img" alt="${label}" src="${url}"></div>
              <div class="hm-row">
                <span class="lo">SDR</span>
                <input id="hm-slider" class="hm-slider" type="range"
                       min="0" max="100" step="1" value="${model.get("mix_percent")}">
                <span class="hi">full HDR</span>
                <span class="hm-readout" id="hm-readout">${model.get("mix_percent")}%</span>
              </div>
              <div class="hm-metrics">
                <span class="hm-pill"><span class="k">peak</span><span class="v" id="hm-peak">— nits</span></span>
                <span class="hm-pill"><span class="k">floor</span><span class="v" id="hm-floor">— nits</span></span>
                <span class="hm-pill"><span class="k">dynamic range</span><span class="v" id="hm-dr">—:1</span></span>
                <span class="hm-pill"><span class="k">stops</span><span class="v" id="hm-stops">—</span></span>
              </div>
            </div>
          `;

          const img = el.querySelector("#hm-img");
          const slider = el.querySelector("#hm-slider");
          const readout = el.querySelector("#hm-readout");
          const peakEl = el.querySelector("#hm-peak");
          const floorEl = el.querySelector("#hm-floor");
          const drEl = el.querySelector("#hm-dr");
          const stopsEl = el.querySelector("#hm-stops");

          function fmtNits(x) {
            if (x >= 100) return Math.round(x).toString() + " nits";
            if (x >= 1)   return x.toFixed(1) + " nits";
            return x.toFixed(2) + " nits";
          }
          function fmtRatio(x) {
            if (x >= 1000) return Math.round(x).toLocaleString() + ":1";
            if (x >= 100)  return Math.round(x) + ":1";
            return x.toFixed(0) + ":1";
          }

          function apply(pct) {
            const css = `dynamic-range-limit-mix(standard ${100 - pct}%, no-limit ${pct}%)`;
            img.style.setProperty("dynamic-range-limit", css);
            readout.textContent = pct + "%";

            const sdrP = model.get("sdr_peak_nits");
            const sdrF = model.get("sdr_floor_nits");
            const hdrP = model.get("display_peak_nits");
            const hdrF = model.get("display_floor_nits");
            const f = pct / 100;
            // Linear interpolation in nits between SDR and full-HDR endpoints.
            const peak = sdrP + (hdrP - sdrP) * f;
            const floor = sdrF + (hdrF - sdrF) * f;
            const dr = peak / floor;
            const stops = Math.log2(dr);
            peakEl.textContent  = fmtNits(peak);
            floorEl.textContent = fmtNits(floor);
            drEl.textContent    = fmtRatio(dr);
            stopsEl.textContent = stops.toFixed(2);
          }
          slider.addEventListener("input", () => {
            const pct = parseInt(slider.value, 10);
            apply(pct);
            model.set("mix_percent", pct);
            model.save_changes();
          });
          apply(parseInt(slider.value, 10));
        }
        export default { render };
        """


    return (HeadroomMixer,)


@app.cell
def _(HeadroomMixer):
    mixer = HeadroomMixer()
    mixer
    return


@app.cell(hide_code=True)
def _():
    import numpy as np
    from hdrviz import (
        DEFAULT_PQ_REC2020_ICC,
        COLORMAP_LIBRARY,
        HDRImage,
        encode_hdr_png,
        extract_icc_from_png,
        hdr_colormap,
        imshow,
        linear_nits_to_pq,
        to_data_url,
    )


    return (
        COLORMAP_LIBRARY,
        HDRImage,
        encode_hdr_png,
        hdr_colormap,
        imshow,
        np,
        to_data_url,
    )


@app.cell(hide_code=True)
def _(fetch_asset, to_data_url):
    # HDR/SDR badges shown on the Pro Display XDR mockup. Pre-rendered locally
    # (where macOS system fonts are available) and committed to assets/, fetched
    # via fetch_asset() so the notebook is portable to molab and other sandboxes.
    # To regenerate: run hdrviz/scripts/make_badges.py (or check older git
    # history for the original make_metal_badge_png helper).
    HDR_BADGE_DATA_URL = to_data_url(fetch_asset("hdr_badge.png"))
    SDR_BADGE_DATA_URL = to_data_url(fetch_asset("sdr_badge.png"))

    return HDR_BADGE_DATA_URL, SDR_BADGE_DATA_URL


@app.cell(hide_code=True)
def _(HDRImage, LOGO_DATA_URL, imshow, mo):
    import inspect

    mo.md(
        '<div style="display:flex; align-items:center; gap:18px; margin: 12px 0 18px;">'
        '<img src="' + LOGO_DATA_URL + '" alt="hdrviz logo" '
        'style="width:96px; height:96px; border-radius:18px; flex-shrink:0;">'
        '<div>'
        '<div style="font-size:1.6rem; font-weight:700; font-family: ui-monospace, SFMono-Regular, monospace;">hdrviz</div>'
        '<div style="margin-top:6px; font-size:0.95rem;">'
        '<a href="https://github.com/ktaletsk/hdrviz">github.com/ktaletsk/hdrviz</a>'
        '</div>'
        '</div>'
        '</div>\n\n'
        "```sh\npip install hdrviz\n```\n\n"
        "The HDR math (the PQ EOTF / SMPTE ST 2084, the Rec2020 primaries) lives in "
        "[`colour-science`](https://www.colour-science.org/), which the library wraps. "
        "The PNG encoding, ICC profile embedding, colormap interpolation, and the anywidget "
        "are ours. MIT-licensed; depends only on `numpy`, `colour-science`, `Pillow`, "
        "`anywidget`, and `traitlets`.\n\n"
        "### `imshow(arr, cmap, peak_nits, ...)`\n\n"
        "```python\n" + inspect.getsource(imshow) + "\n```\n\n"
        "### `class HDRImage`\n\n"
        "```python\n" + inspect.getsource(HDRImage) + "\n```"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The PQ encoding (SMPTE ST 2084 / "perceptual quantizer") maps linear-light luminance in cd/m² to code values, designed so one code-value step ≈ one just-noticeable difference for the human visual system. The math is implemented in [colour-science](https://www.colour-science.org/):

    ```python
    from colour.models import eotf_inverse_ST2084
    pq_code = eotf_inverse_ST2084(rgb_nits)  # rgb_nits in [0, 10000], pq_code in [0, 1]
    ```

    That single line is the mathematical core of `hdrviz.encode_hdr_png`.
    """)
    return


@app.cell
def _(encode_hdr_png, hdr_colormap, np):
    def mandelbrot(width: int, height: int, x_center: float = -0.5, y_center: float = 0.0,
                   x_extent: float = 3.5, max_iter: int = 512) -> tuple[np.ndarray, np.ndarray]:
        """Smooth-iteration-count Mandelbrot. Returns (smooth_iter, interior_mask)."""
        aspect = width / height
        y_extent = x_extent / aspect
        x = np.linspace(x_center - x_extent / 2, x_center + x_extent / 2, width, dtype=np.float64)
        y = np.linspace(y_center - y_extent / 2, y_center + y_extent / 2, height, dtype=np.float64)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        Z = np.zeros_like(C)
        smooth = np.zeros(C.shape, dtype=np.float64)
        alive = np.ones(C.shape, dtype=bool)
        for i in range(max_iter):
            Z[alive] = Z[alive] ** 2 + C[alive]
            absZ = np.abs(Z)
            escaped = alive & (absZ > 2.0)
            if escaped.any():
                log_absZ = np.log(absZ[escaped])
                nu = np.log(log_absZ / np.log(2.0)) / np.log(2.0)
                smooth[escaped] = i + 1 - nu
            alive &= ~escaped
        return smooth, alive


    def render_mandelbrot_hdr(width: int = 800, height: int = 500,
                              x_center: float = -0.7, y_center: float = 0.0,
                              x_extent: float = 3.0, max_iter: int = 512,
                              peak_nits: float = 4000.0,
                              cmap_name: str = "fire-purple") -> bytes:
        """Render a Mandelbrot view to HDR PNG bytes."""
        smooth, interior = mandelbrot(width, height, x_center, y_center, x_extent, max_iter)
        norm = np.where(interior, 0.0, np.log1p(smooth) / np.log1p(max_iter))
        norm = np.clip(norm, 0.0, 1.0)
        rgb_nits = hdr_colormap(norm, cmap_name=cmap_name, peak_nits=peak_nits)
        rgb_nits[interior] = 0.0
        return encode_hdr_png(rgb_nits)


    return mandelbrot, render_mandelbrot_hdr


@app.cell(hide_code=True)
def _(
    COLORMAP_LIBRARY,
    anywidget,
    render_mandelbrot_hdr,
    to_data_url,
    traitlets,
):
    class MandelbrotExplorer(anywidget.AnyWidget):
        """Interactive HDR Mandelbrot: click to recenter, zoom buttons, colormap picker, HDR toggle."""

        # View
        x_center = traitlets.Float(-0.7).tag(sync=True)
        y_center = traitlets.Float(0.0).tag(sync=True)
        x_extent = traitlets.Float(3.0).tag(sync=True)
        max_iter = traitlets.Int(512).tag(sync=True)
        peak_nits = traitlets.Float(4000.0).tag(sync=True)
        cmap_name = traitlets.Unicode("fire-purple").tag(sync=True)
        width = traitlets.Int(800).tag(sync=True)
        height = traitlets.Int(500).tag(sync=True)

        # Display
        hdr_enabled = traitlets.Bool(True).tag(sync=True)

        # Output (kernel -> browser)
        image_data_url = traitlets.Unicode("").tag(sync=True)
        cmap_options = traitlets.List([]).tag(sync=True)
        is_rendering = traitlets.Bool(False).tag(sync=True)
        render_ms = traitlets.Float(0.0).tag(sync=True)
        render_token = traitlets.Int(0).tag(sync=True)

        def __init__(self, **kw):
            super().__init__(**kw)
            self.cmap_options = list(COLORMAP_LIBRARY.keys())
            self._do_render()

        @traitlets.observe("x_center", "y_center", "x_extent", "max_iter",
                            "peak_nits", "cmap_name", "width", "height")
        def _on_change(self, change):
            self._do_render()

        def _do_render(self):
            import time
            self.is_rendering = True
            t0 = time.perf_counter()
            png = render_mandelbrot_hdr(
                width=self.width, height=self.height,
                x_center=self.x_center, y_center=self.y_center,
                x_extent=self.x_extent, max_iter=self.max_iter,
                peak_nits=self.peak_nits, cmap_name=self.cmap_name,
            )
            self.image_data_url = to_data_url(png)
            self.render_ms = (time.perf_counter() - t0) * 1000.0
            self.is_rendering = False
            self.render_token = self.render_token + 1

        _esm = r"""
        function render({ model, el }) {
          el.innerHTML = `
            <style>
              .mb-card { font-family: system-ui, -apple-system, sans-serif; color: inherit;
                border: 1px solid color-mix(in srgb, currentColor 20%, transparent);
                border-radius: 12px; padding: 14px; display: grid; gap: 12px; }
              .mb-img-wrap { position: relative; background:#000; border-radius:10px;
                overflow:hidden; max-height:380px; border:1px solid color-mix(in srgb, currentColor 12%, transparent);
                display:flex; justify-content:center; align-items:center; cursor: crosshair; }
              .mb-img-wrap img { width:100%; max-height:380px; height:auto; object-fit:contain; display:block; user-select:none; -webkit-user-drag:none; }
              .mb-overlay { position:absolute; inset:0; pointer-events:none;
                display:flex; align-items:center; justify-content:center;
                background: rgba(0,0,0,0.35); color:#fff; font-size:14px;
                opacity: 0; transition: opacity 80ms; }
              .mb-overlay.show { opacity: 1; }
              .mb-tools { display:flex; gap:10px; flex-wrap:wrap; align-items:center; font-size:13px; }
              .mb-tools button, .mb-tools select {
                font:inherit; color:inherit; background:transparent;
                border:1px solid color-mix(in srgb, currentColor 25%, transparent);
                padding:4px 10px; border-radius:6px; cursor:pointer;
              }
              .mb-tools select { padding: 4px 8px; }
              .mb-tools .tag { font-family: ui-monospace, SFMono-Regular, monospace; font-size:11px;
                padding: 2px 6px; border-radius: 4px; opacity: 0.75;
                background: color-mix(in srgb, currentColor 8%, transparent); }
              .mb-tools .toggle {
                display:inline-flex; align-items:center; gap:6px; user-select:none; cursor:pointer;
                padding: 2px 8px;
                border:1px solid color-mix(in srgb, currentColor 25%, transparent); border-radius:6px;
              }
              .mb-tools .toggle.on { border-color: currentColor; background: color-mix(in srgb, currentColor 10%, transparent); font-weight:600; }
                .mb-presets { display:flex; gap:6px; flex-wrap:wrap; align-items:center; font-size:13px; }
                .mb-presets .label { opacity:0.75; }
                .mb-presets button {
                  font:inherit; color:inherit; background:transparent;
                  border:1px solid color-mix(in srgb, currentColor 25%, transparent);
                  padding:4px 10px; border-radius:6px; cursor:pointer;
                }
                .mb-presets button:hover { border-color: currentColor; background: color-mix(in srgb, currentColor 8%, transparent); }
              .mb-sliders { display:grid; grid-template-columns: 110px 1fr 80px; gap: 6px 14px;
                font-size: 12px; align-items:center; }
              .mb-sliders input[type=range] { width:100%; }
              .mb-sliders .val { font-family: ui-monospace, SFMono-Regular, monospace;
                font-variant-numeric: tabular-nums; text-align:right; opacity:0.85; }
              .mb-coords { font-family: ui-monospace, SFMono-Regular, monospace; font-size: 11px;
                opacity: 0.75; word-break: break-all; }
            </style>
            <div class="mb-card">
              <div class="mb-img-wrap" id="mb-imgwrap">
                <img id="mb-img" alt="HDR Mandelbrot">
                <div class="mb-overlay" id="mb-overlay">rendering…</div>
              </div>
              <div class="mb-presets">
                <span class="label">Try a preset:</span>
                <button data-preset="default">Full set</button>
                <button data-preset="seahorse">Seahorse Valley</button>
                <button data-preset="antenna">Antenna Tip</button>
                <button data-preset="spirals">Spirals</button>
              </div>
              <div class="mb-tools">
                <span class="toggle" id="mb-hdr">
                  <input type="checkbox" id="mb-hdr-cb">
                  <label for="mb-hdr-cb" style="cursor:pointer;">HDR</label>
                </span>
                <label>Colormap
                  <select id="mb-cmap"></select>
                </label>
                <button id="mb-zoomin">+ zoom 2&times;</button>
                <button id="mb-zoomout">− zoom 2&times;</button>
                <button id="mb-reset">reset</button>
                <span class="tag" id="mb-rendertime"></span>
              </div>
              <div class="mb-sliders">
                <span>max iterations</span>
                <input id="mb-iter" type="range" min="64" max="2048" step="32" value="${model.get("max_iter")}">
                <span class="val" id="mb-iter-val">${model.get("max_iter")}</span>

                <span>peak nits</span>
                <input id="mb-peak" type="range" min="500" max="10000" step="100" value="${model.get("peak_nits")}">
                <span class="val" id="mb-peak-val">${Math.round(model.get("peak_nits"))}</span>
              </div>
              <div class="mb-coords" id="mb-coords"></div>
            </div>
          `;

          const img = el.querySelector("#mb-img");
          const wrap = el.querySelector("#mb-imgwrap");
          const overlay = el.querySelector("#mb-overlay");
          const cmapSel = el.querySelector("#mb-cmap");
          const hdrCb = el.querySelector("#mb-hdr-cb");
          const hdrToggle = el.querySelector("#mb-hdr");
          const iterSlider = el.querySelector("#mb-iter");
          const iterVal = el.querySelector("#mb-iter-val");
          const peakSlider = el.querySelector("#mb-peak");
          const peakVal = el.querySelector("#mb-peak-val");
          const renderTime = el.querySelector("#mb-rendertime");
          const coords = el.querySelector("#mb-coords");

          const DEFAULTS = { x_center: -0.7, y_center: 0.0, x_extent: 3.0,
                              max_iter: 512, peak_nits: 4000, cmap_name: "fire-purple" };

          function syncUI() {
            const opts = model.get("cmap_options") || [];
            if (cmapSel.options.length !== opts.length) {
              cmapSel.innerHTML = "";
              for (const name of opts) {
                const o = document.createElement("option");
                o.value = name; o.textContent = name;
                cmapSel.appendChild(o);
              }
            }
            cmapSel.value = model.get("cmap_name");

            const url = model.get("image_data_url");
            if (url && img.src !== url) img.src = url;

            const hdr = model.get("hdr_enabled");
            hdrCb.checked = hdr;
            hdrToggle.classList.toggle("on", hdr);
            img.style.setProperty("dynamic-range-limit", hdr ? "no-limit" : "standard");

            iterSlider.value = model.get("max_iter");
            iterVal.textContent = model.get("max_iter");
            peakSlider.value = Math.round(model.get("peak_nits"));
            peakVal.textContent = Math.round(model.get("peak_nits"));

            const ms = model.get("render_ms");
            renderTime.textContent = ms ? `${ms.toFixed(0)} ms` : "";

            const xc = model.get("x_center"), yc = model.get("y_center"), xe = model.get("x_extent");
            coords.textContent = `center = (${xc.toExponential(4)}, ${yc.toExponential(4)})  •  x_extent = ${xe.toExponential(3)}  •  zoom = ${(DEFAULTS.x_extent / xe).toExponential(2)}×`;

            overlay.classList.toggle("show", model.get("is_rendering"));
          }
          syncUI();

          // observe relevant traits
          ["image_data_url","hdr_enabled","cmap_options","cmap_name",
           "max_iter","peak_nits","x_center","y_center","x_extent",
           "render_ms","is_rendering","render_token"].forEach(name => {
            model.on("change:" + name, syncUI);
          });

          function pixelToComplex(clientX, clientY) {
            const r = wrap.getBoundingClientRect();
            const px = (clientX - r.left) / r.width;   // 0..1
            const py = (clientY - r.top)  / r.height;  // 0..1
            const xc = model.get("x_center"), yc = model.get("y_center");
            const xe = model.get("x_extent");
            const aspect = r.width / r.height;
            const ye = xe / aspect;
            const real = xc + (px - 0.5) * xe;
            const imag = yc + (py - 0.5) * ye;
            return [real, imag];
          }

          // Click on image: recenter (no zoom)
          wrap.addEventListener("click", (ev) => {
            const [r, i] = pixelToComplex(ev.clientX, ev.clientY);
            model.set("x_center", r);
            model.set("y_center", i);
            model.save_changes();
          });

          // Zoom buttons
          el.querySelector("#mb-zoomin").addEventListener("click", () => {
            model.set("x_extent", model.get("x_extent") / 2.0);
            model.save_changes();
          });
          el.querySelector("#mb-zoomout").addEventListener("click", () => {
            model.set("x_extent", model.get("x_extent") * 2.0);
            model.save_changes();
          });
          el.querySelector("#mb-reset").addEventListener("click", () => {
            model.set("x_center", DEFAULTS.x_center);
            model.set("y_center", DEFAULTS.y_center);
            model.set("x_extent", DEFAULTS.x_extent);
            model.set("max_iter", DEFAULTS.max_iter);
            model.set("peak_nits", DEFAULTS.peak_nits);
            model.set("cmap_name", DEFAULTS.cmap_name);
            model.set("hdr_enabled", true);
            model.save_changes();
          });

          // Preset views: known Mandelbrot navigation points where HDR
          // glow is broad enough to read at a glance (extended bright filament structure).
          const PRESETS = {
            "default":  { x_center: -0.7,     y_center:  0.0,   x_extent: 3.0,    max_iter: 512,  cmap_name: "fire-purple"    },
            "seahorse": { x_center: -0.748,   y_center:  0.103, x_extent: 0.05,   max_iter: 1024, cmap_name: "ember"          },
            "antenna":  { x_center: -1.7748,  y_center:  0.0,   x_extent: 0.06,   max_iter: 1024, cmap_name: "ice"            },
            "spirals":  { x_center: -0.745,   y_center:  0.113, x_extent: 0.005,  max_iter: 1024, cmap_name: "twilight-burst" },
          };
          el.querySelector(".mb-presets").addEventListener("click", (ev) => {
            const btn = ev.target.closest("button[data-preset]");
            if (!btn) return;
            const p = PRESETS[btn.dataset.preset];
            if (!p) return;
            for (const [k, v] of Object.entries(p)) model.set(k, v);
            model.save_changes();
          });

          // HDR toggle
          hdrCb.addEventListener("change", () => {
            model.set("hdr_enabled", hdrCb.checked);
            model.save_changes();
          });

          // Colormap dropdown
          cmapSel.addEventListener("change", () => {
            model.set("cmap_name", cmapSel.value);
            model.save_changes();
          });

          // Slider live preview, only commit on change (release) to avoid Python spam
          iterSlider.addEventListener("input", () => { iterVal.textContent = iterSlider.value; });
          iterSlider.addEventListener("change", () => {
            model.set("max_iter", parseInt(iterSlider.value, 10));
            model.save_changes();
          });
          peakSlider.addEventListener("input", () => { peakVal.textContent = peakSlider.value; });
          peakSlider.addEventListener("change", () => {
            model.set("peak_nits", parseFloat(peakSlider.value));
            model.save_changes();
          });
        }
        export default { render };
        """


    return (MandelbrotExplorer,)


@app.cell
def _(MandelbrotExplorer, dr_box, mandelbrot, mo, np):
    explorer = MandelbrotExplorer()

    # DR snapshot at the explorer's default view (it doesn't update as you zoom).
    _mb_smooth, _mb_interior = mandelbrot(width=720, height=460, max_iter=512)

    mo.vstack([
        explorer,
        dr_box(
            np.log1p(_mb_smooth),
            interior_mask=_mb_interior,
            label="Mandelbrot (log₁p, default view)",
        ),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's talk about dynamic range of different datasets — because not every kind of data benefits equally from HDR. Some datasets are essentially flat (photos in good lighting, screenshots, line plots), and SDR shows all of it without breaking a sweat. Others carry orders of magnitude more variation than SDR can convey, and that's where HDR shines (pun intended).

    Certain datasets lend themselves the best to HDR viewing:

    - **Astronomy** — deep-sky exposures combine bright stellar cores with faint nebular wings spanning 4–6 orders of magnitude.
    - **Fluorescence microscopy** — a single channel can span 2–3 orders of magnitude just from labeling density (bright cell membranes versus dim cytoplasm).
    - **Fractals** — the smooth-iteration count near the Mandelbrot boundary is heavily skewed toward "just-escaped" pixels, with far higher density than the body.
    - **Energy spectra and FFTs** — log-magnitude is often the only readable representation, precisely because the linear range is too wide.
    - **Density / kernel-estimate plots** — sharp peaks over near-uniform backgrounds.

    How do we measure that for a given dataset? Formula and simple numpy code in the next two cells. Then we'll apply it to the first example below: a 19th-century photographic plate of the Horsehead Nebula.
    """)
    return


@app.cell(hide_code=True)
def _(mo, np):
    def dynamic_range(arr, *, ignore_zero=True):
        """Compute dynamic range as max/min ratio plus stops and log10. Skips
        non-positive and non-finite values when ignore_zero=True."""
        a = np.asarray(arr, dtype=np.float64)
        a = a[np.isfinite(a)]
        if ignore_zero:
            a = a[a > 0]
        if a.size == 0:
            return None
        lo, hi = float(a.min()), float(a.max())
        ratio = hi / lo
        return {
            "min": lo, "max": hi, "ratio": ratio,
            "stops": float(np.log2(ratio)),
            "log10": float(np.log10(ratio)),
        }


    def dr_box(arr, *, label="dynamic range", interior_mask=None):
        """Render a small infographic box showing the DR stats of a 2D array.
        Pass `label` to title the box (e.g. dataset name). Pass `interior_mask`
        (boolean array) to exclude pixels (fractal interiors, NaN regions, etc.).
        Returns mo.Html ready to drop into a vstack."""
        a = np.asarray(arr)
        if interior_mask is not None:
            a = a[~np.asarray(interior_mask, dtype=bool)]
        dr = dynamic_range(a)
        if dr is None:
            return mo.Html('<div style="opacity:0.6;">No positive values to compute DR.</div>')

        # Format min/max compactly: integer when both are whole, else 4 sig figs
        if dr["min"] >= 1 and dr["max"] >= 1 and dr["min"] == int(dr["min"]) and dr["max"] == int(dr["max"]):
            rng = f"{int(dr['min']):,} &rarr; {int(dr['max']):,}"
        else:
            rng = f"{dr['min']:.4g} &rarr; {dr['max']:.4g}"

        return mo.Html(f"""
    <div style="display:flex; align-items:center; gap:20px; padding:12px 18px;
                margin-top:8px;
                border:1px solid color-mix(in srgb, currentColor 18%, transparent);
                border-radius:10px;
                font-family: system-ui, -apple-system, sans-serif;
                font-size:13px; line-height:1.35; color: inherit;
                background: color-mix(in srgb, currentColor 4%, transparent);
                flex-wrap:wrap;">
      <div style="font-size:11px; opacity:0.65; text-transform:uppercase;
                  letter-spacing:0.08em; min-width:120px;">{label}</div>
      <div style="display:flex; gap:24px; flex-wrap:wrap; align-items:baseline;">
        <div>
          <div style="font-size:22px; font-weight:700;
                      font-variant-numeric:tabular-nums; line-height:1;">{dr['ratio']:.1f}&times;</div>
          <div style="font-size:11px; opacity:0.65; margin-top:2px;">max &divide; min</div>
        </div>
        <div>
          <div style="font-size:22px; font-weight:700;
                      font-variant-numeric:tabular-nums; line-height:1;">{dr['stops']:.1f}</div>
          <div style="font-size:11px; opacity:0.65; margin-top:2px;">stops (log&#8322;)</div>
        </div>
        <div>
          <div style="font-size:22px; font-weight:700;
                      font-variant-numeric:tabular-nums; line-height:1;">{dr['log10']:.2f}</div>
          <div style="font-size:11px; opacity:0.65; margin-top:2px;">log&#8321;&#8320;</div>
        </div>
        <div style="opacity:0.85;">range: <code style="font-size:12px;">{rng}</code></div>
      </div>
    </div>
    """)


    return dr_box, dynamic_range


@app.cell(hide_code=True)
def _(HDRImage, dr_box, fetch_asset, imshow, mo):
    import io as _io
    from astropy.io import fits

    # Real astronomy data: Horsehead Nebula (B33 / IC 434) photographic plate.
    # Source: astropy tutorials sample. ~6x dynamic range -- modest by deep-Hubble
    # standards, but enough that the brightest stars + Halpha glow hit the HDR
    # top end while diffuse dust stays in SDR luminance.
    with fits.open(_io.BytesIO(fetch_asset("HorseHead.fits"))) as _hdul:
        horsehead = _hdul[0].data.astype(float)

    horsehead_hdr = imshow(
        horsehead,
        cmap="ember",
        peak_nits=4500,
        normalize="linear",
        clip_percentile=(0.5, 99.7),
        label="Horsehead Nebula (B33 / IC 434) -- HDR",
    )
    horsehead_sdr = HDRImage(
        image_data_url=horsehead_hdr.image_data_url,
        label="Same pixels, CSS-clamped to SDR",
        clamp_to_sdr=True,
    )
    mo.vstack([
        mo.hstack([horsehead_hdr, horsehead_sdr], gap=1, widths="equal"),
        dr_box(horsehead, label="Horsehead Nebula"),
    ])
    return (horsehead,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next domain: **fluorescence microscopy** — where HDR has practical day-to-day value for working biologists.

    In a fluorescence image, you have a limited number of photons. The brightest features are densely-labeled organelles or cell membranes collecting tens of thousands of photons per pixel. The faintest are cytoplasm and background, sitting near the camera's read-noise floor at maybe single-digit photon counts. The biology lives in the contrast between them.

    For decades, microscopists fought this with manual contrast adjustment, gamma curves, and the dreaded auto-stretch. HDR display lets you preserve the original contrast — same pixels, same data, just using more of the screen's luminance range.

    Below: a short tour of how these images are produced, how viewing has evolved from the eyepiece to qCMOS sensors, the dynamic range a modern fluorescence camera offers, and what it would take to put HDR rendering inside a real-world bioimaging viewer like `viv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Fluorescence imaging, briefly

    A specimen is tagged with a fluorescent dye or genetically encoded protein (e.g. GFP), excited at one wavelength, and longer-wavelength emission is captured by a camera through an optical filter. Each pixel reports the photon count integrated over the exposure window. Densely labeled features (cell membranes, nuclei) may collect tens of thousands of photons per pixel; faint cytoplasm or background may collect only a few, sitting near the camera's read-noise floor. **That spread is the dynamic range** — and the more of it you preserve, the more biology you can see in one frame.

    #### A short history of looking at fluorescent cells

    | Era | How images were viewed |
    |---|---|
    | Pre-1900s | Natural fluorescence observed by eye through prisms/filters; no imaging |
    | 1911 | Oskar Heimstädt builds the first fluorescence microscope (Reichert). Specimens viewed live through the eyepiece. |
    | 1950s–70s | Photographic film: long exposures, no realtime review |
    | 1980s–90s | Scientific CCDs (Photometrics, Princeton Instruments): ~12-bit digital, live preview |
    | 2000s+ | EMCCDs, then sCMOS: ~16 bits, low read noise, full-frame at >100 fps |
    | Today | Back-illuminated sCMOS at ~95% quantum efficiency; qCMOS for photon counting |

    #### Modern camera dynamic range

    | Camera | Type | DR (max signal / read noise) |
    |---|---|---:|
    | Hamamatsu ORCA-Fusion | sCMOS | ~21,400 : 1 (~14 stops) |
    | Andor Sona 4.2B-11 | sCMOS | ~33,000 : 1 (~15 stops) |
    | Photometrics Prime BSI Express | back-illuminated sCMOS | ~30,000 : 1 |

    The `cells3d` sample used below is a 16-bit recording from this generation of camera. The membrane channel preserves ~150× DR even after the data was compressed to 16 bits. The HDR pipeline reads it natively — no tone mapping required.

    #### Viv integration, sketched

    [viv](https://github.com/hms-dbmi/viv) renders OME-Zarr / OME-TIFF tiles via WebGL canvas — fast, multi-channel, multi-resolution, deck.gl underneath. WebGL canvas does not currently emit HDR pixels in stable Chromium (verified earlier in this notebook via the `configureHighDynamicRange` API check). Two paths to HDR-viv:

    1. **Tile-encoding path**: server pre-encodes each tile as a PQ Rec2020 PNG; viv composites them as `<img>` overlays instead of WebGL textures. Loses some shader-driven interactivity (channel mixing, gamma sliders) but gets HDR for free.
    2. **Wait for browser shader-side HDR**: the `configureHighDynamicRange` API is in the WICG canvas-color-space draft. Once shipped, viv keeps its WebGL pipeline and opts the canvas into HDR mode.
    """)
    return


@app.cell(hide_code=True)
def _(HDRImage, dr_box, fetch_asset, imshow, mo):
    import io as _io
    import tifffile

    # Real fluorescence-microscopy data: scikit-image's cells3d sample.
    # Two-channel z-stack (z=60, c=2, y=256, x=256) of human pluripotent stem
    # cells. Channel 0 = membrane stain, channel 1 = DNA (nuclei).
    # Native dynamic range ~150x in the membrane channel -- genuinely HDR.
    cells_zct = tifffile.imread(_io.BytesIO(fetch_asset("cells3d.tif")))
    _mid_z = cells_zct.shape[0] // 2
    nuclei_2d = cells_zct[_mid_z, 1].astype(float)
    membr_2d  = cells_zct[_mid_z, 0].astype(float)

    nuclei_hdr = imshow(
        nuclei_2d, cmap="ice", peak_nits=4000,
        normalize="linear", clip_percentile=(0.5, 99.7),
        label="Nuclei channel -- HDR (ice cmap)",
    )
    nuclei_sdr = HDRImage(
        image_data_url=nuclei_hdr.image_data_url,
        label="Nuclei -- SDR-clamped",
        clamp_to_sdr=True,
    )
    membr_hdr = imshow(
        membr_2d, cmap="matrix-green", peak_nits=4000,
        normalize="linear", clip_percentile=(0.5, 99.7),
        label="Membranes channel -- HDR (matrix-green cmap)",
    )
    membr_sdr = HDRImage(
        image_data_url=membr_hdr.image_data_url,
        label="Membranes -- SDR-clamped",
        clamp_to_sdr=True,
    )

    mo.vstack([
        mo.hstack([nuclei_hdr, nuclei_sdr], gap=1, widths="equal"),
        dr_box(nuclei_2d, label="cells3d — nuclei channel"),
    ])
    return membr_2d, membr_hdr, membr_sdr, nuclei_2d


@app.cell
def _(dr_box, membr_2d, membr_hdr, membr_sdr, mo):
    mo.vstack([
        mo.hstack([membr_hdr, membr_sdr], gap=1, widths="equal"),
        dr_box(membr_2d, label="cells3d — membrane channel"),
    ])
    return


@app.cell(hide_code=True)
def _(dynamic_range, horsehead, mandelbrot, membr_2d, mo, np, nuclei_2d):
    # DR survey: applies dynamic_range() to every dataset shown in this notebook.
    # Mandelbrot data is recomputed here at the explorer's default view since the
    # static side-by-side cell that originally provided it has been retired.
    _mb_smooth, _mb_interior = mandelbrot(width=720, height=460, max_iter=512)
    mb_dr   = dynamic_range(np.log1p(_mb_smooth)[~_mb_interior])
    hh_dr   = dynamic_range(horsehead)
    nuc_dr  = dynamic_range(nuclei_2d)
    memb_dr = dynamic_range(membr_2d)

    mo.md(f"""
    ### Dynamic range across this notebook's datasets

    | Dataset | min (positive) | max | ratio | stops | log₁₀ |
    |---|---:|---:|---:|---:|---:|
    | Mandelbrot smooth-iter (log₁p stretched) | {mb_dr['min']:.2g} | {mb_dr['max']:.2g} | {mb_dr['ratio']:.1f}× | {mb_dr['stops']:.1f} | {mb_dr['log10']:.2f} |
    | Horsehead Nebula (FITS) | {hh_dr['min']:.0f} | {hh_dr['max']:.0f} | {hh_dr['ratio']:.1f}× | {hh_dr['stops']:.1f} | {hh_dr['log10']:.2f} |
    | cells3d nuclei channel | {nuc_dr['min']:.0f} | {nuc_dr['max']:.0f} | {nuc_dr['ratio']:.1f}× | {nuc_dr['stops']:.1f} | {nuc_dr['log10']:.2f} |
    | cells3d membrane channel | {memb_dr['min']:.0f} | {memb_dr['max']:.0f} | {memb_dr['ratio']:.1f}× | {memb_dr['stops']:.1f} | {memb_dr['log10']:.2f} |

    The membrane channel dominates — its ~150× spread between the brightest cell-edge segments and the dimmest cytoplasm is exactly the structure HDR display reproduces faithfully and SDR has to crush.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Wrap-up

    Three demos, one library: a Mandelbrot explorer, a 19th-century photographic plate of the Horsehead Nebula, and a real fluorescence microscope frame of stem cells. All four datasets have different native dynamic ranges, and the membrane channel of `cells3d` is the surprise winner — its 159× ratio between brightest and dimmest signals is more than the Horsehead's 6×, which is why the cells glow harder than the nebula does on your screen.

    If you want to use this in your own work:

    ```python
    from hdrviz import hdr_imshow
    widget = imshow(my_array, cmap="inferno-hdr", peak_nits=4000)
    widget
    ```

    The library is the smallest possible thing that works. Future work that would extend it:

    - **Browser API maturity** — when Chromium ships `configureHighDynamicRange()` for `<canvas>`, we can render directly without going through PNG encoding. That unlocks real-time HDR for animated and interactive content (pan/zoom, video, simulation).
    - **Matplotlib chrome** — borrow matplotlib for axes, ticks, and colorbars, composite our HDR `<img>` underneath. Currently the data area is HDR but there are no axis labels.
    - **Multi-channel viv-style viewer** — layer multiple HDR `<img>` channels with z-scrolling and channel mixing. Anywidget already has the trait machinery; the missing piece is a tile-encoding pipeline.

    The recipe is simple: PQ-encoded RGB nits + Rec2020 ICC profile + `<img>` tag = HDR rendering in any modern Chromium browser, today.
    """)
    return


if __name__ == "__main__":
    app.run()
