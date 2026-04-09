from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.tools import DuckDuckGoSearchRun, ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain_core.messages import HumanMessage
import streamlit as st
import uuid

# --- Tools ---
wiki_wrapper = WikipediaAPIWrapper()
arxiv_wrapper = ArxivAPIWrapper()
web_wrapper = DuckDuckGoSearchAPIWrapper()

web_search = DuckDuckGoSearchRun(api_wrapper=web_wrapper)
research_search = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wikipedia_search = WikipediaQueryRun(api_wrapper=wiki_wrapper)

tools = [web_search, research_search, wikipedia_search]

# --- Shared MemorySaver (lives for the whole Streamlit session) ---
# st.cache_resource ensures it's created once and reused across reruns
@st.cache_resource
def get_memory():
    return MemorySaver()

memory = get_memory()


def create_agent_with_tools(model: str, api_key: str):
    llm = ChatGroq(model=model, api_key=api_key)
    # Pass the shared checkpointer here — this is what enables chat history
    agent = create_react_agent(llm, tools, checkpointer=memory)
    return agent


# --- SESSION STATE INIT ---
if "chats" not in st.session_state:
    # Each chat = {"title": str, "thread_id": str}
    st.session_state.chats = []

if "active_thread_id" not in st.session_state:
    tid = str(uuid.uuid4())
    st.session_state.active_thread_id = tid
    st.session_state.chats.append({"title": "Chat 1", "thread_id": tid})

if "agent" not in st.session_state:
    st.session_state.agent = None


# --- SIDEBAR ---
with st.sidebar:
    st.header("AgentChatbot", divider=True)

    chat_api_key = st.text_input(
        label="Enter Groq API key",
        type="password",
        placeholder="API Key",
    )

    chat_model = st.selectbox(
        label="Select Chat Model",
        options=[
            "qwen/qwen3-32b",
            "compound-beta",
            "llama-3.1-8b-instant",
            "llama3-70b-8192",
        ],
    )

    if chat_api_key:
        # Recreate agent only when key/model changes
        agent_key = f"{chat_api_key}_{chat_model}"
        if st.session_state.get("_agent_key") != agent_key:
            st.session_state.agent = create_agent_with_tools(chat_model, chat_api_key)
            st.session_state._agent_key = agent_key

    if st.button("➕ New Chat", use_container_width=True):
        tid = str(uuid.uuid4())
        title = f"Chat {len(st.session_state.chats) + 1}"
        st.session_state.chats.append({"title": title, "thread_id": tid})
        st.session_state.active_thread_id = tid
        st.rerun()

    st.subheader("Previous Chats")
    for i, chat in enumerate(reversed(st.session_state.chats)):
        real_idx = len(st.session_state.chats) - 1 - i
        col1, col2 = st.columns([3, 1])
        with col1:
            is_active = chat["thread_id"] == st.session_state.active_thread_id
            label = f"{'▶ ' if is_active else ''}{chat['title']}"
            if st.button(label, key=f"open_{real_idx}", use_container_width=True):
                st.session_state.active_thread_id = chat["thread_id"]
                st.rerun()
        with col2:
            if st.button("🗑️", key=f"del_{real_idx}"):
                st.session_state.chats.pop(real_idx)
                # If we deleted the active chat, switch to latest
                if st.session_state.active_thread_id == chat["thread_id"]:
                    if st.session_state.chats:
                        st.session_state.active_thread_id = st.session_state.chats[-1]["thread_id"]
                    else:
                        tid = str(uuid.uuid4())
                        st.session_state.chats.append({"title": "Chat 1", "thread_id": tid})
                        st.session_state.active_thread_id = tid
                st.rerun()


# --- LOAD HISTORY FOR ACTIVE THREAD from MemorySaver ---
def get_thread_messages(thread_id: str):
    """Reads the saved checkpoint for this thread and extracts display messages."""
    if st.session_state.agent is None:
        return []
    try:
        config = {"configurable": {"thread_id": thread_id}}
        state = st.session_state.agent.get_state(config)
        messages = state.values.get("messages", [])
        display = []
        for m in messages:
            if m.type == "human":
                display.append(("user", m.content))
            elif m.type == "ai" and m.content:  # skip empty AI tool-call messages
                display.append(("assistant", m.content))
        return display
    except Exception:
        return []


# --- DISPLAY EXISTING MESSAGES ---
thread_messages = get_thread_messages(st.session_state.active_thread_id)
for role, content in thread_messages:
    st.chat_message(role).write(content)


# --- CHAT INPUT ---
user_input = st.chat_input("Type your message...")

if user_input:
    if not st.session_state.agent:
        st.warning("Please enter your Groq API key in the sidebar.")
    else:
        # Show user message immediately
        st.chat_message("user").write(user_input)

        config = {"configurable": {"thread_id": st.session_state.active_thread_id}}

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.agent.invoke(
                    {"messages": [HumanMessage(content=user_input)]},
                    config=config,  # ← thread_id makes MemorySaver restore history
                )
                # Last message in state is the final AI response
                answer = response["messages"][-1].content
            st.write(answer)

        # Auto-title the chat after first message
        active_chat = next(
            (c for c in st.session_state.chats if c["thread_id"] == st.session_state.active_thread_id),
            None,
        )
        if active_chat and active_chat["title"].startswith("Chat "):
            active_chat["title"] = user_input[:30] + ("…" if len(user_input) > 30 else "")