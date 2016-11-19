# nlg.py
import random

class NLG(object):
    def acknowledge(self):

        simple_acknoledgement = [
            "Yes?",
            "What can I do for you?",
            "How can I help?",
            "How can I help you Today?",
            "Hi, what can I do for you?"
            "Hey, what can I do for you?"
        ]
            ret_phrase = random.choice(simple_acknoledgement)
            
            return ret_phrase
