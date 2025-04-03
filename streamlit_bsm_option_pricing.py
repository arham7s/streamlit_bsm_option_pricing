import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 🌐 Streamlit Page Settings
st.set_page_config(page_title="Options Pricing Tool", layout="centered")

# 🌑 Dark Theme Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .stApp {
            background-color: #0e1117;
        }
        h1, h4 {
            color: #61dafb;
            text-align: center;
        }
        .stSlider > div {
            color: #ffffff;
        }
        .css-1cpxqw2 {
            background-color: #262730;
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 App Title
st.markdown("<h1>💹 Option Pricing Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h4>Designed by Arham Shah</h4>", unsafe_allow_html=True)

# 🧮 Sidebar Inputs - Interactive Sliders
with st.sidebar:
    st.markdown("## 🎯 Input Parameters")

    st.slider("📌 Spot Price (S)", min_value=50.0, max_value=200.0, value=100.0, step=1.0, key="spot")
    st.slider("🎯 Strike Price (K)", min_value=50.0, max_value=200.0, value=100.0, step=1.0, key="strike")
    st.slider("⏳ Time to Expiry (Years)", min_value=0.01, max_value=3.0, value=1.0, step=0.01, key="expiry")
    st.slider("🏦 Risk-free Interest Rate (r)", min_value=0.0, max_value=0.2, value=0.05, step=0.005, key="rate")
    st.slider("📈 Volatility (σ)", min_value=0.01, max_value=1.0, value=0.2, step=0.01, key="vol")
    
    option_type = st.radio("📑 Option Type", ["Call", "Put"], horizontal=True)

# Assign variables from sidebar
S = st.session_state.spot
K = st.session_state.strike
T = st.session_state.expiry
r = st.session_state.rate
sigma = st.session_state.vol

# 🧠 Black-Scholes Formula
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

if option_type.lower() == "call":
    price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
else:
    price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# 💰 Display Premium
st.markdown("### 💰 Option Price")
st.success(f"**{option_type} Option Premium: ₹{price:.2f}**")

# 📉 Payoff Diagram
spot_prices = np.linspace(S * 0.5, S * 1.5, 100)
if option_type.lower() == 'call':
    payoff = np.maximum(spot_prices - K, 0) - price
else:
    payoff = np.maximum(K - spot_prices, 0) - price

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(spot_prices, payoff, label='Payoff', linewidth=2, color='cyan')
ax.axhline(0, color='white', linestyle='--', linewidth=1)
ax.axvline(S, color='orange', linestyle=':', label='Current Price')
ax.set_facecolor('#1e1e1e')
ax.tick_params(colors='white')
ax.set_title(f'{option_type} Option Payoff at Expiry', color='white')
ax.set_xlabel('Stock Price at Expiry', color='white')
ax.set_ylabel('Profit / Loss', color='white')
ax.legend()
ax.grid(True, color='gray')
st.pyplot(fig)

