# YouTube MCP Server

A Model Context Protocol (MCP) server that provides tools and prompts for working with (Shaw Talebi's) YouTube videos, including transcript extraction, chapter generation, and blog post creation.

Prepared for [AgentCon 2025 - Dallas](https://globalai.community/chapters/dallas/events/agentcon-2025-dallas/) workshop.

Resources:
- [Slides](https://drive.google.com/file/d/121Kg_AfY9k1hbOm6tSaCOvZKCK0mUvuv/view?usp=sharing)

## Overview

This MCP server enables AI assistants to:
- Extract timestamped transcripts from YouTube videos
- Access a curated library of AI and entrepreneurship videos
- Generate structured video chapters from transcripts  
- Convert video transcripts into engaging blog posts
- Get table of Shaw Talebi's YouTube videos as of June 25, 2025

## How to run this example

1. Clone this repo
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already
```bash
# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install dependencies:
```bash
uv sync
```

3. Test the server in dev mode
```bash
uv run mcp dev main.py
```
4. Add server config to AI app (e.g. Claude Desktop or Cursor).
```JSON
{
  "mcpServers": {
    "YT-MCP": {
      "command": "/Users/shawhin/.local/bin/uv", # replace with global path to your uv installation
      "args": [
        "--directory",
        "/Users/shawhin/Documents/repos/yt-mcp/", # replace with global path to repo
        "run",
        "main.py"
      ]
    }
  }
}
```

## Features

### 🛠️ Tools
- **`fetch_youtube_transcript`**: Extract formatted transcripts with timestamps from YouTube URLs

### 📚 Resources  
- **`yt-library://`**: Access to Shaw Talebi's YouTube channel library focused on AI and entrepreneurship topics

### 📝 Prompts
- **`create_chapters_instructions`**: Detailed guidelines for generating meaningful video chapters
- **`write_blog_instructions`**: Instructions for converting transcripts into professional blog posts

## Project Structure

```
yt-mcp/
├── main.py                    # MCP server implementation
├── prompts/
│   ├── create_chapters.md     # Chapter generation guidelines
│   └── write_blog.md         # Blog writing instructions
├── resources/
│   └── videos.csv            # Video library database
├── yt-mcp-example.ipynb      # Usage examples
├── pyproject.toml            # Project configuration
└── requirements.txt          # Dependencies
```

