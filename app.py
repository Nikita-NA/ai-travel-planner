import streamlit as st
from prompt_system import TravelPlannerPromptSystem
import random

# --- CONFIG & STYLES ---
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# --- INSPIRATIONAL QUOTES ---
quotes = [
    '"Travel is the only thing you buy that makes you richer." – Anonymous',
    '"The world is a book and those who do not travel read only one page." – Saint Augustine',
    '"Life is short and the world is wide." – Simon Raven',
    '"To travel is to live." – Hans Christian Andersen',
    '"Adventure may hurt you but monotony will kill you." – Anonymous'
]

# Custom CSS for modern UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;900&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    body {
        background: linear-gradient(135deg, #f6f9fc 0%, #eef2f7 100%);
    }
    
    .main {
        background: transparent;
        padding: 0;
    }
    
    .hero-section {
        position: relative;
        background: #357abd;
        padding: 4rem 2rem 3rem 2rem;
        border-radius: 0 0 2rem 2rem;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        text-align: center;
        min-height: 260px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
        opacity: 0.22;
        z-index: 0;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(135deg, #4a90e2cc 0%, #357abdcc 100%);
        opacity: 0.85;
        z-index: 1;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 1rem;
        color: #fff;
        text-shadow: 0 4px 24px rgba(0,0,0,0.18), 0 1px 0 #357abd;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.97;
        margin-bottom: 2rem;
        color: #f7fafc;
        text-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    
    .destination-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border-radius: 1rem;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s;
        border: 1px solid rgba(255, 255, 255, 0.2);
        cursor: pointer;
        text-align: center;
    }
    
    .destination-card:hover {
        transform: translateY(-5px) scale(1.03);
        box-shadow: 0 8px 32px rgba(74, 144, 226, 0.15);
    }
    
    .destination-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .chat-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 1rem;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .chat-message {
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    
    .chat-message.user {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
    }
    
    .chat-message.assistant {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border: 1px solid #e2e8f0;
    }
    
    .stTextInput>div>div>input {
        font-size: 16px;
        border-radius: 20px;
        padding: 10px 20px;
        border: 2px solid #e0eafc;
        background: white;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #4a90e2;
        box-shadow: 0 0 0 1px #4a90e2;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.2);
    }
    
    .sidebar-content {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">AI TRAVEL PLANNER</h1>
            <p class="hero-subtitle">Your personal travel companion.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- FEATURES SECTION ---
st.markdown("### ✨ Why Choose Our AI Travel Planner?")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🤖</div>
            <h3>AI-Powered Planning</h3>
            <p>Get personalized recommendations based on your preferences</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">⚡</div>
            <h3>Instant Itineraries</h3>
            <p>Generate complete travel plans in seconds</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🎯</div>
            <h3>Smart Suggestions</h3>
            <p>Discover hidden gems and local experiences</p>
        </div>
    """, unsafe_allow_html=True)

# --- POPULAR DESTINATIONS ---
st.markdown("### 🌍 Popular Destinations")
destinations = [
    {
        "name": "Paris, France",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
        "description": "The City of Light awaits with its iconic landmarks and rich culture"
    },
    {
        "name": "Kyoto, Japan",
        "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=800&q=80",
        "description": "Experience ancient traditions in this historic Japanese city"
    },
    {
        "name": "Santorini, Greece",
        "image": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=800&q=80",
        "description": "Stunning sunsets and white-washed buildings in the Aegean Sea"
    }
]

cols = st.columns(3)
for i, dest in enumerate(destinations):
    with cols[i]:
        if st.button(f"✈️ {dest['name']}", key=f"destbtn_{i}"):
            if 'messages' not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": f"I want to visit {dest['name']} next month with a moderate budget. I love culture and food!"})
            response = st.session_state.planner.process_user_input(st.session_state.messages[-1]["content"])
            st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(f"""
            <div class="destination-card">
                <img src="{dest['image']}" class="destination-image">
                <h3>{dest['name']}</h3>
                <p>{dest['description']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'planner' not in st.session_state:
    st.session_state.planner = TravelPlannerPromptSystem()
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- CHAT INTERFACE ---
st.markdown("### 💬 Start Planning Your Trip")
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Chat History
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user">
                    <strong>🧑‍💼 You:</strong><br>
                    {message['content']}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message assistant">
                    <strong>🤖 AI Planner:</strong><br>
                    {message['content']}
                </div>
            """, unsafe_allow_html=True)

# Chat Input
def process_input():
    if st.session_state.user_input:
        st.session_state.messages.append({"role": "user", "content": st.session_state.user_input})
        with st.spinner("AI is planning your adventure..."):
            response = st.session_state.planner.process_user_input(st.session_state.user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.user_input = ""

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Full width input field
user_input = st.text_input(
    "✍️ Tell me about your travel plans...",
    key="user_input",
    placeholder="Enter destination, dates, budget, preferences...",
    on_change=process_input
)

st.markdown('</div>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.header("✨ Quick Actions")
    
    if st.button("🎉 Surprise Me!"):
        surprise = random.choice([
            "Plan me a spontaneous weekend getaway!",
            "Suggest a unique adventure for solo travel.",
            "Find me a hidden gem in Europe.",
            "What's a great family trip for under $2000?",
            "Give me a foodie tour in Asia!"
        ])
        st.session_state.messages.append({"role": "user", "content": surprise})
        response = st.session_state.planner.process_user_input(surprise)
        st.session_state.messages.append({"role": "assistant", "content": response})

    if st.button("🗂️ Generate Full Itinerary"):
        if len(st.session_state.messages) > 0:
            with st.spinner("Generating your itinerary..."):
                preferences = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
                itinerary = st.session_state.planner.generate_itinerary(preferences, "Based on our conversation")
                st.session_state.messages.append({"role": "assistant", "content": f"📋 **Your Travel Itinerary:**\n\n{itinerary}"})
        else:
            st.warning("Please have a conversation first before generating an itinerary.")

    if st.button("🧹 Clear Conversation"):
        st.session_state.messages = []

    st.markdown("---")
    st.markdown("**Pro Tip:** Download your itinerary as a text file for easy access on your trip!")
    if st.session_state.messages:
        if st.download_button(
            label="⬇️ Download Itinerary",
            data="\n\n".join([f'{msg["role"]}: {msg["content"]}' for msg in st.session_state.messages]),
            file_name="itinerary.txt",
            mime="text/plain"
        ):
            st.success("Itinerary downloaded!")

    st.markdown("---")
    st.markdown("**Travel Quote of the Day:**")
    st.info(random.choice(quotes))

    st.markdown("""
        <small>
        Made with ❤️ by your AI Travel Planner<br>
        <b>"Let your dreams set sail."</b>
        </small>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) 