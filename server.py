import os
from mcp.server.fastmcp import FastMCP
from openai import OpenAI

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")

openai_client = OpenAI(api_key=openai_api_key)

mcp = FastMCP()

@mcp.tool()
def search_knowledgebase(query: str) -> str:
    """Pretend to search an internal knowledge base."""
    return f"Result found for '{query}' in knowledge base."

@mcp.tool()
def summarize(text: str) -> str:
    """Summarize a given block of text."""
    if len(text) > 1000:
        text = text[:1000] + "..."  # Truncate to avoid too large inputs
    # Simple naive summary example
    return f"Summary: {text[:50]}..."

@mcp.tool()
def ai_agent(question: str) -> str:
    """Use OpenAI GPT model to answer the question."""
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an intelligent assistant."},
                {"role": "user", "content": question},
            ],
            max_tokens=200,
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"Error in AI agent: {e}"

@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the MCP Agent System."

@mcp.tool()
def add(a: int, b: int) -> int:
    """Example utility function: add two numbers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Example utility function: multiply two numbers."""
    return a * b

if __name__ == "__main__":
    print("Starting MCP server with AI agent and tools...")
    mcp.run(transport="sse", host="0.0.0.0", port=8000)

