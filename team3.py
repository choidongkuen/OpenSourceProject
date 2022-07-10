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

shape_list = ["turtle", "circle", "triangle", "square"] # 추가 : 캐릭터 모양 추가
player.shape(shape_list[0])
player.speed(0)
player.up()
    

screen = t.Screen()
screen.title("Catch Turtle") # 그래픽 창 이름 지정
screen.setup(500,500) # 창 크기 500*500으로 설정


#score_board = t.Turtle()
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
    global random_name # 모양 변수 추가
    maximum = time.time() + 30

    while playing:
        global life
        if time.time() > maximum or life <= 0:
            playing = False
            return playing

        random_name = random.choice(shape_list) # 추가 : 모양 랜덤 지정
        player.shape(random_name) # 추가 : 모양 지정
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
        # show_message("Insert coins!",text)
        score = 0
        

def turn_up(): # 위쪽 방향키 함수
    global score,life

    if player.position() == (0.00, 200.00):
        score = score + 1
        print(player.shape())
        player.settiltangle(-45)  # 추가 : -45도 회전
        player.hideturtle()
        show_life(life)

    else :
        life = life - 1
        show_life(life)

    show_score(score)
    show_life(life)
    

def turn_down(): # 아래쪽 방향키 함수
    global score,life

    if player.position() == (0.00, -200.00):
        score = score + 1
        print(player.shape())
        player.settiltangle(45)  # 추가 : 45도 회전
        player.hideturtle()
        show_life(life)

    else:
        life = life - 1
        show_life(life)
    
    show_score(score)
    show_life(life)

    

def turn_left(): # 왼쪽 방향키 함수
    global score,life
    
    if player.position() == (-200.00, 0.00):
        score = score + 1
        print(player.shape())
        player.settiltangle(90)  # 추가 : 90도 회전
        player.hideturtle()
        show_life(life)
           
    else:
        life = life - 1
        show_life(life)
        
    show_score(score)
    show_life(life)

    


def turn_right(): # 오른쪽 방향키 함수
    global score,life  # 추가
    if player.position() == (200.00, 0.00):
        score = score + 1
        print(player.shape())
        player.settiltangle(0)  # 추가 : 머리 방향 그대로
        player.hideturtle()
        show_life(life)

    else :
        life = life - 1
        show_life(life)
        
    show_score(score)
    show_life(life)


def show_score(score): # 점수 출력
    score_board.clear()
    score_board.color("white")
    score_board.goto(150, 150)
    score_board.pencolor("black")
    score_board.write("Score : %d" % score, False, "left", ("Arial", 13, "bold"))
    score_board.color("white")
    
def show_life(life): # 목습 출력
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


photo = PhotoImage(file = "Please insert your image file address here!!",master = root) # image



label1 = Label(root,width = 450,height = 450,relief = "solid",borderwidth = 10,padx = 5, pady = 10,image = photo)
label1.pack()

def rule():
    root = Tk()
    root.title("Game Rules")
    root.geometry("400x400")
    label2 = Label(root,relief = "solid",borderwidth = 10,padx = 5, pady = 10,text = " == 게임 규칙 ==")
    label2.pack()
    label3 = Label(root,text = "1: 제한 시간은 30초가 주어집니다.")
    label3.pack()
    label4 = Label(root,text = "2: 키보드의 방향키를 이용하여 조작합니다.")
    label4.pack()
    label5 = Label(root,text = "3: 거북이 or 원 or 삼각형 or 사각형 모양이 랜덤하게 출현합니다. 집중력 필수!")
    label5.pack()
    label6 = Label(root,text = "4: 캐릭터 방향과 키보드 방향이 일치시 1점 획득합니다.")
    label6.pack()
    label7 = Label(root,text = "5: 집중력 100% 필수!!")
    label7.pack()
    
    
    
    chkbox1 = Checkbutton(root, text="규칙을 확인했습니다.")
    chkbox1.deselect()
    chkbox1.pack()
    
    btn3 = btn1 = Button(root, text= "Start", command=main)
    btn3.pack()  # options button

    

btn0 = Button(root,width = 22,height = 3,padx = 5, pady= 10,text = "Game Start", command = rule,highlightcolor = "green")
btn0.pack() # start button


def option():
    root2 = Tk()
    root2.title("Options Window")
    root2.geometry("500x500")

    chkbox1 = Checkbutton(root2, text="score 나타내기")
    chkbox1.select()
    chkbox1.pack()

    chkbox2 = Checkbutton(root2, text="키보드로 게임하기")
    chkbox2.select()
    chkbox2.pack()

    chkbox3 = Checkbutton(root2, text="친구와 대결하기")
    chkbox3.deselect()
    chkbox3.pack()


    


btn1 = Button(root, width=18, height=3, padx=5, pady=10, text="Options", command=option)
btn1.pack()  # options button


def exit():  # exit 함수
    global root
    root.destroy()

btn2 = Button(root, width=12, height=5, padx=5, pady=10, text="Exit", command=exit)
btn2.pack()  # Game exit button

root.mainloop()



