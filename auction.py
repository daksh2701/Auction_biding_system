import streamlit as st
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Auction Bidding System",
    page_icon="🔨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional auction-style design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .auction-header {
        text-align: center;
        background: linear-gradient(135deg, #d4af37 0%, #ffd700 50%, #b8860b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: shimmer 3s ease-in-out infinite;
    }
    
    .auction-subtitle {
        text-align: center;
        color: #6C757D;
        font-size: 1.4rem;
        margin-bottom: 2rem;
        font-weight: 400;
        font-style: italic;
    }
    
    .auction-gavel {
        text-align: center;
        font-size: 4rem;
        margin: 1rem 0;
        animation: swing 2s ease-in-out infinite;
    }
    
    .bidding-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        color: white;
        box-shadow: 0 15px 35px rgba(30, 60, 114, 0.4);
        border: 2px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
    }
    
    .current-bid-display {
        background: linear-gradient(135deg, #d4af37 0%, #ffd700 100%);
        color: #1a1a1a;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.4);
        animation: goldGlow 2s ease-in-out infinite;
    }
    
    .highest-bidder {
        font-size: 2.5rem;
        font-weight: 900;
        font-family: 'Playfair Display', serif;
        margin-bottom: 1rem;
    }
    
    .highest-bid {
        font-size: 3rem;
        font-weight: 900;
        color: #b8860b;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .winner-announcement {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(40, 167, 69, 0.4);
        animation: celebrate 1s ease-out;
        border: 3px solid #ffd700;
    }
    
    .winner-crown {
        font-size: 4rem;
        margin-bottom: 1rem;
        animation: bounce 2s infinite;
    }
    
    .bid-history-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 2rem 0;
        border-left: 5px solid #d4af37;
    }
    
    .bid-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        margin: 0.5rem 0;
        background: #f8f9fa;
        border-radius: 10px;
        border-left: 4px solid #6c757d;
        transition: all 0.3s ease;
    }
    
    .bid-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .highest-bid-item {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%) !important;
        border-left: 4px solid #d4af37 !important;
        animation: highlight 1s ease-in-out;
    }
    
    .bid-rank {
        font-weight: 700;
        color: #d4af37;
        font-size: 1.2rem;
    }
    
    .bid-name {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1rem;
    }
    
    .bid-amount {
        font-weight: 700;
        color: #27ae60;
        font-size: 1.3rem;
    }
    
    .bid-time {
        font-size: 0.9rem;
        color: #6c757d;
    }
    
    .stats-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border: 1px solid #dee2e6;
    }
    
    .stat-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 1rem 0;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .stat-label {
        font-weight: 600;
        color: #495057;
    }
    
    .stat-value {
        font-weight: 700;
        color: #d4af37;
        font-size: 1.2rem;
    }
    
    .bid-input-container {
        background: rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d4af37 0%, #ffd700 100%);
        color: #1a1a1a;
        border: none;
        padding: 1rem 2rem;
        border-radius: 15px;
        font-weight: 700;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(212, 175, 55, 0.6);
        background: linear-gradient(135deg, #b8860b 0%, #daa520 100%);
    }
    
    .stTextInput > div > div > input {
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        background: rgba(255,255,255,0.1);
        color: white;
        font-size: 1.1rem;
        padding: 0.75rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ffd700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
    }
    
    .stNumberInput > div > div > input {
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        background: rgba(255,255,255,0.1);
        color: white;
        font-size: 1.3rem;
        font-weight: 600;
        text-align: center;
        padding: 0.75rem;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #ffd700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
    }
    
    .auction-info {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #2196f3;
        margin: 2rem 0;
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #dee2e6;
    }
    
    .countdown-timer {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 1rem 0;
        animation: timerPulse 1s infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    @keyframes swing {
        0%, 100% { transform: rotate(-10deg); }
        50% { transform: rotate(10deg); }
    }
    
    @keyframes goldGlow {
        0%, 100% { box-shadow: 0 10px 30px rgba(212, 175, 55, 0.4); }
        50% { box-shadow: 0 15px 40px rgba(212, 175, 55, 0.6); }
    }
    
    @keyframes celebrate {
        0% {
            transform: scale(0.8) rotate(-5deg);
            opacity: 0;
        }
        50% {
            transform: scale(1.1) rotate(2deg);
            opacity: 1;
        }
        100% {
            transform: scale(1) rotate(0deg);
            opacity: 1;
        }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-20px); }
        60% { transform: translateY(-10px); }
    }
    
    @keyframes highlight {
        0% { background: #f8f9fa; }
        50% { background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); }
        100% { background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); }
    }
    
    @keyframes timerPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .no-bids-message {
        text-align: center;
        padding: 3rem;
        color: #6c757d;
        font-size: 1.2rem;
        font-style: italic;
    }
    
    @media (max-width: 768px) {
        .auction-header {
            font-size: 2.5rem;
        }
        
        .highest-bid {
            font-size: 2rem;
        }
        
        .highest-bidder {
            font-size: 1.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'bids' not in st.session_state:
        st.session_state.bids = {}
    if 'auction_ended' not in st.session_state:
        st.session_state.auction_ended = False
    if 'total_bids' not in st.session_state:
        st.session_state.total_bids = 0
    if 'auction_start_time' not in st.session_state:
        st.session_state.auction_start_time = datetime.now()

def add_bid(name, amount):
    """Add a new bid to the auction"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.bids[name] = {
        'amount': amount,
        'time': timestamp,
        'bid_number': len(st.session_state.bids) + 1
    }
    st.session_state.total_bids += 1

def find_highest_bidder():
    """Find the highest bidder from all bids"""
    if not st.session_state.bids:
        return None, 0
    
    highest_bid = 0
    winner = ""
    
    for bidder, bid_info in st.session_state.bids.items():
        if bid_info['amount'] > highest_bid:
            highest_bid = bid_info['amount']
            winner = bidder
    
    return winner, highest_bid

def get_sorted_bids():
    """Get bids sorted by amount (highest first)"""
    if not st.session_state.bids:
        return []
    
    sorted_bids = sorted(
        st.session_state.bids.items(),
        key=lambda x: x[1]['amount'],
        reverse=True
    )
    return sorted_bids

def reset_auction():
    """Reset the auction to start fresh"""
    st.session_state.bids = {}
    st.session_state.auction_ended = False
    st.session_state.total_bids = 0
    st.session_state.auction_start_time = datetime.now()

# Initialize session state
init_session_state()

# Header
st.markdown('<div class="auction-gavel">🔨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="auction-header">AUCTION HOUSE</h1>', unsafe_allow_html=True)
st.markdown('<p class="auction-subtitle">Premium Bidding Experience</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown("### 🏛️ Auction Controls")
    
    if st.button("🔄 Start New Auction", help="Reset and start fresh auction"):
        reset_auction()
        st.rerun()
    
    if st.session_state.bids and not st.session_state.auction_ended:
        if st.button("🔨 End Auction Now", help="Finalize current auction"):
            st.session_state.auction_ended = True
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Auction Statistics
    if st.session_sta