# Sole trader tax section (2026/27). Exec'd from build.py; uses page(), urls, BASE.
GOV={"it":"https://www.gov.uk/income-tax-rates","ni":"https://www.gov.uk/self-employed-national-insurance-rates","mi":"https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles","poa":"https://www.gov.uk/understand-self-assessment-bill/payments-on-account","exp":"https://www.gov.uk/expenses-if-youre-self-employed","cis":"https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors","cis_sub":"https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/get-paid","sa":"https://www.gov.uk/self-assessment-tax-returns/deadlines","pen":"https://www.gov.uk/self-assessment-tax-returns/penalties"}
TS='<div class="card"><strong>Keep your records straight</strong><p class="note">The TradeSheet Co <a href="https://payhip.com/b/hUVbL">CIS Tracker</a> logs CIS deductions so you can offset them against your bill, and the <a href="https://payhip.com/b/cxBUj">Expenses &amp; Mileage Log</a> records costs and business miles through the year.</p></div>'
TL='<div class="grid"><a href="/sole-trader-tax-calculator/"><strong>Take-home pay calculator</strong>Income Tax and Class 4 NI for 2026/27.</a><a href="/cis-deduction-calculator/"><strong>CIS deduction calculator</strong>20%, 30% or gross on labour only.</a><a href="/self-assessment-deadlines/"><strong>Self Assessment deadlines</strong>2025/26 return dates and penalties.</a><a href="/payments-on-account/"><strong>Payments on account</strong>Why the first January bill is often bigger.</a><a href="/sole-trader-expenses/"><strong>Sole trader expenses</strong>What you can and cannot claim.</a></div>'
def src(*k): return "<h2>Sources</h2><ul>"+"".join(f'<li><a href="{GOV[x]}">{GOV[x].replace("https://www.","")}</a></li>' for x in k)+'</ul><p class="note">Checked against GOV.UK on 6 November 2026. Estimates only, not tax advice. Scottish Income Tax rates differ.</p>'
def crumbs(t): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":t}]}
calc_body='''<h1>Sole Trader Take-Home Pay Calculator UK 2026/27</h1><p class="lead">Estimate your Income Tax, Class 4 National Insurance and how much to set aside each month. England, Wales and Northern Ireland rates for 6 April 2026 to 5 April 2027.</p>
<div class="card"><div class="inputs"><label>Turnover (£ per year)<input id="t" type="number" value="45000"></label><label>Allowable expenses (£, excluding mileage)<input id="e" type="number" value="8000"></label><label>Business miles (car or van)<input id="mi" type="number" value="6000"></label><label>Other employment income (£, PAYE)<input id="o" type="number" value="0"></label></div><div class="out" id="r"></div></div>
<h2>Rates used (2026/27)</h2><ul><li>Personal Allowance £12,570, reduced by £1 for every £2 of adjusted net income over £100,000, reaching zero at £125,140.</li><li>Basic rate 20% on taxable income from £12,571 to £50,270; higher rate 40% from £50,271 to £125,140; additional rate 45% above £125,140.</li><li>Class 4 National Insurance: 6% on profits from £12,570 to £50,270, and 2% above £50,270.</li><li>Class 2 National Insurance: not payable. With profits of £7,105 or more, it is treated as paid to protect your record. Below £7,105 you can choose to pay voluntarily at £3.65 a week.</li><li>Simplified mileage for cars and vans: 55p a mile for the first 10,000 business miles in 2026/27 (up from 45p before 6 April 2026), then 25p a mile.</li></ul>
<h2>How it works</h2><p>Profit is turnover minus allowable expenses minus the mileage allowance. Income Tax on the profit is the tax on your total income minus the tax on your other income alone, so PAYE wages use up your allowance and bands first. Class 4 is worked out on business profit only. You cannot use flat-rate mileage for a vehicle you have claimed capital allowances on.</p>
<h2>Worked examples (no other income, no mileage)</h2><ul><li>£20,000 profit: Income Tax £1,486, Class 4 £445.80, take-home £18,068.20.</li><li>£60,000 profit: Income Tax £11,432, Class 4 £2,456.60, take-home £46,111.40.</li><li>£120,000 profit: Personal Allowance tapered to £2,570, Income Tax £39,432, Class 4 £3,656.60, take-home £76,911.40.</li></ul>
'''+TS+'''<h2>Related guides</h2>'''+TL+src("it","ni","mi")+'''
<script>
const $=i=>+document.getElementById(i).value||0,f=n=>"£"+n.toLocaleString("en-GB",{minimumFractionDigits:2,maximumFractionDigits:2});
function tax(inc){const pa=Math.max(0,12570-Math.max(0,inc-100000)/2),ti=Math.max(0,inc-pa);return Math.min(ti,37700)*.2+Math.min(Math.max(ti-37700,0),125140-37700)*.4+Math.max(ti-125140,0)*.45}
function calc(){const mi=$("mi"),ma=Math.min(mi,10000)*.55+Math.max(mi-10000,0)*.25,p=Math.max(0,$("t")-$("e")-ma),o=$("o"),it=tax(p+o)-tax(o),n4=Math.max(0,Math.min(p,50270)-12570)*.06+Math.max(0,p-50270)*.02;
document.getElementById("r").innerHTML=[["Mileage allowance",ma],["Taxable profit",p],["Income Tax on profit",it],["Class 4 NI",n4],["Take-home from business",p-it-n4],["Set aside per month",(it+n4)/12]].map(x=>`<div><span>${x[0]}</span><strong>${f(x[1])}</strong></div>`).join("")+`<div><span>Effective rate on profit</span><strong>${p?((it+n4)/p*100).toFixed(1):0}%</strong></div>`}
document.querySelectorAll("input").forEach(i=>i.oninput=calc);calc();
</script>'''
t1="Sole Trader Take-Home Pay Calculator UK 2026/27"
page("sole-trader-tax-calculator/index.html",t1+" | Brick & Budget","Free UK sole trader calculator for 2026/27: Income Tax, Class 4 National Insurance, 55p mileage and how much to set aside each month.",calc_body,[{"@context":"https://schema.org","@type":"WebApplication","name":t1,"applicationCategory":"FinanceApplication","offers":{"@type":"Offer","price":"0","priceCurrency":"GBP"}},crumbs(t1)])
poa='''<h1>Payments on Account Explained for Sole Traders</h1><p class="lead">Why your first Self Assessment bill in January is often 150% of what you expected, and what you can do about it.</p>
<h2>What they are</h2><p>Payments on account are advance payments towards your next tax bill, including Class 4 National Insurance. There are two, due by midnight on 31 January and 31 July, and each is normally half of the tax you owed for the previous year.</p>
<h2>When you do not have to make them</h2><ul><li>Your tax owed for the previous year was less than £1,000, or</li><li>More than 80% of the tax you owed was paid outside Self Assessment, for example through your PAYE tax code.</li></ul>
<h2>Your first year</h2><p>If you did not make payments on account last year, the January payment covers the full bill for the year just ended plus the first payment on account for the current year. Using HMRC's own example, a £3,000 bill means £4,500 due on 31 January (£3,000 plus £1,500), then £1,500 on 31 July.</p>
<h2>The balancing payment</h2><p>If your payments on account did not cover the full bill, you pay the difference, the balancing payment, by 31 January after the tax year ends, along with the next first payment on account. If you overpaid, you may be due a refund.</p>
<h2>Reducing them</h2><p>If you expect lower profits, you can ask HMRC to reduce your payments on account through your online account or with form SA303. If you reduce them too far, HMRC charges interest on the shortfall.</p>
<h2>Plan ahead</h2><p>Use the <a href="/sole-trader-tax-calculator/">take-home pay calculator</a> to estimate this year's bill and how much to set aside each month. If you work under CIS, deductions already taken are credited against your bill, so keep every statement.</p>'''+TS+src("poa")
t2="Payments on Account Explained (UK Sole Traders)"
page("payments-on-account/index.html",t2+" | Brick & Budget","How Self Assessment payments on account work: 31 January and 31 July deadlines, the first-year 150% bill, balancing payments and how to reduce them.",poa,[{"@context":"https://schema.org","@type":"Article","headline":t2,"dateModified":"2026-11-05","author":{"@type":"Organization","name":"Brick & Budget"}},crumbs(t2)])
ex='''<h1>What Can a Sole Trader Claim as Expenses?</h1><p class="lead">A plain-English summary of allowable expenses, based on HMRC guidance, with notes for trades.</p>
<h2>The basic rule</h2><p>Allowable expenses are running costs of the business. They reduce your taxable profit: on £40,000 turnover with £10,000 of expenses, you pay tax on £30,000. Money you take out for personal use is not an expense.</p>
<h2>Costs you can usually claim</h2><ul><li>Office costs, such as stationery and phone bills</li><li>Travel costs, such as fuel, parking, and train or bus fares</li><li>Clothing such as uniforms (everyday clothes do not count)</li><li>Staff and subcontractor costs</li><li>Stock and raw materials, such as materials bought for a job</li><li>Financial costs, such as insurance and bank charges</li><li>Business premises costs, such as heating, lighting and business rates</li><li>Advertising and marketing, including website costs</li><li>Trade or professional subscriptions</li><li>Training related to your existing business</li></ul>
<h2>Tools, vans and equipment</h2><p>Under traditional accounting, equipment, machinery and business vehicles are claimed as capital allowances. Under the cash basis, most items you buy and keep are claimed as expenses, except cars, which still go through capital allowances.</p>
<h2>Mileage instead of actual costs</h2><p>Instead of fuel, insurance and servicing, you can use simplified expenses: 55p a mile for the first 10,000 business miles in 2026/27 and 25p after. You cannot do this for a vehicle you have already claimed capital allowances on, and once you choose flat rates for a vehicle you must keep using them for it. Parking and other travel can be claimed on top.</p>
<h2>Mixed business and personal use</h2><p>Only the business share counts. If £70 of a £200 phone bill is business calls, claim £70. If you work from home, use a reasonable split, for example by rooms and time used.</p>
<h2>The trading allowance</h2><p>You cannot claim expenses or capital allowances if you use the £1,000 tax-free trading allowance instead. If you are unsure whether something is allowable, ask HMRC or an accountant.</p>
<p>Track every receipt and mile in the <a href="https://payhip.com/b/cxBUj">Expenses &amp; Mileage Log</a>, then see the effect on your bill in the <a href="/sole-trader-tax-calculator/">take-home pay calculator</a>.</p>'''+TS+src("exp","mi")
t3="What Can a Sole Trader Claim as Expenses? (UK)"
page("sole-trader-expenses/index.html",t3+" | Brick & Budget","Allowable expenses for UK sole traders: what you can claim, capital allowances, 55p mileage for 2026/27, mixed use and the trading allowance.",ex,[{"@context":"https://schema.org","@type":"Article","headline":t3,"dateModified":"2026-11-05","author":{"@type":"Organization","name":"Brick & Budget"}},crumbs(t3)])

