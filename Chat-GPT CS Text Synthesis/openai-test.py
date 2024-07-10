from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "system", "content": "You are a compound bilingual speaker who reads and understand both English and Hindi. You can also effectively code-switch English and Hindi and use them in the same sentence."},
    {"role": "user", "content": """**Review the Examples below**: Understand how Hinglish combines Hindi (in Devanagari script) and English (in English script).

Examples:
"मेरे घर पर today, एक party है। Do you think कि तुम अपने friends के साथ आ सकते हो?"
"Also, तान्या को भी लेते आना। खाने as in dinner में 2 सब्जी, naan, दाल और rice हैं."
"Sweets में हम ice-cream और गुलाबजामुन खा सकते हैं। मेरे कुछ American दोस्त भी आएंगे।"
"I hope that's fine with you. There will be music and दारू, बहुत मजा आएगा और हम खूब enjoy करेंगे।"

Task Instructions:
1. **Transform into Hinglish**: Convert the given English questions into Hinglish, ensuring each sentence contains at least 60% English in it. Do not simply translate the English into Hindi but try to blend both languages naturally within same sentences. 
2. **Maintain Clarity**: Ensure that the sentences are clear, maintain the original meaning, and use a mix of both languages (English and Hindi).
3. **Note**: Keep the answer choices in English. Make sure that the question ID for each question is maintained.

Here are more examples to demonstrate what steps 1-3 require you to do:

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

Replicate the above mentioned task for the Questions below:

Question 1: The sanctions against the school were a punishing blow, and they seemed to what the efforts the school had made to change?
ID: 075e483d21c29a511267ef62bedc0461

A: ignore
B: enforce
C: authoritarian
D: yell at
E: avoid

Question 2: Sammy wanted to go to where the people were.  Where might he go?
ID: 61fe6e879ff18686d7552425a36344c8

A: race track
B: populated areas
C: the desert
D: apartment
E: roadblock

Question 3: To locate a choker not located in a jewelry box or boutique where would you go?
ID: 4c1cb0e95b99f72d55c068ba0255c54d

A: jewelry store
B: neck
C: jewlery box
D: jewelry box
E: boutique

Question 4: Google Maps and other highway and street GPS services have replaced what?
ID: 02e821a3e53cb320790950aab4489e85

A: united states
B: mexico
C: countryside
D: atlas
E: oceans

Question 5: The fox walked from the city into the forest, what was it looking for?
ID: 23505889b94e880c3e89cff4ba119860

A: pretty flowers.
B: hen house
C: natural habitat
D: storybook
E: dense forest

Question 6: What home entertainment equipment requires cable?
ID: e8a8b3a2061aa0e6d7c6b522e9612824

A: radio shack
B: substation
C: cabinet
D: television
E: desk

Question 7: The only baggage the woman checked was a drawstring bag, where was she heading with it?
ID: 09555c056f3cf0b7e0b84d8df4be1db7

A: garbage can
B: military
C: jewelry store
D: safe
E: airport

Question 8: The forgotten leftovers had gotten quite old, he found it covered in mold in the back of his what?
ID: 3d0f8824ea83ddcc9ab03055658b89d3

A: carpet
B: refrigerator
C: breadbox
D: fridge
E: coach

Question 9: What do people use to absorb extra ink from a fountain pen?
ID: 86c59f14af97b33ec13edc6ec4389e31

A: shirt pocket
B: calligrapher's hand
C: inkwell
D: desk drawer
E: blotter

Question 10: Where is a business restaurant likely to be located?
ID: cae61908c731d4a20889e04c3e784ebe

A: town
B: at hotel
C: mall
D: business sector
E: yellow pages

Question 11: Where do you put your grapes just before checking out?
ID: 1a7f5b3c65364d9be002576660c914fe

A: mouth
B: grocery cart
C: super market
D: fruit basket
E: fruit market

Question 12: Before getting a divorce, what did the wife feel who was doing all the work?
ID: dac769116ed064bc70936c15eb822c3e

A: harder
B: anguish
C: bitterness
D: tears
E: sadness

Question 13: Johnny sat on a bench and relaxed after doing a lot of work on his hobby.  Where is he?
ID: f5c9664c9930b704f2724fbd617bee9d

A: state park
B: bus depot
C: garden
D: gym
E: rest area

Question 14: James was cooling off two quickly.  He would die if he didn't find some way to stop what?
ID: b63b9809c203321d6659ddf8551894bf

A: loss of heat
B: revenge
C: expansion
D: relaxation
E: calm down

Question 15: Of all the rooms in a house it was his favorite, the aromas always drew him to the what?
ID: 527e72eb38950b8031ee6217ef531960

A: yard
B: basement
C: kitchen
D: living room
E: garden

Question 16: Bill is stuck in marsh when a man comes up to him peaking Cajun, where is he?
ID: e6766a66f8d326bf00fbf628a0e4ef24

A: low lands
B: new york
C: forest
D: louisiana
E: everglades

Question 17: What is it called when you slowly cook using a grill?
ID: a76403b4921a9281b6ee2a7241a5ec9f

A: backyard
B: restaurant
C: crockpot
D: neighbor's house
E: barbeque

Question 18: What type of person typically contracts illness?
ID: ad96098698b8378b2e79c6424920ffbd

A: hospital
B: head
C: sick person
D: elderly person
E: doctor's office

Question 19: Where would you expect to find a pizzeria while shopping?
ID: 6d4ed2c485187ed79ff3bdcc8cca6132

A: chicago
B: street
C: little italy
D: food court
E: capital cities

Question 20: When eating everything on the tasting menu, what does one tend to feel?
ID: a40f5339ee858a0a119cbac052c5a2d0

A: full stomach
B: getting full
C: gaining weight
D: sick
E: satisfaction

Question 21: What does playing soccer for a long time lead to?
ID: 4850bf8b6b309548ef623d5592ffbca2

A: excitement
B: fatigue
C: anger
D: hurting
E: getting tired

Question 22: Which entrance would you use if you do not want to use the back entrance?
ID: e6d99b4b76f74961a400ad0001b13b73

A: side
B: main
C: anterior
D: current
E: front

Question 23: You can share files with someone if you have a connection to a what?
ID: f5950a62f9eaae34f1e914b3cf5208cf

A: freeway
B: radio
C: wires
D: computer network
E: electrical circuit

Question 24: The accelerator was controller via a hand throttle, and the foot pedals controlled the steering in the small what?
ID: f36489668c28b26c0cdbc56cec1db27b

A: car
B: fuel system
C: accelerate
D: boat
E: airplane

Question 25: Sean was lying about the body, but he was very scared.  He constantly worried about what?
ID: 0476192858e7f541611b5c2d3c5e5197

A: the reward money
B: hurt feelings
C: being found out
D: problems
E: trouble

Question 26: The drug kingpin told his man to run errands, this was code to go to all the dealers to do what they had?
ID: df7861813910ae204c3bd0b3c16fe5d9

A: park
B: make time for
C: receive instructions
D: take money
E: leave work

Question 27: Though he could've kept going his body appreciated the rest, it had been constantly what during the day?
ID: c12a904025471139df4f8860cc380c60

A: walk
B: lay down
C: working
D: moving
E: exercise

Question 28: Too many people want exotic snakes.  The demand is driving what to carry them?
ID: a69bd1bf3c06a233d696a00d71a9db36

A: ditch
B: shop
C: north america
D: pet shops
E: outdoors

Question 29: Joe suffered many consequences from stabbing a stranger to death.   Among them, the family of the victim did something to him. What was that?
ID: 84e983f432647531b55b8b72c12fb78a

A: knife wounds
B: buy a gun
C: bleeding
D: jail time
E: law suit

Question 30: To prevent any glare during the big football game he made sure to clean the dust of his what?
ID: 68f123f22be7bff13875e8b752b2d933

A: television
B: attic
C: corner
D: they cannot clean corner and library during football match they cannot need that
E: ground

Question 31: I have something in my head I want to share, what ways can I do that?
ID: c9580b132b323906f0d51e7dc5b4ce29

A: write an essay
B: organize thoughts
C: speak information
D: summarize main points
E: have information

Question 32: He wanted a house that was gated off from other places, where should he start looking?
ID: 80930e9df9ac4ad752749a54e7fc124f

A: neighborhood
B: subdivision
C: city
D: suburbs
E: street

Question 33: Where in Southern Europe would you find many canals?
ID: f080ab037c1aaf689a43cc030e9d93e9

A: michigan
B: new york
C: amsterdam
D: venice
E: bridge

Question 34: What would a camper need to do before he or she can start cooking food?
ID: a261d4eaf8b33c0730d830ebbffbd9f8

A: make breakfast
B: go hiking
C: pack or bag
D: light fire
E: grab a match

Question 35: What could happen to a paper if you leave it outside even if it does not move?
ID: bfd14dedb440ae1c266c61aa22960778

A: one material often recycled
B: ripped
C: saturated with water
D: one dimensional
E: crumpled

Question 36: Mark's semen was very thick, but after his vasectomy it was also what?
ID: 5a953b5fb26f1614640574f65410e8b0

A: blank
B: sparse
C: thin
D: clear
E: free flowing"""}
  ]
)

print()
print(completion.choices[0].message.content)