# GPT img for ComfyUI

ComfyUI custom nodes for GPT image generation through OpenAI API keys or
Codex/ChatGPT OAuth.

This node pack does not run a web UI, Express API, gallery, sessions, or local
database. It only exposes ComfyUI nodes.

## Nodes

- `GPT img OAuth Generate`
- `GPT img OAuth Edit`
- `GPT img API Generate`
- `GPT img API Edit`

All nodes return:

- `image`
- `revised_prompt`

## Install

Clone this repository into `ComfyUI/custom_nodes`:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/hub2vu/Compyui-GPT-img-node.git GPT-img
```

Restart ComfyUI after installing.

## API Nodes

Use `GPT img API Generate` or `GPT img API Edit`.

Enter an OpenAI API key in the node's `api_key` field, or leave it empty and set
`OPENAI_API_KEY` in your environment.

## OAuth Nodes

Use `GPT img OAuth Generate` or `GPT img OAuth Edit`.

Requirements:

- Node.js with `npx`
- Codex/ChatGPT OAuth login

Login once if needed:

```powershell
npx @openai/codex login
```

The OAuth nodes can auto-start the OAuth proxy on port `10531`. Logs are written
to:

```text
custom_nodes/GPT-img/logs/openai-oauth.log
```

## ComfyUI Manager / Registry

This repository includes `pyproject.toml` metadata for the Comfy Registry.
Publishing to the Registry makes the node searchable/installable from
ComfyUI-Manager.
