# Based on Sam Witteveen's YT Video: https://youtu.be/lvQ96Ssesfk?si=FPy8LSaDxacijl7e
# Sam Witteveen's github is: @samwit
# Sam's Colab Notebook that this is based on:
# https://colab.research.google.com/drive/1WemHvycYcoNTDr33w7p2HL3FF72Nj88i?usp=sharing#scrollTo=jJhoLxciS906

import streamlit as st
import streamlit.components.v1 as components

from csagents import run_responder, INITIAL_STATE


INITIAL_STATE["customer_email"] = """
Hi There,

I had a wonderful time at your resort last week. The only glitch was that I had
a poor experience at the front desk with the lady there, I think her name
was Eleanor Rigby. If you like, you could check with Father MacKenzie who witnessed
the entire incident.

Other than that I had a wonderful time although I have to say that the rain did
put quite a damper on things. What might be a better time for me to visit?
I like to follow the sun!

Paul
"""
st.set_page_config(layout="wide")

st.title("Customer Service Workflow Example")
left_column, right_column = st.columns(2)


with left_column:
    customer_email = st.text_area(
        "Customer Email", INITIAL_STATE["customer_email"],
        height=320)
    if st.button("Respond"):
        with st.spinner("Generating Response..."):
            INITIAL_STATE["customer_email"] = customer_email
            response = run_responder()
        with right_column:
            st.info(response)
