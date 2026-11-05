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
<link rel="stylesheet" href="/assets/style.css">{sc}</head><body><header><div class="w"><a class="logo" href="/">Brick &amp; Budget</a><nav><a href="/#calculators">Calculators</a><a href="https://payhip.com/TradeSheetUK">Templates</a><a href="/about.html">About</a></nav></div></header>
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
("decking","Decking Calculator UK: Boards, Joists and Screws","Work out how many deck boards, joists and screws you need for a garden deck of any size.",
 ["Measure the deck length (the direction the boards run) and width in metres.","Common UK deck boards are 120 or 144 mm wide, sold in 2.4 m, 3.6 m and 4.8 m lengths. Allow a 5 mm gap between boards for drainage.","Space joists at 400 mm centres for standard softwood boards; 47 x 100 mm or 47 x 150 mm C16/C24 treated timber is typical.","Fix each board with two screws at every joist, and add 10% to boards and joists for cuts."],
 "A 4 m by 3 m deck with 144 mm boards: 21 rows of board, 26 boards at 3.6 m, 11 joists needing 8 lengths at 4.8 m, and about 462 screws.",
 [("Which way should deck boards run?","Usually across the joists and along the longest dimension, often away from the house so water runs off with the fall."),("Do I need planning permission for decking?","Decking is usually permitted development if it is no more than 30 cm above the ground and covers no more than half the garden. Check the Planning Portal."),("Grooved side up or down?","Many makers now recommend the smooth side up for grip with modern boards; follow the board manufacturer's guidance."),("What screws should I use?","Exterior-grade coated or stainless deck screws, typically 4.5 x 60 mm for 28 to 32 mm boards.")],
 ["Planning Portal: decking (planningportal.co.uk)","Timber Decking and Cladding Association guidance"]),
("fence","Fence Panel and Post Calculator UK","Work out how many 6ft fence panels, posts and bags of postcrete you need for a fence run.",
 ["Measure the total fence run in metres.","A standard UK 6ft panel is 1.83 m wide. Each panel needs one post, plus one extra post at the end of every separate run.","Use 100 x 100 mm (4 x 4 in) posts, about 2.4 m long for a 1.8 m fence, with roughly a quarter of the post in the ground.","Allow two 20 kg bags of postcrete per post in typical soil, or one in firm ground."],
 "A 12 m straight run: 12 / 1.83 = 6.6, so 7 panels, 8 posts and 16 bags of postcrete.",
 [("How deep should fence posts go?","About 600 mm for a 1.8 m fence, or a quarter of the post length."),("Timber or concrete posts?","Concrete posts last longer and suit slotted panels; treated timber posts are cheaper and easier to cut."),("How high can a garden fence be?","Up to 2 m without planning permission, or 1 m next to a highway. Check the Planning Portal."),("Do I need gravel boards?","They keep the panel off the soil and stop it rotting; most fitters use one per panel.")],
 ["Planning Portal: fences, gates and garden walls (planningportal.co.uk)","Postcrete manufacturer usage guidance"]),
("gravel","Gravel Calculator UK: Tonnes and Bulk Bags","Work out how many tonnes and bulk bags of gravel, sand or MOT Type 1 you need from area and depth.",
 ["Measure the length and width in metres and choose a depth in millimetres.","Typical depths: 40 to 50 mm for decorative gravel, 100 mm or more of MOT Type 1 for a driveway sub-base.","Most gravel and aggregates weigh about 1.5 to 1.7 tonnes per m³; 1.6 is a sensible default. Slate and some stone are lighter.","UK bulk (jumbo) bags usually hold around 800 to 850 kg; check your merchant's bag weight."],
 "A 5 m by 4 m area at 50 mm: 1 m³, about 1.6 tonnes, so 2 bulk bags.",
 [("How much does a bulk bag cover?","At 50 mm deep, a 850 kg bag covers roughly 10 m² of typical gravel."),("Should I use a membrane?","Yes, a weed membrane under decorative gravel stops weeds and stops stones sinking into soil."),("How much extra should I order?","Add 5% to 10% for compaction and uneven ground, more for sub-base material that compacts.")],
 ["Aggregate supplier density and bag weight data"]),
