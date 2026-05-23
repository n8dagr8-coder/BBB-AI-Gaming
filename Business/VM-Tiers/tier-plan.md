# BigBrainBrand VM Tier Plan

## Light Tier
Purpose: browser, office, light AI access

Resources:
- 2 vCPU
- 4GB RAM
- 80GB storage
- no GPU

Allowed:
- browser
- office apps
- approved AI shortcuts

Blocked:
- admin rights
- app installs
- Docker
- unrestricted downloads

## Standard Tier
Purpose: dev, business, productivity

Resources:
- 4 vCPU
- 8GB RAM
- 120GB storage
- no GPU by default

Allowed:
- VS Code
- browser
- SSH tools
- approved dev apps

Blocked:
- host access
- privileged Docker
- unrestricted installs

## Premium Tier
Purpose: heavy compute / AI / media

Resources:
- custom allocation
- possible GPU access
- monitored usage

Allowed:
- approved AI/video/dev workloads

Blocked:
- crypto mining
- abuse workloads
- tenant-to-tenant access

## Internal Admin Tier
Purpose: BigBrainBrand operations only

VM:
- admin-vm

Never rent this VM.
