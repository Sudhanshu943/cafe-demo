import {designs} from './shared/registry.js';
import {readSelection,saveSelection,resolveRoute} from './shared/routing.js';
import {menuItems,modal} from './shared/components.js';
import {renderGallery} from './design-gallery/index.js';

const app=document.querySelector('#app');let cleanup=()=>{};let generation=0;let activeDialog=null;
const storage={getItem:key=>localStorage.getItem(key),setItem:(key,value)=>localStorage.setItem(key,value)};
async function render(focus=false){
 const token=++generation;cleanup();cleanup=()=>{};activeDialog?.close();activeDialog=null;
 const route=resolveRoute(location.pathname,readSelection(storage));
 if(route.redirect)history.replaceState({},'',route.redirect);
 if(route.kind==='gallery'){
  app.innerHTML=renderGallery(readSelection(storage));document.title='Morrow — Eight Café Directions';document.body.dataset.design='gallery';
 }else if(route.kind==='design'){
  const d=designs.find(x=>x.id===route.id);saveSelection(storage,d.id);document.body.dataset.design=d.id;document.title=`Morrow — ${d.name}`;
  app.innerHTML='<main id="main"><p class="boot-message">Finding your morning…</p></main>';
  try{const page=await import(`/designs/${d.id}/index.js`);if(token!==generation)return;
   const style=document.createElement('link');style.rel='stylesheet';style.href=`/designs/${d.id}/styles.css`;style.dataset.pageStyle=d.id;
   await new Promise(resolve=>{style.onload=resolve;style.onerror=resolve;document.head.append(style);});if(token!==generation){style.remove();return;}
   app.innerHTML=`<div class="cafe-page ${d.id}" id="top">${page.render()}</div><a class="design-switch" data-route href="/designs/" aria-label="Change design, return to collection"><span aria-hidden="true">▦</span> Change design <span class="switch-count">${d.number} / 08</span></a>`;
   const pageCleanup=page.mount?.(app)||(()=>{});cleanup=()=>{pageCleanup();style.remove();};
  }catch(error){if(token!==generation)return;app.innerHTML='<main id="main" class="error-page"><h1>That morning needs a moment.</h1><p>The design could not load. Please try again.</p><a data-route href="/designs/">Back to all designs →</a></main>';console.error(error);}
 }else{document.body.dataset.design='gallery';document.title='Design not found — Morrow';app.innerHTML='<main id="main" class="error-page"><p class="eyebrow">404 / A LITTLE DETOUR</p><h1>Let’s find your kind of morning.</h1><a class="button" data-route href="/designs/">Explore all eight designs →</a></main>';}
 if(focus){window.scrollTo({top:0,behavior:'instant'});const h=app.querySelector('h1');if(h){h.tabIndex=-1;h.focus({preventScroll:true});}}
}
function openModal(title,body,src){activeDialog?.remove();app.insertAdjacentHTML('beforeend',modal(title,body));activeDialog=app.querySelector('dialog');if(src){const img=document.createElement('img');img.src=src;img.alt=title;activeDialog.insertBefore(img,activeDialog.querySelector('h2'));}activeDialog.addEventListener('click',e=>{if(e.target===activeDialog)activeDialog.close();});activeDialog.querySelector('[data-dialog-close]').onclick=()=>activeDialog.close();activeDialog.addEventListener('close',()=>{activeDialog?.remove();activeDialog=null;},{once:true});activeDialog.showModal();}
document.addEventListener('click',e=>{
 const link=e.target.closest('a[data-route]');if(link&&!e.metaKey&&!e.ctrlKey&&!e.shiftKey&&!e.altKey&&e.button===0){e.preventDefault();history.pushState({},'',link.getAttribute('href'));render(true);return;}
 const toggle=e.target.closest('.nav-toggle');if(toggle){const state=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(state));app.querySelector('#cafe-navigation')?.classList.toggle('is-open',state);return;}
 const anchor=e.target.closest('a[href^="#"]');if(anchor){const target=document.querySelector(anchor.getAttribute('href'));if(target){e.preventDefault();target.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});target.tabIndex=-1;target.focus({preventScroll:true});app.querySelector('.nav-toggle')?.setAttribute('aria-expanded','false');app.querySelector('#cafe-navigation')?.classList.remove('is-open');}return;}
 const category=e.target.closest('[data-category]');if(category){const section=category.closest('.menu-section');section.querySelectorAll('[data-category]').forEach(b=>b.setAttribute('aria-pressed',String(b===category)));section.querySelector('.menu-results').innerHTML=menuItems(category.dataset.category);return;}
 if(e.target.closest('[data-visit]')){openModal('A place in the making.','Morrow is a café design concept. The menu, prices and opening hours are sample content. A real address, contact details and directions will be added when this concept becomes a café.');return;}
 if(e.target.closest('[data-about]')){openModal('One café. Eight perspectives.','This collection explores eight independent designs for the same fictional café. Images illustrate a possible atmosphere; they do not depict a real Morrow venue. Use Change design to explore the collection.');return;}
 const photo=e.target.closest('[data-lightbox]');if(photo)openModal(photo.getAttribute('aria-label').replace('Enlarge: ',''),'Illustrative atmosphere photography for the Morrow café concept.',`/assets/photos/${photo.dataset.lightbox}.jpg`);
});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){const t=app.querySelector('.nav-toggle[aria-expanded="true"]');if(t){t.setAttribute('aria-expanded','false');app.querySelector('#cafe-navigation')?.classList.remove('is-open');t.focus();}}});
addEventListener('popstate',()=>render(true));render();
