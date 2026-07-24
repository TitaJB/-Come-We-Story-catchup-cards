const CACHE='catchup-cards-v3';
const ASSETS=['./','./index.html','./styles.css','./app-v2.js','./manifest.webmanifest','./icons/icon-192.svg','./icons/icon-512.svg','./data/light-funny.json','./data/catch-up.json','./data/questions-pack-1.json.gz.b64','./data/questions-pack-2.json.gz.b64','./data/questions-pack-3.json.gz.b64','./data/questions-pack-4.json.gz.b64','./data/questions-pack-5.json.gz.b64'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(ASSETS)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
  if(event.request.mode==='navigate'){
    event.respondWith(fetch(event.request).then(response=>{const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));return response;}).catch(()=>caches.match('./index.html')));
    return;
  }
  event.respondWith(caches.match(event.request).then(cached=>cached||fetch(event.request).then(response=>{const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));return response;})));
});
