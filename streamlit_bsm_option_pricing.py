import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 🌐 Page config
st.set_page_config(page_title="Options Pricing Tool", layout="centered")

# 💎 Custom CSS to enhance UI
st.markdown("""
    <style>
        .stApp {
            background-color: #f7f9fc;
        }
        .main > div {
            padding-top: 1.5rem;
        }
        .css-18e3th9 {
            padding-top: 2rem;
        }
        h1, h3 {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Header
st.title("💹 Black-Scholes Option Pricing Calculator")
st.markdown("Designed by **Arham Shah** • Streamlit Web App")

# 🧮 Sidebar Inputs
st.sidebar.header("Input Parameters")
S = st.sidebar.number_input("📌 Spot Price (S)", value=100.0, step=1.0)
K = st.sidebar.number_input("🎯 Strike Price (K)", value=100.0, step=1.0)
T = st.sidebar.number_input("⏳ Time to Expiry (T in years)", value=1.0, step=0.1)
r = st.sidebar.number_input("🏦 Risk-free Interest Rate (r)", value=0.05, step=0.01)
sigma = st.sidebar.number_input("📈 Volatility (σ)", value=0.2, step=0.01)
option_type = st.sidebar.radio("📑 Option Type", ["Call", "Put"])

# 📘 BSM Formula
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

if option_type.lower() == "call":
    price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
else:
    price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# ✅ Output
st.markdown("### 💰 Option Price")
st.success(f"**{option_type} Option Premium: ₹{price:.2f}**")

# 📉 Payoff Diagram
spot_prices = np.linspace(S * 0.5, S * 1.5, 100)
if option_type.lower() == 'call':
    payoff = np.maximum(spot_prices - K, 0) - price
else:
    payoff = np.maximum(K - spot_prices, 0) - price

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(spot_prices, payoff, label='Payoff', linewidth=2)
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.axvline(S, color='grey', linestyle=':', label='Current Price')
ax.set_title(f'{option_type} Option Payoff at Expiry')
ax.set_xlabel('Stock Price at Expiry')
ax.set_ylabel('Profit / Loss')
ax.legend()
ax.grid(True)
st.pyplot(fig)



