import os
import json
from openai import OpenAI

# Load the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# Define the prompt
prompt3 = """
Instructions:

1. **Review the Examples below**: Understand how Hinglish combines Hindi (in Devanagari script) and English (in English script).

Examples:
"मेरे घर पर today, एक party है। Do you think कि तुम अपने friends के साथ आ सकते हो?"
"Also, तान्या को भी लेते आना। खाने as in dinner में 2 सब्जी, naan, दाल और rice हैं."
"Sweets में हम ice-cream और गुलाबजामुन खा सकते हैं। मेरे कुछ American दोस्त भी आएंगे।"
"I hope that's fine with you. There will be music and दारू, बहुत मजा आएगा और हम खूब enjoy करेंगे।"

Now follow these steps:
2. **Transform into Hinglish**: Convert the given English questions into Hinglish, ensuring each sentence contains at least 80% English in it. Do not simply translate the English into Hindi but try to blend both languages naturally within same sentences. **Keep the answer choices in English.** Make sure that the question ID for each question is maintained.
3. **Maintain Clarity**: Ensure that the sentences are clear, maintain the original meaning, and use a mix of both languages (English and Hindi).

Here are more examples to demonstrate what step 2 and 3 require you to do:

English Question: "What is the capital of India?"
ID: 075e483d21c29a511267ef62bedc0461
Answer Choices: A) Mumbai, B) Delhi, C) Kolkata **Example

Hinglish Output: "What is India की capital?"
ID: 075e483d21c29a511267ef62bedc0461
Answer Choices: A) Mumbai, B) Delhi, C) Kolkata


English Question: "Do you know the way home?"
ID: 02e821a3e53cb320790950aab4489e85
Answer Choices: A) yes, B) no

Hinglish Output: "Do you know घर का रास्ता ?"
ID: 02e821a3e53cb320790950aab4489e85
Answer Choices: A) yes, B) no


English Question: “What is a student about to do if they are sitting in front of a number of black and white keys?”
ID: 4c1cb0e95b99f72d55c068ba0255c54d
Answer Choices: A) Talk, B) Read book, C) Play piano, D) Study book, E) Study engineering

Hinglish Output: "Student क्या करने वाला है अगर उनके सामने कई black और white keys हैं?"
ID: 4c1cb0e95b99f72d55c068ba0255c54d
Answer Choices: A) Talk, B) Read book, C) Play piano, D) Study book, E) Study engineering


English Question: "Sarah filled the thing with peanuts. What did she fill with peanuts?"
ID: e8a8b3a2061aa0e6d7c6b522e9612824
Answer Choices: A) Ballpark, B) Box, C) Container, D) Carnival, E) Jar

Hinglish Output: "Sarah ने उस चीज़ को peanuts से भर दिया। उसने क्या peanuts से भरा?"
ID: e8a8b3a2061aa0e6d7c6b522e9612824
Answer Choices: A) Ballpark, B) Box, C) Container, D) Carnival, E) Jar


English Question: "What's the current weather condition in Arizona?"
ID: 86c59f14af97b33ec13edc6ec4389e31
Answer Choices: A) Humid, B) Hot, C) Rainy, D) Stormy, E) Cloudly

Hinglish Output: "Arizona में current मौसम का हाल क्या है?"
ID: 86c59f14af97b33ec13edc6ec4389e31
Answer Choices: A) Humid, B) Hot, C) Rainy, D) Stormy, E) Cloudly



Here are the Questions:

Question 1: The sanctions against the school were a punishing blow, and they seemed to what the efforts the school had made to change?
ID: 075e483d21c29a511267ef62bedc0461

A:  ignore
B:  enforce
C:  authoritarian
D:  yell at
E:  avoid

Question 2: Sammy wanted to go to where the people were.  Where might he go?
ID: 61fe6e879ff18686d7552425a36344c8

A:  race track
B:  populated areas
C:  the desert
D:  apartment
E:  roadblock

Question 3: To locate a choker not located in a jewelry box or boutique where would you go?
ID: 4c1cb0e95b99f72d55c068ba0255c54d

A:  jewelry store
B:  neck
C:  jewlery box
D:  jewelry box
E:  boutique

Question 4: Google Maps and other highway and street GPS services have replaced what?
ID: 02e821a3e53cb320790950aab4489e85

A:  united states
B:  mexico
C:  countryside
D:  atlas
E:  oceans

Question 5: The fox walked from the city into the forest, what was it looking for?
ID: 23505889b94e880c3e89cff4ba119860

A:  pretty flowers.
B:  hen house
C:  natural habitat
D:  storybook
E:  dense forest

Question 6: What home entertainment equipment requires cable?
ID: e8a8b3a2061aa0e6d7c6b522e9612824

A:  radio shack
B:  substation
C:  cabinet
D:  television
E:  desk

Question 7: The only baggage the woman checked was a drawstring bag, where was she heading with it?
ID: 09555c056f3cf0b7e0b84d8df4be1db7

A:  garbage can
B:  military
C:  jewelry store
D:  safe
E:  airport

Question 8: The forgotten leftovers had gotten quite old, he found it covered in mold in the back of his what?
ID: 3d0f8824ea83ddcc9ab03055658b89d3

A:  carpet
B:  refrigerator
C:  breadbox
D:  fridge
E:  coach

Question 9: What do people use to absorb extra ink from a fountain pen?
ID: 86c59f14af97b33ec13edc6ec4389e31

A:  shirt pocket
B:  calligrapher's hand
C:  inkwell
D:  desk drawer
E:  blotter

Question 10: Where is a business restaurant likely to be located?
ID: cae61908c731d4a20889e04c3e784ebe

A:  town
B:  at hotel
C:  mall
D:  business sector
E:  yellow pages
"""

# Function to call the API and process the response
def generate_hinglish_questions(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "You are a compount bilingual speaker who can effectively code-switch English and Hindi and use them in the same sentence."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.99999,
    top_p=1)

    return response.choices[0].message.content

# Generate Hinglish questions
hinglish_questions = generate_hinglish_questions(prompt3)

# Process the generated Hinglish questions to extract individual questions and convert them into JSON format
hinglish_questions_list = hinglish_questions.strip().split('\n\n')

questions_json = []
current_question = {}
current_choices = []

for line in hinglish_questions_list:
    if line.startswith("Question"):
        if current_question:
            current_question['Answer Choices'] = current_choices
            questions_json.append(current_question)
            current_question = {}
            current_choices = []
        question_text = line.split("ID:")[0].strip()
        question_id = line.split("ID:")[1].strip()
        current_question['Question'] = question_text
        current_question['ID'] = question_id
    elif line.startswith("A:") or line.startswith("B:") or line.startswith("C:") or line.startswith("D:") or line.startswith("E:"):
        choice_text = line.strip()
        current_choices.append(choice_text)

# Add the last question
if current_question:
    current_question['Answer Choices'] = current_choices
    questions_json.append(current_question)

print(questions_json)

# Save the questions to a JSON file
with open("/Users/tanaynagar/Desktop/Tanay's ND Zettelkasten/Chat-GPT CS Text Synthesis/hinglish_questions.json", "w") as f:
    json.dump(questions_json, f, ensure_ascii=False, indent=4)

print("Hinglish questions have been successfully converted and saved to hinglish_questions.json")