("insulation","Loft Insulation Calculator UK","Work out how many rolls of loft insulation you need to reach 270 mm, including what is already there.",
 ["Measure the loft floor area (length x width) in m².","The recommended depth for mineral wool loft insulation in the UK is 270 mm.","Lay the first layer between the joists (typically 100 mm), then a second layer across the joists to make up the depth, usually 170 mm.","Roll coverage varies by thickness and brand: around 8.3 m² for a 100 mm roll and 5.6 m² for 170 mm is typical. Check the pack label."],
 "A 40 m² loft with no insulation: 6 rolls of 100 mm between the joists plus 8 rolls of 170 mm across them, 14 rolls in total.",
 [("Is 270 mm enough?","270 mm of mineral wool is the usual recommendation and meets current guidance for existing homes."),("Can I board over insulation?","Not directly over 270 mm without crushing it; use loft legs to raise the boards above the insulation."),("Do I need to leave a gap at the eaves?","Yes, keep the eaves clear for ventilation to avoid condensation in the roof space."),("What safety kit do I need?","Gloves, long sleeves, goggles and a dust mask. Only walk on the joists or boards.")],
 ["Energy Saving Trust: roof and loft insulation (energysavingtrust.org.uk)","Insulation manufacturer roll coverage data"]),
("radiator","Radiator BTU Calculator UK","Work out the radiator heat output in BTU and watts needed for a room, allowing for room type, windows and insulation.",
 ["Measure the room length, width and ceiling height in metres.","The calculation converts the room volume to cubic feet and multiplies by a factor: 5 for living rooms, 4 for bedrooms and kitchens, 6 for bathrooms.","Add 15% for north-facing rooms or large windows, 10% for single glazing, and 15% to 30% for average or poor insulation.","Choose a radiator at or slightly above the result. Check the output at your system's flow temperature (often quoted at Delta T50)."],
 "A 4 m by 3.5 m living room with a 2.4 m ceiling, double glazed and well insulated: about 5,930 BTU/h, or 1,740 W.",
 [("What is Delta T50?","It is the standard test condition for radiator output. Heat pumps and low flow temperatures give less, so you may need a larger radiator."),("BTU or watts?","Both measure heat output; 1 watt is about 3.412 BTU/h."),("Can I use two radiators?","Yes. Split the total between them, which often heats a large room more evenly.")],
 ["Radiator manufacturer output data (Delta T50)"]),
]
PROMO={k:'Budgeting a bigger project? The TradeSheet Co <a href="https://payhip.com/b/c2UC3">Home Renovation Budget Planner</a> tracks materials, labour and costs in one spreadsheet. More templates in the <a href="https://payhip.com/TradeSheetUK">TradeSheet Co shop</a>.' for k in ['decking','fence','gravel','insulation','radiator']}
SB="https://smartbuilduk.co.uk"
SBG={"paint":"how-much-paint-do-i-need","plasterboard":"how-much-plasterboard-do-i-need","plaster":"how-much-plaster-do-i-need","tiles":"how-many-tiles-do-i-need","skirting":"how-much-skirting-board-do-i-need","flooring":"how-much-laminate-flooring-do-i-need","wallpaper":"how-many-rolls-of-wallpaper-do-i-need","insulation":"how-much-loft-insulation-do-i-need","fence":"how-many-fence-panels-do-i-need","decking":"how-much-decking-do-i-need","concrete":"how-much-concrete-for-a-shed-base","gravel":"how-much-gravel-do-i-need","bricks":"how-many-bricks-do-i-need"}
def sb_cta(slug):
    u=f"{SB}/guides/{SBG[slug]}/" if slug in SBG else f"{SB}/app/"
    u+=f"?utm_source=brickandbudget&utm_medium=referral&utm_campaign={slug}-calculator"
    return f'<div class="card sb-cta"><p><strong>Planning the whole job?</strong> Get a full materials list and compare prices from UK suppliers in <a href="{u}">SmartBuild</a>.</p></div>'
