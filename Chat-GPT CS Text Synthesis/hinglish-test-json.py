import os
import json
from openai import OpenAI

# Load the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# Define the prompt
prompt = """
Instructions:

1. **Review the Examples**: Understand how Hinglish combines Hindi (in Devanagari script) and English (in English script).
2. **Transform into Hinglish**: Convert the given English questions into Hinglish, ensuring each sentence contains at least 50% English. Blend both languages naturally within sentences. Keep the answer choices in English. Make sure to return the output in json format, preserving the id I give you for each question
3. **Maintain Clarity**: Ensure the sentences are clear, maintain the original meaning, and use a mix of both languages.

### Examples:

**Example Input**:

English Question: "What is the capital of India?"
Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

**Example Hinglish Output**: "What is India की capital?"
Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

**Additional Hinglish Examples**:
- "Look कितना beautiful this place है!"
- "All boys खेल के लिए ready हैं."
- "Are you बिलकुल भी serious नहीं हैं?"

### Questions:

1. John looked for beavers but couldn't find any, because he lived where?
A: America
B: Australia
C: Countryside
D: Dictionary
E: Woodlands

2. Committing the murder wore on the man, because of his what he swore he could still hear the man's heart beating?
A: Great sorrow
B: Stethoscope
C: Guilty conscience
D: Find God
E: Go to jail

3. When do girls eat ice cream on the couch?
A: Wash hands
B: Were hungry
C: Depressed
D: Athlete's foot
E: Cool down

4. When you want to eat lunch, you need to have what for it?
A: Eat food
B: Shopping for food
C: Prepare food
D: Find food
E: Have time for

5. If you sit back and think about nice memories you will be able to?
A: Sit quietly
B: Concentrate
C: Wake up
D: Stay focused
E: Relax

6. Where is a ballpoint pen best stored?
A: Pocket
B: Stationery store
C: Backpack
D: Desk drawer
E: Bank

7. Sarah filled the thing with peanuts. What did she fill with peanuts?
A: Ballpark
B: Box
C: Container
D: Carnival
E: Jar

8. Where would a restaurant put a candle?
A: Dimly lit room
B: Kitchen
C: Wall
D: Table
E: Birthday cake

9. What is a student about to do if they are sitting in front of a number of black and white keys?
A: Talk
B: Read book
C: Play piano
D: Study book
E: Study engineering

10. Where could you go on top of a superhighway?
A: City
B: Rural area
C: Cyberspace
D: Computer network
E: Industrialized country
"""

# Function to call the API and process the response
def generate_hinglish_questions(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are an expert in code-switching and multilingual text generation."},
        {"role": "user", "content": prompt}
    ],
    temperature=1)

    return response.choices[0].message.content

# Generate Hinglish questions
hinglish_questions = generate_hinglish_questions(prompt)

print(hinglish_questions)

# Parse the generated Hinglish questions and convert to JSON format
def parse_hinglish_questions(text):
    questions = []
    lines = text.strip().split('\n')
    current_question = None

    for line in lines:
        if line.strip() == '':
            continue
        if line[0].isdigit():
            if current_question:
                questions.append(current_question)
            parts = line.split('. ', 1)
            current_question = {
                'question': parts[1].strip(),
                'options': {}
            }
        elif line[0].isalpha() and line[1] == ':':
            option_label = line[0]
            option_text = line[3:].strip()
            current_question['options'][option_label] = option_text

    if current_question:
        questions.append(current_question)

    return questions

parsed_questions = parse_hinglish_questions(hinglish_questions)

# Save the parsed questions to a JSON file
json_data = {"hinglish_questions": parsed_questions}

with open("hinglish_questions.json", "w", encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("Hinglish questions have been successfully converted to JSON and saved to hinglish_questions.json")