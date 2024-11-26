# helper.py is intended to have useful imports and functions that need to be used in multiple other files

# used to save and get the categories while staying as a dict
import json

initial_state_keys = ["model", "customer_email", "organizational_settings", "research_info", "agent_instructions", "agent_descriptions", "num_steps", "responder_signature", "polite_wait"]

prompt_state_keys = ["research_router_instructions", "search_keyword_modifier", "draft_email_modifier"]

# used in Agent Instructions if the dict is not up to the max_categories to make it that long. It gets shortened when saving with json 
def listlengthtomax(list, length):
    templist = list
    listlen = length - len(templist)
    for i in range(listlen):
        templist.append("")
    return templist

def statechange(state, key, value, persist):
    state.update({key: value})
    if persist:
        if key in prompt_state_keys:
            json.dump(state, open("promptstate.json", 'w'))
        elif key in initial_state_keys:
            json.dump(state, open("initialstate.json", 'w'))

def description_to_string(dict):
    keys = list(dict.keys())
    values = list(dict.values())
    string = ""
    for i in range(len(keys)):
        string += keys[i] + " - " + values[i] + "\n"
    return string

def instruction_to_string(dict):
    keys = list(dict.keys())
    values = list(dict.values())
    string = ""
    for i in range(len(keys)):
        string += "If the customer email is '" + keys[i] + "' " + values[i] + "\n"
    string += "\n"
    return string

def remove_space(dict):
    del dict['']