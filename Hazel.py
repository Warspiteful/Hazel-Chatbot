import re
import random

class HazelBot:
  negative_responses = ("nothing", "don't", "stop", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  def __init__(self):
    self.matching_phrases = {'say_name':[r'.*what.*(is)?.*your*.name.*\?',r'.*who.*are.*you\?.*']}

  def welcome(self):
    self.name = input("Hi, I'm Hazel, your friendly chatbot! I'm a work-in-progess, but I'll do my best! First, let me ask: what is your first name and last name? ")
    
    will_help = input(f"Ok, {self.name}, it's nice to meet you! What can I help you with? ")
    
    if will_help in self.negative_responses:
      print("Ok, have a great day!")
      return
    
    self.handle_conversation(will_help)
  
  def handle_conversation(self, reply):
    while not self.make_exit(reply):
      reply = self.match_reply(reply)
      
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a great day!")
        return True
      
    return False
  
  def match_reply(self, reply):
    for key, values in self.matching_phrases.items():
      for regex_pattern in values:
        found_match = re.match(regex_pattern, reply.lower())
        if found_match and key == 'say_name':
            return self.say_name()
        
    return input("I did not understand you. Can you please ask your question again?")
  
 
  def say_name(self):
      return input("Hi, my name is Hazel! Anything else I can help you with?")

 
  
# Create a SupportBot instance
Hazel = HazelBot()
# Call the .welcome() method
Hazel.welcome()