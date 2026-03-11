"""
Configuration Module
====================
This file stores all the settings for our Infographic MCP server in one place.

Why use a separate config file?
    - Keeps settings organized and easy to find
    - Makes it simple to change values without editing the main server code
    - Sensitive data (like API keys) is loaded from environment variables

What are environment variables?
    Environment variables are values stored outside your code, usually in the
    operating system or a .env file. They are used for sensitive data (like
    API keys) so you don't accidentally share them in your code.
"""

import os

SERPER_API_KEY: str = os.environ.get("SERPER_API_KEY", "")

SERPER_SEARCH_URL: str = "https://google.serper.dev/search"

SERPER_IMAGES_URL: str = "https://google.serper.dev/images"

DEFAULT_NUM_RESULTS: int = 10

DEFAULT_IMAGE_SIZE: str = "l"

DEFAULT_ASPECT_RATIO: str = "t"

INFOGRAPHIC_SOURCES: dict[str, str] = {
    "visual capitalist": "visualcapitalist.com",
    "behance": "behance.net",
    "dribbble": "dribbble.com",
    "information is beautiful": "informationisbeautiful.net",
    "cool infographics": "coolinfographics.com",
    "venngage": "venngage.com",
    "canva": "canva.com",
    "statista": "statista.com",
    "pinterest": "pinterest.com",
    "visme": "visme.co",
}

SERVER_NAME: str = "infographic-mcp"

SERVER_HOST: str = "0.0.0.0"

SERVER_PORT: int = 8000
