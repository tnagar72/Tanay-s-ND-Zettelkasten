import os
from openai import OpenAI

# Load the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# # Define the prompt
# prompt = """
# Instructions:

# 1. **Review the Examples**: Understand how Hinglish combines Hindi (in Devanagari script) and English (in English script).
# 2. **Transform into Hinglish**: Convert the given English questions into Hinglish, ensuring each sentence contains at least 50% English. Blend both languages naturally within sentences. Keep the answer choices in English.
# 3. **Maintain Clarity**: Ensure the sentences are clear, maintain the original meaning, and use a mix of both languages.

# ### Examples:

# **Example Input**:

# English Question: "What is the capital of India?"
# Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

# **Example Hinglish Output**: "What is India की capital?"
# Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

# **Additional Hinglish Examples**:
# - "Look कितना beautiful this place है!"
# - "All boys खेल के लिए ready हैं."
# - "Are you बिलकुल भी serious नहीं हैं?"

# ### Questions:

# 1. John looked for beavers but couldn't find any, because he lived where?
# A: America
# B: Australia
# C: Countryside
# D: Dictionary
# E: Woodlands

# 2. Committing the murder wore on the man, because of his what he swore he could still hear the man's heart beating?
# A: Great sorrow
# B: Stethoscope
# C: Guilty conscience
# D: Find God
# E: Go to jail

# 3. When do girls eat ice cream on the couch?
# A: Wash hands
# B: Were hungry
# C: Depressed
# D: Athlete's foot
# E: Cool down

# 4. When you want to eat lunch, you need to have what for it?
# A: Eat food
# B: Shopping for food
# C: Prepare food
# D: Find food
# E: Have time for

# 5. If you sit back and think about nice memories you will be able to?
# A: Sit quietly
# B: Concentrate
# C: Wake up
# D: Stay focused
# E: Relax

# 6. Where is a ballpoint pen best stored?
# A: Pocket
# B: Stationery store
# C: Backpack
# D: Desk drawer
# E: Bank

# 7. Sarah filled the thing with peanuts. What did she fill with peanuts?
# A: Ballpark
# B: Box
# C: Container
# D: Carnival
# E: Jar

# 8. Where would a restaurant put a candle?
# A: Dimly lit room
# B: Kitchen
# C: Wall
# D: Table
# E: Birthday cake

# 9. What is a student about to do if they are sitting in front of a number of black and white keys?
# A: Talk
# B: Read book
# C: Play piano
# D: Study book
# E: Study engineering

# 10. Where could you go on top of a superhighway?
# A: City
# B: Rural area
# C: Cyberspace
# D: Computer network
# E: Industrialized country
# """

# prompt1 = """
# I am providing you with English statements or questions along with their answer choices. Additionally, I will provide examples of code-switched sentences in Hinglish (a mix of Hindi and English) that incorporate Hindi words in Devanagari script and English words in English script. Your task is to transform the given English statements into similar code-switched Hinglish sentences, ensuring a balanced mix of Hindi and English phrases and words in each sentence, following the style and script requirements of the examples provided.

# ### Instructions:

# 1. **Understand the Context and Style**: Review the English statements/questions along with the code-switched examples to fully grasp the context, linguistic style, and script requirements. Code-switching refers to the practice of alternating between two languages within a single conversation or sentence. Notice how the provided examples use English predominantly, while seamlessly integrating Hindi phrases or words within the same sentence.
    
# 2. **Transform into Balanced Hinglish**: Convert the English statements into Hinglish, aiming for a blend where each sentence is primarily in English, with approximately 65% English and 35% Hindi components. Use Devanagari script for the Hindi components and retain the English script for English words. Ensure a smooth and natural integration of Hindi within the English sentences.
    
# 3. **Maintain Clarity and Accuracy**: While code-switching and using different scripts for Hindi and English components, ensure the sentences remain clear, grammatically coherent, and true to the norms of Hinglish. Preserve the original meaning and intent of the English statements.
    
# 4. **Check for Consistency**: Ensure that the style, level of code-switching, and script usage are consistent across all transformed sentences, reflecting the balanced style demonstrated in the examples provided.
    

# ### Example Input:

# **English Statement:** "What is the capital of India?" **Answer Choices:** A) Mumbai, B) Delhi, C) Kolkata