urls=["","about.html","privacy.html","disclosure.html"]
DISC='<p class="disc">Some links are affiliate links. We may earn a small commission at no extra cost to you. <a href="/disclosure.html">Read more</a>.</p>'
for slug,title,desc,steps,ex,faq,src in calcs:
    p=f"{slug}-calculator/index.html"; urls.append(f"{slug}-calculator/")
    body=f'<p class="note"><a href="/">Home</a> / Calculators</p><h1>{title}</h1><p class="lead">{desc}</p>{DISC}<div class="card" id="calc"><noscript>This calculator needs JavaScript.</noscript></div>'
    body+="<h2>How to work it out</h2><ol>"+"".join(f"<li>{s}</li>" for s in steps)+"</ol>"
    body+=f'<h2>Worked example</h2><div class="card"><p>{ex}</p></div>'+sb_cta(slug)
    body+='<h2>What you will need</h2><p class="note">Recommended materials and tools will be listed here. (Affiliate links will be added once programmes are approved.)</p>'
    body+="<h2>Frequently asked questions</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
    body+="<h2>Sources</h2><ul>"+"".join(f"<li>{s}</li>" for s in src)+'</ul><p class="note">Results are estimates. Always confirm quantities with your supplier.</p>'
    body+=f'<script src="/assets/calcs.js"></script><script>bbRender("{slug}")</script>'
    schema=[{"@context":"https://schema.org","@type":"WebApplication","name":title,"url":f"{BASE}/{slug}-calculator/","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"GBP"}},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":title}]}]
    if slug in PROMO: body=body.replace('<h2>Frequently asked questions</h2>','<h2>Plan the whole job</h2><p class="note">'+PROMO[slug]+'</p><h2>Frequently asked questions</h2>')
    page(p,f"{title} | Brick & Budget",desc,body,schema)
# Affiliate-ready slot: renders nothing until links exist; then shows the disclosure line with them.
AFF={"bathroom-cost":[]}  # add (label,url) tuples once a programme approves us
def aff_slot(key):
    links=AFF.get(key) or []
    if not links: return ""
    return '<div class="card aff"><h2>Where to buy</h2>'+DISC+'<ul>'+"".join(f'<li><a href="{u}" rel="sponsored nofollow">{html.escape(l)}</a></li>' for l,u in links)+'</ul></div>'
