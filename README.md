# 🤖 MCP Server

This is the backend **MCP Server** (Modular Cognitive Processor) for routing AI tools like summarization, knowledgebase search, and agent-based responses.

Deployed using **FastAPI** with **Server-Sent Events (SSE)** to support real-time streaming.

---

## 🔧 Features

- 🧠 Modular tool execution via `ClientSession`
- 🔁 Live communication via SSE (`/sse`)
- 🌐 Easily deployable to Render.com or Hugging Face Spaces
- 🤖 Works with frontends like Gradio and ADK Agents

---

## 🚀 Deployment on Render

1. **Clone and push to GitHub**:

    ```bash
    git clone https://github.com/YOUR_USERNAME/mcp-server.git
    cd mcp-server
    git push origin main
    ```

2. **Connect to [Render.com](https://render.com)**:
    - Choose **"New Web Service"**
    - Link your GitHub repo
    - Use the following:

      | Key              | Value                                 |
      |------------------|---------------------------------------|
      | Environment      | Python                                |
      | Build Command    | `pip install -r requirements.txt`     |
      | Start Command    | `uvicorn server:app --host 0.0.0.0 --port 10000` |
      | Instance Type    | Free                                  |

3. **Access endpoint**:  
    Your server will be hosted at:  
    `https://your-app-name.onrender.com/sse`

---

## 📂 Project Structure

```bash
mcp-server/
│
├── server.py           # FastAPI server with SSE endpoint
├── requirements.txt    # Python dependencies
├── Procfile            # Start command for Render
└── README.md           # You're here!
