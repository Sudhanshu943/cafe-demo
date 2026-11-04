import * as THREE from '/assets/vendor/three.module.min.js';
export async function createScene(host,onFailure){
 const renderer=new THREE.WebGLRenderer({alpha:true,antialias:true,powerPreference:'low-power'});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.setClearColor(0x000000,0);renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.3;
 const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(35,1,.1,100);camera.position.set(3.5,3.1,5.8);camera.lookAt(0,.5,0);const group=new THREE.Group();scene.add(group);
 const ceramic=new THREE.MeshStandardMaterial({color:0xa48d6b,roughness:.28,metalness:.15});const coffee=new THREE.MeshStandardMaterial({color:0x48250e,roughness:.25});const cream=new THREE.MeshStandardMaterial({color:0xdec096,roughness:.6});
 const profile=[[0,0],[.4,0],[.58,.12],[.72,.4],[.79,.8],[.8,1.1],[.76,1.14],[.72,1.1],[.71,.8],[.64,.4],[.5,.14],[0,.12]].map(([x,y])=>new THREE.Vector2(x,y));
 const bowl=new THREE.Mesh(new THREE.LatheGeometry(profile,64),ceramic);bowl.position.y=.15;group.add(bowl);
 const handle=new THREE.Mesh(new THREE.TorusGeometry(.36,.085,18,48,Math.PI*1.65),ceramic);handle.position.set(.87,.88,0);handle.rotation.z=-Math.PI*.825;group.add(handle);
 const saucer=new THREE.Mesh(new THREE.LatheGeometry([[0,0],[1.12,0],[1.35,.06],[1.4,.13],[1.38,.17],[1.15,.1],[.7,.09],[0,.09]].map(([x,y])=>new THREE.Vector2(x,y)),64),ceramic);group.add(saucer);
 const surface=new THREE.Mesh(new THREE.CircleGeometry(.718,64),coffee);surface.rotation.x=-Math.PI/2;surface.position.y=1.23;group.add(surface);
 for(let i=0;i<7;i++){const leaf=new THREE.Mesh(new THREE.SphereGeometry(1,24,12),cream);leaf.scale.set(.1+i*.016,.003,.045+i*.009);leaf.position.set(0,1.235,-.24+i*.072);leaf.rotation.y=(i%2?1:-1)*.3;group.add(leaf);}
 const stem=new THREE.Mesh(new THREE.BoxGeometry(.018,.003,.52),cream);stem.position.set(0,1.238,0);group.add(stem);
 scene.add(new THREE.HemisphereLight(0xffeed7,0x32271d,3));const key=new THREE.DirectionalLight(0xffd3a0,4);key.position.set(-3,5,4);scene.add(key);const rim=new THREE.DirectionalLight(0xf3ecda,2);rim.position.set(3,2,-3);scene.add(rim);
 group.rotation.y=-.3;group.rotation.z=-.08;let target=-.3,drag=false,lastX=0,disposed=false;
 const draw=()=>{if(!disposed)renderer.render(scene,camera);};
 const resize=()=>{if(disposed)return;const {width,height}=host.getBoundingClientRect();if(!width||!height)return;renderer.setSize(width,height,false);camera.aspect=width/height;camera.updateProjectionMatrix();draw();};
 const canvas=renderer.domElement;canvas.setAttribute('role','img');canvas.setAttribute('aria-label','Interactive ceramic latte cup. Drag horizontally to rotate, or use left and right arrow keys.');canvas.tabIndex=0;
 canvas.addEventListener('pointerdown',down);canvas.addEventListener('pointermove',move);canvas.addEventListener('pointerup',up);canvas.addEventListener('pointercancel',up);canvas.addEventListener('keydown',keyDown);
 function down(e){drag=true;lastX=e.clientX;canvas.setPointerCapture(e.pointerId);}function move(e){if(!drag)return;target+=(e.clientX-lastX)*.012;lastX=e.clientX;group.rotation.y=target;draw();}function up(){drag=false;}function keyDown(e){if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();target+=(e.key==='ArrowLeft'?-.2:.2);group.rotation.y=target;draw();}}
 const lost=e=>{e.preventDefault();onFailure();};canvas.addEventListener('webglcontextlost',lost);host.append(canvas);const observer=new ResizeObserver(resize);observer.observe(host);resize();
 return()=>{disposed=true;observer.disconnect();canvas.removeEventListener('pointerdown',down);canvas.removeEventListener('pointermove',move);canvas.removeEventListener('pointerup',up);canvas.removeEventListener('pointercancel',up);canvas.removeEventListener('keydown',keyDown);canvas.removeEventListener('webglcontextlost',lost);scene.traverse(o=>{if(o.geometry)o.geometry.dispose();});ceramic.dispose();coffee.dispose();cream.dispose();renderer.dispose();renderer.forceContextLoss();canvas.remove();};
}
