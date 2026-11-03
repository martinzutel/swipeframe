#!/usr/bin/env python3
"""Builds the English and Spanish pages plus SEO files.

Run from the repo root:  python3 _build/build.py
Change SITE_URL if the site lives on another domain.
"""
import html, json, pathlib

SITE_URL = "https://swipeframe.scottyandbilldev.workers.dev"

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "_build" / "template.html").read_text(encoding="utf-8")

EN = {
    "lang": "en", "path": "/", "og_locale": "en_US", "og_locale_alt": "es_LA",
    "title": "Instagram Panorama Splitter – Seamless Carousel Maker | Swipeframe",
    "description": "Split a wide photo into a seamless Instagram carousel or profile grid in seconds. Free, no signup, perfect 1080 px slides. Your photo never leaves your device.",
    "og_title": "Swipeframe: split panoramas into seamless Instagram carousels",
    "og_description": "Drop in a wide photo and get perfectly sized slides that line up edge to edge. Free and private.",
    "og_alt": "A panorama split into three Instagram carousel slides on a green cutting mat.",
    "og_file": "og-en.png",
    "alt_label": "Español",
    "h1": "Split a panorama into a seamless Instagram carousel",
    "lede": "Drop in a wide photo and get perfectly sized slides that line up edge to edge when people swipe. Free, no signup, and your photo never leaves your device.",
    "a_mat": "Your photo and its slices", "a_overview": "Your photo with the cut lines between slides",
    "drop_here": "Drop the photo to load it", "a_slices": "Slices", "your_name": "yourname", "a_settings": "Settings",
    "l_photo": "Photo", "choose_photo": "Choose a photo", "pick_hint": "Or drag it onto the page, or paste it.",
    "l_format": "Post as", "carousel": "Carousel", "profile_grid": "Profile grid",
    "l_shape": "Slide shape", "portrait": "Portrait", "square": "Square", "tall": "Tall",
    "l_slides": "Number of slides", "fewer": "Fewer slides", "more": "More slides", "best_fit": "Best fit",
    "l_rows": "Rows of three", "fewer_rows": "Fewer rows", "more_rows": "More rows",
    "l_edges": "Edges", "crop_fill": "Crop to fill", "whole_photo": "Show whole photo",
    "l_position": "Crop position", "l_border": "Border", "white": "White", "black": "Black", "blurred": "Blurred",
    "zip_instead": "Download as .zip instead",
    "howto_title": "How to post a seamless panorama on Instagram",
    "steps": [
        "Choose a wide photo. Swipeframe suggests how many slides keep the most of it.",
        "Pick Portrait (4:5) for the biggest slides in the feed, or Square (1:1).",
        "Drag the photo to set what stays in frame.",
        "Tap Save. On a phone, choose Save images to put them straight in your camera roll. On a computer you get a .zip file.",
        "In Instagram, tap +, turn on Select multiple and pick the slides in order, starting with 1.",
        "Post it. Every swipe continues the picture.",
    ],
    "faq_title": "Questions",
    "faq": [
        ("How many slides can an Instagram carousel have?", "Up to 20 photos. Swipeframe splits your image into anywhere from 2 to 20 slides."),
        ("What size should carousel slides be?", "1080 × 1350 px (4:5 portrait) takes up the most space in the feed. Swipeframe exports every slide at exactly 1080 px wide, so Instagram has nothing to resize."),
        ("Why is there a visible line between my slides?", "Make sure every slide has the same shape and that you selected them in order. Mixing shapes makes Instagram crop each slide differently."),
        ("How does the profile grid split work?", "It cuts one image into rows of three posts, so your profile shows a single big picture. Upload post 1 first; it ends up in the bottom right once all the posts are up."),
        ("Does Swipeframe upload my photo?", "No. The cutting happens in your browser, so your photo stays on your phone or computer."),
        ("Is it free?", "Yes. No account, no watermark and no limits."),
    ],
    "footer_left": "Swipeframe is free and runs in your browser. Made in Buenos Aires.",
    "footer_right": "Not affiliated with Instagram or Meta.",
    "app_name_desc": "Free online tool that splits a panorama into a seamless Instagram carousel or profile grid.",
    "js": {
        "locale": "en-US", "slide": "slide", "slides": "slides", "post": "post", "posts": "posts",
        "fileSlide": "slide", "filePost": "post", "zipCarousel": "carousel", "zipGrid": "grid",
        "saveShare": "Save {n} {u}", "saveZip": "Download {n} {u}",
        "sumFill": "{n} {u}, {w} × {h} px each. Keeps <b>{k}%</b> of your photo.",
        "sumFit": "{n} {u}, {w} × {h} px each. The whole photo fits, with a border.",
        "total": "{w} × {h} px in total",
        "dragX": "<b>Drag sideways</b> on the photo to move the crop.",
        "dragY": "<b>Drag up or down</b> on the photo to move the crop.",
        "saveOne": "Save number {n} on its own", "slideN": "Slide {n}", "postN": "Post {n}",
        "tapSlice": "Tap a slice to save just that one.", "clickSlice": "Click a slice to download just that one.",
        "pvCarousel": "How it swipes", "pvCarouselLede": "This is what your followers see. Swipe through to check the seams.",
        "pvGrid": "How your profile will look", "pvGridLede": "Each tile is its own post. Together they form one picture on your profile.",
        "tipCarouselTitle": "Select them in order",
        "tipCarousel": "When you pick photos in Instagram, tap slide 1 first and keep going in order. The files are numbered to make it easy.",
        "tipGridTitle": "Upload post 1 first",
        "tipGrid34": "Instagram puts your newest post at the top left, so start with post 1 and finish with the highest number. Tall (3:4) matches the profile grid exactly.",
        "tipGridOther": "Instagram puts your newest post at the top left, so start with post 1. The profile grid crops posts to 3:4, so choose Tall for tiles that line up exactly.",
        "preparing": "Preparing…", "downloaded": "Downloaded {n} images.",
        "notImage": "That file isn't an image. Choose a JPG or PNG.",
        "cantOpen": "Your browser can't open this image. Export it as a JPG and try again.",
        "exportFail": "Saving didn't work. Try a smaller photo or fewer slides.",
        "tapAgain": "Your browser needs one more tap. Press Save again.",
        "shareFail": "The save sheet didn't open. Use Download as .zip instead.",
        "loaded": "{name}, {w} × {h} px", "pasted": "Pasted image", "choosePhotoAgain": "Choose another photo",
        "sampleNote": "Showing a sample panorama.", "pickHintTouch": "Pick a wide photo from your camera roll.",
    },
}

