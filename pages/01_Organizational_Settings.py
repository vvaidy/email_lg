import streamlit as st
from csagents import INITIAL_STATE
from helper import *

st.markdown("# Settings for the Organization")

if 'organizational_settings' not in st.session_state:
    st.session_state.organizational_settings = INITIAL_STATE["organizational_settings"]

org_settings = st.text_area("Organizational Settings", st.session_state.organizational_settings, height=420)
st.session_state.organizational_settings = org_settings
button_update, button_persist, saved_message = st.columns([.2,.3,.5])
with button_update:
    if st.button("Update"):
        statechange(INITIAL_STATE,"organizational_settings", st.session_state.organizational_settings, False)
with button_persist:
    if st.button("Persist"):
        statechange(INITIAL_STATE,"organizational_settings", st.session_state.organizational_settings, True)
        with saved_message:
            st.write("Saved...")
