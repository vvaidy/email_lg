import streamlit as st
from csagents import INITIAL_STATE
from helper import *

st.markdown("# Settings for the Organization")

if 'organizational_settings' not in st.session_state:
    st.session_state.organizational_settings = INITIAL_STATE["organizational_settings"]

if 'responder_signature' not in st.session_state:
    st.session_state.responder_signature = INITIAL_STATE["responder_signature"]

if 'polite_wait' not in st.session_state:
    st.session_state.polite_wait = INITIAL_STATE["polite_wait"]

org_settings = st.text_area("Organizational Settings", st.session_state.organizational_settings, height=200)
st.session_state.organizational_settings = org_settings

resp_sig = st.text_area("Signature for draft emails", st.session_state.responder_signature)
st.session_state.responder_signature = resp_sig

polite_wait = st.text_area("Response when caught as a potential attack", st.session_state.polite_wait)
st.session_state.polite_wait = polite_wait

button_update, button_persist, saved_message = st.columns([.2,.3,.5])
with button_update:
    if st.button("Update"):
        statechange(INITIAL_STATE,"organizational_settings", st.session_state.organizational_settings, False)
        statechange(INITIAL_STATE, "responder_signature", st.session_state.responder_signature, False)
        statechange(INITIAL_STATE,"polite_wait", st.session_state.polite_wait, False)
with button_persist:
    if st.button("Persist"):
        statechange(INITIAL_STATE,"organizational_settings", st.session_state.organizational_settings, True)
        statechange(INITIAL_STATE, "responder_signature", st.session_state.responder_signature, True)
        statechange(INITIAL_STATE,"polite_wait", st.session_state.polite_wait, True)
        with saved_message:
            st.write("Saved...")