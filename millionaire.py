print('''Welcome to Do You Want To Become a Millionaire, Python version!
Answer all questions correctly to win 1,000,000 USD!
''')

prize = 1000000
correct_answers = 0

print('''Question 1: What's the prediominant language spoken on Aruba?

a) Spanish
b) Papiamento
c) Portuguese
d) Dutch \n''')
answer = input("Your answer: ")
correct_answer = "b"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 2: Which of these countries does NOT border Poland?

a) Belarus
b) Czech Republic
c) Austria
d) Lithuania \n''')
answer = input("Your answer: ")
correct_answer = "c"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 3: What is the nationality of film director Julia Durcoumau?

a) Dutch
b) Belgian
c) Algerian
d) French \n''')
answer = input("Your answer: ")
correct_answer = "d"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 4: In which year was William Shakespeare born?

a) 1544
b) 1554
c) 1564
d) 1664 \n''')
answer = input("Your answer: ")
correct_answer = "c"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 5: In which year was Python first released?

a) 1991
b) 1990
c) 1995
d) 1999 \n''')
answer = input("Your answer: ")
correct_answer = "a"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 6: Who created the South Korean series "Squid Game" (2021)?

a) Hwang Dong-hyuk
b) Hwang Jung-hyuk
c) Hwang Sung-hyuk
d) Hwang Joo-hyuk\n''')
answer = input("Your answer: ")
correct_answer = "a"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")   

print('''Question 7: What is the largest animal known to have ever existed?

a) Beluga
b) Sperm whale
c) Killer whale
d) Blue whale \n''')
answer = input("Your answer: ")
correct_answer = "d"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = 10000
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 8: In which year was Bitcoin invented?

a) 2007
b) 2008
c) 2009
d) 2010 \n''')
answer = input("Your answer: ")
correct_answer = "b"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 9: What is the official currency of Ecuador?

a) Ecuadorian Peso
b) Sol
c) Balboa
d) US Dollar \n''')
answer = input("Your answer: ")
correct_answer = "d"
if answer == correct_answer:
    print("Correct! Next question \n")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}. You can still win {prize_display} USD \n")

print('''Question 10: What is the literal meaning of the Japanese word "karaoke"?

a) Empty voice
b) Only orchestra
c) Enpty orchestra
d) Only voice \n''')
answer = input("Your answer: ")
correct_answer = "c"
if answer == correct_answer:
    print("\nCorrect!")
    correct_answers += 1
else:
    prize = prize // 2
    prize_display = "{:,}".format(prize)
    print(f"Incorrect. The correct answer was {correct_answer}.\n")

if correct_answers == 10:
    print("CONGRATULATIONS! You have become a Millionaire! Your knowledge is really admirable")
elif 0 < correct_answers < 10:
    print(f"Congratulations! You have won {prize_display} USD")
else:
    print("You've lost the game. Better luck next time!")