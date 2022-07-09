import turtle as t
import random
import time
from tkinter import *

score = 0
life = 10

# 기본 setting

player = t.Turtle() # 거북이 객체 생성
screen = t.Screen()
score_board = t.Turtle()

player.shape("turtle")
player.speed(0)
player.up()
    

screen = t.Screen()
screen.title("Catch Turtle") # 그래픽 창 이름 지정
screen.setup(500,500) # 창 크기 500*500으로 설정


player = t.Turtle() # 거북이 객체 생성
player.shape("turtle")
player.speed(0)
player.up()

screen = t.Screen()
screen.title("Catch Turtle") # 그래픽 창 이름 지정
screen.setup(500, 500) # 창 크기 500*500으로 설정

score_board = t.Turtle()
score_board.color("white") # 보드판 색깔 지정
score_board.goto(150,150)
location_list = [(0,200), (0,-200), (200,0), (-200,0)] # 거북이의 위치(위, 아래, 오른쪽, 왼쪽) 리스트로 생성




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
        global life
        if time.time() > maximum or life <= 0:
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
    global life
    if player.position() == (0.00, 200.00):
        score = score + 1
        player.hideturtle()
        show_score(score)
        show_life(life)
    else :
        life = life - 1 
        show_score(score)
        show_life(life)

def turn_down():
    global score
    global life
    if player.position() == (0.00, -200.00):
        score = score + 1
        player.hideturtle()
        show_score(score)
        show_life(life)
    else :
        life = life - 1 
        show_score(score)
        show_life(life)

def turn_left():
   global score
   global life
   if player.position() == (-200.00, 0.00):
       player.hideturtle()
       score = score + 1
       show_score(score)
       show_life(life)
   else :
        life = life - 1 
        show_score(score)
        show_life(life)


def turn_right(): # 왼쪽 방향키 함수
    global score
    global life
    if player.position() == (200.00, 0.00):
        player.hideturtle()
        score = score + 1
        show_score(score)
        show_life(life)
    else :
        life = life - 1 
        show_score(score)
        show_life(life)

def show_score(score): # 점수 출력
    score_board.clear()
    score_board.color("white")
    score_board.goto(150, 150)
    score_board.pencolor("black")
    score_board.write("Score : %d" % score, False, "left", ("Arial", 13, "bold"))
    score_board.color("white")
    
def show_life(life):
    score_board.color("white")
    score_board.goto(50, 150)
    score_board.pencolor("red")
    score_board.write("Life : %d" % life, False, "left", ("Arial", 13, "bold"))
    score_board.color("white")

    
# ========================================================================= #
# main part

def main(): # 메인 함수 호출

    screen.onkeypress(start, "space") # 스페이스 바를 누르면 start 함수 실행
    screen.onkeypress(turn_right, "Right") # 오른쪽 키를 누르면 right 함수 실행
    screen.onkeypress(turn_left, "Left")
    screen.onkeypress(turn_up, "Up")
    screen.onkeypress(turn_down, "Down")
    screen.listen() # 이 명령어를 실행시켜야 키 입력모드가 실행되어 입력된 키에 반응

    show_message("Let's Catch Turtle!", "[Space]") # 게임 시작하기 전 첫 화면


    t.done()

# ========================================================================== #
# GUI part

root = Tk() # tikinter 객체 생성
root.title("Catch Turtle") # 창 이름
root.geometry("1200x700") # 창 크기

photo = PhotoImage(file = "/Users/077tech/Desktop/Team3Turtle/oss_project/KakaoTalk_Photo_2022-07-09-16-50-21.png",master = root) # image

label1 = Label(root,width = 450,height = 450,relief = "solid",borderwidth = 10,padx = 5, pady = 10,image = photo)
label1.pack() # L

btn0 = Button(root,width = 22,height = 3,padx = 5, pady= 10,text = "Game Start", command = main,highlightcolor = "green")
btn0.pack() # start button


def option():
    root2 = Tk()
    root2.title("Options Window")
    root2.geometry("1200x700")
    
    chkbox1 = Checkbutton(root2,text = "score 나타내기")
    chkbox1.select()
    chkbox1.pack()
    
    chkbox2 = Checkbutton(root2,text = "키보드로 게임하기")
    chkbox2.select()
    chkbox2.pack()
    
    chkbox3 = Checkbutton(root2,text = "친구와 대결하기")
    chkbox3.deselect()
    chkbox3.pack()
    
    
btn1 = Button(root,width = 18,height = 3,padx = 5, pady = 10,text = "Options",command = option)
btn1.pack() # options button


def exit(): # exit 함수
    root.destroy()

btn2 = Button(root,width = 12,height = 5, padx = 5, pady = 10, text = "Exit",command = exit)
btn2.pack() # Game exit button


show_message("Let's Catch Turtle!", "[Space]") # 게임 시작하기 전 첫 화면으로

t.done()
    
    
root = Tk()
root.title("Catch Turtle")
root.geometry("400x300")


bt1 = Button(root,width = 50, height = 30, text = "Game Start", command = main)
bt1.pack()



root.mainloop()



