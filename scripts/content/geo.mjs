// Real country outlines for the picture tasks (content standard v2 §5).
// Natural Earth 1:50m (world-atlas, public domain) → d3-geo projection → SVG paths in a fixed viewBox.
// Output: scripts/content/geo.json, read by the Python generators. Run: node scripts/content/geo.mjs
import { readFileSync, writeFileSync } from 'node:fs';
import { geoConicConformal, geoPath } from 'd3-geo';
import { feature } from 'topojson-client';

const topo = JSON.parse(readFileSync(new URL('../../node_modules/world-atlas/countries-50m.json', import.meta.url)));
const all = feature(topo, topo.objects.countries).features;
const byName = (n) => all.find((f) => f.properties.name === n);

const CITIES = {
	Wien: [16.37, 48.21], Graz: [15.44, 47.07], Linz: [14.29, 48.31], Salzburg: [13.04, 47.81], Innsbruck: [11.4, 47.27],
	Klagenfurt: [14.31, 46.62], Bregenz: [9.75, 47.5], 'St. Pölten': [15.63, 48.2], Eisenstadt: [16.52, 47.85],
	Berlin: [13.4, 52.52], München: [11.58, 48.14], Bern: [7.45, 46.95], Zürich: [8.54, 47.37]
};

// A view: countries to fill (`main`), neighbours drawn quietly for context, the box they are fitted into.
const view = (main, around, w, h, pad) => {
	const fit = { type: 'FeatureCollection', features: main.map(byName) };
	const projection = geoConicConformal().parallels([46, 49]).rotate([-12, 0]).fitExtent([[pad, pad], [w - pad, h - pad]], fit);
	const path = geoPath(projection);
	const round = (d) => d.replace(/(\d+\.\d{1})\d+/g, '$1');
	const shapes = Object.fromEntries([...main, ...around].map((n) => [n, round(path(byName(n)))]));
	const centroids = Object.fromEntries(main.map((n) => [n, path.centroid(byName(n)).map((v) => Math.round(v))]));
	const cities = Object.fromEntries(Object.entries(CITIES).map(([n, ll]) => [n, projection(ll).map((v) => Math.round(v))]));
	return { w, h, main, shapes, centroids, cities };
};

const out = {
	dach: view(['Germany', 'Austria', 'Switzerland'], ['France', 'Italy', 'Czechia', 'Poland', 'Liechtenstein', 'Slovenia', 'Hungary', 'Slovakia', 'Netherlands', 'Belgium', 'Luxembourg', 'Denmark'], 400, 260, 12),
	austria: view(['Austria'], ['Germany', 'Switzerland', 'Italy', 'Czechia', 'Slovenia', 'Hungary', 'Slovakia', 'Liechtenstein'], 380, 160, 10)
};
writeFileSync(new URL('./geo.json', import.meta.url), JSON.stringify(out));
console.log('geo.json:', Object.keys(out).map((k) => `${k} ${Object.keys(out[k].shapes).length} shapes`).join(', '));