# **Example of Code-switched Sentence:** "India की राजधानी क्या है?"

# ### Additional Example Hinglish Code-switched Sentences:

# - "Look कितना beautiful यह place है!"
# - "All boys खेल के लिए तैयार हो रहे हैं."
# - "Are you बिलकुल भी serious नहीं हैं?"

# ### Task:

# Using the above instructions and examples, please convert the following English questions into Hinglish sentences. Ensure that the answers for each question stay in English and the questions themselves are transformed into code-switched Hinglish.

# ### Questions:

# 1. John looked for beavers but couldn't find any, because he lived where?
# A: America
# B: Australia
# C: Countryside
# D: Dictionary
# E: Woodlands

# 2. Committing the murder wore on the man, because of his what he swore he could still hear the man's heart beating?
# A: Great sorrow
# B: Stethoscope
# C: Guilty conscience
# D: Find God
# E: Go to jail

# 3. When do girls eat ice cream on the couch?
# A: Wash hands
# B: Were hungry
# C: Depressed
# D: Athlete's foot
# E: Cool down

# 4. When you want to eat lunch, you need to have what for it?
# A: Eat food
# B: Shopping for food
# C: Prepare food
# D: Find food
# E: Have time for

# 5. If you sit back and think about nice memories you will be able to?
# A: Sit quietly
# B: Concentrate
# C: Wake up
# D: Stay focused
# E: Relax

# 6. Where is a ballpoint pen best stored?
# A: Pocket
# B: Stationery store
# C: Backpack
# D: Desk drawer
# E: Bank

# 7. Sarah filled the thing with peanuts. What did she fill with peanuts?
# A: Ballpark
# B: Box
# C: Container
# D: Carnival
# E: Jar

# 8. Where would a restaurant put a candle?
# A: Dimly lit room
# B: Kitchen
# C: Wall
# D: Table
# E: Birthday cake

# 9. What is a student about to do if they are sitting in front of a number of black and white keys?
# A: Talk
# B: Read book
# C: Play piano
# D: Study book
# E: Study engineering

# 10. Where could you go on top of a superhighway?
# A: City
# B: Rural area
# C: Cyberspace
# D: Computer network
# E: Industrialized country

# """

# prompt2 = """
# Instructions:

# 1. **Review the Examples below**: Understand how Hinglish combines Hindi (in Devanagari script) and English (in English script).

# ### Examples:

# "मेरे घर पर today, एक party है। Do you think कि तुम अपने friends के साथ आ सकते हो?" 
# "Also, तान्या को भी लेते आना। खाने as in dinner में 2 सब्जी, naan, दाल और rice हैं." 
# "Sweets में हम ice-cream और गुलाबजामुन खा सकते हैं। मेरे कुछ American दोस्त भी आएंगे।"
# "I hope that's fine with you. There will be music and दारू, बहुत मजा आएगा और हम खूब enjoy करेंगे।"

# Now follow these steps:

# 2. **Transform into Hinglish**: Convert the given English questions into Hinglish, ensuring each sentence contains at least 50% English in it. Blend both languages naturally within sentences. Keep the answer choices in English.

# 3. **Maintain Clarity**: Ensure that the sentences are clear, maintain the original meaning, and use a mix of both languages.

# ### Here are more examples to demostrate what steps 2 and 3 require you to do:

# English Question: "What is the capital of India?"
# Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

# **Example Hinglish Output**: "What is India की capital?"
# Answer Choices: A) Mumbai, B) Delhi, C) Kolkata

# English Question: "Do you know the way home?"
# Answer Choices: A) yes, B) no

# **Example Hinglish Output**: "Do you know घर का रास्ता?"
# Answer Choices: A) yes, B) no

# ### Here are the Questions:

# 1. John looked for beavers but couldn't find any, because he lived where?
# A: America
# B: Australia
# C: Countryside
# D: Dictionary
# E: Woodlands

# 2. Committing the murder wore on the man, because of his what he swore he could still hear the man's heart beating?
# A: Great sorrow
# B: Stethoscope
# C: Guilty conscience
# D: Find God
# E: Go to jail

# 3. When do girls eat ice cream on the couch?
# A: Wash hands
# B: Were hungry
# C: Depressed
# D: Athlete's foot
# E: Cool down

