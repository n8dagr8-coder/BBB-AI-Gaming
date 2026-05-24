import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

EPYC_HOST = "192.168.0.101"

SSH = [
    "ssh",
    "-i", "/home/nate/.ssh/admin_to_epyc",
    "-o", "BatchMode=yes",
    f"nate@{EPYC_HOST}"
]

def run_epyc(cmd):
    try:
        out = subprocess.run(
            SSH + cmd,
            capture_output=True,
            text=True,
            timeout=20
        )

        return out.stdout.strip() or out.stderr.strip()

    except Exception as e:
        return str(e)

def parse_vms(raw):

    vms = []

    for line in raw.splitlines():

        line = line.strip()

        if (
            not line or
            line.startswith("Id") or
            line.startswith("-")
        ):
            continue

        parts = line.split()

        if len(parts) >= 3:

            name = parts[1]
            state = " ".join(parts[2:])

            vms.append({
                "name": name,
                "state": state
            })

    return vms

@app.route("/")
def home():

    return """
<!DOCTYPE html>
<html>
<head>

<title>BBB VM CONTROL</title>

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<style>

body{
margin:0;
padding:24px;
font-family:Arial;
background:
radial-gradient(circle at top,#0f172a,#020617);
color:#e6f3f7;
}

h1{
color:#7df9ff;
letter-spacing:.15em;
margin-bottom:20px;
}

.topbar{
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:20px;
}

.refresh{
opacity:.7;
font-size:14px;
}

.grid{
display:grid;
grid-template-columns:
repeat(auto-fit,minmax(280px,1fr));
gap:18px;
}

.card{
background:rgba(255,255,255,.05);
border:1px solid rgba(125,249,255,.25);
border-radius:22px;
padding:20px;
backdrop-filter:blur(16px);
transition:.25s;
}

.card:hover{
transform:translateY(-4px);
border-color:#7df9ff;
box-shadow:0 0 25px rgba(125,249,255,.18);
}

.name{
font-size:24px;
font-weight:bold;
margin-bottom:8px;
}

.state{
margin-bottom:14px;
opacity:.82;
}

.running{
color:#34d399;
}

.off{
color:#f87171;
}

.controls{
display:flex;
flex-wrap:wrap;
gap:8px;
}

button{
padding:10px 14px;
border-radius:12px;
border:1px solid #7df9ff;
background:transparent;
color:#7df9ff;
font-weight:bold;
cursor:pointer;
transition:.2s;
}

button:hover{
background:rgba(125,249,255,.12);
}

button.danger{
border-color:#f87171;
color:#f87171;
}

button.danger:hover{
background:rgba(248,113,113,.14);
}

pre{
margin-top:20px;
padding:14px;
border-radius:16px;
background:rgba(0,0,0,.35);
overflow:auto;
white-space:pre-wrap;
}

</style>
</head>

<body>

<div class="topbar">

<h1>BBB VM CONTROL</h1>

<div class="refresh" id="refresh">
Updating...
</div>

</div>

<div class="grid" id="grid">

Loading...

</div>

<pre id="result">
Ready.
</pre>

<script>

async function loadVMs(){

    const r =
    await fetch('/api/vms');

    const d =
    await r.json();

    let html = '';

    d.vms.forEach(vm => {

        const running =
        vm.state.includes('running');

        html += `

        <div class="card">

            <div class="name">
            ${vm.name}
            </div>

            <div class="state ${running ? 'running':'off'}">
            ${vm.state}
            </div>

            <div class="controls">

                <button
                onclick="act('${vm.name}','start')">
                Start
                </button>

                <button
                onclick="act('${vm.name}','shutdown')">
                Shutdown
                </button>

                <button
                class="danger"
                onclick="forceOff('${vm.name}')">
                Force Off
                </button>

            </div>

        </div>
        `;
    });

    document.getElementById('grid').innerHTML =
    html || 'No VMs Found';

    document.getElementById('refresh').innerText =
    'Updated: ' +
    new Date().toLocaleTimeString();
}

async function act(name, action){

    const r =
    await fetch(
        `/api/vm/${name}/${action}`
    );

    const d =
    await r.json();

    document.getElementById('result').innerText =
    d.output;

    setTimeout(loadVMs,800);
}

function forceOff(name){

    if(
        confirm(
            'Force power off ' +
            name +
            '?'
        )
    ){
        act(name,'destroy');
    }
}

loadVMs();

setInterval(loadVMs,5000);

</script>
</body>
</html>
"""

@app.route("/api/vms")
def api_vms():

    raw = run_epyc(
        ["virsh", "list", "--all"]
    )

    return jsonify({
        "vms": parse_vms(raw)
    })

@app.route("/api/vm/<name>/<action>")
def api_vm_action(name, action):

    allowed = [
        "start",
        "shutdown",
        "destroy"
    ]

    if action not in allowed:

        return jsonify({
            "output": "Invalid action"
        }), 400

    out = run_epyc(
        ["virsh", action, name]
    )

    return jsonify({
        "output": out
    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8088
    )
