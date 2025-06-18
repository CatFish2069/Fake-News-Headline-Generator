import random

# Step 1: Lists of Subjects, Actions, and Places/Objects
subjects = [
    "SRK",
    "Salman Khan",
    "PM Modi",
    "A Cow",
    "Amit Shah",
    "Virat Kohli",
    "A Random Uncle",
    "Deepika Padukone",
    "Ranveer Singh",
    "A Rickshaw Driver",
    "Alia Bhatt",
    "A School Kid",
    "An Auto",
    "Baba Ramdev",
]

actions = [
    "dances on",
    "declares war against",
    "eats",
    "argues with",
    "meditates on",
    "sings to",
    "runs away from",
    "bans",
    "rides",
    "faints at the sight of",
    "throws chappals at",
    "launches new app with",
    "paints",
    "arrests",
]

places_objects = [
    "a buffalo near India Gate",
    "a pani puri stall",
    "on Mars",
    "in a Mumbai local train",
    "at a wedding baraat",
    "with a tandoori chicken",
    "on top of Qutub Minar",
    "at Marine Drive",
    "inside a coconut tree",
    "on a PUBG livestream",
    "in a Delhi traffic jam",
    "at Gateway of India",
    "with a dosa",
    "in a Lonavala resort",
]

# Step 2: Loop to keep generating headlines
while True:
    # Pick random elements
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_object = random.choice(places_objects)

    # Format and print headline
    headline = f"BREAKING: {subject} {action} {place_object}!"
    print("\n📰", headline)

    # Ask user if they want another headline
    another = input("\nWant another fake headline? (yes/no): ").strip().lower()
    if another != "y":
        print("👋 Exiting... Stay fake, stay fun!")
        break
