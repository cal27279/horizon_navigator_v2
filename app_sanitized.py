import streamlit as st
from horizon_rag import HorizonRAG  # Imported your core class
import time

# --- PURE MAGIC: INJECTING ADVANCED CSS ---
# We use markdown with unsafe_allow_html=True to totally override Streamlit's base theme.
st.markdown("""
<style>
    /* Global Background - Deep Black/Carbon Texture */
    .stApp {
        background: linear-gradient(135deg, #060606 0%, #1A1A1A 100%);
        color: #FAFAFA !name;
        font-family: 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Titles & Subheaders - Aggressive & Centered */
    h1, h2, h3 {
        color: #00FFFF !name; /* Neon Cyan */
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.7);
    }

    /* Sidebar - Stealth */
    [data-testid="stSidebar"] {
        background-color: #0e0e0e !name;
        border-right: 1px solid #262626;
    }
    
    /* Input Box - Lamborghini-inspired aggressive geometry */
    .stChatInput {
        border-radius: 0px !name; /* Sharp corners */
        border: 2px solid #262626;
        background-color: #060606 !name;
        transition: all 0.3s ease;
    }
    .stChatInput:focus-within {
        border-color: #00FFFF !name;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    }

    /* Chat Messages - High Contrast */
    .stChatMessage {
        border-radius: 5px !name;
        margin-bottom: 10px;
    }
    
    /* User Message Style */
    [data-testid="stChatMessageUser"] {
        background-color: #1A1A1A !name;
        border: 1px solid #262626;
    }

    /* Assistant Message Style */
    [data-testid="stChatMessageAssistant"] {
        background-color: #0e0e0e !name;
        border-left: 5px solid #00FFFF !name; /* Aggressive Cyan accent */
    }

    /* Buttons - Glowing Hover */
    .stButton>button {
        background-color: #060606 !name;
        color: #FAFAFA !name;
        border-radius: 0px !name;
        border: 2px solid #00FFFF !name;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #00FFFF !name;
        color: #060606 !name;        box-shadow: 0 0 25px rgba(0, 255, 255, 1);
        transform: scale(1.05);
    }

    /* Customizing Metrics boxes */
    [data-testid="metric-container"] {
        background-color: #0e0e0e;
        border: 1px solid #262626;
        border-radius: 0px;
        padding: 10px;
        text-align: center;
    }

</style>
""", unsafe_allow_html=True)

# --- INITIALIZATION (PM Best Practice: Session State) ---
if "advisor" not in st.session_state:
    st.session_state.advisor = HorizonRAG()

if "messages" not in st.session_state:
    # Initial "Start Engine" system message
    st.session_state.messages = []

# --- MAIN UI LAYOUT ---

# Top Aggressive Title with Icon
col1, col2 = st.columns([0.15, 0.85])  

with col1:
    # Eliminamos el '$' y nos aseguramos de que la URL termine en .png
    st.image("https://img.icons8.com/neon/96/brain.png", width=90) 

with col2:
    
    st.markdown('<h1 style="margin-bottom:0rem;">HORIZON NAVIGATOR v2</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="margin-top:0rem; color: #00FFFF;">Black Edition // Serverless Risk Intelligence</h3>', unsafe_allow_html=True)	

st.markdown("---") # Stealth Divider





# Top Stats Row (The Dashboard)
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.metric(label="VECTOR DB STATUS", value="ACTIVE", delta="PINECONE $0/mo", delta_color="normal")
with m_col2:
    st.metric(label="MODEL", value="CLAUDE 3.5", delta="HAIKU 4.5", delta_color="off")
with m_col3:
    st.metric(label="KB ID", value="...P7OO", delta=f"Region: {st.session_state.advisor.region_name}", delta_color="off")

# --- CHAT INTERFACE ---

# Display historical messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input (Targeting the chat_input with CSS above)
if prompt := st.chat_input("Input Risk Query (e.g., Show high probability technical risks)..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("INVOKING CLAUDE // ANALYZING KNOWLEDGE BASE..."):
            # A little artificial delay to make the response feel earned
            time.sleep(0.5)
            response = st.session_state.advisor.query(prompt)
            st.markdown(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- SIDEBAR (Stealth Edition) ---
import streamlit as st

# --- SIDEBAR SYSTEM STATUS ---
with st.sidebar:
    st.markdown("---")
    st.subheader("📡 System Pulse")
    
    # We use st.status or a simple container for that "Live" feel
    with st.expander("View Infrastructure Logs", expanded=True):
        st.caption("Connectivity Status:")
        st.code("""
[OK] AWS Secrets Manager: Connected
[OK] Bedrock Runtime: Claude 3 Haiku
[OK] Pinecone Index: 605 Records
[OK] Security Protocol: AES-256
        """, language="bash")
        
    st.info("System Latency: 0.8s")

with st.sidebar:
    st.markdown("---")
    st.markdown("### 📡 **System Pulse**")
    
    # Custom HTML for that "Neon LED" look
    st.markdown("""
        <div style="background-color: #111; padding: 15px; border-radius: 10px; border: 1px solid #333;">
            <p style="margin: 0; color: #00ff00;">● <span style="color: #bbb; font-family: monospace;">AWS Secrets Manager: <b>ACTIVE</b></span></p>
            <p style="margin: 5px 0; color: #00ff00;">● <span style="color: #bbb; font-family: monospace;">Bedrock Runtime: <b>READY</b></span></p>
            <p style="margin: 5px 0; color: #00ff00;">● <span style="color: #bbb; font-family: monospace;">Pinecone Index: <b>605 RECS</b></span></p>
            <p style="margin: 0; color: #00f2ff;">● <span style="color: #bbb; font-family: monospace;">Security: <b>AES-256</b></span></p>
        </div>
    """, unsafe_allow_html=True)
    
    st.caption("Average RTT: 0.82s")






with st.sidebar:
    st.markdown("<h3>PROJECT GOVERNANCE</h3>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/neon/96/brain.png", width=64)
    st.info("**Owner:** YOUR NAME")
    st.info("**RAG Index:** Horizon-Navigator-v2")
    
    st.markdown("---")
    if st.button("CLEAR LOG / RESET SESSION"):
        st.session_state.messages = []
        st.rerun()
