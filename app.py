import streamlit as st
import pandas as pd

# -----------------------------
# Data
# -----------------------------
data = [
    ["Care Center of Honolulu (LTC)", "RN", 48.31],
    ["East Hawaii State Veterans Home dba Yukio Okutsu State Veterans Home", "LPN", 34.90],
    ["East Hawaii State Veterans Home dba Yukio Okutsu State Veterans Home", "RN", 45.94],
    ["Hale Makua Health Services (LTC)", "RN", 46.89],
    ["Hale Nani Rehab & Nursing Center (LTC)", "LPN", 37.77],
    ["Hale Nani Rehab & Nursing Center (LTC)", "RN", 50.06],
    ["Hawaii Care Choices (Hospice of Hilo)", "RN", 47.94],
    ["Kahuku Medical Center", "RN", 59.84],
    ["Kaiser Foundation Hospital - Patient Care & Clinical Coordinators", "PCC", 75.88],
    ["Kaiser Foundation Hospital - Patient Care & Clinical Coordinators", "CC", 79.64],
    ["Kapiolani Medical Center - Registered Nurses (HPH)", "RN", 70.89],
    ["Kapiolani Medical Center - Respiratory Therapists (HPH)", "RSP", 51.46],
    ["Kauai Medical Clinic (HPH)", "LPN", 32.90],
    ["Kuakini Geriatric Care, Inc. (LTC)", "RN", 49.86],
    ["Kuakini Medical Center (LTC)", "RN", 67.51],
    ["Kulana Malama (Pediahealth Corp)", "CNA", 19.24],
    ["Kulana Malama (Pediahealth Corp)", "LPN", 30.15],
    ["Kulana Malama (Pediahealth Corp)", "RN", 41.00],
    ["Liberty Dialysis Hawaii, LLC; (Fresenius Kidney Care)", "RN", 58.80],
    ["North Hawaii Community Hospital", "RN", 66.68],
    ["Oahu Care Facility - Certified Nurse Assistants (LTC)", "CNA", 19.24],
    ["Oahu Care Facility - Registered Nurses / Licensed Practical Nurses (LTC)", "LPN", 29.03],
    ["Oahu Care Facility - Registered Nurses / Licensed Practical Nurses (LTC)", "RN", 40.56],
    ["Pohai Nani Good Samaritan (LTC)", "RN", 45.66],
    ["Rehabilitation Hospital of the Pacific - Licensed Practical Nurses", "LPN", 29.79],
    ["Rehabilitation Hospital of the Pacific - Registered Nurses", "RN", 60.33],
    ["St Francis Community Health Services (Hospice)", "RN", 54.59],
    ["Straub Clinic and Hospital (HPH)", "RN", 70.89],
    ["The Queen's Medical Center - Case Managers", "CM", 69.53],
    ["The Queen's Medical Center - Case Managers", "CR", 69.53],
    ["The Queen's Medical Center - Case Managers", "PTC", 69.53],
    ["The Queen's Medical Center - Central Transport Services (Punchbowl)", "CTS", 23.69],
    ["The Queen's Medical Center - Radiation Therapists", "RT", 54.37],
    ["The Queen's Medical Center - Registered Nurses (Punchbowl & West)", "RN", 73.32],
    ["The Queen's Medical Center - Wound Care RN", "WCCM", 69.77],
    ["US Renal Care", "RN", 59.78],
    ["Wilcox Memorial Hospital (HPH)", "RN", 68.16],
]

df = pd.DataFrame(data, columns=["CBU", "Job Classification", "Rate"])

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="Calculate my dues")

# Title & Blurb
st.title("Calculate my dues")
st.write("""
The proposed dues structure determines your dues using the formula: Monthly Dues = Job Rate x Standard Hours of Work per Week x 4.333 x 0.008

Use this tool to calculate your **expected monthly dues**.
Your job rate is determined by your **CBU** and **Job Classification**.

1. Select your **CBU (Collective Bargaining Unit)**.  
2. Choose your **Job Classification**.  
3. Enter your **Standard hours of work per week**.  
Your monthly dues will update automatically!
""")

st.markdown("---")

# --- Dropdown 1: Select CBU ---
cbu_list = df["CBU"].unique()
selected_cbu = st.selectbox("Select CBU:", sorted(cbu_list))

# Filter job classifications based on selected CBU
filtered_jobs = df[df["CBU"] == selected_cbu]["Job Classification"].unique()

# --- Dropdown 2: Select Job Classification ---
selected_job = st.selectbox("Select Job Classification:", sorted(filtered_jobs))

# --- Look up rate based on selection ---
rate = df[(df["CBU"] == selected_cbu) & (df["Job Classification"] == selected_job)]["Rate"].values[0]

# --- Numeric Input: Standard hours per week ---
hours_per_week = st.number_input(
    "Standard hours of work per week:",
    min_value=0.0,
    value=40.0,
    step=0.5
)

# --- Calculation: Expected Monthly Dues ---
monthly_dues = rate * hours_per_week * 4.333 * 0.008

# --- Display ---
st.markdown("### Expected Monthly Dues:")
st.success(f"${monthly_dues:,.2f}")

# Display current rate for clarity
st.caption(f"This estimate is calculated using an **Hourly Rate of  ${rate:.2f}** which is determined based on your selection of CBU and Job Classification.")

