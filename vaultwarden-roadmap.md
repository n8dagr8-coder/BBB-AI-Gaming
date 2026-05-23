# BBB Vaultwarden Roadmap

## Goal
Centralize passwords, SSH keys, API keys, and infrastructure credentials.

---

## Purpose
admin-vm becomes the trusted credential zone.

Only admin-vm should contain:
- password manager
- SSH keys
- infrastructure credentials
- billing/admin accounts
- API secrets

---

## Planned Stack

Primary:
- Vaultwarden

Access:
- Browser
- Mobile app
- Admin VM only

---

## Stored Items

### Infrastructure
- Portainer
- Grafana
- Prometheus
- n8n
- Open WebUI
- Proxmox/libvirt
- Router/firewall

### Business
- Domains
- Hosting
- Cloudflare
- WordPress
- Email accounts

### Development
- GitHub
- API keys
- AI services
- deployment tokens

---

## Security Rules

- Never store plaintext passwords in scripts
- Never store secrets in Git repos
- Never share admin vault
- Use strong generated passwords
- Backup vault regularly

---

## Future Goals

- Multi-device sync
- Family/business shared vaults
- Emergency recovery vault
- Hardware security integration later

