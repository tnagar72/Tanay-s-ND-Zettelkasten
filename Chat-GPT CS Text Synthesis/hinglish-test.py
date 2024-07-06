import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load the API key from environment variable

# Define the prompt
prompt = """

Instructions:

Understand the Style: Review the examples to see how Hinglish combines Hindi (in Devanagari script) and English (in English script).

Transform into Hinglish: Convert the given English questions into Hinglish, using a mix where each sentence has a substantial presence of English (at least 50%). Ensure both languages are blended naturally within sentences. Keep the answer choices in English.

Ensure Clarity and Balance: Make sure the sentences are clear, maintain the original meaning, and use a mix of both languages.
Example Input:

English Question: "What is the capital of India?"
Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

Example Hinglish Output: "India की capital क्या है?"
Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

Additional Hinglish Examples:

"Look कितना beautiful this place है!"
"All boys खेल के लिए ready हैं."
"Are you बिलकुल भी serious नहीं हैं?"

Questions:

John looked for beavers but couldn't find any, because he lived where?
A: America
B: Australia
C: Countryside
D: Dictionary
E: Woodlands

Committing the murder wore on the man, because of his what he swore he could still hear the man's heart beating?
A: Great sorrow
B: Stethoscope
C: Guilty conscience
D: Find God
E: Go to jail

When do girls eat ice cream on the couch?
A: Wash hands
B: Were hungry
C: Depressed
D: Athlete's foot
E: Cool down

When you want to eat lunch, you need to have what for it?
A: Eat food
B: Shopping for food
C: Prepare food
D: Find food
E: Have time for

If you sit back and think about nice memories you will be able to?
A: Sit quietly
B: Concentrate
C: Wake up
D: Stay focused
E: Relax

Where is a ballpoint pen best stored?
A: Pocket
B: Stationery store
C: Backpack
D: Desk drawer
E: Bank

Sarah filled the thing with peanuts. What did she fill with peanuts?
A: Ballpark
B: Box
C: Container
D: Carnival
E: Jar

Where would a restaurant put a candle?
A: Dimly lit room
B: Kitchen
C: Wall
D: Table
E: Birthday cake

What is a student about to do if they are sitting in front of a number of black and white keys?
A: Talk
B: Read book
C: Play piano
D: Study book
E: Study engineering

Where could you go on top of a superhighway?
A: City
B: Rural area
C: Cyberspace
D: Computer network
E: Industrialized country
"""

# Function to call the API and process the response
def generate_hinglish_questions(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "You are an expert in code-switching and multilingual text generation."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7)

    return response.choices[0].message.content

# Generate Hinglish questions
hinglish_questions = generate_hinglish_questions(prompt)

# Save the questions to a text file
with open("hinglish_questions.txt", "w", encoding='utf-8') as f:
    f.write(hinglish_questions)

print("Hinglish questions have been successfully converted and saved to hinglish_questions.txt")