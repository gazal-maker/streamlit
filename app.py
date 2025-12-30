import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NEURO-MUSE", layout="wide")
st.title("🧠 Project NEURO-MUSE")
st.write("Generating 'Impossible' human experiences using Gemini 1.5 Pro.")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # The Golden Prompt is programmed here
    model = genai.GenerativeModel('gemini-1.5-pro', 
                                  system_instruction="You are the Omni-Dimensional Neuro-Architect. Synthesize a brand new human emotion. Name it, give the HEX color, the Hz frequency, and a logic-breaking poem.")

    if st.button("Synthesize New Human Experience"):
        with st.spinner('Calculating Neurological Gaps...'):
            response = model.generate_content("Synthesize an emotion for a future-human.")
            st.success("Synthesis Complete")
            st.markdown(f"### Result: \n {response.text}")
else:
    st.warning("Please enter your API Key in the sidebar.")
