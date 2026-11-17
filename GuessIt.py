import random

numbers = list(range(1, 501))

secret_number = random.choice(numbers)


count = 0
while True: 
    count += 1  
    try: 
        answer = int(input("Guess the number: "))
    except ValueError:
        print("Invalid input, please enter a whole number between 1 and 500")
        continue
    if answer < 1 or answer > 500:
        print("your guess must be between 1 and 500 please")  
        continue 

    diff = abs(answer - secret_number)

    if answer < secret_number and diff >= 10:
        print("incorrect! your guess is too low")
    elif answer < secret_number and diff < 10:
        print("incorrect! your guess is low")    
    elif answer > secret_number and diff >= 10:
        print("incorrect! your guess is too high")
    elif answer > secret_number and diff < 10:
        print("incorrect! your guess is high")
    else:
        print("correct! you have guessed the correct number")
        print(f"it took you {count} tries to get it right")
        break


    