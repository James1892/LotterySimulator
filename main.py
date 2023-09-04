import random
import locale

def getOrdinalSuffix(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return str(number) + suffix

def playersTicketNumbers():
    userNumbers = []
    usersLuckyStars = []
    count = 0
    while count < 5: # gets the user to add 5 numbers
        userInput = int(input(f"Enter the {getOrdinalSuffix(count + 1)} number for your ticket: "))
        userNumbers.append(userInput)  # Adds the numbers to the list
        count += 1

    count = 0
    while count < 2:
        userInput = int(input(f"Enter the {getOrdinalSuffix(count + 1)} Lucky Star for your ticket: "))
        usersLuckyStars.append(userInput)
        count+=1

    return userNumbers,usersLuckyStars

def generateResults():
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

    return numbers, luckyStars


def calculateWinnings(mathchedNumbers, matchedLuckystars):
    winnings = {
        # Uses the average winnings
        (2,0): 2.69,
        (2,1): 4.27,
        (1,2): 5.45,
        (3,0): 6.86,
        (3,1): 8.32,
        (2,2): 10.93,
        (4,0): 31.64,
        (3,2): 52.22,
        (4,1): 94.31,
        (4,2): 1482.66,
        (5,0): 26707.26,
        (5,1): 263915.79,
        (5,2): 58531809.53
    }
    if(mathchedNumbers, matchedLuckystars) in winnings:
        return winnings[(mathchedNumbers, matchedLuckystars)]
    else:
        return 0



def main():
    amountOfGames = int(input("How many games do you want to simulate? "))
    numTickets = amountOfGames  # The number of tickets you want to generate and check
    totalCost = numTickets * 2.50  # Calculate the total cost of the tickets
    wins = 0
    totalWinnings = 0
    jackpotCount = 0
    highestPayout = 0

    playersNumbers, playerLuckyStars = playersTicketNumbers() # Get the players ticket

    # Generate and check the numbers for each ticket
    for i in range(numTickets):
        randomNumbers, randomLuckyStars = generateResults()  # Generates the numbers for each game

        matchedNumbers = len(set(playersNumbers).intersection(randomNumbers))
        matchedLuckystars = len(set(playerLuckyStars).intersection(randomLuckyStars))

        winnings = calculateWinnings(matchedNumbers, matchedLuckystars)
        totalWinnings += winnings

        if (matchedNumbers, matchedLuckystars) == (5, 2):
            jackpotCount += 1

        if winnings > 0:
            wins += 1

        if winnings > highestPayout:
            highestPayout = winnings 

        # Determine the color based on whether the game is a winning game
        if winnings > 0:
            colourCode = "\033[32m"  # Green color for winning games
        else:
            colourCode = "\033[0m"   # Reset color to default

        print()
        print(f"{colourCode}Game Number: {i+1}")
        print("Player Balls:", ", ".join(map(str, playersNumbers)), "Lucky Stars:", ", ".join(map(str, playerLuckyStars)))
        print("Result Balls:", ", ".join(map(str, randomNumbers)), "Lucky Stars:", ", ".join(map(str, randomLuckyStars)))
        print(f"Winnings: £{winnings:.2f}")
        print("\033[0m")  # Reset colour after printing

    locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
    print("----------------------------------------------------------------")
    print("                          Results")
    print("----------------------------------------------------------------")

    print(f"Number of Games:                               {numTickets}")
    print(f"Total 5 numbers 2 luckyStars wins:             {jackpotCount}")
    print(f"Number of wins:                                {wins}")
    print(f"Highest payout:                                {locale.currency(highestPayout)}")
    print(f"Total Cost of tickets:                         {locale.currency(totalCost)}")
    print(f"Total winnings:                                {locale.currency(totalWinnings)}")
    print(f"Cost/winnings offset:                          {locale.currency(totalWinnings - totalCost)}")

main()
