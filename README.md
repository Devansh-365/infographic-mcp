# Design Inspiration MCP Server

A beginner-friendly Python MCP (Model Context Protocol) server that fetches design inspiration using the Serper API.

## What is This Project?

This project creates a **server** that AI assistants (like Claude) can connect to and use as a tool. When connected, the AI can search the web for design inspiration on your behalf — finding UI designs, color palettes, typography ideas, and more.

### Key Concepts for Beginners

- **MCP (Model Context Protocol)**: A standard way for AI assistants to use external tools. Think of it like a universal plug that lets AIs connect to different services.
- **API (Application Programming Interface)**: A way for programs to talk to each other. Our server talks to the Serper API to get search results.
- **Serper API**: A service that lets you search Google programmatically. Instead of opening a browser, your code sends a request and gets results back as data.
- **SSE (Server-Sent Events)**: The communication method our server uses. It keeps a connection open so the AI can send requests and receive responses in real time.

## Project Structure

```
.
├── server.py          # Main server file — starts the MCP server and defines tools
├── config.py          # Configuration — all settings in one place
├── pyproject.toml     # Python project metadata and dependencies
├── .gitignore         # Files that Git should ignore
└── README.md          # This file — you're reading it!
```

### File Explanations

**`server.py`** — The Heart of the Project
- Creates the MCP server instance
- Defines two tools the AI can use:
  - `get_design_inspiration`: Searches for design-related web pages
  - `search_design_images`: Searches specifically for design images
- Handles errors gracefully so the AI gets helpful messages if something goes wrong

**`config.py`** — Settings Central
- Stores all configuration values (API URL, default result count, server port)
- Loads the API key from environment variables (keeps it secure)
- Uses Python type hints to make the code self-documenting

## Setup Guide

### Step 1: Get a Serper API Key

1. Go to [serper.dev](https://serper.dev) and create a free account
2. After signing in, find your API key on the dashboard
3. Copy the API key — you'll need it in the next step

### Step 2: Set the Environment Variable

Add your Serper API key as an environment secret named `SERPER_API_KEY` in Replit's Secrets tab (the lock icon in the sidebar).

### Step 3: Run the Server

The server starts automatically via the configured workflow, or you can run it manually:

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000` and be accessible via SSE at `/sse`.

### Step 4: Connect an MCP Client

To use this server with an AI assistant, configure the MCP client to connect to:

```
http://<your-server-address>:8000/sse
```

## Available Tools

### `get_design_inspiration`

Searches for design inspiration across the web.

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | What to search for (e.g., "modern dashboard UI") |
| `num_results` | integer | 10 | Number of results (1-20) |

**Example queries:**
- "minimalist website design 2024"
- "mobile app onboarding screen inspiration"
- "color palette for food delivery app"
- "typography trends for tech startups"

### `search_design_images`

Searches specifically for design-related images.

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | What images to search for |
| `num_results` | integer | 10 | Number of results (1-20) |

**Example queries:**
- "flat illustration style examples"
- "dark mode UI screenshots"
- "gradient background designs"

## Python Concepts Used

This project demonstrates several Python concepts:

### 1. Async/Await
```python
async def search_serper(query: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(url, ...)
```
**What it means:** `async` functions can pause while waiting for slow operations (like network requests) without freezing the entire program. `await` is where the pause happens.

### 2. Type Hints
```python
def format_results(raw_results: dict) -> str:
```
**What it means:** `: dict` tells you the parameter should be a dictionary, and `-> str` tells you the function returns a string. These are hints for developers — Python doesn't enforce them.

### 3. Decorators
```python
@mcp.tool()
async def get_design_inspiration(...):
```
**What it means:** The `@mcp.tool()` line registers the function as an MCP tool. It's like putting a label on the function that says "hey MCP, this is a tool you can offer to AI assistants."

### 4. Environment Variables
```python
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")
```
**What it means:** This reads a value from the system's environment. The second argument (`""`) is a default value used if the variable isn't set.

### 5. Context Managers
```python
async with httpx.AsyncClient() as client:
```
**What it means:** `async with` ensures the HTTP client is properly cleaned up after use, even if an error occurs. It's like opening and automatically closing a file.

### 6. Error Handling
```python
try:
    result = await search_serper(query)
except ValueError as e:
    return f"Error: {e}"
```
**What it means:** `try/except` catches errors so your program doesn't crash. Instead, it handles the error gracefully and returns a helpful message.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "SERPER_API_KEY is not set" | Add your API key as an environment secret |
| "API Error: status 401" | Your API key is invalid — check it on serper.dev |
| "API Error: status 429" | You've hit the rate limit — wait a moment and try again |
| "Network Error" | Check your internet connection |

## Learn More

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Serper API Documentation](https://serper.dev/docs)
- [Python httpx Library](https://www.python-httpx.org/)
- [Python asyncio Guide](https://docs.python.org/3/library/asyncio.html)
