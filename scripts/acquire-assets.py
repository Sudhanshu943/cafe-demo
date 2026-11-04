from pathlib import Path
import urllib.request, concurrent.futures, json
ROOT=Path(__file__).resolve().parents[1]
photos={
 'interior':'photo-1501339847302-ac426a4a7cbb',
 'latte':'photo-1570968915860-54d5c301fa9f',
 'coffee':'photo-1442512595331-e89e73853f31',
 'iced':'photo-1461023058943-07fcbe16d735',
 'espresso':'photo-1510707577719-ae7c14805e3a',
 'pastry':'photo-1555507036-ab1f4038808a',
 'bread':'photo-1509440159596-0249088772ff',
 'brunch':'photo-1525351484163-7529414344d8',
 'barista':'photo-1511537190424-bbbab87ac5eb',
 'table':'photo-1495474472287-4d71bcdd2085',
 'matcha':'photo-1515823064-d6e0c04616a7',
}
def fetch(pair):
 name,pid=pair; url=f'https://images.unsplash.com/{pid}?auto=format&fit=crop&w=1400&q=82'
 path=ROOT/'assets/photos'/f'{name}.jpg';path.parent.mkdir(parents=True,exist_ok=True)
 try:
  urllib.request.urlretrieve(url,path)
  return {'id':name,'source':url,'bytes':path.stat().st_size,'status':'downloaded','license':'Unsplash license; stock illustration, not actual venue','creator':'See linked source item; attribution identity not independently verified'}
 except Exception as e:return {'id':name,'source':url,'status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,photos.items()))
(ROOT/'assets/provenance.json').write_text(json.dumps({'date':'2026-11-05','license_url':'https://unsplash.com/license','usage':'Illustrative demo photography only; review item rights before a real business launch.','photos':results},indent=2),encoding='utf-8')
for r in results: print(r['id'],r['status'],r.get('bytes',0))
# Self-host only the requested font files; retain the Google Fonts stylesheet source.
fontdir=ROOT/'assets/fonts';fontdir.mkdir(parents=True,exist_ok=True)
url='https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Space+Grotesk:wght@400;500;600;700&display=swap'
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
try:
 css=urllib.request.urlopen(req).read().decode();import re
 for i,fonturl in enumerate(dict.fromkeys(re.findall(r'url\((https:[^)]+)\)',css))):
  ext='woff2' if '.woff2' in fonturl else 'ttf';filename=f'font-{i}.{ext}';urllib.request.urlretrieve(fonturl,fontdir/filename);css=css.replace(fonturl,'/assets/fonts/'+filename)
 (fontdir/'fonts.css').write_text(css,encoding='utf-8')
 (fontdir/'README.md').write_text('Self-hosted DM Sans, Fraunces and Space Grotesk via Google Fonts. Stylesheet source: '+url+'\nFont licenses are retained in this folder.\n',encoding='utf-8')
 for family,repo in [('dm-sans','dmsans'),('fraunces','fraunces'),('space-grotesk','spacegrotesk')]:
  urllib.request.urlretrieve(f'https://raw.githubusercontent.com/google/fonts/main/ofl/{repo}/OFL.txt',fontdir/f'{family}-OFL.txt')
 print('Fonts acquired')
except Exception as e:
 print('Font acquisition limitation:',e)
 if not (fontdir/'fonts.css').exists():(fontdir/'fonts.css').write_text('/* System fallback fonts active. */')
