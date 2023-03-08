import random
user = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors:")
computer = random.choice(['r', 'p', 's'])

if user =='r' and computer == 's':
    print("Comuter seleceted scissors and you won!!")
elif user =='p' and computer == 'r':
    print("Computer selected rock and you won!")
elif user == 's' and computer == 'p':
    print("Computer selected paper and you won!")
elif user == 'r' and computer == 'r':
    print("Its a tie!")
elif user == 's' and computer == 's':
    print("Its a tie!")
elif user == 's' and computer == 's':
    print("Its a tie!")
else:
    print(f"computer selected {computer} and you lost!")
