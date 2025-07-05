import asyncio
import os
from mcp_use import MCPAgent, MCPClient
import google.generativeai as genai
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

async def run_airbnb_example():


    # Create MCPClient with Airbnb configuration
    # Create configuration dictionary
    config = {
  "mcpServers": {
    "airbnb": {
      "command": "npx",
      "args": [
        "-y",
        "@openbnb/mcp-server-airbnb",
        "--ignore-robots-txt"
      ]
    }
  }
}

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM - you can choose between different models
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                             temperature=0.3)

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        # Run a query to search for accommodations
        result = await agent.run(
            "Find me a nice place to stay in Barcelona for 2 adults "
            "for a week from 2nd to 8th August."
            "Show me the top 3 options along with price.",
            max_steps=30,
        )
        print(f"\nResult: {result}")
    finally:
        # Ensure we clean up resources properly
        if client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_airbnb_example())