# Appended by build: CIS calculator + Self Assessment deadlines

cis_body = '''<p class="note"><a href="/">Home</a> / Sole trader tax</p><h1>CIS Deduction Calculator UK</h1><p class="lead">Work out how much a contractor should deduct under the Construction Industry Scheme, and what the subcontractor takes home. Rates: 20% registered, 30% unregistered or unmatched, 0% with gross payment status.</p>
<div class="card"><div class="inputs">
<label>Gross invoice total (&pound;)<input id="g" type="number" value="5000"></label>
<label>Materials paid for by subcontractor (&pound;)<input id="m" type="number" value="1200"></label>
<label>VAT on the invoice (&pound;, if charged)<input id="v" type="number" value="0"></label>
<label>Plant hire / consumables excluded (&pound;)<input id="p" type="number" value="0"></label>
<label>CIS rate<select id="r" style="display:block;width:100%;margin-top:6px;padding:11px;font-size:17px"><option value="0.2" selected>20% &mdash; registered subcontractor</option><option value="0.3">30% &mdash; unregistered or unmatched</option><option value="0">0% &mdash; gross payment status</option></select></label>
</div><div class="out" id="o"></div></div>
<h2>How the deduction is worked out</h2>
<ol>
<li>Start with the gross amount on the subcontractor\'s invoice.</li>
<li>Take away VAT, materials the subcontractor paid for directly, plant hire, consumable stores, and manufacturing or prefabricating materials.</li>
<li>Apply the CIS rate HMRC gave you when you verified the subcontractor to what is left (the labour element).</li>
<li>Pay the subcontractor the net amount. Pay the deduction to HMRC. It counts as an advance towards the subcontractor\'s tax and Class 4 National Insurance.</li>
</ol>
<h2>Worked example</h2>
<div class="card"><p>&pound;5,000 gross invoice, &pound;1,200 materials, no VAT, registered at 20%. Deductible amount = &pound;5,000 &minus; &pound;1,200 = &pound;3,800. CIS deduction = &pound;760. Net paid to the subcontractor = &pound;4,240.</p></div>
<h2>Who this is for</h2>
<ul>
<li><strong>Contractors:</strong> check a payment before you approve it, and give a payment and deduction statement within 14 days of the end of each tax month.</li>
<li><strong>Subcontractors:</strong> check what should have been taken off, and keep every statement so the deductions are credited on your Self Assessment return.</li>
</ul>
''' + TS + '''
<h2>Frequently asked questions</h2>
<details><summary>Is CIS deducted from materials?</summary><p>No. Genuine materials the subcontractor paid for directly, VAT, plant hire and consumable stores are taken off before the percentage is applied. The contractor can ask for receipts; if there are none, they estimate the materials cost.</p></details>
<details><summary>Why am I on 30%?</summary><p>The higher rate applies if you are not registered for CIS, or if HMRC cannot match your details when the contractor verifies you. Register and make sure the name and UTR match HMRC\'s records.</p></details>
<details><summary>Does CIS replace my tax bill?</summary><p>No. CIS deductions are payments on account of your Income Tax and Class 4 NI. On your Self Assessment return they are credited against the bill; if too much was taken you can get a refund.</p></details>
<details><summary>When must the contractor give me a statement?</summary><p>Within 14 days of the end of the tax month. For a tax month ending 5 June, the statement is due by 19 June.</p></details>
''' + src("cis", "cis_sub") + '''
<script>
const $=i=>+document.getElementById(i).value||0,f=n=>"£"+n.toLocaleString("en-GB",{minimumFractionDigits:2,maximumFractionDigits:2});
function calc(){const g=$("g"),ex=$("m")+$("v")+$("p"),lab=Math.max(0,g-ex),rate=+document.getElementById("r").value,ded=lab*rate,net=g-ded;
document.getElementById("o").innerHTML=[["Amount excluded (materials, VAT, plant)",ex],["Amount CIS applies to (labour)",lab],["CIS deduction",ded],["Net paid to subcontractor",net]].map(x=>`<div><span>${x[0]}</span><strong>${f(x[1])}</strong></div>`).join("")+`<div><span>Effective deduction on gross invoice</span><strong>${g?(ded/g*100).toFixed(1):0}%</strong></div>`}
document.querySelectorAll("input,select").forEach(i=>i.oninput=calc);calc();
</script>'''
t4 = "CIS Deduction Calculator UK"
page("cis-deduction-calculator/index.html", t4 + " | Brick & Budget",
     "Free UK CIS calculator: work out 20% or 30% deductions on labour only, after materials, VAT and plant hire, for contractors and subcontractors.",
     cis_body,
     [{"@context": "https://schema.org", "@type": "WebApplication", "name": t4, "applicationCategory": "FinanceApplication",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"}},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
          {"@type": "Question", "name": "Is CIS deducted from materials?",
           "acceptedAnswer": {"@type": "Answer",
                              "text": "No. Genuine materials the subcontractor paid for directly, VAT, plant hire and consumable stores are taken off before the percentage is applied."}},
          {"@type": "Question", "name": "Why am I on 30%?",
           "acceptedAnswer": {"@type": "Answer",
                              "text": "The higher rate applies if you are not registered for CIS, or if HMRC cannot match your details when the contractor verifies you."}}]},
      crumbs(t4)])

