import streamlit as st
from csagents import INITIAL_STATE
from helper import statechange

st.markdown("Model Changer")

input_column, space_column= st.columns(2)

model_options = ["llama3-8b-8192", "gemma2-9b-it", "mixtral-8x7b-32768"]

if "model_index" not in st.session_state:
    st.session_state.model_index = model_options.index(INITIAL_STATE.get("model"))

with input_column:
    model = st.selectbox("Model", model_options, st.session_state.model_index)
    st.session_state.model_index = model_options.index(model)
    if st.button("Persist"):
        statechange(INITIAL_STATE, "model", model, True)
st.text("A 'Persist' and a restart of the program is needed to change models")
