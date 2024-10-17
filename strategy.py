def strategy(opponent_prev_move):
    """
    Define the strategy for the prisoner's dilemma game.
    """
    if opponent_prev_move is None:
        return "D"  # Initial move
    elif opponent_prev_move == "C":
        return "C"  # Cooperate if opponent cooperated
    else:
        return "D"  # Defect if opponent defected