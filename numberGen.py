import random

def main():
    numbers = []
    while len(numbers) < 5:
        newNumber = random.randrange(1,51)
        if newNumber not in numbers:
            numbers.append(newNumber)

    luckyStars = []
    while len(luckyStars) < 2:
        newLuckStar = random.randrange(1,12)
        if newLuckStar not in luckyStars:
            luckyStars.append(newLuckStar)

    print(numbers, luckyStars)

main()