# 4. When you want to eat lunch, you need to have what for it?
# A: Eat food
# B: Shopping for food
# C: Prepare food
# D: Find food
# E: Have time for

# 5. If you sit back and think about nice memories you will be able to?
# A: Sit quietly
# B: Concentrate
# C: Wake up
# D: Stay focused
# E: Relax

# 6. Where is a ballpoint pen best stored?
# A: Pocket
# B: Stationery store
# C: Backpack
# D: Desk drawer
# E: Bank

# 7. Sarah filled the thing with peanuts. What did she fill with peanuts?
# A: Ballpark
# B: Box
# C: Container
# D: Carnival
# E: Jar

# 8. Where would a restaurant put a candle?
# A: Dimly lit room
# B: Kitchen
# C: Wall
# D: Table
# E: Birthday cake

# 9. What is a student about to do if they are sitting in front of a number of black and white keys?
# A: Talk
# B: Read book
# C: Play piano
# D: Study book
# E: Study engineering

# 10. Where could you go on top of a superhighway?
# A: City
# B: Rural area
# C: Cyberspace
# D: Computer network
# E: Industrialized country
# """

# prompt3 = """
# Instructions:

# 1. **Review the Examples below**: Understand how Hinglish combines Hindi (in Devanagari script) and English (in English script).

# ### Examples:

# अपुन ने बहुत drink किया हुआ था
#  अपुन बहुत नशा किया हुआ था

# brother हमसे जितना बन पड़ रहा है कर रहे हैं
# हमसे जितना बन पड़ रहा है brother, हम कर रहे हैं

# तेरे से कौन बात कर रहा है यह तो तेरे relatives है
# who is speaking to you तेरे तो सगे वाले है यह

# joints में pain है ना
# joints में दर्द है ना

# Now follow the next two steps:

# 2. **Transform into Hinglish**: Convert the given English questions into Hinglish, ensuring each sentence contains at least 50% English. Blend both languages naturally within sentences. Keep the answer choices in English.
# 3. **Maintain Clarity**: Ensure the sentences are clear, maintain the original meaning, and use a mix of both languages.

# ### Here are the Questions:

# 1. John looked for beavers but couldn't find any, because he lived where?
# A: America
# B: Australia
# C: Countryside
# D: Dictionary
# E: Woodlands

# 2. Committing the murder wore on the man, because of his what he swore he could still hear the man's heart beating?
# A: Great sorrow
# B: Stethoscope
# C: Guilty conscience
# D: Find God
# E: Go to jail

# 3. When do girls eat ice cream on the couch?
# A: Wash hands
# B: Were hungry
# C: Depressed
# D: Athlete's foot
# E: Cool down

# 4. When you want to eat lunch, you need to have what for it?
# A: Eat food
# B: Shopping for food
# C: Prepare food
# D: Find food
# E: Have time for

# 5. If you sit back and think about nice memories you will be able to?
# A: Sit quietly
# B: Concentrate
# C: Wake up
# D: Stay focused
# E: Relax

# 6. Where is a ballpoint pen best stored?
# A: Pocket
# B: Stationery store
# C: Backpack
# D: Desk drawer
# E: Bank

# 7. Sarah filled the thing with peanuts. What did she fill with peanuts?
# A: Ballpark
# B: Box
# C: Container
# D: Carnival
# E: Jar

# 8. Where would a restaurant put a candle?
# A: Dimly lit room
# B: Kitchen
# C: Wall
# D: Table
# E: Birthday cake

# 9. What is a student about to do if they are sitting in front of a number of black and white keys?
# A: Talk
# B: Read book
# C: Play piano
# D: Study book
# E: Study engineering

# 10. Where could you go on top of a superhighway?
# A: City
# B: Rural area
# C: Cyberspace
# D: Computer network
# E: Industrialized country
# """

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
    # max_tokens=1000, 
    top_p=1)

    return response.choices[0].message.content

# Generate Hinglish questions
hinglish_questions = generate_hinglish_questions(prompt3)

# Save the questions to a text file
with open("hinglish_questions.txt", "w", encoding='utf-8') as f:
    f.write(hinglish_questions)

print("Hinglish questions have been successfully converted and saved to hinglish_questions.txt")