import streamlit as st
from csagents import INITIAL_STATE
from helper import *

st.markdown("# Settings for the Organization")

if 'organizational_settings' not in st.session_state:
    st.session_state.organizational_settings = INITIAL_STATE["organizational_settings"]

org_settings = st.text_area("Organizational Settings", st.session_state.organizational_settings, height=420)
st.session_state.organizational_settings = org_settings
col1, col2, col3 = st.columns([.2,.3,.5])
with col1:
    if st.button("Update"):
        statechange(INITIAL_STATE,"organizational_settings", st.session_state.organizational_settings, False)
with col2:
    if st.button("Persist"):
        statechange(INITIAL_STATE,"organizational_settings", st.session_state.organizational_settings, True)
        with col3:
            st.write("Saved...")
