import random

# Lists of words to generate random operation names
verbs = ["Arrest", "Capture", "Secure", "Apprehend", "Detain", "Contain"]
adjectives = ["Rapid", "Stealth", "Covert", "Surprise", "Swift", "Invisible"]
nouns = ["Justice", "Operation", "Force", "Intervention", "Response", "Task"]

def generate_operation_name():
    """Generate a random operation name."""
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {verb} {noun}"

def main():
    print("Welcome to the Law Enforcement Operation Name Generator!")
    print("Generating a random operation name:")
    operation_name = generate_operation_name()
    print(operation_name)

if __name__ == "__main__":
    main()
