import json,html,os
# Site base URL: change this one line to move the site (e.g. custom domain).
BASE="https://curtisrobertrc-droid.github.io/brickandbudget"
from urllib.parse import urlparse
P=urlparse(BASE).path.rstrip("/")
CSS="""*{box-sizing:border-box}body{margin:0;font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1d2733;background:#f6f7f9}
a{color:#1f4e79}header{background:#1f3a5f;color:#fff}header .w{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;padding:14px 18px}
header a{color:#fff;text-decoration:none}.logo{font-weight:700;font-size:20px;letter-spacing:.3px}nav a{margin-left:16px;font-size:15px;opacity:.9}
.w{max-width:860px;margin:0 auto;padding:0 18px}main{padding:24px 0 40px}h1{font-size:30px;line-height:1.2;margin:8px 0 10px}h2{margin-top:32px;font-size:21px}
.lead{color:#4a5868;font-size:18px}.card{background:#fff;border:1px solid #dde3ea;border-radius:12px;padding:20px;margin:18px 0}
.inputs{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}label{display:block;font-size:14px;font-weight:600;color:#33414f}
input{display:block;width:100%;margin-top:6px;padding:11px 12px;font-size:17px;border:1px solid #b9c4d0;border-radius:8px}input:focus{outline:2px solid #1f4e79;border-color:#1f4e79}
button{margin-top:16px;background:#1f3a5f;color:#fff;border:0;border-radius:8px;padding:12px 22px;font-size:16px;font-weight:600;cursor:pointer}
.out{margin-top:18px;border-top:1px solid #e3e8ee}.out div{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid #eef1f5}.out strong{font-size:18px}
.disc{font-size:14px;background:#eef2f7;border-left:4px solid #1f3a5f;padding:10px 14px;border-radius:6px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.grid a{display:block;background:#fff;border:1px solid #dde3ea;border-radius:12px;padding:16px;text-decoration:none;color:#1d2733}.grid a strong{display:block;color:#1f3a5f;margin-bottom:4px}
details{background:#fff;border:1px solid #dde3ea;border-radius:8px;padding:12px 14px;margin:8px 0}summary{font-weight:600;cursor:pointer}
footer{background:#1d2733;color:#c4ccd6;font-size:14px;padding:24px 0}footer a{color:#e6ebf0;margin-right:14px}.note{font-size:14px;color:#5b6876}"""
def page(path,title,desc,body,schema=None):
    sc="".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in (schema or []))
    h=f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{BASE}/{path.replace('index.html','')}">
