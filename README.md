# MCP-Gemini

A project showcasing how to integrate **MCP (Model Context Protocol)** with **Gemini** (Google's LLM) to run multi-step agentic workflows for real-world applications like searching and recommending accommodations (e.g., via Airbnb).

*Example Output: Accommodation recommendations for a 5-night stay in Barcelona.*
![image](https://github.com/user-attachments/assets/411b47ac-d177-40da-8404-1208c640633e)

---

## 🚀 Features

- 🔌 Integration of Gemini with **MCP (Model Context Protocol)**
- 🧠 Autonomous multi-step decision making
- 🌍 Real-time travel recommendations (e.g., Airbnb)
- 📎 Dynamic tool calling and chaining
- ⏱️ Fast execution with informative logs

---

## 🧩 What is MCP?

**Model Context Protocol (MCP)** allows you to manage multi-agent and multi-step workflows across various tools. It enables agents to retain context and perform reasoning across multiple steps, making it suitable for complex LLM-driven applications.

---

## 🧠 LLM Used

- **Gemini** (via Vertex AI or compatible runtime)
- Agent handles steps like:
  - Finding tools
  - Initializing sessions
  - Executing toolchains
  - Fetching listings
  - Presenting results

---

## 🛠️ Tools Used

- `airbnb_search`: Queries listings for given dates/location
- `airbnb_listing_details`: Fetches detailed pricing info
- `mcp_use`: MCP agent runtime handler

---

## 📷 Output Example

The following screenshot displays the terminal output when the script is executed with the prompt:

> _"Find me a nice place to stay in Barcelona for 2 adults from August 2nd to August 8th"_

The agent:
1. Identifies and chains relevant tools
2. Executes searches with context
3. Returns top 3 results with estimated pricing and direct links

📸 **Screenshot from terminal output:**  
![image](https://github.com/user-attachments/assets/73bad855-0c22-4af0-a3f7-55c826e37bac)

---

## 📂 File Structure

```bash
.
├── new.py                    # Main entry script
├── README.md                 # You're here!
└── requirements.txt          # Dependencies

```

# MCP-Gemini

## 🛠️ Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/MayurPimpude/MCP-Gemini.git
cd MCP-Gemini

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3.Configure Environment Variables
Make sure to set any required environment variables such as:
Your Vertex/Gemini keys

### 4.Run the Script
```bash
python new.py
```

## 🙌 Acknowledgements
Model Context Protocol (MCP)
Gemini / Vertex AI
Airbnb (for test scraping/search)

## ✍️ Author
### Mayur Pimpude
