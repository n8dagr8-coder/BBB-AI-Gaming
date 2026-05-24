#!/usr/bin/env python3
"""
BBB GAMING LAUNCHER - Command Center Edition
Drop-in replacement for the original app.py.

Features beyond the original:
  - Live service health checks (UP / DOWN / latency) for all 6 services
  - Live host system stats (CPU, RAM, load, uptime) via psutil
  - Live GPU stats (util, VRAM, temp, power) via nvidia-smi when present
  - Animated command-center UI that polls /api/status and /api/stats

Run:
    pip install flask psutil
    python3 app.py
Then open http://<this-host>:5100

Everything degrades gracefully: if psutil/nvidia-smi/a service is missing
or times out, the page still loads and just shows that piece as unavailable.
"""

import socket
import time
import shutil
import subprocess
from urllib.parse import urlparse

from flask import Flask, jsonify

try:
    import psutil
except Exception:
    psutil = None

app = Flask(__name__)

SERVICES = [
    {"key": "spectator", "name": "AI Spectator",    "code": "AI",
     "desc": "Live gameplay vision and commentary analysis.",
     "url": "http://192.168.0.102:5090", "accent": "#21d4ff"},
    {"key": "summary",   "name": "Session Summary", "code": "SM",
     "desc": "AI generated stream recaps and creator notes.",
     "url": "http://192.168.0.102:5091", "accent": "#2aa8ff"},
    {"key": "highlights","name": "Highlight Queue", "code": "HQ",
     "desc": "Detected gameplay moments and content candidates.",
     "url": "http://192.168.0.102:5092", "accent": "#ff3f8e"},
    {"key": "reports",   "name": "Highlight Report","code": "RP",
     "desc": "Ranked session notes, hype scores, and recaps.",
     "url": "http://192.168.0.102:5093", "accent": "#ffe600"},
    {"key": "portal",    "name": "BBB AI Portal",   "code": "AI",
     "desc": "Open WebUI for local private AI access.",
     "url": "http://192.168.0.101:3000", "accent": "#70ff42"},
    {"key": "ops",       "name": "Operations",      "code": "OP",
     "desc": "Infrastructure control through Portainer.",
     "url": "https://192.168.0.101:9443", "accent": "#c084fc"},
]

CHECK_TIMEOUT = 1.0


def check_service(svc):
    parsed = urlparse(svc["url"])
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    start = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=CHECK_TIMEOUT):
            latency = round((time.perf_counter() - start) * 1000)
            return {"key": svc["key"], "up": True, "latency": latency}
    except Exception:
        return {"key": svc["key"], "up": False, "latency": None}


def _num(s):
    try:
        return float(s)
    except Exception:
        return None


