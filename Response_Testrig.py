# Based on Sam Witteveen's YT Video: https://youtu.be/lvQ96Ssesfk?si=FPy8LSaDxacijl7e
# Sam Witteveen's github is: @samwit
# Sam's Colab Notebook that this is based on:
# https://colab.research.google.com/drive/1WemHvycYcoNTDr33w7p2HL3FF72Nj88i?usp=sharing#scrollTo=jJhoLxciS906

import streamlit as st
import streamlit.components.v1 as components

from helper import *
# New run_responder function that uses functions that are grouped together in a better way to turn into nodes...
# WIP to be able to make your own nodes
from TestCreatingNodes import run_responder_test, INITIAL_STATE

if 'customer_email' not in st.session_state:
    st.session_state.customer_email = INITIAL_STATE["customer_email"]

st.set_page_config(layout="wide")

st.title("Customer Service Workflow Example")
input_column, output_column = st.columns(2)

with input_column:
    cust_email = st.text_area(
        "Customer Email", st.session_state.customer_email,
        height=320)
    st.session_state.customer_email = cust_email
    respond_button, save_button, saved_message = st.columns(3)
    with respond_button:
        if st.button("Respond"):
            with st.spinner("Generating Response..."):
                statechange(INITIAL_STATE,"customer_email", st.session_state.customer_email, False)
                response = run_responder_test()
            with output_column:
                st.info(response)