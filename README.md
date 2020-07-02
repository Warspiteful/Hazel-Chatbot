# Hazel
A python chatbot with a visual GUI using `tkinter` and `re` Libraries.

## Regular Expression Intents
Cubing - Find the cube of a number.
```python
'cubed_intent': r'.*cubed?.*(\d+)' 
```
Answer Why - Answers why this Chatbot is running.
```python
'answer_why_intent': r'.*why.*are.*you.*'
```
Describe Creator - Describes creator and intent.
```python
'describe_creator_intent': r'.*your creator.*'
```

## Classes
`HazelBot` - Does RegEx Recognition. \
`HazelGUI` - Handles Introduction and GUI.

