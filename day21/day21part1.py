def play_game(player1_start, player2_start):
    player1_position = player1_start
    player2_position = player2_start
    player1_score = 0
    player2_score = 0
    die = 1
    total_rolls = 0

    def roll_die():
        nonlocal die, total_rolls
        total_rolls += 1
        roll_value = die
        die = (die % 100) + 1
        return roll_value

    while True:
        # Player 1's turn
        roll_sum = roll_die() + roll_die() + roll_die()
        player1_position = (player1_position + roll_sum - 1) % 10 + 1
        player1_score += player1_position
        if player1_score >= 1000:
            break

        # Player 2's turn
        roll_sum = roll_die() + roll_die() + roll_die()
        player2_position = (player2_position + roll_sum - 1) % 10 + 1
        player2_score += player2_position
        if player2_score >= 1000:
            break

    losing_score = player1_score if player2_score >= 1000 else player2_score
    return losing_score * total_rolls

player1_start = 7
player2_start = 10
result = play_game(player1_start, player2_start)
print("Result:", result)
