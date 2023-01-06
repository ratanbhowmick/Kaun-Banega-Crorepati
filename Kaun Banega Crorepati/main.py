questions = [
    ["Which language was used to create facebook?",
        "Python", "C++", "Java", "Php", "None", 4],

    ["Which company built Burj Khalifa in Dubai?",
        "Samsung", "L&T", "LG", "AVL", "None", 1],

    ["Which language was used to create facebook?",
     "Python", "C++", "Java", "Php", "None", 4],

    ["Which language was used to create facebook?",
     "Python", "C++", "Java", "Php", "None", 4],

    ["Which language was used to create facebook?",
     "Python", "C++", "Java", "Php", "None", 4],

    ["Which language was used to create facebook?",
     "Python", "C++", "Java", "Php", "None", 4],

    ["Which language was used to create facebook?",
     "Python", "C++", "Java", "Php", "None", 4],

]

price = [0, 1000, 2000, 5000, 10000, 20000,
         30000, 50000, 100000, 200000, 1000000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {price[i+1]}")
    print(f"Q.{question[0]}")
    print(f"a. {question[1]} \tb. {question[2]}")
    print(f"c. {question[3]} \tc. {question[4]}")
    reply = int(input("Enter your answer (1-5) or 0 to quit : \n"))
    if (reply == 0):
        money = price[i]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won {price[i+1]}")

    else:
        print("Wrong answer!")

print(f"You take home money is {money}.")
