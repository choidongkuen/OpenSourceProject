import turtle as t

def turn_down():
    global score
    if player.position() == (0.00, -200.00):
        score = score + 1
        player.hideturtle()
        show_score(score)

