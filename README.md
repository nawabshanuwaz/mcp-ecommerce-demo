# Local AI E-commerce Concierge (MCP Demo)

A lightweight, zero-cost Model Context Protocol (MCP) server that connects Claude Desktop to a local Python-based e-commerce product database. 

This repository demonstrates how AI agents can securely access and query local data (like inventory or catalogs) using natural language, entirely offline, without needing cloud infrastructure or API keys.

## Prerequisites
- [Claude Desktop](https://claude.ai/download) installed
- Python 3.10+ installed

## 🚀 Setup Instructions

### 1. Download the Script
Clone this repository or download `ecommerce_demo.py` directly to your local machine (e.g., to your `Downloads` folder).

### 2. Install the MCP Library
Open your terminal or command prompt and install the specific, stable version of the Anthropic MCP library that matches this script:
```bash
python -m pip install "mcp<2"
```

### 3. Configure Claude Desktop
1. Open the Claude Desktop app.
2. Go to **Settings** > **Developer** > **Edit config**.
3. Copy the JSON from the `claude_desktop_config.json` file in this repository.
4. Replace the placeholder paths with the *actual* absolute paths on your machine:
   - The path to your `python.exe` (Run `where python` in Command Prompt to find it).
   - The path to where you saved `ecommerce_demo.py`.
5. Save the configuration file.

### 4. Restart and Test
1. Completely quit Claude Desktop (Right-click the Claude icon in your system tray and select **Quit**).
2. Reopen Claude Desktop.
3. Start a new chat. You should see a small plug or wrench icon in the text input box indicating the server is attached.
4. **Test the integration** by asking Claude: 
   *"Can you search the store for some outdoor gear?"* or *"Do you have any computer accessories under $100?"*
