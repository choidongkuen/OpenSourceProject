import turtle as t
import random
import time

score = 0

def game_end(playing): # 게임 종료 함수
    global score
    if not playing:
        score_board.clear()
        message("Game Over!", text)
        text = "Your Score : %d" % score
        score = 0
       
def turn_up(): # 오른쪽 방향키 함수
    global score
    if player.position() == (0.00, 200.00):
        score = score + 1
        player.hideturtle()
        show_score(score)

def screen_setting(): # screen 객체 설정 함수
    screen = t.Screen()
    screen.title("Catch Turtle") # 그래픽 창 이름 지정
    screen.setup(500, 500) # 창 크기 500*500으로 설정

def score_board_setting(): # score_board 객체 설정 함수
    score_board = t.Turtle()
    color = input("Color of score_board : ")
    score_board.color("white") # 보드판 색깔 지정
    score_board.goto(150,150)

def main(): # 메인 함수

    player = t.Turtle() # 거북이 객체 생성
    shape = input("shape : ") # refer to turtle help
    player.shape("turtle")
    player.speed(0)
    player.up()

    screen = screen_setting() # screen 객체 생성
    score_board = score_board_setting() # score_board 객체 생성


    location_list = [(0,200), (0,-200), (200,0), (-200,0)] # 거북이의 위치(위, 아래, 오른쪽, 왼쪽) 리스트로 생성

    screen.onkeypress(game_start, "space") # 스페이스 바를 누르면 start 함수 실행
    screen.onkeypress(turn_right, "Right") # 오른쪽 키를 누르면 turn_right 함수 실행
    screen.onkeypress(turn_left, "Left") # 왼쪽 키를 누르면 turn_left 함수 실행
    screen.onkeypress(turn_up, "Up") # 위 키를 누르면 turn_up 함수 실행
    screen.onkeypress(turn_down, "Down") # 아래 키를 누르면 turn_down 
    screen.listen() # 이 명령어를 실행시켜야 키 입력모드가 실행되어 입력된 키에 반응

    message("Let's Catch Turtle!", "[Space]") # 게임 시작하기 전 첫 화면으로 "Catch Turtle"과 "[Space]"를 출력



print("Welcome to the Catch Turtle Game!")
main() # 메인 함수 호출
