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
C.decking = { inputs: [["length","Deck length, along the boards (m)",4],["width","Deck width (m)",3],["boardw","Board width (mm)",144],["boardl","Board length (m)",3.6],["joistl","Joist length (m)",4.8],["waste","Waste allowance (%)",10]],
  compute: function (v) { var cover = (v.boardw+5)/1000; /* 5 mm gap between boards */ var rows = ceil(v.width/cover); var boards = ceil(rows*v.length*(1+v.waste/100)/v.boardl);
    var joists = Math.floor(v.length/0.4)+1; /* joists across the deck at 400 mm centres */ var joistLengths = ceil(joists*v.width*(1+v.waste/100)/v.joistl); var screws = rows*joists*2;
    return [["Deck area", r2(v.length*v.width)+" m²"],["Board rows", rows],["Deck boards", boards],["Joists (400 mm centres)", joists],["Joist lengths to buy", joistLengths],["Deck screws (2 per board per joist)", screws],["Boxes of 200 screws", ceil(screws/200)]]; } };
C.fence = { inputs: [["run","Fence run length (m)",12],["panelw","Panel width incl. post (m)",1.83],["bags","Postcrete bags per post",2],["ends","Separate runs or ends (1 for one straight run)",1]],
  compute: function (v) { var panels = ceil(v.run/v.panelw); var posts = panels + Math.max(v.ends,1);
    return [["Fence panels", panels],["Posts", posts],["Postcrete bags (20 kg)", posts*v.bags],["Gravel boards (optional)", panels]]; } };
C.gravel = { inputs: [["length","Length (m)",5],["width","Width (m)",4],["depth","Depth (mm)",50],["density","Density (tonnes per m³)",1.6],["bag","Bulk bag weight (tonnes)",0.85]],
  compute: function (v) { var m3 = v.length*v.width*v.depth/1000; var t = m3*v.density;
    return [["Area", r2(v.length*v.width)+" m²"],["Volume", r2(m3)+" m³"],["Weight", r2(t)+" tonnes"],["Bulk bags", ceil(t/v.bag)],["25 kg bags", ceil(t*1000/25)]]; } };
C.insulation = { inputs: [["area","Loft floor area (m²)",40],["depth","Target total depth (mm)",270],["existing","Existing insulation depth (mm)",0],["joist","Joist depth, first layer (mm)",100],["roll1","Roll coverage, first layer (m²)",8.3],["roll2","Roll coverage, top layer (m²)",5.6]],
  compute: function (v) { var need = Math.max(v.depth - v.existing, 0); var l1 = Math.min(Math.max(v.joist - v.existing,0), need); var l2 = need - l1;
    var r1 = l1>0 ? ceil(v.area*1.05/v.roll1) : 0; var r2n = l2>0 ? ceil(v.area*1.05/v.roll2) : 0;
    return [["Depth to add", need+" mm"],["First layer, between joists", l1+" mm: "+r1+" rolls"],["Top layer, cross-laid", l2+" mm: "+r2n+" rolls"],["Total rolls", r1+r2n]]; } };
C.radiator = { inputs: [["length","Room length (m)",4],["width","Room width (m)",3.5],["height","Ceiling height (m)",2.4],["type","Room: 1 living, 2 bedroom, 3 kitchen, 4 bathroom",1],["north","North-facing or large windows: 1 yes, 0 no",0],["glazing","Glazing: 1 double, 2 single",1],["insul","Insulation: 1 good, 2 average, 3 poor",1]],
  compute: function (v) { var ft3 = v.length*v.width*v.height*35.315; var f = {1:5,2:4,3:4,4:6}[v.type] || 5; var b = ft3*f;
    if (v.north===1) b *= 1.15; if (v.glazing===2) b *= 1.1; if (v.insul===2) b *= 1.15; else if (v.insul===3) b *= 1.3;
    return [["Room volume", r2(v.length*v.width*v.height)+" m³"],["Heat output needed", Math.round(b)+" BTU/h"],["In watts", Math.round(b/3.412)+" W"]]; } };
function bbRender(id) {
  var c = C[id], box = document.getElementById("calc"), f = "";
  c.inputs.forEach(function (i) { f += '<label>' + i[1] + '<input type="number" step="any" inputmode="decimal" id="in-' + i[0] + '" value="' + i[2] + '"></label>'; });
  box.innerHTML = '<div class="inputs">' + f + '</div><button type="button" id="go">Calculate</button><div id="out" class="out" aria-live="polite"></div>';
  var run = function () { var v = {}; c.inputs.forEach(function (i) { v[i[0]] = parseFloat(document.getElementById("in-" + i[0]).value) || 0; });
    document.getElementById("out").innerHTML = c.compute(v).map(function (r) { return '<div><span>' + r[0] + '</span><strong>' + r[1] + '</strong></div>'; }).join(""); };
  document.getElementById("go").onclick = run; box.addEventListener("input", run); run();
}
if (typeof module !== "undefined") module.exports = C;
