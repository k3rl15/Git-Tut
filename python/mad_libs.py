import random
import sys

football_libs = {
    "Noun1": "",
    "Noun2": "",
    "Adjective1": "",
    "Adjective2": "",
    "Verb": "",
    "Name": "",
    "Team": "",
    "Title": ""
}

horror_libs = {
    "Noun1": "",
    "Noun2": "",
    "Adjective1": "",
    "Adjective2": "",
    "Adjective3": "",
    "Adjective4": "",
    "Verb1": "",
    "Verb2": "",
    "Name": "",
    "Number": "",
    "Past Tense Verb": ""
}

fantasy_libs = {
    "Noun1": "",
    "Noun2": "",
    "Noun3": "",
    "Adjective1": "",
    "Adjective2": "",
    "Adjective3": "",
    "Adjective4": "",
    "Verb1": "",
    "Verb2": "",
    "Verb3": "",
    "Name": "",
    "Number": "",
    "Adverb": ""

}


def main():
    selected_story = random.choice([football_libs, horror_libs, fantasy_libs])

    print("Give me a couple words, let's see if we can make a spectacular story.")
    for key in selected_story:
        selected_story[key] = input(f"{key}: ")

    story = stories(selected_story)
    print(story)
    sys.exit()


def stories(libs):
    story = ""
    if libs == football_libs:
        story = f"Meet {libs['Name']}, the {libs['Adjective1']} football superstar. " \
                f"Their {libs['Noun1']} dribbling and {libs['Adjective2']} shots have made \n" \
                f"them a {libs['Title']} in the world of football. They've played for " \
                f"{libs['Team']} and led them to numerous {libs['Adjective1']} \n" \
                f"victories. Their {libs['Noun1']} is known for its {libs['Adjective2']} " \
                f"accuracy, and fans from around the world {libs['Verb']} to see them in action."

    elif libs == horror_libs:
        story = f"In a {libs['Adjective1']} room, there hung a {libs['Adjective2']} mirror. " \
                f"Legend has it that the mirror was {libs['Adjective3']} and \n" \
                f"{libs['Adjective4']}, hiding {libs['Noun1']} within its depths. On a " \
                f"{libs['Adjective2']} night, {libs['Name']} decided to {libs['Verb1']} \n" \
                f"the mirror. As they gazed into it, they were {libs['Past Tense Verb']} to see a " \
                f"{libs['Adjective3']} {libs['Noun2']}. The mirror {libs['Verb2']}, and {libs['Adjective1']} \n" \
                f"whispers filled the room. In terror, {libs['Name']} {libs['Verb1']} the " \
                f"mirror, breaking it into {libs['Number']} {libs['Adjective4']} pieces."

    elif libs == fantasy_libs:
        story = f"In a {libs['Adjective1']} forest, {libs['Name']} stumbled upon a " \
                f"{libs['Noun1']}. As they {libs['Verb2']} deeper into the forest, \n" \
                f"they encountered {libs['Number']} {libs['Adjective4']} " \
                f"{libs['Noun3']} that {libs['Verb1']} and {libs['Verb3']}. " \
                f"Along the way, they met \na {libs['Adjective2']} {libs['Noun3']} who " \
                f"offered {libs['Noun1']} and {libs['Name']} advice. " \
                f"{libs['Name']} finally reached the {libs['Noun3']} and \ndiscovered " \
                f"a {libs['Adjective3']} {libs['Noun1']} that granted them the power to " \
                f"{libs['Verb1']} {libs['Adverb']}. With \ntheir newfound power, " \
                f"{libs['Name']} {libs['Verb3']} the forest, leaving it forever " \
                f"{libs['Adjective4']}."

    return story


if __name__ == "__main__":
    main()
