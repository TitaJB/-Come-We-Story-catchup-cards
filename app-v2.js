const $=s=>document.querySelector(s);let all=[],session=[],index=0,mode="smart";const stateKey="catchup-cards-state-v2",favKey="catchup-cards-favourites-v1";
function shuffle(a){const x=[...a];for(let i=x.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[x[i],x[j]]=[x[j],x[i]];}return x;}
function journeyDeck(){const order=["Light & Funny","Catch-up","Memories & Family","London","Football & Sport","Would You Rather","Remove One","Black British Culture","Black American Culture","Cameroon","West African & Sub-Saharan African Culture","Career & Money","Relationships & Family","Hot Takes","Philosophy & Future"];return order.flatMap(c=>shuffle(all.filter(q=>q.category===c)));}
function smartDeck(){const remaining=shuffle(all),out=[];let last=null;while(remaining.length){const candidates=remaining.map((q,i)=>({q,i,score:Math.random()*3}));if(last)candidates.forEach(x=>{if(Math.abs(x.q.intensity-last.intensity)<=1)x.score+=2;if(x.q.category!==last.category)x.score+=1.2;if(x.q.tags.some(t=>last.tags.includes(t)))x.score+=.8;});candidates.sort((a,b)=>b.score-a.score);const pick=candidates[0];out.push(pick.q);last=pick.q;remaining.splice(pick.i,1);}return out;}
function save(){localStorage.setItem(stateKey,JSON.stringify({ids:session.map(q=>q.id),index,mode}));}
function restore(){try{const s=JSON.parse(localStorage.getItem(stateKey)||"null");if(!s)return false;session=s.ids.map(id=>all.find(q=>q.id===id)).filter(Boolean);index=Math.max(0,Math.min(s.index,session.length-1));mode=s.mode||"smart";return session.length>0;}catch{return false;}}
function render(){const q=session[index];if(!q)return;$("#category").textContent=q.category;$("#progress").textContent=`${index+1} / ${session.length}`;$("#cardType").textContent=q.type.replaceAll("_"," ");$("#question").textContent=q.question;$("#followUp").textContent=q.followUp;$("#followUp").classList.add("hidden");$("#followBtn").textContent="Reveal follow-up";const favs=new Set(JSON.parse(localStorage.getItem(favKey)||"[]"));$("#favBtn").textContent=favs.has(q.id)?"♥ Favourited":"♡ Favourite";save();}
function start(selectedMode,category=null){if(!all.length)return;mode=selectedMode;if(selectedMode==="random")session=shuffle(all);else if(selectedMode==="journey")session=journeyDeck();else if(selectedMode==="deck")session=shuffle(all.filter(q=>q.category===category));else session=smartDeck();index=0;$("#home").classList.add("hidden");$("#game").classList.remove("hidden");render();}
async function loadQuestions(){
  try{
    const response=await fetch("data/questions.json");
    if(!response.ok)throw new Error("Missing data/questions.json");
    const data=await response.json();
    if(!Array.isArray(data))throw new Error("Dataset is not an array");
    if(data.length!==750)throw new Error(`Expected 750 questions, found ${data.length}`);
    if(new Set(data.map(q=>q.id)).size!==750)throw new Error("Question IDs are not unique");
    if(new Set(data.map(q=>q.question)).size!==750)throw new Error("Question text is not unique");
    return data;
  }catch(error){
    console.warn("Using fallback decks",error);
    const paths=["data/light-funny.json","data/catch-up.json"];
    const decks=await Promise.all(paths.map(p=>fetch(p).then(r=>{if(!r.ok)throw new Error(`Missing ${p}`);return r.json();})));
    return decks.flat();
  }
}
function initialiseDeckPicker(){const cats=[...new Set(all.map(q=>q.category))];$("#deckPicker").innerHTML=cats.map(c=>`<button data-cat="${c.replaceAll('"','&quot;')}">${c}</button>`).join("");$("#deckPicker").addEventListener("click",e=>{if(e.target.dataset.cat)start("deck",e.target.dataset.cat)});if(localStorage.getItem(stateKey))$("#resumeBtn").classList.remove("hidden");}
loadQuestions().then(data=>{all=data;initialiseDeckPicker();}).catch(error=>{console.error(error);document.querySelector("#home h2").textContent="The question deck could not be loaded. Please refresh while online once.";});
document.addEventListener("click",e=>{const m=e.target.closest("[data-mode]")?.dataset.mode;if(m==="deck")$("#deckPicker").classList.toggle("hidden");else if(m)start(m);});
$("#nextBtn").onclick=()=>{if(index<session.length-1){index++;render();}};$("#prevBtn").onclick=()=>{if(index>0){index--;render();}};$("#followBtn").onclick=()=>{$("#followUp").classList.toggle("hidden");$("#followBtn").textContent=$("#followUp").classList.contains("hidden")?"Reveal follow-up":"Hide follow-up";};$("#favBtn").onclick=()=>{const q=session[index],f=new Set(JSON.parse(localStorage.getItem(favKey)||"[]"));f.has(q.id)?f.delete(q.id):f.add(q.id);localStorage.setItem(favKey,JSON.stringify([...f]));render();};$("#homeBtn").onclick=()=>{$("#game").classList.add("hidden");$("#home").classList.remove("hidden");};$("#resetBtn").onclick=()=>{localStorage.removeItem(stateKey);start(mode);};$("#resumeBtn").onclick=()=>{if(restore()){$("#home").classList.add("hidden");$("#game").classList.remove("hidden");render();}};$("#themeBtn").onclick=()=>{const d=document.documentElement;d.dataset.theme=d.dataset.theme==="dark"?"light":"dark";localStorage.setItem("theme",d.dataset.theme);};document.documentElement.dataset.theme=localStorage.getItem("theme")||"light";if("serviceWorker" in navigator)window.addEventListener("load",()=>navigator.serviceWorker.register("./sw-v2.js"));
