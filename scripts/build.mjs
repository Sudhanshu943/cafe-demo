import {cp,mkdir,readFile,writeFile,stat} from 'node:fs/promises';
import path from 'node:path';
const root=process.cwd();await mkdir('dist',{recursive:true});
for(const name of ['index.html','app.js','shared','design-gallery','designs','assets'])await cp(name,path.join('dist',name),{recursive:true,filter:source=>!source.split(path.sep).includes('docs')});
const {designs}=await import('../shared/registry.js');
for(const d of designs){const dir=path.join('dist','designs',d.id);await mkdir(dir,{recursive:true});await cp('index.html',path.join(dir,'index.html'));await stat(path.join(dir,'index.js'));await stat(path.join(dir,'styles.css'));}
await cp('index.html','dist/designs/index.html');await cp('index.html','dist/404.html');
await writeFile('dist/_redirects','/* /index.html 200\n');
const manifest=JSON.parse(await readFile('.openai/hosting.json','utf8'));if(manifest.static?.directory!=='dist')throw Error('Incorrect static directory');
console.log(`Built gallery and ${designs.length} independent design routes into dist/`);
