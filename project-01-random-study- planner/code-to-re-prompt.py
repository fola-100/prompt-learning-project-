import random

# A dictionary of study categories and possible tasks
study_tasks = {
    "python": [
        "Practice list comprehensions",
        "Build a small function",
        "Read about classes and objects",
        "Write a script that uses files"
    ],
    "math": [
        "Solve 5 algebra problems",
        "Review trigonometry basics",
        "Practice mental arithmetic",
        "Study coordinate geometry"
    ],
    "science": [
        "Read an article on physics",
        "Watch a biology explanation video",
        "Study the periodic table",
        "Research how solar panels work"
    ]
}

def pick_random_task(category):
    """Return a random study task from a category."""
    if category not in study_tasks:
        return None
    return random.choice(study_tasks[category])

print("Available categories: python, math, science")

user_choice = input("Choose a category to study: ").strip().lower()

selected_task = pick_random_task(user_choice)

if selected_task is None:
    print("That category doesn't exist. Please try again.")
else:
    print(f"Your study task for today: {selected_task}")
