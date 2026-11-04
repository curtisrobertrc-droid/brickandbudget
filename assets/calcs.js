/* Brick & Budget calculators. All maths in plain functions so they can be tested. */
var C = {};
var r2 = function (n) { return Math.round(n * 100) / 100; };
var ceil = Math.ceil;
var gbp = function (n) { return "£" + n.toFixed(2); };
C.plasterboard = { inputs: [["length","Wall or ceiling length (m)",4],["height","Height or width (m)",2.4],["openings","Doors/windows area to deduct (m²)",1.9],["waste","Waste allowance (%)",10]],
  compute: function (v) { var area = Math.max(v.length*v.height - v.openings, 0); var a = area*(1+v.waste/100); var sheets = ceil(a/2.88);
    return [["Net area", r2(area)+" m²"],["Sheets (2400 x 1200 mm)", sheets],["Drywall screws (approx. 30 per sheet)", sheets*30],["Jointing tape (m, approx. 1.3 m per m²)", ceil(area*1.3)]]; } };
C.plaster = { inputs: [["area","Area to plaster (m²)",12],["thickness","Coat thickness (mm)",2],["waste","Waste allowance (%)",10]],
  compute: function (v) { var kg = v.area * v.thickness * 1.15 * (1+v.waste/100); /* multi-finish approx. 1.15 kg per m² per mm */
    return [["Plaster needed", r2(kg)+" kg"],["25 kg bags", ceil(kg/25)]]; } };
C.paint = { inputs: [["area","Wall area (m²)",30],["coats","Number of coats",2],["coverage","Coverage on tin (m² per litre)",12]],
  compute: function (v) { var l = v.area*v.coats/v.coverage; return [["Paint needed", r2(l)+" litres"],["2.5 L tins", ceil(l/2.5)],["5 L tins", ceil(l/5)]]; } };
C.tiles = { inputs: [["area","Area to tile (m²)",6],["tw","Tile width (mm)",300],["th","Tile height (mm)",600],["waste","Waste allowance (%)",10]],
  compute: function (v) { var t = (v.tw/1000)*(v.th/1000); var n = ceil(v.area*(1+v.waste/100)/t); var adh = v.area*4;
    return [["Tiles needed", n],["Adhesive (approx. 4 kg per m²)", r2(adh)+" kg"],["20 kg adhesive bags", ceil(adh/20)],["Grout (approx. 0.5 kg per m²)", r2(v.area*0.5)+" kg"]]; } };
C.concrete = { inputs: [["length","Length (m)",3],["width","Width (m)",2],["depth","Depth (mm)",100],["waste","Waste allowance (%)",5]],
  compute: function (v) { var m3 = v.length*v.width*(v.depth/1000)*(1+v.waste/100); var bags = ceil(m3/0.01);
    return [["Volume", r2(m3)+" m³"],["20 kg ready-mix bags (approx. 0.01 m³ each)", bags],["Or 1:2:4 mix: cement 25 kg bags", ceil(m3*12)]]; } };
C.bricks = { inputs: [["length","Wall length (m)",5],["height","Wall height (m)",1],["skins","Skins (1 = half-brick wall, 2 = full)",1],["waste","Waste allowance (%)",5]],
  compute: function (v) { var area = v.length*v.height; var b = ceil(area*60*v.skins*(1+v.waste/100)); var mortar = area*v.skins*0.022;
    return [["Wall area", r2(area)+" m²"],["Bricks (60 per m² per skin)", b],["Mortar", r2(mortar)+" m³"],["Building sand (tonnes, approx.)", r2(mortar*1.6)]]; } };
C.flooring = { inputs: [["length","Room length (m)",4],["width","Room width (m)",3.5],["pack","Pack coverage (m²)",2.2],["waste","Waste allowance (%)",8]],
  compute: function (v) { var a = v.length*v.width; var packs = ceil(a*(1+v.waste/100)/v.pack);
    return [["Floor area", r2(a)+" m²"],["Packs needed", packs],["Underlay (m²)", ceil(a)],["Perimeter for beading (m)", r2(2*(v.length+v.width))]]; } };
C.vat = { inputs: [["amount","Amount (£)",100],["rate","VAT rate (%)",20],["mode","1 = add VAT, 2 = remove VAT",1]],
  compute: function (v) { var net, vat, gross; if (v.mode === 2) { gross = v.amount; net = gross/(1+v.rate/100); vat = gross-net; } else { net = v.amount; vat = net*v.rate/100; gross = net+vat; }
    return [["Net (ex VAT)", gbp(net)],["VAT", gbp(vat)],["Gross (inc VAT)", gbp(gross)]]; } };
C.skirting = { inputs: [["perimeter","Room perimeter (m)",14],["doors","Number of doorways",1],["doorw","Door width (m)",0.85],["len","Length per piece (m)",2.4],["waste","Waste allowance (%)",10]],
  compute: function (v) { var run = Math.max(v.perimeter - v.doors*v.doorw, 0); return [["Run length", r2(run)+" m"],["Lengths needed", ceil(run*(1+v.waste/100)/v.len)]]; } };
C.wallpaper = { inputs: [["perimeter","Total wall width (m)",14],["height","Wall height (m)",2.4],["repeat","Pattern repeat (cm)",0],["rollw","Roll width (cm)",53],["rolll","Roll length (m)",10]],
  compute: function (v) { var drop = v.height + 0.1 + v.repeat/100; var perRoll = Math.floor(v.rolll/drop); var drops = ceil(v.perimeter/(v.rollw/100));
    return [["Drops needed", drops],["Full drops per roll", perRoll],["Rolls needed", perRoll>0 ? ceil(drops/perRoll) : "Roll too short"]]; } };
function bbRender(id) {
  var c = C[id], box = document.getElementById("calc"), f = "";
  c.inputs.forEach(function (i) { f += '<label>' + i[1] + '<input type="number" step="any" inputmode="decimal" id="in-' + i[0] + '" value="' + i[2] + '"></label>'; });
  box.innerHTML = '<div class="inputs">' + f + '</div><button type="button" id="go">Calculate</button><div id="out" class="out" aria-live="polite"></div>';
  var run = function () { var v = {}; c.inputs.forEach(function (i) { v[i[0]] = parseFloat(document.getElementById("in-" + i[0]).value) || 0; });
    document.getElementById("out").innerHTML = c.compute(v).map(function (r) { return '<div><span>' + r[0] + '</span><strong>' + r[1] + '</strong></div>'; }).join(""); };
  document.getElementById("go").onclick = run; box.addEventListener("input", run); run();
}
if (typeof module !== "undefined") module.exports = C;