G="bathroom-cost"
urls.append("new-bathroom-cost-uk/")
gt="How Much Does a New Bathroom Cost in the UK? (2026)"
gd="Honest 2026 UK price ranges for a new bathroom, supplied and fitted, with a cost breakdown, a simple estimator and the published sources behind every figure."
gfaq=[("How much does an average new bathroom cost in the UK?","Checkatrade and MyJobQuote both publish an average of about £7,000 supplied and fitted in 2026, with most jobs between £5,500 and £8,000. High-end or complex bathrooms start at around £14,000."),
("How much is labour only?","Published guides put full bathroom fitting labour at roughly £1,500 to £4,000, with fitters charging about £320 to £480 per day."),
("How long does a new bathroom take?","Typically 5 to 10 working days, longer if the layout changes, walls are re-plastered or a wet room is tanked."),
("Do I need building regulations approval?","Like-for-like replacement usually does not, but new electrical circuits in a bathroom are notifiable under Part P and new drainage or ventilation must meet building regulations. Use a registered electrician who can self-certify."),
("Is VAT included?","Trade guide prices are usually quoted including VAT for homeowners. A VAT-registered fitter will add 20% to labour, so always ask whether a quote is inclusive.")]
gbody=f'''<p class="note"><a href="/">Home</a> / Cost guides</p><h1>{gt}</h1><p class="lead">Most UK homeowners pay between £5,500 and £8,000 for a new bathroom supplied and fitted in 2026, with an average of about £7,000. A small refresh can be done for £4,000; a large or luxury bathroom often costs £14,000 or more.</p>
<h2>Typical 2026 price ranges</h2><div class="card"><div class="out">
<div><span>Basic refresh (like-for-like suite, minimal tiling)</span><strong>£4,000 to £5,500</strong></div>
<div><span>Standard bathroom, supplied and fitted</span><strong>£5,500 to £8,000</strong></div>
<div><span>Large, high-end or complex (10+ days)</span><strong>£14,000+</strong></div>
<div><span>En-suite added to an existing bedroom</span><strong>£4,000 to £10,000</strong></div>
<div><span>Fitting labour only, full project</span><strong>£1,500 to £4,000</strong></div></div></div>
<h2>Where the money goes</h2><p>Published averages for the individual jobs that make up a bathroom:</p><div class="card"><div class="out">
<div><span>Ripping out the old bathroom</span><strong>£600 to £1,000</strong></div>
<div><span>Plumbing, first and second fix</span><strong>£1,500 to £3,000</strong></div>
<div><span>Wall tiling (labour, mid-sized room)</span><strong>£950 to £1,250</strong></div>
<div><span>Electrical work (lighting, extractor fan)</span><strong>about £900</strong></div>
<div><span>Re-plastering</span><strong>about £1,500</strong></div>
<div><span>Vinyl flooring</span><strong>£250 to £950</strong></div>
<div><span>Underfloor heating</span><strong>about £100 per m²</strong></div>
<div><span>Fitter day rate</span><strong>£320 to £480</strong></div></div></div>
<p class="note">Guides disagree: MyBuilder puts the average nearer £4,500, while Checkatrade and MyJobQuote both say about £7,000. Treat all figures as ballpark national averages; London and the South East tend to be higher, the North East lower.</p>
<h2>Quick bathroom cost estimator</h2><div class="card" id="est">
<div class="inputs"><label>Bathroom size<select id="sz" style="display:block;width:100%;margin-top:6px;padding:11px;font-size:17px"><option value="0.8">Small or en-suite</option><option value="1" selected>Average family bathroom</option><option value="1.35">Large</option></select></label>
<label>Specification<select id="sp" style="display:block;width:100%;margin-top:6px;padding:11px;font-size:17px"><option value="4500">Budget</option><option value="7000" selected>Mid-range</option><option value="14000">High-end</option></select></label>
<label>Moving the layout?<select id="ly" style="display:block;width:100%;margin-top:6px;padding:11px;font-size:17px"><option value="0">No, like-for-like</option><option value="1750">Yes (new stud wall, pipe moves)</option></select></label>
<label>Underfloor heating area (m², 0 for none)<input id="uf" type="number" min="0" value="0"></label></div>
<button onclick="bbEst()">Estimate cost</button><div class="out" id="eo"></div></div>
<script>function bbEst(){{var b=+sz.value*+sp.value,t=b+ +ly.value+ (+uf.value||0)*100,lo=Math.round(t*0.85/100)*100,hi=Math.round(t*1.2/100)*100,f=function(n){{return "£"+n.toLocaleString("en-GB")}};eo.innerHTML="<div><span>Likely range</span><strong>"+f(lo)+" to "+f(hi)+"</strong></div><div><span>Add a 10% contingency</span><strong>"+f(Math.round(hi*0.1/100)*100)+"</strong></div>"}}bbEst()</script>
<p class="note">The estimator scales published national averages by size and specification. It is a budgeting guide, not a quote.</p>
<div class="card sb-cta"><p><strong>Ready to plan your bathroom?</strong> <a href="{SB}/app/?utm_source=brickandbudget&utm_medium=referral&utm_campaign=bathroom-cost-guide">Plan the whole job and compare prices in SmartBuild</a>. It is free and needs no sign-up.</p><p class="note">Tiling or re-boarding yourself? See the <a href="{SB}/guides/how-many-floor-tiles-for-a-bathroom/?utm_source=brickandbudget&utm_medium=referral&utm_campaign=bathroom-cost-guide">bathroom floor tiles guide</a>.</p></div>
<h2>How to keep the cost down</h2><ul><li>Keep the toilet, basin and bath or shower in the same positions to avoid moving waste pipes.</li><li>Tile only the wet zones and use moisture-resistant paint elsewhere.</li><li>Get at least three written quotes that list what is included: removal, plastering, electrics, tiling and waste.</li><li>Buy the suite yourself only if the fitter agrees; some will not warranty customer-supplied items.</li></ul>
<h2>Plan the whole budget</h2><p class="note">Track quotes, materials and labour in the TradeSheet Co <a href="https://payhip.com/b/c2UC3">Home Renovation Budget Planner</a>. Doing the kitchen too? See SmartBuild's <a href="{SB}/guides/cost-to-renovate-a-kitchen-uk/?utm_source=brickandbudget&utm_medium=referral&utm_campaign=bathroom-cost-guide">kitchen renovation cost guide</a> and the <a href="https://payhip.com/b/KTcDH">Kitchen Planner Printable</a>.</p>
{aff_slot(G)}
<h2>Frequently asked questions</h2>'''+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in gfaq)+'''<h2>Sources</h2><ul><li><a href="https://www.checkatrade.com/blog/cost-guides/new-bathroom-cost/">Checkatrade: How much does a new bathroom cost (updated March 2026)</a></li><li><a href="https://www.checkatrade.com/blog/cost-guides/ensuite-bathroom-installation-cost/">Checkatrade: Cost to add an en-suite (updated June 2026)</a></li><li><a href="https://whito.co.uk/kitchen-bathroom-fitters/guides/kitchen-and-bathroom-fitting-prices-what-to-publish/">Whito: comparison of Checkatrade, MyBuilder and MyJobQuote bathroom prices (2026)</a></li><li><a href="https://www.gov.uk/guidance/electrical-safety-approved-document-p">GOV.UK: Approved Document P (electrical safety)</a></li></ul><p class="note">Figures checked November 2026. Prices are estimates; always get written quotes.</p>'''
gschema=[{"@context":"https://schema.org","@type":"Article","headline":gt,"dateModified":"2026-11-05","author":{"@type":"Organization","name":"Brick & Budget"}},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in gfaq]},
 {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":gt}]}]
page("new-bathroom-cost-uk/index.html",f"New Bathroom Cost UK 2026 | Brick & Budget",gd,gbody,gschema)
exec(open("tax.py").read())
grid="".join(f'<a href="/{s}-calculator/"><strong>{t.split(":")[0]}</strong>{d}</a>' for s,t,d,*_ in calcs)
page("index.html","Brick & Budget: Free UK Building and DIY Material Calculators","Free UK calculators for plasterboard, plaster, paint, tiles, concrete, bricks, flooring, VAT, skirting, wallpaper, decking, fencing, gravel, loft insulation and radiators.",
 f'<h1>Free UK material calculators for builders and DIYers</h1><p class="lead">Work out what to buy before you go to the merchant. Metric, UK product sizes, and plain-English guides written from real trade experience.</p><h2 id="calculators">Calculators</h2><div class="grid">{grid}</div><h2 id="guides">Cost guides</h2><div class="grid"><a href="/new-bathroom-cost-uk/"><strong>New bathroom cost UK (2026)</strong>Price ranges, breakdown and a quick estimator.</a></div><h2 id="sole-trader">Sole trader tax (2026/27)</h2>'+TL,
 [{"@context":"https://schema.org","@type":"WebSite","name":"Brick & Budget","url":BASE+"/"}])
page("about.html","About Brick & Budget","About Brick & Budget.","<h1>About Brick &amp; Budget</h1><p>Brick &amp; Budget is a set of free calculators and guides for UK homeowners and tradespeople, built by people with hands-on experience in the North East building and refurbishment trade.</p><p>Every calculator uses UK product sizes and is checked against manufacturer guidance. Results are estimates: site conditions, waste and product variation all matter, so confirm with your supplier before ordering.</p>")
page("privacy.html","Privacy Policy | Brick & Budget","Privacy policy.","<h1>Privacy policy</h1><p>This site does not ask for or store personal information. Calculators run entirely in your browser; nothing you enter is sent to us.</p><p>Our host may keep standard server logs (such as IP address and pages requested) for security. If we add analytics, advertising or affiliate tracking, they may set cookies, and this policy and a cookie notice will be updated first.</p><p>Affiliate partners such as retailers may set cookies when you click through to their sites, under their own privacy policies.</p><p>Contact: <a href='mailto:brickandbudget.uk@gmail.com'>brickandbudget.uk@gmail.com</a></p><p>Last updated: November 2026.</p>")
page("disclosure.html","Affiliate Disclosure | Brick & Budget","Affiliate disclosure.","<h1>Affiliate disclosure</h1><p>Some links on Brick &amp; Budget are affiliate links. If you click one and buy something, we may earn a commission from the retailer at no extra cost to you. This helps keep the calculators free.</p><p>We only recommend products that are suitable for the job, and commissions do not affect calculator results. Pages containing affiliate links are clearly labelled.</p><p>As an Amazon Associate we earn from qualifying purchases (this statement applies once we join the Amazon Associates programme).</p>")
open("assets/style.css","w").write(CSS)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}/{u}</loc><lastmod>2026-11-05</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("404.html","w").write('<!doctype html><title>Not found</title><p>Page not found. <a href="'+P+'/">Back to Brick &amp; Budget</a></p>')
