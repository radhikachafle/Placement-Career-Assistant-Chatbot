import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

st.set_page_config(
    page_title="Placement & Career Assistant",
    page_icon="🏹",
    layout="centered",
    initial_sidebar_state="expanded"
)

@st.cache_resource(show_spinner="Loading assistant...")
def load_chatbot():
    from core.chatbot import get_response
    return get_response

get_response = load_chatbot()

ROADMAPS = {
    "ai engineer": """
graph TD
    A([Start: AI Engineer]) --> B[Learn Python and Math]
    B --> C[Statistics and Linear Algebra]
    C --> D[Machine Learning Basics]
    D --> E[Deep Learning and Neural Networks]
    E --> F[TensorFlow or PyTorch]
    F --> G[NLP and Computer Vision]
    G --> H[MLOps and Model Deployment]
    H --> I([AI Engineer Ready])
    style A fill:#00916e,color:#fff
    style I fill:#1a73e8,color:#fff
""",
    "data science": """
graph TD
    A([Start: Data Scientist]) --> B[Python and R Basics]
    B --> C[Statistics and Probability]
    C --> D[Pandas and NumPy]
    D --> E[Data Visualization]
    E --> F[Machine Learning]
    F --> G[SQL and Databases]
    G --> H([Data Scientist Ready])
    style A fill:#00916e,color:#fff
    style H fill:#1a73e8,color:#fff
""",
    "placement": """
graph TD
    A([Start Placement Prep]) --> B[Build Strong Resume]
    B --> C[Aptitude Practice]
    C --> D[DSA and Coding]
    D --> E[Core Subject Revision]
    E --> F[Apply to Companies]
    F --> G[Online Assessment]
    G --> H[Technical Interview]
    H --> I[HR Interview]
    I --> J([Placement Secured])
    style A fill:#00916e,color:#fff
    style J fill:#1a73e8,color:#fff
"""
}


def detect_roadmap(text):
    text_lower = text.lower()
    if any(k in text_lower for k in ["ai engineer", "artificial intelligence", "machine learning engineer"]):
        return "ai engineer"
    elif any(k in text_lower for k in ["data science", "data scientist"]):
        return "data science"
    elif any(k in text_lower for k in ["placement", "campus placement"]):
        return "placement"
    return None


WELCOME_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: #0a0f1e;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
}

