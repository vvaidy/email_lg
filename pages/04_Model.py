import streamlit as st
from csagents import INITIAL_STATE
from helper import statechange
import requests
import os
import sys

st.markdown("Model Changer")

input_column, space_column= st.columns(2)

api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
model_options = []
for val in response.json()["data"]:
    model_options.append(val["id"])


if "model_index" not in st.session_state:
    st.session_state.model_index = model_options.index(INITIAL_STATE.get("model"))

with input_column:
    model = st.selectbox("Model", model_options, st.session_state.model_index)
    st.session_state.model_index = model_options.index(model)
    if st.button("Persist"):
        statechange(INITIAL_STATE, "model", model, True)

st.text("A 'Persist' and a restart of the program is needed currently to change models")