sa_body = '''<p class="note"><a href="/">Home</a> / Sole trader tax</p><h1>Self Assessment Deadlines UK 2026/27</h1><p class="lead">Key dates for the 2025/26 tax year return, what happens if you miss them, and how to plan for January.</p>
<h2>Tax year this return covers</h2>
<p>6 April 2025 to 5 April 2026. You file and pay after the year ends.</p>
<h2>Key deadlines</h2>
<div class="card"><div class="out">
<div><span>Tell HMRC you need a return (if new, or you did not need one last year)</span><strong>5 October 2026</strong></div>
<div><span>Paper tax return</span><strong>31 October 2026, 11:59pm</strong></div>
<div><span>Online return if you want the bill collected through your PAYE tax code</span><strong>30 December 2026, 11:59pm</strong></div>
<div><span>Online tax return AND payment of tax due</span><strong>31 January 2027, 11:59pm</strong></div>
<div><span>Second payment on account (if you make them)</span><strong>31 July 2027</strong></div>
</div></div>
<p class="note">If you register after 5 October 2026, HMRC will give you a filing deadline 3 months from the date on their letter or email. You must still pay any tax due by 31 January 2027.</p>
<h2>Late filing penalties</h2>
<ul>
<li>&pound;100 as soon as the return is late, even if no tax is due.</li>
<li>After 3 months: &pound;10 a day, up to &pound;900.</li>
<li>After 6 months: a further 5% of the tax due or &pound;300, whichever is greater.</li>
<li>After 12 months: another 5% or &pound;300.</li>
</ul>
<h2>Late payment penalties</h2>
<ul>
<li>5% of the unpaid tax at 30 days, again at 6 months, and again at 12 months.</li>
<li>Interest is also charged on the amount owed.</li>
</ul>
<h2>What to do now</h2>
<ol>
<li>Estimate this year\'s bill with the <a href="/sole-trader-tax-calculator/">take-home pay calculator</a> and set that amount aside each month.</li>
<li>If you work under CIS, check every deduction with the <a href="/cis-deduction-calculator/">CIS calculator</a> and keep the statements &mdash; they reduce what you pay in January.</li>
<li>Read <a href="/payments-on-account/">payments on account</a> so the first January bill does not surprise you.</li>
<li>Gather expenses and mileage; see <a href="/sole-trader-expenses/">what you can claim</a>.</li>
</ol>
''' + TS + '''
<h2>Frequently asked questions</h2>
<details><summary>Do I still get the &pound;100 penalty if I owe no tax?</summary><p>Yes. The initial late filing penalty applies even when there is no tax to pay.</p></details>
<details><summary>Can I pay through my tax code?</summary><p>Often yes if you owe less than &pound;3,000 and file online by 30 December, and you have enough PAYE income. Otherwise pay HMRC directly by 31 January.</p></details>
<details><summary>What about the 2026/27 tax year?</summary><p>That year runs 6 April 2026 to 5 April 2027. The online return and payment deadline will be 31 January 2028, with a paper deadline of 31 October 2027.</p></details>
''' + src("sa", "pen", "poa")

t5 = "Self Assessment Deadlines UK 2026/27"
page("self-assessment-deadlines/index.html", t5 + " | Brick & Budget",
     "Self Assessment deadlines for the 2025/26 tax year: 31 October paper, 31 January online and payment, penalties, and how to prepare.",
     sa_body,
     [{"@context": "https://schema.org", "@type": "Article", "headline": t5, "dateModified": "2026-11-06",
       "author": {"@type": "Organization", "name": "Brick & Budget"}},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
          {"@type": "Question", "name": "Do I still get the £100 penalty if I owe no tax?",
           "acceptedAnswer": {"@type": "Answer",
                              "text": "Yes. The initial late filing penalty applies even when there is no tax to pay."}},
          {"@type": "Question", "name": "What about the 2026/27 tax year?",
           "acceptedAnswer": {"@type": "Answer",
                              "text": "That year runs 6 April 2026 to 5 April 2027. The online return and payment deadline will be 31 January 2028."}}]},
      crumbs(t5)])

urls += ["sole-trader-tax-calculator/", "cis-deduction-calculator/", "self-assessment-deadlines/",
         "payments-on-account/", "sole-trader-expenses/"]
