import streamlit as st
from csagents import workflow, PROMPT_STATE
import graphviz
from helper import *


st.markdown("# Workflow Routing Rules")

edges = workflow.edges
graph = graphviz.Digraph()
for val in edges:
    graph.edge(val[0], val[1])
graph.edge("categorize_email", "research_info_search")
graph.edge("categorize_email", "threat_responder")
graph.edge("categorize_email", "draft_email_writer")

st.graphviz_chart(graph)

if 'research_router_instructions' not in st.session_state:
    st.session_state.research_router_instructions = PROMPT_STATE["research_router_instructions"]

if 'search_keyword_modifier' not in st.session_state:
    st.session_state.search_keyword_modifier = PROMPT_STATE["search_keyword_modifier"]

if 'draft_email_modifier' not in st.session_state:
    st.session_state.draft_email_modifier = PROMPT_STATE["draft_email_modifier"]

research_router = st.text_area("Research Router Instructions", st.session_state.research_router_instructions, height= 200)
if st.button("Persist", key="research_router_button"):
    statechange(PROMPT_STATE, "research_router_instructions", research_router, True)

search_keyword = st.text_area("Add additional instructions for the search function", st.session_state.search_keyword_modifier, height=200)
if st.button("Persist", key= "search_keyword_button"):
    statechange(PROMPT_STATE, "search_keyword_modifier", research_router, True)

draft_email = st.text_area("Add additional instructions for the draft email function", st.session_state.draft_email_modifier, height=200)
if st.button("Persist", key= "draft_email_button"):
    statechange(PROMPT_STATE, "draft_email_modifier", draft_email, True)