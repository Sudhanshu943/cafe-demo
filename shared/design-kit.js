import {image} from './components.js';
export {image};
export {menu,money} from './content.js';
export function navigation(menuLabel='Menu',storyLabel='Our story',visitLabel='Visit us') {return `<button class="nav-toggle" aria-label="Open navigation" aria-controls="cafe-navigation" aria-expanded="false">Menu <span aria-hidden="true">＋</span></button><nav id="cafe-navigation" aria-label="Café navigation"><a href="#menu">${menuLabel}</a><a href="#story">${storyLabel}</a><a href="#visit">${visitLabel} ↗</a></nav>`;}
export function filters(selected='coffee'){return `<div class="menu-filters" role="group" aria-label="Menu categories">${[['coffee','Coffee','04'],['matcha','Matcha','03'],['kitchen','Kitchen','03']].map(([id,label,n])=>`<button data-category="${id}" aria-pressed="${id===selected}">${label}<span>${n}</span></button>`).join('')}</div>`;}
export const menuNote='<p class="menu-note">Sample menu & prices. Please ask about ingredients and allergens.</p>';
export const hours='<p>MON — FRI <span>8am — 8pm</span><br>SAT — SUN <span>9am — 9pm</span></p><small>Illustrative hours · Location to be announced</small>';
export const colophon=()=>`<div class="revision-colophon"><span>© ${new Date().getFullYear()} Morrow · Café concept</span><span>Sample content · Illustrative photography</span><button data-about>About this concept ↗</button></div>`;
export function photoButton(id,alt,classes=''){return `<button class="photo-button ${classes}" data-lightbox="${id}" aria-label="Enlarge: ${alt}">${image(id,alt)}<span aria-hidden="true">↗</span></button>`;}
