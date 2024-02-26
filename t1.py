import turtle as t
import random
import time

score = 0

def show_message(up, down): # 메세지 출력
    player.goto(0,200)
    player.write(up, False, "center", ("Arial", 20, "bold"))
    player.goto(0,-200)
    player.write(down, False, "center", ("Arial",15, "normal"))
    player.goto(0,0)
    player.showturtle()


def start(): # 게임 시작
    playing = True
    player.clear()
    playing = game_play(playing)
    game_end(playing)


def game_play(playing): # 게임 진행 함수
    current_time = time.time()
    maximum = current_time + 30

    while playing:
        if time.time() > maximum:
            playing = False
            return playing

        player.showturtle()
        player.up()
        location = random.choice(location_list)
        player.goto(location)
        sleep_time = random.uniform(1, 2)
        time.sleep(sleep_time)


def game_end(playing): # 게임 종료 함수
    global score
    if not playing:
        score_board.clear()
        text = "Your Score : %d" % score
        show_message("Game Over!", text)
        score = 0

def turn_up(): # 오른쪽 방향키 함수
    global score
    if player.position() == (0.00, 200.00):
        score = score + 1
        player.hideturtle()
        show_score(score)

def turn_down():
    global score
    if player.position() == (0.00, -200.00):
        score = score + 1
        player.hideturtle()
        show_score(score)

def turn_left():
   global score
   if player.position() == (-200.00, 0.00):
       player.hideturtle()
       score = score + 1
       show_score(score)


def turn_right(): # 왼쪽 방향키 함수
    global score
    if player.position() == (200.00, 0.00):
        player.hideturtle()
        score = score + 1
        show_score()

def show_score(score): # 점수 출력
    score_board.clear()
    score_board.color("white")
    score_board.goto(150, 150)
    score_board.pencolor("black")
    score_board.write("Score : %d" % score, False, "left", ("Arial", 13, "bold"))
    score_board.color("white")

#def screen_setting(): # screen 객체 설정 함수

 #   screen = t.Screen()
 #   screen.title("Catch Turtle") # 그래픽 창 이름 지정
 #   screen.setup(500, 500) # 창 크기 500*500으로 설정
 #   return screen

#def score_board_setting(): # score_board 객체 설정 함수

 #   score_board = t.Turtle()
  #  color = input("Color of score_board : ")
  #  score_board.color("white") # 보드판 색깔 지정
  #  score_board.goto(150,150)
  #  return score_board

# def main(): # 메인 함수



print("Welcome to the Catch Turtle Game!")
#main() # 메인 함수 호출
print("==============GAME START!===============")
shape = input("shape : ") # refer to turtle help

player = t.Turtle() # 거북이 객체 생성
player.shape(shape)
player.speed(0)
player.up()

screen = t.Screen()
screen.title("Catch Turtle") # 그래픽 창 이름 지정
screen.setup(500, 500) # 창 크기 500*500으로 설정

score_board = t.Turtle()
color = input("Color of score_board : ")
score_board.color(color) # 보드판 색깔 지정
score_board.goto(150,150)
location_list = [(0,200), (0,-200), (200,0), (-200,0)] # 거북이의 위치(위, 아래, 오른쪽, 왼쪽) 리스트로 생성

screen.onkeypress(start, "space") # 스페이스 바를 누르면 start 함수 실행
screen.onkeypress(turn_right, "Right") # 오른쪽 키를 누르면 right 함수 실행
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_up, "Up")
screen.onkeypress(turn_down, "Down")
screen.listen() # 이 명령어를 실행시켜야 키 입력모드가 실행되어 입력된 키에 반응

show_message("Let's Catch Turtle!", "[Space]") # 게임 시작하기 전 첫 화면으로

t.done()
