# AgenticChatbot

An intelligent conversational AI chatbot powered by **LangChain**, **LanGraph**, and **Groq API**, built with a **Streamlit** user interface. The chatbot has access to multiple tools for real-time information retrieval and can maintain persistent conversation history across multiple chat sessions.

## 🎯 Overview

AgenticChatbot is a multi-agent conversational system that leverages the power of large language models (LLMs) with tool integration to provide intelligent, context-aware responses. It uses the ReAct (Reasoning + Acting) pattern to autonomously decide when and how to use available tools to answer user queries.

The application is designed for easy deployment and can be configured to work with different Groq LLM models. It provides a user-friendly interface for managing multiple chat sessions with persistent memory across conversations.

## ✨ Features

- **Multi-Tool Integration**: Access to three specialized tools for comprehensive information gathering
  - 🔍 **Web Search**: Real-time web search using DuckDuckGo
  - 📚 **Academic Research**: Access to research papers via Arxiv
  - 🌍 **Wikipedia**: Encyclopedia knowledge and general information
  
- **Intelligent Agent System**: Uses ReAct pattern for reasoning and tool usage
  - Autonomous decision-making on when to use tools
  - Context-aware responses based on user queries
  - Intelligent fallback to general knowledge when tools aren't needed

- **Multi-Model Support**: Choose from multiple Groq LLM models
  - Qwen 3 (32B parameters)
  - Compound Beta
  - Llama 3.1 (8B Instant)
  - Llama 3 (70B, 8192 token context)

- **Persistent Chat History**: 
  - Multiple concurrent chat sessions
  - Conversation memory maintained via LanGraph checkpointing
  - Session switching without losing context
  - Delete individual chat sessions

- **User-Friendly Interface**:
  - Clean Streamlit web interface
  - Sidebar for API key and model configuration
  - Real-time chat message display
  - Visual indicators for active chats
  - Loading indicators for agent processing

- **Session Management**:
  - Create and manage multiple independent chat sessions
  - Thread-based conversation tracking
  - Automatic chat numbering
  - Quick switching between previous conversations

## 🏗️ Architecture

### Components

```
AgenticChatbot
├── Main Application (main.py)
│   ├── LLM Configuration (Groq API)
│   ├── Tool Integration Layer
│   ├── Agent Factory
│   ├── Session State Management
│   ├── Streamlit UI Components
│   └── Memory/Checkpoint Manager
└── Dependencies
    ├── LangChain Ecosystem
    ├── LanGraph (Agent Framework)
    └── Streamlit (Web Interface)
```

### Key Flow