ES = {
    "lang": "es", "path": "/es/", "og_locale": "es_LA", "og_locale_alt": "en_US",
    "title": "Dividir foto panorámica para Instagram – Carrusel sin cortes | Swipeframe",
    "description": "Divide una foto ancha en un carrusel de Instagram sin cortes o en una cuadrícula para tu perfil. Gratis, sin registro, a 1080 px. Tu foto no sale de tu dispositivo.",
    "og_title": "Swipeframe: convierte una panorámica en un carrusel de Instagram sin cortes",
    "og_description": "Sube una foto ancha y obtén slides del tamaño exacto que encajan al deslizar. Gratis y privado.",
    "og_alt": "Una foto panorámica dividida en tres slides de carrusel de Instagram sobre una plancha de corte verde.",
    "og_file": "og-es.png",
    "alt_label": "English",
    "h1": "Convierte una panorámica en un carrusel de Instagram sin cortes",
    "lede": "Sube una foto ancha y obtén slides del tamaño exacto que encajan borde con borde al deslizar. Gratis, sin registro, y tu foto nunca sale de tu dispositivo.",
    "a_mat": "Tu foto y sus partes", "a_overview": "Tu foto con las líneas de corte entre slides",
    "drop_here": "Suelta la foto para cargarla", "a_slices": "Partes", "your_name": "tunombre", "a_settings": "Ajustes",
    "l_photo": "Foto", "choose_photo": "Elegir una foto", "pick_hint": "O arrástrala a la página, o pégala.",
    "l_format": "Publicar como", "carousel": "Carrusel", "profile_grid": "Cuadrícula",
    "l_shape": "Forma de cada slide", "portrait": "Vertical", "square": "Cuadrada", "tall": "Alta",
    "l_slides": "Cantidad de slides", "fewer": "Menos slides", "more": "Más slides", "best_fit": "Ajuste ideal",
    "l_rows": "Filas de tres", "fewer_rows": "Menos filas", "more_rows": "Más filas",
    "l_edges": "Bordes", "crop_fill": "Recortar para llenar", "whole_photo": "Mostrar foto entera",
    "l_position": "Posición del recorte", "l_border": "Borde", "white": "Blanco", "black": "Negro", "blurred": "Desenfocado",
    "zip_instead": "Descargar como .zip",
    "howto_title": "Cómo publicar una panorámica sin cortes en Instagram",
    "steps": [
        "Elige una foto ancha. Swipeframe sugiere cuántas slides conservan más de la imagen.",
        "Elige Vertical (4:5) para las slides más grandes del feed, o Cuadrada (1:1).",
        "Arrastra la foto para decidir qué queda dentro del encuadre.",
        "Toca Guardar. En el celular, elige Guardar imágenes para que vayan directo a tu galería. En la computadora se descarga un .zip.",
        "En Instagram, toca +, activa Seleccionar varias y elige las slides en orden, empezando por la 1.",
        "Publica. Cada deslizamiento continúa la imagen.",
    ],
    "faq_title": "Preguntas frecuentes",
    "faq": [
        ("¿Cuántas fotos puede tener un carrusel de Instagram?", "Hasta 20. Swipeframe divide tu imagen en 2 a 20 slides."),
        ("¿Qué tamaño deben tener las slides del carrusel?", "1080 × 1350 px (vertical 4:5) ocupa más espacio en el feed. Swipeframe exporta cada slide a exactamente 1080 px de ancho, así Instagram no tiene que redimensionar nada."),
        ("¿Por qué se ve una línea entre mis slides?", "Revisa que todas las slides tengan la misma forma y que las hayas elegido en orden. Si mezclas formas, Instagram recorta cada una de forma distinta."),
        ("¿Cómo funciona la división para la cuadrícula del perfil?", "Corta una imagen en filas de tres publicaciones para que tu perfil muestre una sola foto grande. Sube primero la publicación 1; quedará abajo a la derecha cuando estén todas."),
        ("¿Swipeframe sube mi foto a algún servidor?", "No. El corte se hace en tu navegador, así que tu foto se queda en tu celular o computadora."),
        ("¿Es gratis?", "Sí. Sin cuenta, sin marca de agua y sin límites."),
    ],
    "footer_left": "Swipeframe es gratis y funciona en tu navegador. Hecho en Buenos Aires.",
    "footer_right": "Sin relación con Instagram ni Meta.",
    "app_name_desc": "Herramienta online gratuita que divide una foto panorámica en un carrusel de Instagram sin cortes o en una cuadrícula para el perfil.",
    "js": {
        "locale": "es-AR", "slide": "slide", "slides": "slides", "post": "publicación", "posts": "publicaciones",
        "fileSlide": "slide", "filePost": "post", "zipCarousel": "carrusel", "zipGrid": "cuadricula",
        "saveShare": "Guardar {n} {u}", "saveZip": "Descargar {n} {u}",
        "sumFill": "{n} {u} de {w} × {h} px. Conserva el <b>{k}%</b> de tu foto.",
        "sumFit": "{n} {u} de {w} × {h} px. La foto entera entra, con borde.",
        "total": "{w} × {h} px en total",
        "dragX": "<b>Arrastra hacia los costados</b> sobre la foto para mover el recorte.",
        "dragY": "<b>Arrastra hacia arriba o abajo</b> sobre la foto para mover el recorte.",
        "saveOne": "Guardar solo la número {n}", "slideN": "Slide {n}", "postN": "Publicación {n}",
        "tapSlice": "Toca una parte para guardar solo esa.", "clickSlice": "Haz clic en una parte para descargar solo esa.",
        "pvCarousel": "Cómo se desliza", "pvCarouselLede": "Esto es lo que ven tus seguidores. Desliza para revisar las uniones.",
        "pvGrid": "Cómo se verá tu perfil", "pvGridLede": "Cada parte es una publicación. Juntas forman una sola imagen en tu perfil.",
        "tipCarouselTitle": "Elígelas en orden",
        "tipCarousel": "Al elegir las fotos en Instagram, toca primero la slide 1 y sigue en orden. Los archivos están numerados para que sea fácil.",
        "tipGridTitle": "Sube primero la publicación 1",
        "tipGrid34": "Instagram pone la publicación más nueva arriba a la izquierda, así que empieza por la 1 y termina con el número más alto. Alta (3:4) coincide exactamente con la cuadrícula del perfil.",
        "tipGridOther": "Instagram pone la publicación más nueva arriba a la izquierda, así que empieza por la 1. La cuadrícula del perfil recorta las publicaciones a 3:4; elige Alta para que encajen perfecto.",
        "preparing": "Preparando…", "downloaded": "Se descargaron {n} imágenes.",
        "notImage": "Ese archivo no es una imagen. Elige un JPG o PNG.",
        "cantOpen": "Tu navegador no puede abrir esta imagen. Expórtala como JPG y vuelve a intentarlo.",
        "exportFail": "No se pudo guardar. Prueba con una foto más chica o menos slides.",
        "tapAgain": "Tu navegador necesita un toque más. Toca Guardar otra vez.",
        "shareFail": "No se abrió el menú para guardar. Usa Descargar como .zip.",
        "loaded": "{name}, {w} × {h} px", "pasted": "Imagen pegada", "choosePhotoAgain": "Elegir otra foto",
        "sampleNote": "Se muestra una panorámica de ejemplo.", "pickHintTouch": "Elige una foto ancha de tu galería.",
    },
}

