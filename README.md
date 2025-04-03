# 💹 Black-Scholes Option Pricing Dashboard

A modern, interactive, and visually stunning **option pricing calculator** built using the Black-Scholes-Merton model. This web app allows users to simulate Call and Put options, calculate option premiums, visualize payoffs, and analyze Greeks — all with beautiful UI and real-time 3D surface plots.

🌐 **Live Demo** → [Launch App](https://appbsmoptionpricingpy-eyabcjgdhsktxkq4xbhpff.streamlit.app/)

---

## 🚀 Features

- 🎯 Dynamic input sliders for:
  - Spot Price, Strike Price
  - Time to Expiry (T) [0.1 to 10 years]
  - Risk-free Rate (r)
  - Volatility (σ)
- 📊 Black-Scholes model for both **Call** and **Put**
- 📈 Greeks: Delta, Gamma, Theta, Vega, Rho
- 🌐 3D Surface Plot of Option Price vs Time and Volatility (Plotly)
- 🖤 Dark Mode UI with intuitive design

---

## 📸 Screenshots

### 📊 Dashboard View
![Dashboard](https://github.com/arham7s/streamlit_bsm_option_pricing/blob/main/DASHBOARD.jpg?raw=true)

### 🌐 3D Surface Plot
![3D Plot](https://github.com/arham7s/streamlit_bsm_option_pricing/blob/main/SURFACE_PLOT.jpg?raw=true)

---

## ⚙️ How It Works

1. **Adjust the sliders** in the sidebar to input your option parameters.
2. The app calculates:
   - Theoretical option price (using Black-Scholes formula)
   - Greeks (Delta, Gamma, Theta, Vega, Rho)
3. It also visualizes a 3D surface showing how the **Call option price** changes with time and volatility.
4. Fully responsive, deployed on Streamlit Cloud.

---

## 📦 Tech Stack

| Tool         | Description                        |
|--------------|------------------------------------|
| 🐍 Python     | Core language                     |
| 📈 Streamlit  | Interactive frontend and layout   |
| 📊 Plotly     | 3D Surface Plot rendering          |
| 📐 NumPy      | Numerical computations             |
| 📚 SciPy      | Cumulative distributions & math    |

---

## 🛠 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/arham7s/streamlit_bsm_option_pricing.git
cd streamlit_bsm_option_pricing

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app locally
streamlit run streamlit_app.py
```

Or deploy directly on [Streamlit Cloud](https://streamlit.io/cloud).

---

## ✍️ Author

**Arham Shah**  

---

## 🌟 Star This Repo

If you found this useful, feel free to **star ⭐ the repository** and share it with others!
