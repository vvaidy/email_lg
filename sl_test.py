# Based on Sam Witteveen's YT Video: https://youtu.be/lvQ96Ssesfk?si=FPy8LSaDxacijl7e
# Sam Witteveen's github is: @samwit
# Sam's Colab Notebook:
# https://colab.research.google.com/drive/1WemHvycYcoNTDr33w7p2HL3FF72Nj88i?usp=sharing#scrollTo=jJhoLxciS906

import streamlit as st

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

st.title("Customer Service Agents Example")
st.write("This is a simple example of a customer service agent that can respond to emails.")

INITIAL_STATE["customer_email"] = st.text_area(
    "Customer Email", INITIAL_STATE["customer_email"],
    height=320)

if st.button("Respond to email"):
    with st.spinner("Generating Response..."):
        response = run_responder()
    st.markdown("# The response from the agent is:")
    st.info(response)
