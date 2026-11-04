import {ids} from './registry.js';
export function readSelection(storage){try{const v=JSON.parse(storage.getItem('morrow-design'));return v?.version===1&&ids.has(v.id)?v.id:null;}catch{return null;}}
export function saveSelection(storage,id){if(!ids.has(id))return;try{storage.setItem('morrow-design',JSON.stringify({version:1,id}));}catch{/* Optional persistence. */}}
export function resolveRoute(path,selection){const p=path.replace(/\/+$/,'')||'/';if(p==='/')return selection?{kind:'design',id:selection,redirect:`/designs/${selection}/`}:{kind:'gallery',redirect:'/designs/'};if(p==='/designs')return{kind:'gallery'};const m=p.match(/^\/designs\/([^/]+)$/);return m&&ids.has(m[1])?{kind:'design',id:m[1]}:{kind:'missing'};}
