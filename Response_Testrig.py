# Based on Sam Witteveen's YT Video: https://youtu.be/lvQ96Ssesfk?si=FPy8LSaDxacijl7e
# Sam Witteveen's github is: @samwit
# Sam's Colab Notebook that this is based on:
# https://colab.research.google.com/drive/1WemHvycYcoNTDr33w7p2HL3FF72Nj88i?usp=sharing#scrollTo=jJhoLxciS906

import streamlit as st
import streamlit.components.v1 as components

from csagents import run_responder, INITIAL_STATE
from helper import *

if 'customer_email' not in st.session_state:
    st.session_state.customer_email = INITIAL_STATE["customer_email"]

st.set_page_config(layout="wide")

st.title("Customer Service Workflow Example")
left_column, right_column = st.columns(2)

with left_column:
    cust_email = st.text_area(
        "Customer Email", st.session_state.customer_email,
        height=320)
    st.session_state.customer_email = cust_email
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Respond"):
            with st.spinner("Generating Response..."):
                statechange(INITIAL_STATE,"customer_email", st.session_state.customer_email, False)
                response = run_responder()
            with right_column:
                st.info(response)
    with col2:
        if st.button("Save"):
            statechange(INITIAL_STATE,"customer_email", st.session_state.customer_email, True)
            with col3:
                st.write("Saved...")
