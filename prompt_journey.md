MY ATTEMPTS 
first prompt:
You are my coding assistance i want to generate some python code for a project
i am working on i will send you prompt for what i want to generate and you will give me the
output in code. do you understand the task ?

second prompt:
import a python module name random

Third prompt:
now create a dictionary , which is the called available subject and inside available subject the
create a key called python, math, sciences, for the value python should contain a list of subject
that are a value to study e.g practice list comprehensions, build a small function e.tc make it only
5 for math, also create a list and inside the list of 5 math topic e.g solve 5 algebra problems, review
trigonometry basics make and for the science perform the same operation

Fourth prompt:
create a function called selecting topic and inside the augment call it category then create a condition
that check if category is inside available subject and a nested loop under that that returns random.
Choice from the available subject base on what is inside category

fifth prompt:
and a else condition that return none

sixth prompt:
then in another line outside of the def function create a print statement that says
Available categories: python, math, science then the next line create a variable called user input where the
user enter is input with a word that says choose a category to study and a function .strip() and .lower()
and the the next line create a variable called select task inside the variable call the function we
created before and add user input in the argument

seventh prompt:
now in the next line write a condition that tell the check if not selected task it should print
("that category doen't exist. pls try again) else print f string that say your study task for 
today and the selected task

PROMPT TUTOR CORRECTION/IMPROVEMENT 
You don’t need to say “now create this, now create that” every time.
One prompt can contain multiple steps if they belong together.

You also don’t need the first prompt (asking the AI if it understands).
Just give the instructions directly.

Improved Version of Your Whole Prompt
Create a Python program with this structure:
1. Import `random`.
2. Create a dictionary named `available_subject` with keys: "python", "math", "science".
   Each key should map to a list of 5 study topics.
3.Write a function `selecting_topic(category)`:
      - If the category exists in the dictionary, return a random topic.
      - Otherwise return None.
4, Print the available categories.
5. Ask the user for a category using input(), convert it to lowercase and strip spaces.
6. Call the function and store the result.
7. If result is None, print an error. Else print the chosen topic.
Do not copy any existing structure. Use your own coding style.
