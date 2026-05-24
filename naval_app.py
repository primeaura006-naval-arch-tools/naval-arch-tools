import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Naval Architecture Master Tool 🚢")
st.write("Built by Harshit Rama — Age 17")

option = st.sidebar.selectbox(
    "Choose Calculator",
    ["Buoyancy Calculator",
     "Stability (GM) Calculator",
     "Resistance & Power Calculator"]
)

# ═══════════════════════════════
if option == "Buoyancy Calculator":
    st.header("Buoyancy Calculator 🌊")
    v = st.number_input("Enter Volume (m³)", min_value=0.0)
    mass = st.number_input("Enter Ship Mass (kg)", min_value=0.0)
    
    if st.button("Calculate"):
        rho, g = 1025, 9.81
        FB = rho * v * g
        w = mass * g
        st.write(f"Buoyancy Force: {FB:.2f} N")
        st.write(f"Ship Weight: {w:.2f} N")
        if FB > w:
            st.success(f"✅ Ship will FLOAT — Extra Margin: {FB-w:.2f} N")
        else:
            st.error(f"❌ Ship will SINK — Deficit: {w-FB:.2f} N")

# ═══════════════════════════════
elif option == "Stability (GM) Calculator":
    st.header("Stability Calculator ⚓")
    KM = st.number_input("Enter KM (m)", min_value=0.0)
    KG = st.number_input("Enter KG (m)", min_value=0.0)
    
    if st.button("Calculate"):
        GM = KM - KG
        st.write(f"GM = {GM:.2f} m")
        if GM > 1.0:
            st.success("💪 Very Highly Stable")
        elif GM > 0.5:
            st.success("✅ Moderately Stable")
        elif GM > 0:
            st.warning("⚠️ Slightly Stable")
        elif GM == 0:
            st.warning("⚠️ Neutral — Dangerous")
        else:
            st.error("❌ UNSTABLE — Very Risky!")

# ═══════════════════════════════
elif option == "Resistance & Power Calculator":
    st.header("Resistance & Power Calculator ⚙️")
    V = st.number_input("Enter Speed (m/s)", min_value=0.0)
    Cd = st.number_input("Enter Drag Coefficient", min_value=0.0, value=0.2)
    A = st.number_input("Enter Wetted Surface Area (m²)", min_value=0.0)
    
    if st.button("Calculate"):
        rho = 1025
        R = 0.5 * rho * (V**2) * Cd * A
        P = R * V
        st.write(f"Resistance: {R:.2f} N")
        st.write(f"Power: {P/1000:.2f} kW")
        
        # Graph
        speeds = np.linspace(1, 20, 100)
        R_graph = 0.5 * rho * speeds**2 * Cd * A
        fig, ax = plt.subplots()
        ax.plot(speeds, R_graph, color='blue', linewidth=2)
        ax.set_xlabel("Speed (m/s)")
        ax.set_ylabel("Resistance (N)")
        ax.set_title("Speed vs Resistance")
        ax.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig)