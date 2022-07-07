import turtle as t
import random
import time


def screen_setting():
    screen = t.Screen()
    screen.title("Catch Turtle") # 그래픽 창 이름 지정
    screen.setup(500, 500) # 창 크기 500*500으로 설정

def score_board_setting():
    score_board = t.Turtle()
    score_board.color("white") # 보드판 색깔 지정
    score_board.goto(150,150)

def turn_left():
    global score
    if player.position() == (-200.00, 0.00):
        player.hideturtle()
        score = score + 1
        show_score(score)
        
def main:
    player = t.Turtle() # 거북이 객체 생성
    player.shape("turtle")
    player.speed(0)
    player.up()

    screen = screen_setting() # screen 객체 생성
    score_board = score_board_setting() # score_board 객체 생성

    score = 0

    location_list = [(0,200), (0,-200), (200,0), (-200,0)] # 거북이의 위치(위, 아래, 오른쪽, 왼쪽) 리스트로 생성

    screen.onkeypress(start, "space") # 스페이스 바를 누르면 start 함수 실행
    screen.onkeypress(right, "Right") # 오른쪽 키를 누르면 right 함수 실행
    screen.onkeypress(left, "Left")
    screen.onkeypress(up, "Up")
    screen.onkeypress(down, "Down")
    screen.listen() # 이 명령어를 실행시켜야 키 입력모드가 실행되어 입력된 키에 반응

    message("Let's Catch Turtle!", "[Space]") # 게임 시작하기 전 첫 화면으로 "Catch Turtle"과 "[Space]"를 출력

    input()
