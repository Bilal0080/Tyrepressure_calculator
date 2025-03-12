import streamlit as st
import streamlit.components.v1 as components

def get_recommended_pressure(vehicle_type, load_condition):
    pressure_data = {
        "Car": {"Light Load": 32, "Heavy Load": 35},
        "Bike": {"Light Load": 28, "Heavy Load": 30},
        "Truck": {"Light Load": 80, "Heavy Load": 100},
    }
    return pressure_data.get(vehicle_type, {}).get(load_condition, "N/A")

st.set_page_config(page_title="Tyre Pressure Calculator", page_icon="🚗", layout="centered")

st.markdown("""
    <style>
        body {background-color: #f0f2f6;}
        .main {
            background: linear-gradient(135deg, #2E86C1, #A569BD);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
            color: white;
            text-align: center;
        }
        h1 {color: #F4D03F; text-align: center; font-size: 2.5rem;}
        .stButton>button {
            background-color: #F4D03F;
            color: black;
            border-radius: 8px;
            padding: 12px;
            font-size: 1.2rem;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #D4AC0D;
            color: white;
        }
        .stSelectbox, .stRadio {background-color: white; border-radius: 8px; padding: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("🚗 Tyre Pressure Calculator")

vehicle_type = st.selectbox("🚙 Select Vehicle Type", ["Car", "Bike", "Truck"])
load_condition = st.radio("⚖️ Select Load Condition", ["Light Load", "Heavy Load"])

if st.button("🔍 Calculate Pressure"):
    recommended_pressure = get_recommended_pressure(vehicle_type, load_condition)
    st.success(f"✅ Recommended Tyre Pressure: {recommended_pressure} PSI")

st.markdown('</div>', unsafe_allow_html=True)