from random import choice, randint
from string import ascii_lowercase as a_l

bots = ["".join(choice(a_l + " ") for _ in range(19)) for _ in range(200)]

target = "dragon ball z"

gen = 0

best_bot = bots[0]

while best_bot != target:
    gen += 1

    best_bot = bots[0]
    best_score = 0
    second_best = bots[0]
    second_score = 0

    for bot in bots:
        score = 0
        
        for i in range(13):
            if bot[i] == target[i]:
                score += 1

        if score > best_score:
            second_best = best_bot
            best_bot = bot
            second_score = best_score
            best_score = score
        elif score > second_score:
            second_best = bot
            second_score = score

    for num, bot in enumerate(bots):
        bot = ""
        for i in range(13):
            bot = bot + (choice([best_bot[i], second_best[i]]))
            bots[num] = bot

    for num, bot in enumerate(bots):
        for i in range(13):
            mutate = randint(1, 8)

            if mutate == 1:
                bot = bot[:i] + choice(a_l + " ") + bot[i+1:]
                bots[num] = bot

    print("Gen -", gen, "|", "Score -", str(best_score) + "/13")
    print(best_bot)
    print(target)
    print("")