.scene {
    position: relative;
    width: 100%;
    height: 520px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

/* ── Animated background blobs ── */
.blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.5;
    animation: blobFloat 8s ease-in-out infinite;
}
.blob1 {
    width: 400px; height: 400px;
    background: radial-gradient(circle, #00916e, transparent);
    top: -100px; left: -100px;
    animation-delay: 0s;
}
.blob2 {
    width: 350px; height: 350px;
    background: radial-gradient(circle, #1a73e8, transparent);
    bottom: -80px; right: -80px;
    animation-delay: -3s;
}
.blob3 {
    width: 250px; height: 250px;
    background: radial-gradient(circle, #00c896, transparent);
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    animation-delay: -5s;
}
@keyframes blobFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33%       { transform: translate(30px, -30px) scale(1.1); }
    66%       { transform: translate(-20px, 20px) scale(0.9); }
}

/* ── Floating particles ── */
.particles {
    position: absolute;
    width: 100%; height: 100%;
    pointer-events: none;
}
.particle {
    position: absolute;
    width: 4px; height: 4px;
    border-radius: 50%;
    background: #00c896;
    opacity: 0;
    animation: particleFloat linear infinite;
}
@keyframes particleFloat {
    0%   { opacity: 0; transform: translateY(100%) scale(0); }
    10%  { opacity: 0.8; }
    90%  { opacity: 0.4; }
    100% { opacity: 0; transform: translateY(-100vh) scale(1.5); }
}

/* ── 3D rotating ring ── */
.ring-container {
    position: absolute;
    width: 300px; height: 300px;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    perspective: 800px;
}
.ring {
    position: absolute;
    width: 100%; height: 100%;
    border-radius: 50%;
    border: 2px solid transparent;
    animation: ring3D 6s linear infinite;
}
.ring1 {
    border-top-color: rgba(0,200,150,0.6);
    border-right-color: rgba(0,200,150,0.2);
    animation-duration: 4s;
}
.ring2 {
    width: 80%; height: 80%;
    top: 10%; left: 10%;
    border-top-color: rgba(26,115,232,0.6);
    border-left-color: rgba(26,115,232,0.2);
    animation-duration: 6s;
    animation-direction: reverse;
}
.ring3 {
    width: 60%; height: 60%;
    top: 20%; left: 20%;
    border-bottom-color: rgba(0,200,150,0.8);
    border-right-color: rgba(0,200,150,0.3);
    animation-duration: 3s;
}
@keyframes ring3D {
    0%   { transform: rotateX(65deg) rotateZ(0deg); }
    100% { transform: rotateX(65deg) rotateZ(360deg); }
}

/* ── Liquid glass card ── */
.glass-card {
    position: relative;
    z-index: 10;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 28px;
    padding: 48px 44px;
    text-align: center;
    max-width: 480px;
    width: 90%;
    box-shadow:
        0 8px 32px rgba(0, 0, 0, 0.4),
        inset 0 1px 0 rgba(255,255,255,0.2),
        inset 0 -1px 0 rgba(0,0,0,0.1),
        0 0 80px rgba(0,145,110,0.2);
    animation: cardEntrance 1s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    transform-style: preserve-3d;
}
@keyframes cardEntrance {
    0%   { opacity: 0; transform: scale(0.7) translateY(40px) rotateX(20deg); }
    100% { opacity: 1; transform: scale(1) translateY(0) rotateX(0deg); }
}

/* ── Glass highlight effect ── */
.glass-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 50%;
    background: linear-gradient(
        180deg,
        rgba(255,255,255,0.12) 0%,
        rgba(255,255,255,0.02) 100%
    );
    border-radius: 28px 28px 0 0;
    pointer-events: none;
}

/* ── Liquid shimmer on card ── */
.glass-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: linear-gradient(
        45deg,
        transparent 30%,
        rgba(255,255,255,0.05) 50%,
        transparent 70%
    );
    animation: shimmer 4s ease-in-out infinite;
    pointer-events: none;
    border-radius: 28px;
}
@keyframes shimmer {
    0%   { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}

/* ── Emoji bounce ── */
.card-emoji {
    font-size: 56px;
    display: block;
    margin-bottom: 16px;
    animation: emojiBounce 2s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(0,200,150,0.6));
}
@keyframes emojiBounce {
    0%, 100% { transform: translateY(0) scale(1); }
    50%       { transform: translateY(-10px) scale(1.1); }
}

/* ── Title ── */
.card-title {
    color: white;
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 10px;
    text-shadow: 0 0 30px rgba(0,200,150,0.5);
    background: linear-gradient(135deg, #ffffff, #00c896);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ── Subtitle ── */
.card-subtitle {
    color: rgba(255,255,255,0.7);
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 28px;
}

/* ── Feature pills ── */
.feature-pills {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 24px;
}
.pill {
    background: rgba(0,200,150,0.15);
    border: 1px solid rgba(0,200,150,0.3);
    border-radius: 20px;
    padding: 5px 14px;
    color: #00c896;
    font-size: 12px;
    font-weight: 600;
    animation: pillPop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}
.pill:nth-child(1) { animation-delay: 0.8s; }
.pill:nth-child(2) { animation-delay: 1.0s; }
.pill:nth-child(3) { animation-delay: 1.2s; }
.pill:nth-child(4) { animation-delay: 1.4s; }
@keyframes pillPop {
    0%   { opacity: 0; transform: scale(0); }
    100% { opacity: 1; transform: scale(1); }
}

/* ── Divider line ── */
.glass-divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00c896, transparent);
    margin: 0 auto 20px;
    animation: dividerGlow 2s ease-in-out infinite;
}
@keyframes dividerGlow {
    0%, 100% { opacity: 0.5; width: 60px; }
    50%       { opacity: 1; width: 100px; }
}

