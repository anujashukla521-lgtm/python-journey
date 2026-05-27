# A Harry Potter themed KBC-style quiz game built in Python using lists, dictionaries, loops, and conditional statements.


questions = [
    {
        "question" : "What's the name of the dog guarding the Sorcerer's Stone?",
        "options" : [
            "A. Fang",
            "B. Fluffy",
            "C. Hedwig",
            "D. Scabbers"
        ],
        "answer" : "B",
        "money" : 5000
    },
    {
        "question" : "Who is Harry Potter's best friend?",
        "options" :[
            "A. Cedric",
            "B. Ron",
            "C. Draco",
            "D. Malfoy"
        ],
        "answer": "B",
        "money" : 10000
    },
    {
        "question" : "How do Harry and the Weasleys travel to the Quidditch World Cup?",
        "options" : [
            "A. Floo Powder",
            "B. Port Key",
            "C. Broomsticks",
            "D. Magical Car"
        ],
        "answer": "B",
        "money" : 15000
    },
    {
        "question" : "While visiting the Dursley's, what do Fred and George leave on the floor for Dudley to find?",
        "options" : [
            "A. A large spider",
            "B. Dr Filibuster's Fabulous Wet-Start, No-Heat Fireworks",
            "C. An Acid Pop",
            "D. A Ton-Tongue Toffee"
        ],
        "answer": "D",
        "money" : 20000
    },
    {
        "question" : "Who is the new Defense Against the Dark Arts teacher in Harry's 4th year at Hogwarts??",
        "options" : [
            "A. Dolores Umbridge",
            "B. Lupin",
            "C. Mad-Eye Moody",
            "D. Gilderoy Lockhart"
        ],
        "answer": "C",
        "money" : 25000
    },
    {
        "question" : "Why can't Harry enter the Triwizard Tournament?",
        "options" : [
            "A. He isn't the best wizard in the school to represent Hogwarts",
            "B. He is under the age of seventeen",
            "C. He has broken too many rules at Hogwarts",
            "D. Dumbledore asked him not to"
        ],
        "answer": "B",
        "money" : 50000
    },
    {
        "question" : "What creature does Mad Eye Moody turn Malfoy into?",
        "options" : [
            "A. A brown slug",
            "B. A white ferret",
            "C. A black spider",
            "D. A green toad"
        ],
        "answer": "B",
        "money" : 100000
    },
    {
        "question" : "How does Harry Potter get past the Hungarian Horntail?",
        "options" : [
            "A. He blinds the dragon with the Conjunctivitis Curse",
            "B. He uses a bubble charm",
            "C. He summons his Firebolt",
            "D. He says 'accio egg!'"
        ],
        "answer": "C",
        "money" : 200000
    },
    {
        "question" : "Who does Harry go with to the Yule Ball?",
        "options" : [
            "A. Hermione Granger",
            "B. Parvati Patil",
            "C. Padma Patil",
            "D. Fleur Delacour"
        ],
        "answer" : "B",
        "money" : 300000
    },
    {
        "question"  : "Who helps Harry figure out the how to solve the golden egg?",
        "options" : [
            "A. Cedric Diggory",
            "B. Moaning Myrtle",
            "C. Rubeus Hagrid",
            "D. Both Cedric and Myrtle"
        
        ],
        "answer" : "D",
        "money" : 500000
    },
    {
        "question" : "What does Harry see in Dumbledore’s pensive while waiting alone in his office?",
        "options" : [
            "A. A vision of his parents at school",
            "B. Dumbledore's last memory of his family",
            "C. Dumbledore talking to Riddle as a child",
            "D. Trials of various witches and wizards"
        ],
        "answer" : "D",
        "money" : 750000
    },
    {
        "question" : "Who ultimately gives Harry the idea to use Gillyweed to breathe underwater?",
        "options" : [
            "A. Neville Longbottom",
            "B. Ronald Weasley",
            "C. Cedric Diggory",
            "D. Professor Sprout"
        ],
        "answer" : "A",
        "money" : 1250000
    },
    {
        "question" : "What does SPEW stand for?",
        "options" : [
            "A. The Society for the Protection of Everything Wizard",
            "B. Students Protecting Elves Wellbeing",
            "C. The Society for the Promotion of Elfish Welfare",
            "D. Students Promoting Equality for Wizards",
        
        ],
        "answer"  : "C",
        "money" : 5000000
    },
    {
        "question" : "Which reporter shows up to write articles about the progression of the Triwizard Tournament?",
        "options" : [
            "A. Barnabas Cuffe",
            "B. Xenophilius Lovegood",
            "C. Henry Shaw Senior",
            "D. Rita Skeeter"
        ],
        "answer" : "D",
        "money" : 10000000
    },
    {
        "question" : "Who was impersonating Mad-Eye Moody throughout the Goblet of Fire?",
        "options" : [
            "A. Peter Pettigrew",
            "B. Barty Crouch Jr.",
            "C. Voldemort",
            "D. Lucius Malfoy"
        ],
        "answer" : "B",
        "money" : 450000000
    },
    {
        "question" : "How does Voldemort summon Harry to the graveyard?",
        "options" : [
            "A. A Summoning spell",
            "B. Floo powder",
            "C. A port key",
            "D. The Accio spell"
        ],
        "answer" : "C",
        "money" : 550000000
    },
    {
        "question" : "What does Wormtail sacrifice in the graveyard to revive Lord Voldemort?",
        "options" : [
            "A. His sister",
            "B. His most loved possession",
            "C. His hand",
            "D. His power"

        ],
        "answer" : "C",
        "money" : 70000000
    },
    {
        "question" : "Why does a house elf visit Harry Potter at the beginning of The Chamber of Secrets?",
        "options" : [
            "A. Because his master sent him to get Harry Potter in trouble",
            "B. To meet the famous Harry Potter",
            "C. To warn him not to return to Hogwarts",
            "D. To expose Harry's magical powers to the Dursleys"
        ],
        "answer" : "C",
        "money" : 80000000
    },
    {
        "question" : "What method of transportation did Harry Potter use to travel to London to get his school supplies in his second year?",
        "options" :[
            "A. A flying car",
            "B. The Floo Network",
            "C. The Hogwarts Express",
            "D. His broomstick"
        ],
        "answer" : "B",
        "money" : 90000000
    },
    {
        "question" : "Why did Harry Potter not receive any letters from his friends over the summer?",
        "options"  :[
            "A. The Dursley’s wouldn’t give them to Harry",
            "B. His friends didn't send him any",
            "C. A house elf was intercepting them",
            "D. Students at Hogwarts aren't allowed to receive letters during the summer"
        ],
        "answer" : "C",
        "money" : 100000000
    }
]
total_money = 0
safe_point = 0
print("===== KBC Harry Potter Edition =====")
print("Answer correctly to win money!\n")
for ques in questions:
    print(ques["question"])
    print("Question for Rs.", ques["money"])
    for option in ques["options"]:
        print(option)

    user_input = input("Choose option: (A/B/C/D): ").upper()
    if user_input == ques["answer"]:
        print("You won Rs.", ques["money"])
        total_money = ques["money"]
        if ques["money"] in [25000, 500000, 5000000]:
            safe_point = ques["money"]
    else:
        print("Wrong answer")
        for option in ques["options"]:
            if option.startswith(ques["answer"]):
                print("Correct answer was:", option)
                print("You take home Rs.", safe_point)
                break

print("Final winnings:", total_money)
    