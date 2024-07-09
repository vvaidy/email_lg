import streamlit as st
from csagents import INITIAL_STATE
from helper import statechange

st.markdown("Model Changer")

input_column, space_column= st.columns(2)

model_options = ["llama3-8b-8192", "gemma2-9b-it", "mixtral-8x7b-32768"]

with input_column:
    model = st.selectbox("Model", model_options, 0)
    if st.button("Persist"):
        statechange(INITIAL_STATE, "model", model, True)