/* ── Typing indicator ── */
.typing-hint {
    color: rgba(255,255,255,0.4);
    font-size: 11px;
    margin-top: 12px;
    animation: fadeInUp 0.5s ease 1.6s both;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
</style>
</head>
<body>
<div class="scene">

    <!-- Background blobs -->
    <div class="blob blob1"></div>
    <div class="blob blob2"></div>
    <div class="blob blob3"></div>

    <!-- Floating particles -->
    <div class="particles" id="particles"></div>

    <!-- 3D rotating rings -->
    <div class="ring-container">
        <div class="ring ring1"></div>
        <div class="ring ring2"></div>
        <div class="ring ring3"></div>
    </div>

    <!-- Liquid glass card -->
    <div class="glass-card">
        <span class="card-emoji">🏹</span>
        <div class="card-title">Placement Assistant</div>
        <div class="card-subtitle">
            Your AI-powered career guide.<br>
            Land your dream job with confidence!
        </div>
        <div class="glass-divider"></div>
        <div class="feature-pills">
            <span class="pill">🧠 ANN Powered</span>
            <span class="pill">🤖 Groq LLM</span>
            <span class="pill">🎯 10+ Topics</span>
            <span class="pill">✨ Free Forever</span>
        </div>
        <div class="typing-hint">↓ Enter your name below to get started ↓</div>
    </div>

</div>

<script>
// Generate floating particles
const container = document.getElementById('particles');
for (let i = 0; i < 30; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    p.style.left = Math.random() * 100 + '%';
    p.style.animationDuration = (Math.random() * 8 + 4) + 's';
    p.style.animationDelay = (Math.random() * 8) + 's';
    p.style.width = p.style.height = (Math.random() * 4 + 2) + 'px';
    const colors = ['#00c896', '#1a73e8', '#4ade80', '#60a5fa'];
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    container.appendChild(p);
}

// 3D tilt effect on mouse move
const card = document.querySelector('.glass-card');
document.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const rotateX = (e.clientY - centerY) / 20;
    const rotateY = (centerX - e.clientX) / 20;
    card.style.transform = `scale(1) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
});
document.addEventListener('mouseleave', () => {
    card.style.transform = 'scale(1) rotateX(0) rotateY(0)';
    card.style.transition = 'transform 0.5s ease';
});
</script>
</body>
</html>
"""


def get_css(dark_mode):
    if dark_mode:
        bg            = "#0a0f1e"
        card_bg       = "#0d1b2a"
        primary       = "#00c896"
        text          = "#e0f7f1"
        muted         = "#7ecfc0"
        btn_bg        = "#0d2a1e"
        btn_hover     = "#0f3d2a"
        border        = "#1a3a2a"
        btn_text      = "#00c896"
        bottom_bg     = "#0d1b2a"
        bubble_bot    = "#0d2a1e"
        bubble_border = "#00916e33"
        input_bg      = "#061510"
    else:
        bg            = "#f0faf6"
        card_bg       = "#ffffff"
        primary       = "#00916e"
        text          = "#0a1f1a"
        muted         = "#2d6a5a"
        btn_bg        = "#00916e"
        btn_hover     = "#007a5c"
        border        = "#80c8b0"
        btn_text      = "#ffffff"
        bottom_bg     = "#d0ede5"
        bubble_bot    = "#ffffff"
        bubble_border = "#80c8b0"
        input_bg      = "#ffffff"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    @keyframes fadeInDown {{
        from {{ opacity: 0; transform: translateY(-20px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to   {{ opacity: 1; }}
    }}
    @keyframes pulse {{
        0%   {{ box-shadow: 0 0 0 0 rgba(0,145,110,0.4); }}
        70%  {{ box-shadow: 0 0 0 10px rgba(0,145,110,0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(0,145,110,0); }}
    }}
    @keyframes slideInLeft {{
        from {{ opacity: 0; transform: translateX(-30px); }}
        to   {{ opacity: 1; transform: translateX(0); }}
    }}
    @keyframes bounce {{
        0%, 100% {{ transform: translateY(0); }}
        50%       {{ transform: translateY(-6px); }}
    }}
    @keyframes gradientShift {{
        0%   {{ background-position: 0% 50%; }}
        50%  {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif !important;
        background-color: {bg} !important;
        color: {text} !important;
    }}
    .stApp {{ background-color: {bg} !important; }}

    section[data-testid="stBottom"] {{
        background-color: {bottom_bg} !important;
        border-top: 1px solid {border} !important;
        padding: 10px 16px !important;
    }}
    section[data-testid="stBottom"] > div {{
        background-color: {bottom_bg} !important;
    }}
    div[data-testid="stChatInput"] {{
        background-color: {input_bg} !important;
        border: 1.5px solid #00916e55 !important;
        border-radius: 30px !important;
    }}
    div[data-testid="stChatInput"] textarea {{
        background-color: {input_bg} !important;
        color: {text} !important;
        font-size: 0.9rem !important;
    }}

    .app-header {{
        background: linear-gradient(135deg, #00916e, #1a73e8);
        background-size: 200% 200%;
        border-radius: 18px;
        padding: 18px 22px;
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 16px;
        animation: fadeInDown 0.6s ease forwards, gradientShift 4s ease infinite;
    }}
    .header-avatar {{
        width: 52px; height: 52px;
        border-radius: 50%;
        background: rgba(255,255,255,0.2);
        display: flex; align-items: center; justify-content: center;
        font-size: 26px;
        border: 2px solid rgba(255,255,255,0.4);
        flex-shrink: 0;
        animation: bounce 2s ease infinite;
    }}
    .header-text h2 {{ color: white !important; font-size: 1.1rem; font-weight: 700; margin-bottom: 3px; }}
    .header-text p  {{ color: rgba(255,255,255,0.8) !important; font-size: 0.82rem; margin: 0; }}
    .online-dot {{
        width: 8px; height: 8px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        margin-right: 5px;
        animation: pulse 1.5s infinite;
    }}
    .header-stats {{ margin-left: auto; display: flex; gap: 8px; }}
    .stat-pill {{
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 20px;
        padding: 5px 12px;
        text-align: center;
    }}
    .stat-pill span  {{ display: block; color: white !important; font-size: 13px; font-weight: 700; }}
    .stat-pill small {{ color: rgba(255,255,255,0.7) !important; font-size: 10px; }}

    .welcome-banner {{
        background: linear-gradient(135deg, #00916e22, #1a73e822);
        border: 1px solid #00916e44;
        border-radius: 14px;
        padding: 16px 20px;
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 16px;
        animation: fadeInUp 0.6s ease 0.2s both;
    }}
    .welcome-icon {{ font-size: 32px; flex-shrink: 0; }}
    .welcome-text h3 {{ color: {primary} !important; font-size: 0.95rem; font-weight: 700; margin-bottom: 4px; }}
    .welcome-text p  {{ color: {muted} !important; font-size: 0.82rem; line-height: 1.5; margin: 0; }}

    .stats-bar {{
        display: flex;
        gap: 12px;
        margin-bottom: 16px;
        animation: fadeInUp 0.6s ease 0.3s both;
    }}
    .stat-card {{
        background: {card_bg};
        border: 1px solid {border};
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        flex: 1;
        animation: fadeInUp 0.5s ease both;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .stat-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,145,110,0.2);
    }}
    .stat-num   {{ font-size: 1.3rem; font-weight: 700; color: {primary}; }}
    .stat-label {{ font-size: 0.7rem; color: {muted}; margin-top: 2px; font-weight: 500; }}

    .quick-label {{
        font-size: 0.75rem;
        font-weight: 700;
        color: {muted};
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 8px;
        animation: slideInLeft 0.5s ease forwards;
    }}

    .stButton > button {{
        background-color: {btn_bg} !important;
        color: {btn_text} !important;
        border: 1px solid {border} !important;
        border-radius: 12px !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        padding: 10px 8px !important;
        width: 100% !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}
    .stButton > button:hover {{
        background-color: {btn_hover} !important;
        border-color: {primary} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,145,110,0.3) !important;
    }}

    [data-testid="stSidebar"] {{
        background-color: {card_bg} !important;
        border-right: 1px solid {border} !important;
    }}
    [data-testid="stSidebar"] * {{ color: {text} !important; }}

    /* ── Creative chat bubbles ── */
    .stChatMessage {{
        background-color: {bubble_bot} !important;
        border: 1px solid {bubble_border} !important;
        border-radius: 20px !important;
        padding: 8px 16px !important;
        margin: 8px 0 !important;
        animation: fadeIn 0.4s ease forwards;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }}
    .stChatMessage:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(0,145,110,0.15) !important;
    }}

    /* User message bubble */
    .stChatMessage[data-testid="stChatMessageUser"] {{
        background: linear-gradient(135deg, #00916e22, #1a73e822) !important;
        border: 1px solid #00916e44 !important;
        border-radius: 20px 20px 4px 20px !important;
    }}

    /* Bot message bubble */
    .stChatMessage[data-testid="stChatMessageAssistant"] {{
        background-color: {bubble_bot} !important;
        border: 1px solid {bubble_border} !important;
        border-radius: 20px 20px 20px 4px !important;
        border-left: 3px solid #00916e !important;
    }}

    /* Markdown inside chat */
    .stChatMessage h2 {{
        color: {primary} !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        margin: 14px 0 8px 0 !important;
        padding-bottom: 4px !important;
        border-bottom: 1px solid {border} !important;
    }}
    .stChatMessage h3 {{
        color: {primary} !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        margin: 10px 0 6px 0 !important;
    }}
    .stChatMessage ul {{
        padding-left: 20px !important;
        margin: 8px 0 !important;
    }}
    .stChatMessage ul li {{
        color: {text} !important;
        font-size: 0.9rem !important;
        line-height: 1.7 !important;
        margin-bottom: 6px !important;
        padding-left: 4px !important;
    }}
    .stChatMessage ul li::marker {{
        color: {primary} !important;
    }}
    .stChatMessage p {{
        color: {text} !important;
        font-size: 0.92rem !important;
        line-height: 1.7 !important;
        margin-bottom: 8px !important;
    }}
    .stChatMessage strong {{
        color: {primary} !important;
        font-weight: 700 !important;
    }}
    .stChatMessage code {{
        background: {card_bg} !important;
        border: 1px solid {border} !important;
        border-radius: 6px !important;
        padding: 2px 8px !important;
        font-size: 0.85rem !important;
        color: #00c896 !important;
    }}

    /* Chat avatar */
    .stChatMessage .stAvatar {{
        background: linear-gradient(135deg, #00916e, #1a73e8) !important;
        border-radius: 50% !important;
    }}

    .stTextInput > div > div > input {{
        background-color: {input_bg} !important;
        border: 1.5px solid #00916e55 !important;
        border-radius: 14px !important;
        color: {text} !important;
        font-size: 1rem !important;
        padding: 12px 16px !important;
    }}
    .stTextInput > div > div > input:focus {{
        border-color: {primary} !important;
        box-shadow: 0 0 0 3px rgba(0,145,110,0.15) !important;
    }}

    hr {{ border-color: {border} !important; margin: 12px 0 !important; }}
    ::-webkit-scrollbar {{ width: 4px; }}
    ::-webkit-scrollbar-track {{ background: {bg}; }}
    ::-webkit-scrollbar-thumb {{ background: #00916e; border-radius: 10px; }}
    h1, h2, h3, h4, h5, h6 {{ color: {text} !important; }}
    p, li, span, label {{ color: {text} !important; }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """


# ── Session state ──────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True
if "question_count" not in st.session_state:
    st.session_state.question_count = 0
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "name_entered" not in st.session_state:
    st.session_state.name_entered = False

st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# NAME ENTRY SCREEN — 3D LIQUID GLASS
# ══════════════════════════════════════════════════════════
if not st.session_state.name_entered:
    st.components.v1.html(WELCOME_HTML, height=520)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name_input = st.text_input(
            "Enter your name to continue",
            placeholder="e.g. Radhika",
            label_visibility="visible"
        )
        if st.button("🚀 Get Started", use_container_width=True):
            if name_input.strip():
                st.session_state.user_name = name_input.strip().title()
                st.session_state.name_entered = True
                st.rerun()
            else:
                st.error("Please enter your name to continue!")
    st.stop()

# ══════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(f"## 🏹 Hi, {st.session_state.user_name}!")
    st.caption("Placement & Career Assistant")
    st.divider()

    dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    if dark != st.session_state.dark_mode:
        st.session_state.dark_mode = dark
        st.rerun()

    st.divider()
    st.markdown("### 📚 Topics I Cover")
    for topic in [
        "📄 Resume Writing",
        "🎤 Interview Preparation",
        "🧮 Aptitude Tests",
        "💰 Salary Negotiation",
        "🏢 Company Processes",
        "💻 Coding Round Prep",
        "🗺️ Career Roadmaps",
        "🎓 Higher Studies vs Job"
    ]:
        st.markdown(f"- {topic}")

    st.divider()
    st.markdown("### 📊 Session Stats")
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Questions", st.session_state.question_count)
    with c2:
        st.metric("Messages", len(st.session_state.messages))

    st.divider()
    if len(st.session_state.messages) > 0:
        chat_text = f"Placement Assistant - Chat History\n"
        chat_text += f"User: {st.session_state.user_name}\n"
        chat_text += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        chat_text += "=" * 50 + "\n\n"
        for msg in st.session_state.messages:
            role = st.session_state.user_name if msg["role"] == "user" else "Assistant"
            chat_text += f"{role}:\n{msg['content']}\n\n"
            chat_text += "-" * 30 + "\n\n"
        st.download_button(
            label="📥 Download Chat History",
            data=chat_text,
            file_name=f"placement_chat_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    else:
        st.info("Chat history will appear here after your first message.")

    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.session_state.show_welcome = True
        st.rerun()
    if st.button("🔄 Change Name", use_container_width=True):
        st.session_state.name_entered = False
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.session_state.show_welcome = True
        st.rerun()

# ══════════════════════════════════════════════════════════
# MAIN SCREEN
# ══════════════════════════════════════════════════════════
st.markdown(f"""
<div class="app-header">
    <div class="header-avatar">🏹</div>
    <div class="header-text">
        <h2>Placement Assistant</h2>
        <p><span class="online-dot"></span>Hello, {st.session_state.user_name}! Ready to help you succeed</p>
    </div>
    <div class="header-stats">
        <div class="stat-pill"><span>10+</span><small>Topics</small></div>
        <div class="stat-pill"><span>AI</span><small>Powered</small></div>
    </div>
</div>
""", unsafe_allow_html=True)

if st.session_state.show_welcome:
    st.markdown(f"""
    <div class="welcome-banner">
        <div class="welcome-icon">👋</div>
        <div class="welcome-text">
            <h3>Welcome, {st.session_state.user_name}!</h3>
            <p>Your personalized placement guide is ready. Ask me anything about
            interviews, resumes, salary or career roadmaps!</p>
        </div>
    </div>
    <div class="stats-bar">
        <div class="stat-card"><div class="stat-num">10+</div><div class="stat-label">Topics</div></div>
        <div class="stat-card"><div class="stat-num">Free</div><div class="stat-label">Always Free</div></div>
        <div class="stat-card"><div class="stat-num">24/7</div><div class="stat-label">Available</div></div>
        <div class="stat-card"><div class="stat-num">AI</div><div class="stat-label">Powered</div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="quick-label">✨ Quick Questions</div>',
            unsafe_allow_html=True)

quick_questions = [
    ("📄 Resume Tips",    "how to write a resume for campus placement"),
    ("🎤 Interview Prep", "how to prepare for technical interview"),
    ("💰 Salary Advice",  "how to negotiate salary as a fresher"),
    ("🗺️ AI Roadmap",     "give me roadmap for becoming AI engineer"),
    ("💻 DSA Tips",       "how to prepare for coding round"),
    ("🎓 GATE vs Job",    "should I go for higher studies or job"),
]

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, (label, question) in enumerate(quick_questions):
    with cols[i % 3]:
        if st.button(label, key=f"quick_{i}"):
            st.session_state.show_welcome = False
            st.session_state.messages.append({"role": "user", "content": question})
            roadmap_key = detect_roadmap(question)
            with st.spinner("Thinking..."):
                reply = get_response(question)
            st.session_state.messages.append({
                "role": "assistant",
                "content": reply,
                "roadmap": roadmap_key
            })
            st.session_state.question_count += 1
            st.rerun()

st.divider()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input(f"Ask me anything, {st.session_state.user_name}..."):
    st.session_state.show_welcome = False
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.question_count += 1

    with st.chat_message("user"):
        st.markdown(user_input)

    roadmap_key = detect_roadmap(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_response(user_input)
        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "roadmap": roadmap_key
    })
    st.rerun()