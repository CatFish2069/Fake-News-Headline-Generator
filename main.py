import os
import random
from datetime import datetime

# Define categories and related word banks
word_bank = {
    "Politics": {
        "subjects": [
            "PM Modi",
            "Amit Shah",
            "Rahul Gandhi",
            "Baba Ramdev",
            "Election Commission",
        ],
        "actions": [
            "declares war on",
            "bans",
            "throws chappals at",
            "meditates with",
            "celebrates victory with",
        ],
        "places": [
            "in Lok Sabha",
            "on Rajpath",
            "near Rashtrapati Bhavan",
            "on top of Parliament",
            "inside RBI office",
        ],
    },
    "Bollywood": {
        "subjects": [
            "SRK",
            "Salman Khan",
            "Alia Bhatt",
            "Ranveer Singh",
            "Karan Johar",
        ],
        "actions": [
            "dances with",
            "argues with",
            "launches movie with",
            "eats biryani with",
            "cries for",
        ],
        "places": [
            "at Film City",
            "in Bandra",
            "on Instagram Live",
            "in Koffee with Karan",
            "on a red carpet",
        ],
    },
    "Sports": {
        "subjects": [
            "Virat Kohli",
            "MS Dhoni",
            "Neeraj Chopra",
            "Sania Mirza",
            "KL Rahul",
        ],
        "actions": [
            "throws bat at",
            "dances with",
            "eats protein shake with",
            "wins against",
            "gets run out by",
        ],
        "places": [
            "in Wankhede Stadium",
            "at IPL auction",
            "during practice",
            "on commentary",
            "in a wrestling ring",
        ],
    },
    "Food": {
        "subjects": [
            "A Pani Puri Wala",
            "Zomato Guy",
            "A hungry uncle",
            "Baba Ramdev",
            "A Vada Pav",
        ],
        "actions": [
            "jumps into",
            "declares love for",
            "starts fight over",
            "sings to",
            "runs away from",
        ],
        "places": [
            "a biryani plate",
            "at Haldiram's",
            "inside a samosa",
            "on Swiggy",
            "with a dosa in hand",
        ],
    },
}

reporters = [
    "Arnab Goswami",
    "Ravish Kumar",
    "A Random YouTuber",
    "Aj Tak Insider",
    "Your Neighbor",
]
sources = [
    "FakeTimes",
    "News9",
    "ZeeGullible",
    "India Troll News",
    "Whatsapp University",
]
emojis = ["😂", "🔥", "😱", "💥", "🚨", "🤣", "🤯", "🥴"]


def generate_headline(category):
    subject = random.choice(word_bank[category]["subjects"])
    action = random.choice(word_bank[category]["actions"])
    place = random.choice(word_bank[category]["places"])
    emoji = random.choice(emojis)
    reporter = random.choice(reporters)
    source = random.choice(sources)
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    headline = f"[{timestamp}] BREAKING: {subject} {action} {place}! {emoji}\nReported by {reporter} | Source: {source}"
    return headline


# Save headlines to a file
def save_headline_to_file(headline):
    with open("fake_headlines.txt", "a", encoding="utf-8") as file:
        file.write(headline + "\n\n")


# Program loop
while True:
    print("\n📢 Choose a category:")
    for idx, cat in enumerate(word_bank.keys(), start=1):
        print(f"{idx}. {cat}")
    choice = input("Enter the number of your choice (or 'q' to quit): ").strip().lower()

    if choice == "q":
        print("👋 Thanks for using Fake News Generator. Stay fake, stay fun!")
        break

    try:
        choice = int(choice)
        category = list(word_bank.keys())[choice - 1]
    except:
        print("❌ Invalid input. Try again.")
        continue

    headline = generate_headline(category)
    print("\n📰", headline)
    save_headline_to_file(headline)

    again = input("\nGenerate another? (y/n): ").strip().lower()
    if again != "y":
        print("👍 Exiting now. Headlines saved in 'fake_headlines.txt'")
        print("📂 Opening file in Notepad...")
        os.system("notepad fake_headlines.txt")
        break
