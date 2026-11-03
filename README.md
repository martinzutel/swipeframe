# Swipeframe

Free, in-browser tool that splits a wide photo into a seamless Instagram carousel or profile grid at 1080 px. No uploads, no signup. English at `/`, Spanish at `/es/`.

## Editing

The pages are generated. Edit `_build/template.html` (layout, styles, script) or the text in `_build/build.py`, then run:

```
python3 _build/build.py
```

If the site moves to its own domain, change `SITE_URL` at the top of `build.py` and rebuild so canonical links, the sitemap and link previews point to it.

## Deploying

Cloudflare Pages, connected to this repo. Framework preset: None. Build command: empty. Output directory: `/`.

## Ads

Paste the AdSense script tag into the `<head>` of `_build/template.html` and ad units into the `ad-slot` divs, then rebuild.

Font: Schibsted Grotesk (SIL Open Font License, see `assets/schibsted-OFL.txt`).
