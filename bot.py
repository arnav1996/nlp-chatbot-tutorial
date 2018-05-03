##
# This module is the interface with the humans. It takes in English language,
# decides which module should deal with this, and reurns the response back in English Language
# Integrations with Slack, Messenger, SMS or anything else can be done here
##
from job_search import *

while True:
    message = raw_input(">> ")
    if message == "stop":
        break
    if message == "thanks":
        print "Sure"
    else:
        print(handle_message(message))