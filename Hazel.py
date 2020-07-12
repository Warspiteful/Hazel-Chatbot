# importing regex and random libraries
import re, random
from datetime import datetime


class HazelBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "How's it going? ",
        "What're you up to? ",
        "Anything interesting happen lately? ",
        "Want to talk about something? ",
        "What's up? ",
    )

    def __init__(self):
        self.alienbabble = {'describe_creator_intent': r'.*your creator.*',
                            'answer_why_intent': r'.*why.*are.*you.*',
                            'cubed_intent': r'.*cubed?.*(\d+)'
                                }
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices') 
        self.engine.setProperty('rate', self.engine.getProperty('rate')+5)
        self.engine.setProperty('voice', self.voices[1].id)
        self.textFile =  open(r"testText.txt","a")
       

  # Define .greet() below:
    def greet(self):
        self.textFile.write("\n")
        self.say("It is currently {}".format(datetime.now().strftime("%H:%M")))
   
        self.name = self.ask("Heya! It's nice to meet you. What's your name?")
        will_help = self.ask("Hi {}, I\'m Hazel, a friendly chat bot! I'm slowly getting worked on. Could you spend some time with me?".format(self.name))
   
        if will_help in self.negative_responses:
            self.say("Ok, bye!")
            self.textFile.close() 
            return
        self.chat()
            
    
    def ask(self, text):
        self.engine.say(text)
        print(text)
        self.textFile.write("\n")
        self.textFile.write(text)
        self.engine.runAndWait() 
        reply = input(">")
        self.textFile.write("\n")
        self.textFile.write(">" + reply)
        return reply
    
    def say(self, text):
        self.engine.say(text)
        print(text)
        self.textFile.write("\n")
        self.textFile.write(text)
        self.engine.runAndWait() 
       

  # Define .make_exit() here:
    def make_exit(self, reply):
        for words in self.exit_commands:
            if words in reply:
                return True        
            return False      

  # Define .chat() next:
    def chat(self):
        return random.choice(self.random_questions)
        #while not(self.make_exit(reply)):
         #   reply = self.ask(self.match_reply(reply))

  # Define .match_reply() below:
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_creator_intent':
                return self.describe_creator_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent() 
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])

        return self.no_match_intent()
        
   
  # Define .describe_planet_intent():
    def describe_creator_intent(self):
        responses = ["I'm a chatbot written up by a student for practice","My creator? I'm not really sure to be honest."]
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

