# importing regex and random libraries
import re, random, pyttsx3 
from datetime import datetime

class HazelBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

    def __init__(self):
        self.alienbabble = {'describe_creator_intent': r'.*\s*your creator.*',
                            'answer_why_intent': r'.*why.*are.*you.*',
                            'cubed_intent': r'.*cubed?.*(\d+)'
                                }
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices') 
        self.engine.setProperty('voice', self.voices[1].id)


  # Define .greet() below:
    def greet(self):
        print("It is currently {}".format(datetime.now().strftime("%H:%M")))
        self.engine.say("It is currently {}".format(datetime.now().strftime("%H:%M")))
   
        self.name = self.ask("What's your name?")
        will_help = self.ask("Hi {}, I\'m Etcetera. I\'m not from this planet. Will you help me learn about your planet?".format(self.name))
   
        if will_help in self.negative_responses:
            self.say("Ok, have a nice Earth day!")
            return
        self.chat()
            
    
    def ask(self, text):
        self.engine.say(text)
        print(text)
        self.engine.runAndWait() 
        reply = input(">")
        return reply
    
    def say(self, text):
        self.engine.say(text)
        print(text)
        self.engine.runAndWait() 
       

  # Define .make_exit() here:
    def make_exit(self, reply):
        for words in self.exit_commands:
            if words in reply:
                self.say("Ok, have a nice Earth day!")
                return True
            return False      

  # Define .chat() next:
    def chat(self):
        reply = self.ask(random.choice(self.random_questions)).lower()
        while not(self.make_exit(reply)):
            reply = self.ask(self.match_reply(reply))

  # Define .match_reply() below:
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent() 
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])
            else:
                return self.no_match_intent()
        

  # Define .describe_planet_intent():
    def describe_planet_intent(self):
        responses = ["My planet is a utopia of diverse organisms and species. ","I am from Opidipus, the capital of the Wayward Galaxies. "]
        return random.choice(responses)

  # Define .answer_why_intent():
    def answer_why_intent(self):
        responses = ["I come in peace."
    "I am here to collect data on your planet and its inhabitants."
    "I heard the coffee is good."]
        return random.choice(responses)
       
  # Define .cubed_intent():
    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number**3
        return "The cube of {} is {}. Isn't that cool?".format(number,cubed_number)

  # Define .no_match_intent():
    def no_match_intent(self):
        responses = ["Please tell me more.","Tell me more!","Why do you say that?","I see. Can you elaborate?","Interesting. Can you tell me more?", "I see. How do you think?","Why?","How do you think I feel when you say that?"]
        return random.choice(responses)

# Create an instance of AlienBot below:
Hazel = HazelBot()
Hazel.greet()
