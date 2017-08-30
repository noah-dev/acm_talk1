# Eightball Program - Ask a question, get answer
import random

input("Ask a question: ")

choice = random.randint(1,6)
if choice == 1:
    print("Absolutely")
elif choice == 2:
    print("You can rely on it")
elif choice == 3:
    print("Be careful")
else:
    print("Ask Again")