import streamlit as st
from csagents import INITIAL_STATE
from helper import *

st.markdown("# Instructions for Agents")

left_column, right_column, blank_column = st.columns(3)

# Select box for agent creation
# Currently Categorizer is the only one that works
category_selectbox_options = ["", "Categorizer", "Researcher"]

# Max number of categories allowed in the categorizer
max_categories = 10

# Hard coding of default categories for when you open up the Categorizer settings
categorizer_description = json.load(open("categories_description.txt"))

categorizer_instruction = json.load(open("categories_instruction.txt"))

# Set up a list in session_state for the agent categories
if "agent_descriptions_keys" not in st.session_state:
    temp = list(categorizer_description.keys())
    if len(temp) > max_categories:
        print("Your input dictionary is too long")
    else:
        if len(temp) < max_categories:
            temp = listlengthtomax(temp,max_categories)
        st.session_state.agent_descriptions_keys = temp

# Set up a list in session_state for the agent categories
if "agent_descriptions_values" not in st.session_state:
    temp = list(categorizer_description.values())
    if len(temp) > max_categories:
        print("Your input dictionary is too long")
    else:
        if len(temp) < max_categories:
            temp = listlengthtomax(temp,max_categories)
        st.session_state.agent_descriptions_values = temp

# Set up a list in session_state for the agent instructions
if "agent_instructions_values" not in st.session_state:
    temp = list(categorizer_instruction.values())
    if len(temp) > max_categories:
        print("Your input dictionary is too long")
    else:
        if len(temp) < max_categories:
            temp = listlengthtomax(temp,max_categories)
        st.session_state.agent_instructions_values = temp

# Set up a number for the Descriptions Needed
if "categorizer_num" not in st.session_state:
    st.session_state.categorizer_num = len(categorizer_description)

# Set up a way to have "Base Category" selectbox remember which choice was selected
if "agent_selectbox_index" not in st.session_state:
    st.session_state.agent_selectbox_index = 0

with left_column:
    # Create Base Category selectbox, and save it to session_state
    base_option = st.selectbox(label="Base Category", options=category_selectbox_options, index = st.session_state.agent_selectbox_index)
    st.session_state.agent_selectbox_index = category_selectbox_options.index(base_option)

# Code for Categorizer information
if(base_option == "Categorizer"):
    state_len = len(categorizer_description)
    # Number of categories needed
    with right_column:
        num_descriptions = st.number_input(label="Descriptions Needed", min_value = 1, max_value = max_categories, value=st.session_state.categorizer_num)
        st.session_state.categorizer_num = num_descriptions
    left, mid, right = st.columns([.2,.4,.4])
    st.write("""Built-in categories:\n
             'possible_adversarial_attack' - used if the response may be a malicious attack may try manipulating the use of AI
             'off_topic' - when it does not relate to any of the other categories
             """)
    # Titles for the two parts of the categories
    with left:
        st.write("Category Name")
    with mid:
        st.write("Description")
    with right:
        st.write("Instructions")
    # Creates as many Categories and Descriptions as dictated from the Descriptions Needed number input
    for i in range(num_descriptions):
        with left:
            label = "Category" + str(i)
            keys_value = ""
            if i < state_len:
                keys_value = st.session_state.agent_descriptions_keys[i]
            keys_holder = st.text_area(label=label, label_visibility="hidden", height = 15, value = st.session_state.agent_descriptions_keys[i])
            st.session_state.agent_descriptions_keys[i] = keys_holder
        with mid:
            label = "Description" + str(i)
            values_value = ""
            if i < state_len:
                values_value = st.session_state.agent_descriptions_values[i]
            values_holder = st.text_area(label = label, label_visibility="hidden", height=15, value = st.session_state.agent_descriptions_values[i])
            st.session_state.agent_descriptions_values[i] = values_holder
        with right:
            label = "Instruction" + str(i)
            values_value = ""
            if i < state_len:
                values_value = st.session_state.agent_instructions_values[i]
            values_holder = st.text_area(label = label, label_visibility="hidden", height=15, value = st.session_state.agent_instructions_values[i])
            st.session_state.agent_instructions_values[i] = values_holder
    # Save Button
    with left:
        if st.button("Save"):
            result_description = dict(zip(st.session_state.agent_descriptions_keys, st.session_state.agent_descriptions_values))
            result_instruction = dict(zip(st.session_state.agent_descriptions_keys, st.session_state.agent_instructions_values))
            # Removes and empty spaces that can be created from the lists
            if '' in result_description:
                del result_description['']
            if '' in result_instruction:
                del result_instruction['']
            print(result_description)
            print(result_instruction)
            # Currently needed, until CSAGENTS gets updated. A restart of the program is needed for the saved info to be used
            json.dump(result_description, open("categories_description.txt", 'w'))
            json.dump(result_instruction, open("categories_instruction.txt", 'w'))
            statechange(INITIAL_STATE,"agent_descriptions",result_description,True)
            statechange(INITIAL_STATE,"agent_instructions",result_instruction,True)
