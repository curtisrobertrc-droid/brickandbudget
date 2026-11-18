# Trade business tools (exec'd from build.py after tax.py)
MM_SLUG="margin-markup-calculator"
MM_SB=f"{SB}/app/?utm_source=brickandbudget&utm_medium=referral&utm_campaign={MM_SLUG}"
t6="Margin vs Markup Calculator UK for Trades"
mm_faq=[
("What is the difference between margin and markup?","Both use the same profit figure. Margin divides the profit by the selling price; markup divides it by the cost. A job that costs &pound;3,000 and is priced at &pound;4,000 makes &pound;1,000 profit: a 25% margin but a 33.3% markup."),
("How do I convert margin to markup?","Markup = margin &divide; (1 &minus; margin). A 20% margin is 0.2 &divide; 0.8 = 25% markup. A 30% margin is 0.3 &divide; 0.7 = 42.9% markup."),
("How do I convert markup to margin?","Margin = markup &divide; (1 + markup). A 50% markup is 0.5 &divide; 1.5 = 33.3% margin. A 100% markup (doubling the cost) is a 50% margin."),
("Should VAT be included?","No. Work out margin and markup on prices before VAT. VAT is collected for HMRC and is not your profit. If you are VAT registered, add VAT at 20% after you have set the price."),
("What should my cost include?","Everything the job uses: materials and delivery, waste and skip hire, labour (your own time at a fair day rate as well as anyone you pay), subcontractors, plant and tool hire, and fuel. Overheads such as van, insurance and phone are often covered by adding them to the cost or by aiming for a higher margin."),
]
mm_body=f'''<p class="note"><a href="/">Home</a> / Trade business</p><h1>{t6}</h1><p class="lead">Price a job from its cost, or check what margin and markup a quote really gives you. A 25% margin is not a 25% markup: on a &pound;3,000 job the difference is &pound;250.</p>
<div class="card"><div class="inputs">
<label>Job cost before VAT (&pound;)<input id="c" type="number" value="3000" min="0" step="any"></label>
<label>What do you know?<select id="mode" style="display:block;width:100%;margin-top:6px;padding:11px;font-size:17px"><option value="m" selected>Target margin (%)</option><option value="k">Target markup (%)</option><option value="p">Selling price (&pound;)</option></select></label>
<label id="vl">Target margin (%)<input id="v" type="number" value="25" step="any"></label>
<label>VAT registered?<select id="vat" style="display:block;width:100%;margin-top:6px;padding:11px;font-size:17px"><option value="0" selected>No</option><option value="0.2">Yes, add 20% VAT</option></select></label>
</div><div class="out" id="o"></div></div>
<h2>The formulas</h2>
<ol>
<li><strong>Profit</strong> = selling price &minus; cost (both before VAT).</li>
<li><strong>Margin</strong> = profit &divide; selling price &times; 100.</li>
<li><strong>Markup</strong> = profit &divide; cost &times; 100.</li>
<li><strong>Price for a target margin</strong> = cost &divide; (1 &minus; margin). For 25%, divide by 0.75.</li>
<li><strong>Price for a target markup</strong> = cost &times; (1 + markup). For 25%, multiply by 1.25.</li>
</ol>
<h2>Worked examples</h2>
<div class="card"><p><strong>Target margin.</strong> A job costs &pound;3,000 and you want a 25% margin. Price = &pound;3,000 &divide; 0.75 = &pound;4,000. Profit &pound;1,000, which is a 33.3% markup. Adding 25% to cost instead would give &pound;3,750 and only a 20% margin.</p>
<p><strong>Check a quote.</strong> Cost &pound;5,430, quoted at &pound;6,850. Profit &pound;1,420. Margin = 1,420 &divide; 6,850 = 20.7%. Markup = 1,420 &divide; 5,430 = 26.2%.</p>
<p><strong>VAT registered.</strong> Cost &pound;800, target 30% margin. Price = &pound;800 &divide; 0.7 = &pound;1,142.86 before VAT. Add 20% VAT: &pound;1,371.43 to the customer. The VAT of &pound;228.57 goes to HMRC, so profit stays &pound;342.86.</p></div>
<h2>Quick conversion table</h2>
<div class="card"><table style="width:100%;border-collapse:collapse;font-size:15px"><tr style="text-align:left"><th>Margin</th><th>Markup needed</th><th>Divide cost by</th></tr>
<tr><td>10%</td><td>11.1%</td><td>0.90</td></tr><tr><td>15%</td><td>17.6%</td><td>0.85</td></tr><tr><td>20%</td><td>25.0%</td><td>0.80</td></tr><tr><td>25%</td><td>33.3%</td><td>0.75</td></tr><tr><td>30%</td><td>42.9%</td><td>0.70</td></tr><tr><td>40%</td><td>66.7%</td><td>0.60</td></tr><tr><td>50%</td><td>100.0%</td><td>0.50</td></tr></table></div>
<h2>Get the cost right first</h2>
<p>Margin is only as good as the cost behind it. Most underpriced jobs come from a short materials list: missed fixings, waste allowance, delivery and the second trip to the merchant.</p>
<div class="card sb-cta"><p><strong>Plan the whole job.</strong> Build a full materials list and compare prices from UK suppliers in <a href="{MM_SB}">SmartBuild</a>, then use that total as your cost here.</p></div>
'''+related_box(['job','pipeline','starter'], 'Related template')+'''
<h2>Frequently asked questions</h2>'''+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in mm_faq)+'''
<h2>Related tools</h2><div class="grid"><a href="/vat-calculator/"><strong>VAT calculator</strong>Add or remove 20% VAT.</a><a href="/cis-deduction-calculator/"><strong>CIS deduction calculator</strong>20%, 30% or gross on labour only.</a><a href="/sole-trader-tax-calculator/"><strong>Take-home pay calculator</strong>Income Tax and Class 4 NI for 2026/27.</a></div>
<p class="note">Estimates only. Margin and markup are worked out on prices before VAT; the 20% standard rate is from <a href="https://www.gov.uk/vat-rates">GOV.UK VAT rates</a> (checked 18 November 2026).</p>
<script>
const g=i=>document.getElementById(i),n=i=>+g(i).value||0,f=x=>"£"+x.toLocaleString("en-GB",{minimumFractionDigits:2,maximumFractionDigits:2}),pc=x=>isFinite(x)?x.toFixed(1)+"%":"n/a";
const LBL={m:"Target margin (%)",k:"Target markup (%)",p:"Selling price before VAT (£)"};
function calc(){const c=n("c"),mode=g("mode").value,v=n("v"),vat=+g("vat").value;g("vl").firstChild.nodeValue=LBL[mode];
let p;if(mode==="m"){if(v>=100){g("o").innerHTML="<div><span>A margin must be below 100%.</span></div>";return}p=c/(1-v/100)}else if(mode==="k"){p=c*(1+v/100)}else{p=v}
const pr=p-c,rows=[["Selling price before VAT",f(p)],["Profit",f(pr)],["Margin (profit ÷ price)",p?pc(pr/p*100):"n/a"],["Markup (profit ÷ cost)",c?pc(pr/c*100):"n/a"]];
if(vat)rows.push(["VAT at 20%",f(p*vat)],["Price to customer inc. VAT",f(p*(1+vat))]);
g("o").innerHTML=rows.map(x=>`<div><span>${x[0]}</span><strong>${x[1]}</strong></div>`).join("")}
let last="m";g("mode").onchange=()=>{const c=n("c"),v=n("v"),m=g("mode").value;let p=last==="m"?c/(1-v/100):last==="k"?c*(1+v/100):v;
if(m==="p")g("v").value=p.toFixed(2);else if(m==="m")g("v").value=p?((p-c)/p*100).toFixed(1):0;else g("v").value=c?((p-c)/c*100).toFixed(1):0;last=m;calc()};
document.querySelectorAll("input").forEach(i=>i.oninput=calc);g("vat").onchange=calc;calc();
</script>'''
page(f"{MM_SLUG}/index.html", t6+" | Brick & Budget",
     "Free UK margin and markup calculator for trades: price a job from cost for a target margin or markup, check a quote, and add 20% VAT.",
     mm_body,
     [{"@context":"https://schema.org","@type":"WebApplication","name":t6,"url":f"{BASE}/{MM_SLUG}/","applicationCategory":"FinanceApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"GBP"}},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":html.unescape(a)}} for q,a in mm_faq]},
      crumbs(t6)])
urls += [f"{MM_SLUG}/"]
