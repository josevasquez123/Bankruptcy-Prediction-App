import streamlit as st
import json
import requests

st.set_page_config(layout="wide")

st.title("Bankruptcy Predictor")

st.markdown('#')

col1, col2, col3 = st.columns(3)

with col1:
    val_1 = st.number_input("ROA(C) before interest and depreciation before interest",step=1e-6,format="%.6f")

    val_2 = st.number_input("ROA(A) before interest and % after tax",step=1e-6,format="%.6f")

    val_3 = st.number_input("ROA(B) before interest and depreciation after tax",step=1e-6,format="%.6f")

    val_4 = st.number_input("Tax rate (A)",step=1e-6,format="%.6f")

    val_5 = st.number_input("Net Value Per Share (B)",step=1e-6,format="%.6f")

    val_6 = st.number_input("Net Value Per Share (A)",step=1e-6,format="%.6f")

    val_7  = st.number_input("Net Value Per Share (C)",step=1e-6,format="%.6f")

with col2:

    val_8 = st.number_input("Persistent EPS in the Last Four Seasons",step=1e-6,format="%.6f")

    val_9 = st.number_input("Operating Profit Per Share (Yuan ¥)",step=1e-6,format="%.6f")

    val_10 = st.number_input("Per Share Net profit before tax (Yuan ¥)",step=1e-6,format="%.6f")

    val_11 = st.number_input("Debt ratio %",step=1e-6,format="%.6f")

    val_12 = st.number_input("Net worth/Assets",step=1e-6,format="%.6f")

    val_13 = st.number_input("Operating profit/Paid-in capital",step=1e-6,format="%.6f")

    val_14 = st.number_input("Net profit before tax/Paid-in capital",step=1e-6,format="%.6f")

with col3:

    val_15 = st.number_input("Working Capital to Total Assets",step=1e-6,format="%.6f")

    val_16 = st.number_input("Cash/Total Assets",step=1e-6,format="%.6f")

    val_17 = st.number_input("Current Liability to Assets",step=1e-6,format="%.6f")

    val_18 = st.number_input("Retained Earnings to Total Assets",step=1e-6,format="%.6f")

    val_19 = st.number_input("Current Liability to Current Assets",step=1e-6,format="%.6f")

    val_20 = st.number_input("Net Income to Total Assets",step=1e-6,format="%.6f")

input_api = {
    "val_1":val_1,
    "val_2":val_2,
    "val_3":val_3,
    "val_4":val_4,
    "val_5":val_5,
    "val_6":val_6,
    "val_7":val_7,
    "val_8":val_8,
    "val_9":val_9,
    "val_10":val_10,
    "val_11":val_11,
    "val_12":val_12,
    "val_13":val_13,
    "val_14":val_14,
    "val_15":val_15,
    "val_16":val_16,
    "val_17":val_17,
    "val_18":val_18,
    "val_19":val_19,
    "val_20":val_20
}

st.markdown('#')

if st.button("Calculate"):
    res = requests.post(url="http://127.0.0.1:8000/model", data=json.dumps(input_api))

    if (res.text=="1"):
        st.title("More chances of possible Bankruptcy")
    else:
        st.title("Less chance of Bankruptcy")
