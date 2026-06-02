# BBB AI Gaming Architecture

## Current Goal

Build a local AI-powered development workstation for BBB game, media, app, and automation work.

## Current Active Layer

Dev Station VM:

- Kubuntu Desktop
- RTX 6000 Blackwell passthrough
- Ollama
- Open WebUI
- ComfyUI
- GitHub development workspace
- Godot / Blender / Krita / VS Code toolchain

## Future Components

Gaming VM:

- Windows gaming station
- AI companion integration later
- BBB avatar response system later

EPYC Host:

- VM orchestration
- RTX 6000 passthrough control
- Permanent VFIO mode

Server #2 Later:

- X9DRi-F
- 512GB RAM
- 12/16 bay storage chassis
- Bulk storage and backup layer
- Future extra GPU pool

## Design Rule

Only build infrastructure that survives future hardware reconfiguration.
