def calculateHighestBreakWithRemainingBalls(balls_left):
    return calculateHighestBreakExcludingLastSixBalls(balls_left) + calculateLastSixBalls(6)


def calculateLastSixBalls(balls):
    sum = 0
    for ball in range(7, 7 - balls, -1):
        sum += ball
    return sum


def calculateHighestBreakExcludingLastSixBalls(balls):
    sum = 0
    for ball in range(0, balls - 6):
        sum += 8
    return sum


def calculateBreak(b):
    t = 0
    for x in range(7, 7 - b, -1):
        t += x
    b -= 6
    for x in range(0, b):
        t += 8
    return t


print(calculateHighestBreakWithRemainingBalls(21))