<link rel="stylesheet" href="/assets/style.css">{sc}</head><body><header><div class="w"><a class="logo" href="/">Brick &amp; Budget</a><nav><a href="/#calculators">Calculators</a><a href="/about.html">About</a></nav></div></header>
<main><div class="w">{body}</div></main><footer><div class="w"><p><a href="/about.html">About</a><a href="/privacy.html">Privacy</a><a href="/disclosure.html">Affiliate disclosure</a><a href="mailto:brickandbudget.uk@gmail.com">Contact</a></p>
<p>Brick &amp; Budget gives estimates only. Always check quantities with your supplier and allow for site conditions.</p></div></footer></body></html>"""
    h=h.replace('href="/','href="'+P+'/').replace('src="/','src="'+P+'/')
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(h)
calcs=[
("plasterboard","Plasterboard Calculator UK","How many sheets of plasterboard do you need? Work out boards, screws and tape for any wall or ceiling.",
 ["Measure the length and height of each wall (or the length and width of a ceiling) in metres.","Deduct doors and windows: a standard internal door is about 1.9 m² (0.84 x 2.04 m).","Standard UK boards are 2400 x 1200 mm, covering 2.88 m². Add 10% for offcuts, or 15% for rooms with lots of corners.","Use 12.5 mm board for walls and ceilings; 15 mm or acoustic board where sound matters, and moisture-resistant board in bathrooms."],
 "A 4 m by 2.4 m wall with one door: 9.6 m² minus 1.9 m² is 7.7 m². Add 10% and divide by 2.88 m², giving 3 sheets.",
 [("Should I buy 2400 or 1800 mm boards?","2400 mm boards mean fewer joints on standard 2.4 m ceilings. 1800 mm boards are easier to carry and fit in a car."),("Screw spacing?","Typically every 230 mm on walls and 150 mm on ceilings for 12.5 mm board; check the board maker's guidance."),("Do I need to skim afterwards?","Either tape and joint for a decorative finish, or skim with a finishing plaster such as multi-finish.")],
 ["British Gypsum: Gyproc board installation guidance (british-gypsum.com)"]),
("plaster","Plaster Calculator: How Much Plaster Do I Need?","Work out how many 25 kg bags of finishing plaster you need for a skim coat, by area and thickness.",
 ["Measure the area in m² (length x height for each wall).","A skim coat of finishing plaster is usually 2 mm, applied in two passes.","Multi-finish covers roughly 10 to 11 m² per 25 kg bag at 2 mm, which is about 1.15 kg per m² per mm.","Add 10% for mixing waste and the first bucket that goes off."],
 "A 12 m² wall at 2 mm: 12 x 2 x 1.15 = 27.6 kg, plus 10% is 30.4 kg, so 2 bags.",
 [("How long does plaster take to dry?","Typically 3 to 7 days for a skim, longer in cold or damp rooms. It is dry when the colour is an even light pink."),("Can I paint new plaster straight away?","Seal it first with a mist coat of watered-down emulsion or a dedicated plaster primer."),("Bonding or multi-finish?","Bonding is an undercoat for building up depth; multi-finish is the final skim coat.")],
 ["British Gypsum: Thistle Multi-Finish product data (british-gypsum.com)"]),
("paint","Paint Calculator UK","Work out how many litres and tins of paint you need for walls and ceilings.",
 ["Measure wall area: total wall width multiplied by height. Ignore small windows; deduct large patio doors.","Check the coverage on the tin, commonly 10 to 14 m² per litre for emulsion.","Plan two coats on most walls, and a mist coat plus two coats on new plaster.","Dark-to-light colour changes may need a third coat."],
 "30 m² of wall, two coats at 12 m² per litre: 30 x 2 / 12 = 5 litres, so one 5 L tin or two 2.5 L tins.",
 [("Does ceiling paint cover the same?","Similar, but ceilings often need a little more because of absorbent surfaces."),("Should I buy trade paint?","Trade emulsions often have better opacity and coverage, but check the coverage figure on the tin."),("How much for woodwork?","Gloss and satinwood cover around 12 to 16 m² per litre; a 750 ml tin does most rooms' skirting and doors.")],
 ["Manufacturer coverage figures printed on the tin"]),
("tiles","Tile Calculator UK: Tiles, Adhesive and Grout","Calculate how many tiles you need, plus adhesive and grout, for floors and walls.",
 ["Measure each wall or floor area in m² and add them together.","Enter the tile size in millimetres.","Add 10% waste for straight lay, 15% for diagonal or herringbone patterns.","Adhesive use depends on trowel size: about 3 to 5 kg per m² is typical for standard tiles."],
 "6 m² with 300 x 600 mm tiles (0.18 m² each): 6 x 1.1 / 0.18 = 36.7, so 37 tiles, about 24 kg adhesive and 3 kg grout.",
 [("Should I buy extra tiles?","Yes. Keep a few spare from the same batch in case one cracks later; batches can vary in shade."),("Which adhesive for large tiles?","Use a flexible, rapid or large-format adhesive and a bigger notched trowel, following the tile maker's guidance."),("Do I need to tank a shower?","Yes, wet areas should be tanked with a waterproofing system before tiling.")],
 ["Tile and adhesive manufacturer coverage guides"]),
("concrete","Concrete Calculator UK","Work out the volume of concrete and the number of ready-mix bags for slabs, bases and paths.",
 ["Measure length and width in metres and depth in millimetres.","Typical depths: 100 mm for a shed base or path, 150 mm for a driveway or garage floor.","Add 5% to 10% for uneven ground.","A 20 kg bag of ready-mix makes roughly 0.01 m³. For larger jobs, ready-mixed concrete delivered by truck is usually cheaper above about 1 m³."],
 "A 3 m by 2 m shed base at 100 mm: 0.6 m³ plus 5% is 0.63 m³, about 64 bags of ready-mix, or around 8 bags of cement in a 1:2:4 mix.",
 [("What mix for a shed base?","A general-purpose 1:2:4 mix (cement:sand:aggregate) or a C20 ready-mix is common."),("Do I need a sub-base?","Usually yes: about 75 to 100 mm of compacted hardcore (MOT Type 1) under the slab."),("How long before I can build on it?","Light use after about 48 hours; concrete reaches most of its strength at 28 days.")],
 ["Concrete supplier and bag manufacturer yield figures"]),
("bricks","Brick Calculator UK: Bricks and Mortar","Calculate how many bricks and how much mortar you need for a wall.",
 ["UK standard bricks are 215 x 102.5 x 65 mm, laid with 10 mm joints.","That gives 60 bricks per m² for a single skin (half-brick wall).","A full-brick (double skin) wall needs 120 per m².","Add 5% for cuts and breakages."],
 "A 5 m long, 1 m high single-skin garden wall: 5 m² x 60 = 300 bricks, plus 5% = 315 bricks and about 0.11 m³ of mortar.",
 [("What mortar mix?","Commonly 1:4 to 1:5 cement to building sand for general brickwork; follow structural guidance for load-bearing walls."),("Do I need foundations?","Yes. Even a small garden wall needs a concrete footing; taller or retaining walls need professional design."),("Do I need planning permission?","Walls over 1 m next to a highway, or over 2 m elsewhere, usually need permission. Check the Planning Portal.")],
 ["Planning Portal: walls and fences (planningportal.co.uk)","Brick Development Association guidance"]),
("flooring","Laminate Flooring Calculator UK","Work out how many packs of laminate or engineered flooring, underlay and beading you need.",
 ["Measure the room length and width in metres. For L-shaped rooms, split into rectangles and add.","Check the m² per pack printed on the box.","Add 5% to 10% for cuts; 15% for herringbone.","Underlay is sold by m²; beading or scotia is sold by length to cover the perimeter."],
 "A 4 m by 3.5 m room: 14 m² plus 8% = 15.1 m², at 2.2 m² per pack that is 7 packs.",
 [("Should I acclimatise flooring?","Most makers recommend leaving packs flat in the room for 48 hours before fitting."),("Expansion gap?","Leave about 8 to 10 mm around the edges, covered by skirting or beading."),("Which way should boards run?","Usually parallel to the main light source or the longest wall.")],
 ["Flooring manufacturer installation instructions"]),
("vat","VAT Calculator UK: Add or Remove 20% VAT","Add VAT to a net price or remove VAT from a gross price, at 20%, 5% or any rate.",
 ["Standard UK VAT is 20%; the reduced rate is 5% (for example some energy-saving materials); some items are zero-rated.","To add VAT, multiply the net amount by 1.2.","To remove VAT, divide the gross amount by 1.2. Do not just subtract 20%.","Enter 1 to add VAT or 2 to remove VAT."],
 "£120 including VAT: £120 / 1.2 = £100 net, so the VAT is £20. Subtracting 20% would wrongly give £96.",
 [("Do builders charge VAT?","Only if VAT registered. The registration threshold is £90,000 of taxable turnover."),("What is the domestic reverse charge?","For some construction services between VAT-registered businesses in CIS, the customer accounts for the VAT instead of the supplier."),("Is VAT charged on new builds?","Construction of new dwellings is generally zero-rated; most renovation work is standard-rated.")],
 ["GOV.UK: VAT rates (gov.uk/vat-rates)","GOV.UK: VAT domestic reverse charge for building and construction services"]),
("skirting","Skirting Board Calculator","Work out how many lengths of skirting board or coving you need for a room.",
 ["Measure the room perimeter: add the length of every wall.","Deduct the width of each doorway.","Skirting is commonly sold in 2.4 m, 3 m, 4.2 m and 4.4 m lengths. Longer lengths mean fewer joints.","Add 10% for mitres and offcuts."],
 "A 14 m perimeter with one 0.85 m doorway: 13.15 m of run, plus 10% at 2.4 m lengths is 7 lengths.",
 [("MDF or timber?","Primed MDF is cheaper, stable and ready to paint; timber suits staining and high-impact areas."),("How do I join internal corners?","Scribing gives a tighter internal joint than a mitre; external corners are mitred."),("Does coving use the same calculation?","Yes, measure the ceiling perimeter. No doorway deduction is needed.")],
 ["Supplier product length specifications"]),
("wallpaper","Wallpaper Calculator UK: How Many Rolls?","Work out how many rolls of wallpaper you need, including pattern repeat.",
 ["Measure the total width of the walls to paper and the wall height.","Standard UK rolls are 10.05 m long and 53 cm wide.","Each drop is the wall height plus about 10 cm trimming, plus the pattern repeat.","Divide roll length by drop length to get full drops per roll, then divide the number of drops needed."],
 "14 m of wall at 2.4 m high, no repeat: 27 drops are needed, each roll gives 4 full drops, so 7 rolls.",
 [("Should I buy an extra roll?","Yes, and check all rolls share the same batch number so the shade matches."),("What about wide rolls?","Change the roll width and length to match the label, for example 70 cm or 1 m wide."),("Do I deduct windows?","Not for small windows; the offcuts are rarely usable. Deduct large patio doors.")],
 ["Wallpaper manufacturer label guidance"]),
]
urls=["","about.html","privacy.html","disclosure.html"]
DISC='<p class="disc">Affiliate disclosure: some links on this page may be affiliate links. If you buy through them we may earn a small commission at no extra cost to you. <a href="/disclosure.html">Read more</a>.</p>'
for slug,title,desc,steps,ex,faq,src in calcs:
    p=f"{slug}-calculator/index.html"; urls.append(f"{slug}-calculator/")
    body=f'<p class="note"><a href="/">Home</a> / Calculators</p><h1>{title}</h1><p class="lead">{desc}</p>{DISC}<div class="card" id="calc"><noscript>This calculator needs JavaScript.</noscript></div>'
    body+="<h2>How to work it out</h2><ol>"+"".join(f"<li>{s}</li>" for s in steps)+"</ol>"
    body+=f'<h2>Worked example</h2><div class="card"><p>{ex}</p></div>'
    body+='<h2>What you will need</h2><p class="note">Recommended materials and tools will be listed here. (Affiliate links will be added once programmes are approved.)</p>'
    body+="<h2>Frequently asked questions</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
    body+="<h2>Sources</h2><ul>"+"".join(f"<li>{s}</li>" for s in src)+'</ul><p class="note">Results are estimates. Always confirm quantities with your supplier.</p>'
    body+=f'<script src="/assets/calcs.js"></script><script>bbRender("{slug}")</script>'
    schema=[{"@context":"https://schema.org","@type":"WebApplication","name":title,"url":f"{BASE}/{slug}-calculator/","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"GBP"}},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":title}]}]
    page(p,f"{title} | Brick & Budget",desc,body,schema)
grid="".join(f'<a href="/{s}-calculator/"><strong>{t.split(":")[0]}</strong>{d}</a>' for s,t,d,*_ in calcs)
page("index.html","Brick & Budget: Free UK Building and DIY Material Calculators","Free UK calculators for plasterboard, plaster, paint, tiles, concrete, bricks, flooring, VAT, skirting and wallpaper.",
 f'<h1>Free UK material calculators for builders and DIYers</h1><p class="lead">Work out what to buy before you go to the merchant. Metric, UK product sizes, and plain-English guides written from real trade experience.</p><h2 id="calculators">Calculators</h2><div class="grid">{grid}</div>',
 [{"@context":"https://schema.org","@type":"WebSite","name":"Brick & Budget","url":BASE+"/"}])
page("about.html","About Brick & Budget","About Brick & Budget.","<h1>About Brick &amp; Budget</h1><p>Brick &amp; Budget is a set of free calculators and guides for UK homeowners and tradespeople, built by people with hands-on experience in the North East building and refurbishment trade.</p><p>Every calculator uses UK product sizes and is checked against manufacturer guidance. Results are estimates: site conditions, waste and product variation all matter, so confirm with your supplier before ordering.</p>")
page("privacy.html","Privacy Policy | Brick & Budget","Privacy policy.","<h1>Privacy policy</h1><p>This site does not ask for or store personal information. Calculators run entirely in your browser; nothing you enter is sent to us.</p><p>Our host may keep standard server logs (such as IP address and pages requested) for security. If we add analytics, advertising or affiliate tracking, they may set cookies, and this policy and a cookie notice will be updated first.</p><p>Affiliate partners such as retailers may set cookies when you click through to their sites, under their own privacy policies.</p><p>Contact: <a href='mailto:brickandbudget.uk@gmail.com'>brickandbudget.uk@gmail.com</a></p><p>Last updated: November 2026.</p>")
page("disclosure.html","Affiliate Disclosure | Brick & Budget","Affiliate disclosure.","<h1>Affiliate disclosure</h1><p>Some links on Brick &amp; Budget are affiliate links. If you click one and buy something, we may earn a commission from the retailer at no extra cost to you. This helps keep the calculators free.</p><p>We only recommend products that are suitable for the job, and commissions do not affect calculator results. Pages containing affiliate links are clearly labelled.</p><p>As an Amazon Associate we earn from qualifying purchases (this statement applies once we join the Amazon Associates programme).</p>")
open("assets/style.css","w").write(CSS)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}/{u}</loc><lastmod>2026-11-04</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("404.html","w").write('<!doctype html><title>Not found</title><p>Page not found. <a href="'+P+'/">Back to Brick &amp; Budget</a></p>')