def e(s):
    return html.escape(s, quote=True)

def page(L, other):
    url = SITE_URL + L["path"]
    steps = "".join(f"<li>{e(s)}</li>" for s in L["steps"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in L["faq"])
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebApplication", "@id": url + "#app", "name": "Swipeframe", "url": url,
             "description": L["app_name_desc"], "inLanguage": L["lang"],
             "applicationCategory": "MultimediaApplication", "operatingSystem": "Any (web browser)",
             "browserRequirements": "Requires JavaScript",
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
             "image": SITE_URL + "/assets/" + L["og_file"],
             "featureList": [L["carousel"], L["profile_grid"], "1080 px JPG", "4:5, 1:1, 3:4"]},
            {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": L["lang"],
             "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]]},
        ],
    }
    vals = {k: e(v) for k, v in L.items() if isinstance(v, str)}
    vals.update({
        "url": url, "url_en": SITE_URL + "/", "url_es": SITE_URL + "/es/",
        "og_image": SITE_URL + "/assets/" + L["og_file"],
        "home_path": L["path"], "alt_path": other["path"], "alt_lang": other["lang"],
        "howto_steps": steps, "faq_items": faq,
        "jsonld": json.dumps(jsonld, ensure_ascii=False).replace("</", "<\\/"),
        "js_strings": json.dumps(L["js"], ensure_ascii=False).replace("</", "<\\/"),
    })
    out = TEMPLATE
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", v)
    left = [m for m in __import__("re").findall(r"\{\{(\w+)\}\}", out)]
    assert not left, f"unfilled placeholders: {left}"
    return out

