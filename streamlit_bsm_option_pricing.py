import streamlit as st
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

# 🌐 Page setup
st.set_page_config(page_title="BSM Option Tool", layout="centered")

# 🌑 Dark theme styling
st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: white; }
        h1, h3 { text-align: center; color: #61dafb; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>💹 Black-Scholes Option Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3>By Arham Shah</h3>", unsafe_allow_html=True)

# -------------------
# 🧮 Inputs
# -------------------
st.sidebar.header("🔧 Input Parameters")

S = st.sidebar.slider("📌 Spot Price (S)", 50.0, 1000.0, 350.0, step=10.0)
K = st.sidebar.slider("🎯 Strike Price (K)", 50.0, 1000.0, 280.0, step=10.0)
T = st.sidebar.slider("⏳ Time to Expiry (T in Years)", 0.1, 10.0, 2.5, step=0.1)  # ✅ Dynamic T
r = st.sidebar.slider("🏦 Risk-Free Rate (r)", 0.00, 0.20, 0.10, step=0.01)
sigma = st.sidebar.slider("📈 Volatility (σ)", 0.10, 1.50, 0.75, step=0.01)
option_type = st.sidebar.radio("📑 Option Type", ["Call", "Put"], horizontal=True)

# -------------------
# 📈 Black-Scholes Model
# -------------------
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

if option_type == "Call":
    price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
else:
    price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Greeks
delta = norm.cdf(d1) if option_type == "Call" else -norm.cdf(-d1)
gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) -
         r * K * np.exp(-r * T) * norm.cdf(d2 if option_type == 'Call' else -d2))
vega = S * norm.pdf(d1) * np.sqrt(T)
rho = K * T * np.exp(-r * T) * (norm.cdf(d2) if option_type == "Call" else -norm.cdf(-d2))

# -------------------
# 🧾 Output Results
# -------------------
st.markdown("### 💰 Option Price")
st.success(f"**{option_type} Option Premium: ₹{price:.2f}**")

st.markdown("### 📊 Greeks")
st.markdown(f"""
- **Delta**: {delta:.4f}  
- **Gamma**: {gamma:.8f}  
- **Theta**: {theta:.4f}  
- **Vega**: {vega / 100:.4f} per 1%  
- **Rho**: {rho / 100:.4f} per 1%  
""")

# -------------------
# 🌐 3D Surface Plot (Call Only)
# -------------------
st.markdown("### 🌐 3D Option Price Surface (Volatility vs Time)")

vol_range = np.linspace(0.1, 1.5, 50)
time_range = np.linspace(0.1, 10.0, 50)
vol_grid, time_grid = np.meshgrid(vol_range, time_range)

def bsm_call_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

price_surface = bsm_call_price(S, K, time_grid, r, vol_grid)

fig = go.Figure(data=[go.Surface(z=price_surface, x=vol_grid, y=time_grid, colorscale='Viridis')])
fig.update_layout(
    scene=dict(
        xaxis_title='Volatility (σ)',
        yaxis_title='Time to Expiry (T)',
        zaxis_title='Call Option Price'
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    title=f'Call Option Price Surface (S={S}, K={K})'
)

st.plotly_chart(fig, use_container_width=True)

# -------------------
# 📎 Footer
# -------------------
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>Made with ❤️ by Arham Shah • Powered by <a style='color:#1f77b4;' href='https://streamlit.io'>Streamlit</a></p>", unsafe_allow_html=True)