def get_gpu():
    if not shutil.which("nvidia-smi"):
        return []
    query = ("--query-gpu=name,utilization.gpu,memory.used,memory.total,"
             "temperature.gpu,power.draw")
    try:
        out = subprocess.run(
            ["nvidia-smi", query, "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=2.0,
        )
        gpus = []
        for line in out.stdout.strip().splitlines():
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 6:
                continue
            name, util, mem_u, mem_t, temp, power = parts
            gpus.append({
                "name": name, "util": _num(util),
                "mem_used": _num(mem_u), "mem_total": _num(mem_t),
                "temp": _num(temp), "power": _num(power),
            })
        return gpus
    except Exception:
        return []


def get_system():
    if psutil is None:
        return {"available": False}
    try:
        vm = psutil.virtual_memory()
        boot = psutil.boot_time()
        up_s = int(time.time() - boot)
        days, rem = divmod(up_s, 86400)
        hours, rem = divmod(rem, 3600)
        mins = rem // 60
        uptime = f"{days}d {hours}h {mins}m" if days else f"{hours}h {mins}m"
        try:
            load = [round(x, 2) for x in psutil.getloadavg()]
        except Exception:
            load = None
        return {
            "available": True,
            "cpu": psutil.cpu_percent(interval=None),
            "cores": psutil.cpu_count(logical=True),
            "mem_pct": vm.percent,
            "mem_used_gb": round(vm.used / 1e9, 1),
            "mem_total_gb": round(vm.total / 1e9, 1),
            "load": load, "uptime": uptime,
        }
    except Exception:
        return {"available": False}


@app.route("/api/status")
def api_status():
    results = [check_service(s) for s in SERVICES]
    up = sum(1 for r in results if r["up"])
    return jsonify({"services": results, "online": up,
                    "total": len(results), "ts": int(time.time())})


@app.route("/api/stats")
def api_stats():
    return jsonify({"system": get_system(), "gpu": get_gpu()})


def build_cards():
    html = []
    for s in SERVICES:
        html.append(
            '<a class="card" data-key="%s" href="%s" style="--accent:%s">'
            '<div class="card-glow"></div>'
            '<div class="icon">%s</div>'
            '<div class="card-body"><div class="card-head">'
            '<h2>%s</h2><span class="dot" data-dot="%s"></span></div>'
            '<p>%s</p>'
            '<div class="card-meta" data-meta="%s">checking&hellip;</div>'
            '</div><div class="arrow">&rsaquo;</div></a>'
            % (s["key"], s["url"], s["accent"], s["code"], s["name"],
               s["key"], s["desc"], s["key"])
        )
    return "\n".join(html)


@app.route("/")
def home():
    return PAGE.replace("<!--CARDS-->", build_cards())


PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BBB Gaming &mdash; Command Center</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root{
  --bg0:#04080d; --bg1:#070f17; --bg2:#0c1622;
  --ink:#e8f8ff; --muted:rgba(216,242,255,.55);
  --line:rgba(160,220,255,.18); --line2:rgba(160,220,255,.30);
  --cyan:#7df9ff; --up:#3dffa2; --down:#ff5470; --warn:#ffd23f;
}
*{box-sizing:border-box}
html,body{margin:0;min-height:100%}
body{
  font-family:"Segoe UI",system-ui,Arial,sans-serif;
  color:var(--ink); background:var(--bg0);
  background:
    radial-gradient(1200px 600px at 50% -10%, rgba(125,249,255,.10), transparent 60%),
    radial-gradient(900px 500px at 100% 110%, rgba(192,132,252,.08), transparent 60%),
    linear-gradient(160deg,var(--bg0),var(--bg1) 45%,var(--bg2));
  overflow-x:hidden;
}
body::before{
  content:"";position:fixed;inset:-2px;z-index:0;pointer-events:none;
  background:
    linear-gradient(90deg,rgba(125,249,255,.05) 1px,transparent 1px),
    linear-gradient(rgba(125,249,255,.035) 1px,transparent 1px);
  background-size:46px 46px;
  -webkit-mask:radial-gradient(circle at 50% 30%,#000 0%,transparent 80%);
  mask:radial-gradient(circle at 50% 30%,#000 0%,transparent 80%);
  animation:drift 28s linear infinite;
}
@keyframes drift{to{background-position:46px 46px,46px 46px}}
body::after{
  content:"";position:fixed;inset:0;z-index:0;pointer-events:none;
  background:linear-gradient(180deg,transparent,rgba(125,249,255,.06),transparent);
  height:160px;animation:sweep 7s ease-in-out infinite;opacity:.5;
}
@keyframes sweep{0%{transform:translateY(-160px)}100%{transform:translateY(110vh)}}

.shell{position:relative;z-index:1;width:min(1480px,95vw);margin:26px auto 40px}

.topbar{display:flex;justify-content:space-between;align-items:center;
  gap:16px;flex-wrap:wrap;
  border:1px solid var(--line);border-radius:18px;padding:14px 20px;
  background:linear-gradient(180deg,rgba(10,20,30,.6),rgba(6,12,18,.5));
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.brandmini{display:flex;align-items:center;gap:14px;font-weight:800;letter-spacing:.18em}
.chip{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;
  font-family:Georgia,serif;font-weight:900;font-size:18px;color:var(--cyan);
  border:1px solid var(--line2);background:rgba(0,0,0,.3);
  box-shadow:inset 0 0 16px rgba(125,249,255,.12)}
.statusrail{display:flex;gap:10px;flex-wrap:wrap;font-size:12px;letter-spacing:.08em}
.pill{display:flex;align-items:center;gap:8px;padding:7px 13px;border-radius:999px;
  border:1px solid var(--line);background:rgba(0,0,0,.28)}
.pill b{font-variant-numeric:tabular-nums}
.beacon{width:9px;height:9px;border-radius:50%;background:var(--up);
  box-shadow:0 0 0 0 var(--up);animation:beat 1.8s ease-out infinite}
@keyframes beat{0%{box-shadow:0 0 0 0 rgba(61,255,162,.6)}100%{box-shadow:0 0 0 12px rgba(61,255,162,0)}}

.hero{text-align:center;margin:34px 0 26px}
.hero h1{margin:0;font-weight:900;letter-spacing:.14em;
  font-size:clamp(40px,8vw,92px);
  background:linear-gradient(#f4fbff,#86b9d6 42%,#d8f8ff 58%,#2b4a5e);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 4px 26px rgba(125,249,255,.25))}
.hero p{margin:10px 0 0;letter-spacing:.5em;text-transform:uppercase;
  font-size:clamp(10px,2vw,14px);color:var(--muted)}

.layout{display:grid;grid-template-columns:1fr minmax(280px,440px) 1fr;
  gap:30px;align-items:center;margin-top:8px}
.side{display:grid;gap:20px}

.card{position:relative;display:flex;align-items:center;gap:16px;min-height:112px;
  padding:18px 20px;border-radius:18px;color:var(--ink);text-decoration:none;
  border:1px solid var(--line);overflow:hidden;
  background:linear-gradient(135deg,rgba(9,18,28,.9),rgba(4,9,15,.72));
  transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}
.card:hover{transform:translateY(-3px);border-color:color-mix(in srgb,var(--accent) 70%,white 0%);
  box-shadow:0 0 30px color-mix(in srgb,var(--accent) 35%,transparent)}
.card-glow{position:absolute;inset:0;opacity:0;transition:opacity .25s ease;
  background:radial-gradient(280px 120px at 18% 50%,color-mix(in srgb,var(--accent) 22%,transparent),transparent 70%)}
.card:hover .card-glow{opacity:1}
.icon{flex:0 0 auto;width:56px;height:56px;border-radius:50%;display:grid;place-items:center;
  font-weight:900;color:var(--accent);border:1px solid var(--accent);
  box-shadow:0 0 18px color-mix(in srgb,var(--accent) 60%,transparent)}
.card-body{position:relative;z-index:1;flex:1;min-width:0}
.card-head{display:flex;align-items:center;gap:10px}
.card h2{margin:0;font-size:17px;letter-spacing:.06em;text-transform:uppercase}
.card p{margin:5px 0 0;font-size:12.5px;color:var(--muted);line-height:1.35}
.card-meta{margin-top:7px;font-size:11px;letter-spacing:.06em;color:var(--muted);
  font-variant-numeric:tabular-nums}
.dot{width:10px;height:10px;border-radius:50%;flex:0 0 auto;
  background:#5b6b78;box-shadow:0 0 0 3px rgba(255,255,255,.04)}
.dot.up{background:var(--up);box-shadow:0 0 10px var(--up);animation:beat 1.8s ease-out infinite}
.dot.down{background:var(--down);box-shadow:0 0 10px var(--down)}
.arrow{position:relative;z-index:1;margin-left:auto;font-size:30px;color:var(--accent);opacity:.7}

.reactor{aspect-ratio:1;border-radius:50%;display:grid;place-items:center;position:relative;
  border:2px solid rgba(230,250,255,.4);overflow:hidden;
  background:
    radial-gradient(circle at 35% 25%,rgba(255,255,255,.4),transparent 26%),
    radial-gradient(circle at 50% 60%,rgba(125,249,255,.12),rgba(0,0,0,.25) 70%);
  box-shadow:inset 0 0 70px rgba(125,249,255,.2),inset 0 -24px 80px rgba(0,0,0,.4),
    0 0 50px rgba(125,249,255,.18)}
.ring{position:absolute;border-radius:50%;border:1px solid rgba(125,249,255,.35)}
.ring.r1{inset:6%;animation:spin 18s linear infinite}
.ring.r2{inset:15%;border-style:dashed;border-color:rgba(125,249,255,.25);animation:spin 26s linear infinite reverse}
.ring.r3{inset:26%;border-color:rgba(192,132,252,.3)}
@keyframes spin{to{transform:rotate(360deg)}}
.reactor .logo{position:relative;z-index:2;font-family:Georgia,serif;font-weight:900;
  font-size:clamp(70px,12vw,140px);letter-spacing:-.06em;color:rgba(210,235,245,.18);
  -webkit-text-stroke:1px rgba(235,250,255,.5);
  text-shadow:1px 1px 1px rgba(255,255,255,.7),-1px -1px 1px rgba(0,0,0,.8),0 0 18px rgba(125,249,255,.25)}
.reactor .sub{position:absolute;bottom:18%;z-index:2;font-size:11px;letter-spacing:.3em;
  color:var(--cyan);text-transform:uppercase}

.telemetry{margin-top:30px;display:grid;grid-template-columns:1.4fr 1fr;gap:18px}
@media(max-width:820px){.telemetry{grid-template-columns:1fr}}
.panel{border:1px solid var(--line);border-radius:18px;padding:18px 20px;
  background:linear-gradient(180deg,rgba(8,16,24,.7),rgba(4,9,15,.55));
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.panel h3{margin:0 0 14px;font-size:12px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--cyan);display:flex;align-items:center;gap:10px}
.panel h3::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--cyan);
  box-shadow:0 0 10px var(--cyan)}
.gauges{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:16px}
.gauge .lbl{font-size:11px;letter-spacing:.1em;color:var(--muted);text-transform:uppercase}
.gauge .val{font-size:24px;font-weight:800;font-variant-numeric:tabular-nums;margin:2px 0 7px}
.bar{height:7px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}
.bar i{display:block;height:100%;width:0;border-radius:99px;
  background:linear-gradient(90deg,var(--up),var(--cyan));transition:width .6s ease}
.bar.hot i{background:linear-gradient(90deg,var(--warn),var(--down))}
.kv{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.05);
  font-size:13px}
.kv:last-child{border-bottom:none}
.kv span{color:var(--muted)} .kv b{font-variant-numeric:tabular-nums}
.unavail{color:var(--muted);font-size:13px;padding:8px 0}

.footer{text-align:center;margin-top:26px;font-size:11px;letter-spacing:.24em;
  text-transform:uppercase;color:rgba(225,245,255,.28)}
.footer b{color:var(--cyan)}

@media(max-width:920px){
  .layout{grid-template-columns:1fr}
  .reactor{width:min(72vw,340px);margin:0 auto;order:-1}
}

/* BBB POLISH ANIMATION PATCH */
.card {
  animation: cardFloat 6s ease-in-out infinite;
}

.card:nth-child(2n) {
  animation-delay: .35s;
}

.card:nth-child(3n) {
  animation-delay: .7s;
}

@keyframes cardFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}

.reactor {
  animation: reactorPulse 4s ease-in-out infinite;
}

@keyframes reactorPulse {
  0%, 100% {
    box-shadow:
      inset 0 0 70px rgba(125,249,255,.20),
      inset 0 -24px 80px rgba(0,0,0,.40),
      0 0 50px rgba(125,249,255,.18);
  }
  50% {
    box-shadow:
      inset 0 0 95px rgba(125,249,255,.30),
      inset 0 -24px 90px rgba(0,0,0,.42),
      0 0 85px rgba(125,249,255,.32);
  }
}

.logo {
  animation: etchedGlow 5s ease-in-out infinite;
}

@keyframes etchedGlow {
  0%, 100% { opacity: .82; filter: drop-shadow(0 8px 10px rgba(0,0,0,.65)); }
  50% { opacity: 1; filter: drop-shadow(0 0 18px rgba(125,249,255,.32)); }
}

.panel {
  animation: glassBreath 8s ease-in-out infinite;
}

@keyframes glassBreath {
  0%, 100% { border-color: rgba(160,220,255,.18); }
  50% { border-color: rgba(125,249,255,.36); }
}

@media (prefers-reduced-motion: reduce) {
  .card,
  .reactor,
  .logo,
  .panel,
  body::before,
  body::after,
  .ring,
  .beacon {
    animation: none !important;
  }
}

</style>
</head>
<body>
<div class="shell">

  <div class="topbar">
    <div class="brandmini"><div class="chip">B</div> BBB COMMAND CENTER</div>
    <div class="statusrail">
      <div class="pill"><span class="beacon"></span> <b id="svcCount">&mdash;/&mdash;</b> SERVICES</div>
      <div class="pill">CPU <b id="pCpu">&mdash;</b></div>
      <div class="pill">RAM <b id="pRam">&mdash;</b></div>
      <div class="pill">GPU <b id="pGpu">&mdash;</b></div>
      <div class="pill">UP <b id="pUptime">&mdash;</b></div>
    </div>
  </div>

  <section class="hero">
    <h1>BBB GAMING</h1>
    <p>AI Enhanced Gaming Infrastructure</p>
  </section>

  <main class="layout">
    <section class="side" id="sideLeft"></section>
    <section class="reactor">
      <div class="ring r1"></div><div class="ring r2"></div><div class="ring r3"></div>
      <div class="logo">BBB</div>
      <div class="sub" id="reactorSub">initializing</div>
    </section>
    <section class="side" id="sideRight"></section>
  </main>

  <section class="telemetry">
    <div class="panel">
      <h3>System Telemetry</h3>
      <div class="gauges">
        <div class="gauge"><div class="lbl">CPU Load</div><div class="val" id="gCpu">&mdash;</div>
          <div class="bar"><i id="bCpu"></i></div></div>
        <div class="gauge"><div class="lbl">Memory</div><div class="val" id="gRam">&mdash;</div>
          <div class="bar"><i id="bRam"></i></div></div>
        <div class="gauge"><div class="lbl">GPU Util</div><div class="val" id="gGpu">&mdash;</div>
          <div class="bar"><i id="bGpu"></i></div></div>
        <div class="gauge"><div class="lbl">VRAM</div><div class="val" id="gVram">&mdash;</div>
          <div class="bar"><i id="bVram"></i></div></div>
      </div>
      <div style="margin-top:14px" id="sysExtra"></div>
    </div>
    <div class="panel">
      <h3>GPU Detail</h3>
      <div id="gpuDetail"><div class="unavail">Querying nvidia-smi&hellip;</div></div>
    </div>
  </section>

  <div class="footer">Big Brain Brand &bull; <b>Local-First</b> AI Gaming Platform
    &bull; <span id="clock">&mdash;</span></div>

</div>

<script>
const CARDS = `<!--CARDS-->`;
(function(){
  const tmp=document.createElement('div'); tmp.innerHTML=CARDS;
  const cards=[...tmp.querySelectorAll('.card')];
  const L=document.getElementById('sideLeft'), R=document.getElementById('sideRight');
  cards.forEach((c,i)=>(i%2===0?L:R).appendChild(c));
})();

const fmt=(n,suf='')=>(n==null||isNaN(n))?'\u2014':(Math.round(n)+suf);
function setBar(el,pct,hotAt=85){
  el.style.width=Math.max(0,Math.min(100,pct||0))+'%';
  el.parentElement.classList.toggle('hot',(pct||0)>=hotAt);
}

async function pollStatus(){
  try{
    const r=await fetch('/api/status',{cache:'no-store'}); const d=await r.json();
    document.getElementById('svcCount').textContent=d.online+'/'+d.total;
    document.getElementById('reactorSub').textContent=d.online+' of '+d.total+' online';
    d.services.forEach(s=>{
      const dot=document.querySelector('[data-dot="'+s.key+'"]');
      const meta=document.querySelector('[data-meta="'+s.key+'"]');
      if(dot){dot.classList.remove('up','down');dot.classList.add(s.up?'up':'down');}
      if(meta)meta.textContent=s.up?('ONLINE \u2022 '+s.latency+' ms'):'OFFLINE';
    });
  }catch(e){}
}
async function pollStats(){
  try{
    const r=await fetch('/api/stats',{cache:'no-store'}); const d=await r.json();
    const s=d.system||{};
    if(s.available){
      document.getElementById('gCpu').textContent=fmt(s.cpu,'%');
      document.getElementById('pCpu').textContent=fmt(s.cpu,'%');
      setBar(document.getElementById('bCpu'),s.cpu);
      document.getElementById('gRam').textContent=fmt(s.mem_pct,'%');
      document.getElementById('pRam').textContent=fmt(s.mem_pct,'%');
      setBar(document.getElementById('bRam'),s.mem_pct);
      document.getElementById('pUptime').textContent=s.uptime||'\u2014';
      document.getElementById('sysExtra').innerHTML=
        '<div class="kv"><span>Cores</span><b>'+(s.cores!=null?s.cores:'\u2014')+'</b></div>'+
        '<div class="kv"><span>Memory</span><b>'+(s.mem_used_gb!=null?s.mem_used_gb:'\u2014')+' / '+(s.mem_total_gb!=null?s.mem_total_gb:'\u2014')+' GB</b></div>'+
        '<div class="kv"><span>Load avg</span><b>'+(s.load?s.load.join('  '):'\u2014')+'</b></div>'+
        '<div class="kv"><span>Uptime</span><b>'+(s.uptime!=null?s.uptime:'\u2014')+'</b></div>';
    }else{
      document.getElementById('sysExtra').innerHTML=
        '<div class="unavail">psutil not installed \u2014 run: pip install psutil</div>';
    }
    const g=d.gpu||[];
    if(g.length){
      const g0=g[0], vramPct=g0.mem_total?100*g0.mem_used/g0.mem_total:0;
      document.getElementById('gGpu').textContent=fmt(g0.util,'%');
      document.getElementById('pGpu').textContent=fmt(g0.util,'%');
      setBar(document.getElementById('bGpu'),g0.util);
      document.getElementById('gVram').textContent=fmt(vramPct,'%');
      setBar(document.getElementById('bVram'),vramPct);
      document.getElementById('gpuDetail').innerHTML=g.map(function(x,i){return(
        '<div class="kv"><span>GPU '+i+' \u2014 '+(x.name||'?')+'</span><b>'+fmt(x.util,'%')+'</b></div>'+
        '<div class="kv"><span>VRAM</span><b>'+fmt(x.mem_used)+' / '+fmt(x.mem_total)+' MB</b></div>'+
        '<div class="kv"><span>Temp</span><b>'+fmt(x.temp,'\u00b0C')+'</b></div>'+
        '<div class="kv"><span>Power</span><b>'+fmt(x.power,' W')+'</b></div>'
      );}).join('');
    }else{
      document.getElementById('gGpu').textContent='n/a';
      document.getElementById('pGpu').textContent='n/a';
      document.getElementById('gpuDetail').innerHTML=
        '<div class="unavail">No NVIDIA GPU detected on this host.</div>';
    }
  }catch(e){}
}
function tick(){document.getElementById('clock').textContent=new Date().toLocaleTimeString();}

pollStatus(); pollStats(); tick();
setInterval(pollStatus,5000);
setInterval(pollStats,3000);
setInterval(tick,1000);
</script>
</body>
</html>"""



# BBB VM CONTROL ROUTES

def run_epyc(cmd):
    try:
        out = subprocess.run(
            ["ssh", "epyc", cmd],
            capture_output=True,
            text=True,
            timeout=15
        )
        return out.stdout.strip() or out.stderr.strip()
    except Exception as e:
        return str(e)

@app.route("/api/vms")
def api_vms():
    output = run_epyc("virsh list --all")
    return jsonify({"output": output})

@app.route("/api/vm/<name>/<action>")
def api_vm_action(name, action):
    allowed = {
        "start": f"virsh start {name}",
        "shutdown": f"virsh shutdown {name}",
        "reboot": f"virsh reboot {name}",
        "forceoff": f"virsh destroy {name}"
    }

    if action not in allowed:
        return jsonify({"error": "Invalid action"}), 400

    output = run_epyc(allowed[action])
    return jsonify({"vm": name, "action": action, "output": output})

@app.route("/vms")
def vm_control():
    return """
<!DOCTYPE html>
<html>
<head>
<title>BBB VM Control</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
    font-family: Arial, sans-serif;
    padding: 30px;
}
h1 {
    color: #7df9ff;
    letter-spacing: .12em;
}
.panel {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(125,249,255,.25);
    border-radius: 20px;
    padding: 24px;
    backdrop-filter: blur(18px);
}
button {
    margin: 8px;
    padding: 12px 18px;
    border: 1px solid rgba(125,249,255,.45);
    border-radius: 12px;
    background: rgba(0,0,0,.35);
    color: #7df9ff;
    font-weight: bold;
}
button:hover {
    background: rgba(125,249,255,.14);
}
pre {
    white-space: pre-wrap;
    background: rgba(0,0,0,.35);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,.12);
}
.vm {
    margin: 18px 0;
    padding: 16px;
    border-radius: 16px;
    background: rgba(255,255,255,.045);
}
</style>
</head>
<body>
<h1>BBB VM CONTROL</h1>

<div class="panel">
    <button onclick="loadVMs()">Refresh VM List</button>
    <pre id="vmlist">Loading...</pre>
</div>

<div class="panel" style="margin-top:25px;">
    <h2>Quick Controls</h2>

    <div class="vm">
        <h3>Gaming</h3>
        <button onclick="vm('gaming','start')">Start</button>
        <button onclick="vm('gaming','shutdown')">Shutdown</button>
        <button onclick="vm('gaming','reboot')">Reboot</button>
        <button onclick="vm('gaming','forceoff')">Force Off</button>
    </div>

    <div class="vm">
        <h3>Office</h3>
        <button onclick="vm('office','start')">Start</button>
        <button onclick="vm('office','shutdown')">Shutdown</button>
        <button onclick="vm('office','reboot')">Reboot</button>
        <button onclick="vm('office','forceoff')">Force Off</button>
    </div>

    <div class="vm">
        <h3>Media Creation</h3>
        <button onclick="vm('media-creation','start')">Start</button>
        <button onclick="vm('media-creation','shutdown')">Shutdown</button>
        <button onclick="vm('media-creation','reboot')">Reboot</button>
        <button onclick="vm('media-creation','forceoff')">Force Off</button>
    </div>

    <div class="vm">
        <h3>Dev Suite</h3>
        <button onclick="vm('dev-suite','start')">Start</button>
        <button onclick="vm('dev-suite','shutdown')">Shutdown</button>
        <button onclick="vm('dev-suite','reboot')">Reboot</button>
        <button onclick="vm('dev-suite','forceoff')">Force Off</button>
    </div>

    <pre id="result"></pre>
</div>

<script>
async function loadVMs() {
    const r = await fetch('/api/vms');
    const d = await r.json();
    document.getElementById('vmlist').innerText = d.output;
}

async function vm(name, action) {
    const r = await fetch(`/api/vm/${name}/${action}`);
    const d = await r.json();
    document.getElementById('result').innerText = JSON.stringify(d, null, 2);
    loadVMs();
}

loadVMs();
setInterval(loadVMs, 5000);
</script>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