1. **User Input**: User enters a query through the Streamlit chat interface
2. **Agent Processing**: ReAct agent analyzes the query
3. **Tool Invocation**: Agent decides whether to use available tools
4. **Information Retrieval**: Tools fetch real-time data if needed
5. **Response Generation**: LLM generates response with retrieved information
6. **History Storage**: Conversation saved to memory via checkpointer
7. **Display**: Response shown in chat interface

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Groq API key ([Get one free here](https://groq.com))
- pip or uv package manager

### Installation

#### Option 1: Using pip

```bash
# Clone the repository
git clone https://github.com/SambhavSurthi/AgenticChatbot.git
cd AgenticChatbot

# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Using uv (faster)

```bash
# Clone the repository
git clone https://github.com/SambhavSurthi/AgenticChatbot.git
cd AgenticChatbot

# Install with uv
uv sync
```

### Configuration

#### Step 1: Obtain Groq API Key

1. Visit [Groq Console](https://groq.com)
2. Sign up or log in to your account
3. Generate a new API key
4. Copy your API key

#### Step 2: Run the Application

```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

#### Step 3: Configure API Key

1. In the sidebar, paste your Groq API key in the "Enter Groq API key" field
2. Select your preferred chat model from the dropdown
3. Start chatting!

## 📖 Usage Guide

### Basic Usage

1. **Start a New Chat**: Click the "➕ New Chat" button to create a new conversation thread
2. **Select a Model**: Choose your preferred LLM from the dropdown menu
3. **Enter Your Query**: Type your question or message in the chat input field
4. **Review Response**: The agent will process your query and respond with relevant information

### Supported Models

| Model | Parameters | Best For | Context Window |
|-------|-----------|----------|-----------------|
| `qwen/qwen3-32b` | 32B | General purpose | Not specified |
| `compound-beta` | Hybrid | Multi-task | Not specified |
| `llama-3.1-8b-instant` | 8B | Fast responses | Standard |
| `llama3-70b-8192` | 70B | Complex reasoning | 8,192 tokens |

### Chat Management

- **Previous Chats**: All past conversations are listed in the sidebar
- **Switch Chats**: Click on any previous chat title to switch to that conversation
- **Delete Chats**: Click the 🗑️ button next to a chat to remove it
- **Active Chat**: The current active chat is marked with a ▶ indicator

### Example Queries

```
- "What are the latest developments in quantum computing?"
- "Summarize the research on machine learning optimization"
- "Tell me about the Great Wall of China"
- "How does photosynthesis work?"
- "What's the current state of AI in 2026?"
```

## 📁 Project Structure

```
AgenticChatbot/
├── main.py              # Main Streamlit application
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Python package dependencies
├── README.md            # This file
├── .gitignore           # Git ignore patterns
├── .python-version      # Python version specification
└── uv.lock              # UV package manager lock file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Core application logic, Streamlit UI, agent configuration, and session management |
| `pyproject.toml` | Project metadata, dependencies, and build configuration (PEP 517/518) |
| `requirements.txt` | Simple pip-compatible dependency list |
| `.python-version` | Specifies the Python version for the project (used by pyenv) |
| `uv.lock` | Lock file for reproducible builds with uv package manager |

## 📦 Dependencies

### Core Framework
- **langchain** (>=1.2.15): LLM framework for building AI applications
- **langchain-core** (>=1.2.28): Core abstractions for LangChain
- **langchain-community** (>=0.4.1): Community integrations and tools
- **langgraph**: Agent runtime for ReAct pattern implementation

### LLM Providers
- **langchain-groq** (>=1.1.2): Groq API integration
- **langchain-google-genai** (>=4.2.1): Google GenAI models support
- **langchain-huggingface** (>=1.2.1): Hugging Face models support

### Tools & Utilities
- **wikipedia** (>=1.4.0): Wikipedia API wrapper for knowledge retrieval
- **arxiv** (>=2.4.1): Arxiv API wrapper for research paper access
- **ddgs** (>=9.13.0): DuckDuckGo search API wrapper

### Vector Storage
- **faiss-cpu** (>=1.13.2): Efficient similarity search and clustering

### UI Framework
- **streamlit** (>=1.56.0): Web app framework for rapid UI development

## ⚙️ Advanced Configuration

### Using Different Models

To use a different Groq model, modify the model selection in the sidebar or update the options list in `main.py`:

```python
chat_model = st.selectbox(
    label="Select Chat Model",
    options=[
        "qwen/qwen3-32b",
        "compound-beta",
        "llama-3.1-8b-instant",
        "llama3-70b-8192",
        "mixtral-8x7b-32768",  # Add more models as needed
    ],
)
```

### Adding Custom Tools

To add new tools, extend the tools list in `main.py`:

```python
# Example: Add a custom calculator tool
from langchain_community.tools import Tool

def calculator(expression: str) -> str:
    """Evaluate mathematical expressions"""
    return str(eval(expression))

custom_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for evaluating mathematical expressions"
)

tools = [web_search, research_search, wikipedia_search, custom_tool]
```

### Memory Configuration

The application uses `MemorySaver` for conversation persistence. To use a different checkpointer:

```python
# Instead of MemorySaver()
from langgraph.checkpoint.mongodb import MongoDBSaver

memory = MongoDBSaver(conn_string="mongodb://...")
```

### Environment Variables

For production deployment, store sensitive data in environment variables:

```bash
export GROQ_API_KEY="your-api-key-here"
export GROQ_MODEL="llama3-70b-8192"
```

Then modify `main.py` to read from environment:

```python
import os
groq_api_key = os.getenv("GROQ_API_KEY")
```

## 🔐 Security Considerations

- **API Key Protection**: The sidebar uses `type="password"` to hide API key input
- **No Key Storage**: API keys are stored only in Streamlit session state, not persisted to disk
- **Session Isolation**: Each browser session maintains independent conversation threads
- **Model Safety**: Groq models include built-in safety mechanisms

### Best Practices

1. Never commit API keys to version control
2. Use environment variables in production
3. Rotate API keys periodically
4. Monitor API usage through Groq dashboard
5. Use `.gitignore` to exclude sensitive files

## 🚀 Deployment

### Local Deployment

```bash
streamlit run main.py
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
```

Build and run:

```bash
docker build -t agenticchatbot .
docker run -p 8501:8501 agenticchatbot
```

### Cloud Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Create new app and connect to your repository
4. Set environment variables in app settings
5. Deploy

## 🛠️ Development

### Code Structure

The main application follows this pattern:

```python
# 1. Tool Configuration
web_search = DuckDuckGoSearchRun(...)
research_search = ArxivQueryRun(...)
wikipedia_search = WikipediaQueryRun(...)
tools = [web_search, research_search, wikipedia_search]

# 2. Memory/Session Management
@st.cache_resource
def get_memory():
    return MemorySaver()

# 3. Agent Factory
def create_agent_with_tools(model: str, api_key: str):
    llm = ChatGroq(model=model, api_key=api_key)
    agent = create_react_agent(llm, tools, checkpointer=memory)
    return agent

# 4. Streamlit UI Components
# Sidebar for configuration
# Chat history display
# Chat input and processing
```

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Resources

- [LangChain Documentation](https://python.langchain.com)
- [LanGraph Documentation](https://langchain-ai.github.io/langgraph)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Groq API Documentation](https://groq.com/docs)
- [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629)

## 🐛 Troubleshooting

### API Key Errors

**Issue**: "Invalid API key"
- **Solution**: Ensure your Groq API key is correct and has active credits

### Model Not Found

**Issue**: "Model not available"
- **Solution**: Check available models in your Groq account; some may require higher tier access

### Memory Issues

**Issue**: Chat history not persisting
- **Solution**: Ensure `MemorySaver` is properly initialized; check browser cookies/cache

### Tool Failures

**Issue**: Web/Arxiv/Wikipedia searches not working
- **Solution**: Check internet connection; verify API wrapper configurations

### Streamlit Port Issues

**Issue**: "Port 8501 already in use"
- **Solution**: Use `streamlit run main.py --server.port 8502`

## 📊 Performance Metrics

- **Response Time**: 2-10 seconds (depending on model and tool usage)
- **Tool Invocation**: < 1 second overhead per tool call
- **Memory Usage**: ~500MB-1GB depending on model
- **Concurrent Users**: Limited by Groq API rate limits

## 🗺️ Future Enhancements

- [ ] User authentication and chat sharing
- [ ] PDF document support and analysis
- [ ] Custom tool creation UI
- [ ] Response streaming for faster feedback
- [ ] Chat export (PDF, JSON, Markdown)
- [ ] Model comparison mode
- [ ] Cost tracking and usage analytics
- [ ] Advanced prompt engineering interface
- [ ] Multi-language support
- [ ] Voice input/output capabilities

## 📄 License

This project is open source and available under the MIT License. See LICENSE file for details.

## 👨‍💻 Author

**Sambhav Surthi** - [GitHub Profile](https://github.com/SambhavSurthi)

## 🤝 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review existing [GitHub Issues](https://github.com/SambhavSurthi/AgenticChatbot/issues)
3. Create a new issue with detailed description
4. Include error logs and steps to reproduce

## 📞 Contact

- GitHub: [@SambhavSurthi](https://github.com/SambhavSurthi)
- Issues: [GitHub Issues](https://github.com/SambhavSurthi/AgenticChatbot/issues)

---

**Last Updated**: April 2026 | **Status**: Active Development | **Python Version**: 3.10+
