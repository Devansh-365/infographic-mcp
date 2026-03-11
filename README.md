# Design Inspiration MCP Server

A Python MCP server that lets AI assistants search for design inspiration using the [Serper API](https://serper.dev). Find UI/UX ideas, images, color palettes, and creative references — all from within your AI workflow.

## Features

- **`get_design_inspiration`** — Search for design-related web pages, articles, and portfolios
- **`search_design_images`** — Search specifically for design images and visual references
- SSE transport for real-time communication with MCP clients
- Graceful error handling with clear, actionable messages

## Quick Start

### 1. Install dependencies

```bash
pip install mcp httpx
```

### 2. Set your API key

Get a free key at [serper.dev](https://serper.dev), then set it as an environment variable:

```bash
export SERPER_API_KEY="your-api-key-here"
```

### 3. Run the server

```bash
python server.py
```

The server starts on `http://0.0.0.0:8000` with the SSE endpoint at `/sse`.

### 4. Connect your MCP client

Point your MCP client (e.g. Claude Desktop) to:

```
http://<your-server-address>:8000/sse
```

## Tools

### `get_design_inspiration`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | What to search for |
| `num_results` | integer | 10 | Number of results (1–20) |

Example queries: `"modern dashboard UI"`, `"color palette for food app"`, `"minimalist logo ideas"`

### `search_design_images`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | What images to search for |
| `num_results` | integer | 10 | Number of results (1–20) |

Example queries: `"flat illustration style"`, `"dark mode UI screenshots"`, `"gradient backgrounds"`

## Project Structure

```
server.py        # MCP server — tool definitions and API integration
config.py        # Configuration — API keys, server settings
pyproject.toml   # Project metadata and dependencies
```

## Configuration

All settings live in `config.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `SERPER_API_KEY` | from env | Your Serper API key |
| `SERPER_API_URL` | `https://google.serper.dev/search` | Serper search endpoint |
| `DEFAULT_NUM_RESULTS` | `10` | Default number of results per query |
| `SERVER_HOST` | `0.0.0.0` | Server bind address |
| `SERVER_PORT` | `8000` | Server port |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `SERPER_API_KEY is not set` | Set the environment variable or add it to `.env` |
| `API Error: status 401` | Invalid API key — verify it at [serper.dev](https://serper.dev) |
| `API Error: status 429` | Rate limit hit — wait and retry |
| `Network Error` | Check your internet connection |

## Resources

- [MCP Protocol Docs](https://modelcontextprotocol.io/)
- [Serper API Docs](https://serper.dev/docs)
- [httpx Docs](https://www.python-httpx.org/)
