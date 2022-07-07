import turtle as t

def turn_left():
    global score
    if player.position() == (-200.00, 0.00):
        player.hideturtle()
        score = score + 1
        show_score(score)

