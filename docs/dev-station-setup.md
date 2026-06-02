# BBB Dev Station Setup

Dev Station is the Kubuntu AI, game, media, and application development VM running on the EPYC Brain Server.

## Access

Dev Station hostname: BBBDev

Private Tailscale SSH:

    ssh bbbdev@100.67.240.116

LAN SSH fallback:

    ssh bbbdev@192.168.0.107

## Private Web Services

Open WebUI:

    http://100.67.240.116:3000

ComfyUI:

    http://100.67.240.116:8188

## Core Stack

- Ollama for local LLM backend
- Open WebUI for AI chat
- ComfyUI for AI image/media workflows
- RTX 6000 Blackwell passthrough
- Tailscale-only private access
- 1TB /workspace disk

## Status Command

Run:

    ai-status

## Current Rule

Keep the public-facing stack private for now. Do not expose Ollama, ComfyUI, Open WebUI, SSH, Docker, or VM controls directly to the public internet.
