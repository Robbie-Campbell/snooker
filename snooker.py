def calculateHighestBreakWithRemainingBalls(balls_left):
    if balls_left <= 6:
        return calculateLastSixBalls(balls_left)
    return calculateHighestBreakExcludingLastSixBalls(balls_left) + calculateLastSixBalls(6)


def calculateLastSixBalls(balls):
    sum = 0
    for ball in range(7, 7 - balls, -1):
        sum += ball
    return sum


def calculateHighestBreakExcludingLastSixBalls(balls):
    sum = 0
    for ball in range(0, balls - 6):
        sum += addBlackIfEnoughReds(ball)
    return sum


def addBlackIfEnoughReds(ball):
    if ball % 2 == 1:
        return 7
    return 1


print(calculateHighestBreakWithRemainingBalls(10))
