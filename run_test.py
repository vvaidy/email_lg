# Based on Sam Witteveen's YT Video: https://youtu.be/lvQ96Ssesfk?si=FPy8LSaDxacijl7e
# Sam Witteveen's github is: @samwit
# Sam's Colab Notebook:
# https://colab.research.google.com/drive/1WemHvycYcoNTDr33w7p2HL3FF72Nj88i?usp=sharing#scrollTo=jJhoLxciS906

import os
from csagents import run_responder, INITIAL_STATE


INITIAL_STATE["customer_email"] = """
Hi There,

I had a wonderful time at your resort last week. The only glitch was that I had
a poor experience at the front desk with the lady there, I think her name
was Eleanor Rigby. If you like, you could check with Father MacKenzie who witnessed
the entire incident.

Other than that I had a wonderful time although I have to say that the rain did
put quite a damper on things. When would you consider a better time for me to visit?
I like to follow the sun!

Paul
"""

print("=====================")
print("  Running the agent  ")
print("=====================")

# pprint(INITIAL_STATE)

# for output in email_responder_app.stream(INITIAL_STATE):
#     for key, value in output.items():
#         print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
#         pprint(f"Finished running: {key}:")
#         print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#         # pprint(f"Obtained value: {value}")

response = run_responder()
print(f"\nFinal output:\n{response}")