(ROOT / "index.html").write_text(page(EN, ES), encoding="utf-8")
(ROOT / "es").mkdir(exist_ok=True)
(ROOT / "es" / "index.html").write_text(page(ES, EN), encoding="utf-8")

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE_URL}/sitemap.xml\n")

(ROOT / "sitemap.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE_URL}/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/"/>
    <xhtml:link rel="alternate" hreflang="es" href="{SITE_URL}/es/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}/"/>
  </url>
  <url>
    <loc>{SITE_URL}/es/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/"/>
    <xhtml:link rel="alternate" hreflang="es" href="{SITE_URL}/es/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}/"/>
  </url>
</urlset>
""")

(ROOT / "site.webmanifest").write_text(json.dumps({
    "name": "Swipeframe", "short_name": "Swipeframe",
    "description": EN["app_name_desc"], "start_url": "/", "scope": "/", "display": "standalone",
    "background_color": "#F4F5F2", "theme_color": "#2E5B4C",
    "icons": [
        {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "/assets/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}, indent=2) + "\n")

(ROOT / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/assets/*
  Cache-Control: public, max-age=2592000

/_build/*
  X-Robots-Tag: noindex
""")

(ROOT / "404.html").write_text("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Swipeframe</title><meta name="robots" content="noindex">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<style>
@font-face{font-family:"Schibsted Grotesk";src:url("/assets/schibsted.woff") format("woff");font-weight:400 900;font-display:swap}
:root{--paper:#F4F5F2;--ink:#18201C;--muted:#5B6660;--mat:#2E5B4C}
@media (prefers-color-scheme:dark){:root{--paper:#111513;--ink:#E7ECE9;--muted:#9AA59F;--mat:#1F3F35;color-scheme:dark}}
body{margin:0;min-height:100vh;display:grid;place-items:center;background:var(--paper);color:var(--ink);font:400 17px/1.5 "Schibsted Grotesk",system-ui,sans-serif;padding:24px}
main{max-width:34ch}h1{font-size:34px;letter-spacing:-.03em;line-height:1.1;margin:0 0 10px}p{color:var(--muted);margin:0 0 22px}
a{display:inline-block;background:var(--mat);color:#fff;text-decoration:none;font-weight:600;padding:12px 18px;border-radius:10px}
</style></head><body><main><h1>This page doesn't exist</h1><p>The link may be old or mistyped. The splitter is on the home page.</p><a href="/">Open Swipeframe</a></main></body></html>
""")

print("built:", SITE_URL)
