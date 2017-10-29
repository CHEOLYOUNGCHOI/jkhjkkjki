import turtle as t      
import random           #random함수





        #상자 만들기


t.up()                  #꼬리를 올린다
t.goto(-250,-250)       #(-250,-250) 로 보낸다
t.down()                #꼬리를 내림
n = 4
for x in range(n):      #n번 반복시킨다
    t.forward(500)      #500만큼 이동
    t.left(360/n)       #왼쪽방향으로 360/n만큼 회전


      #거북이 튕기기위한 준비

    
t.speed(0)              #스피드 최대로
t.up()                  #꼬리 올림
t.home()                #각도와 좌표를 초기화 함
t.down()                #꼬리 내림
t.color("red")          #색상 red
a = random.randint(1, 360)           #각도를 1부터 360도로 랜덤 저장
t.seth(a)                            #거북이 랜덤 지정


      #반복을 통한 거북이 튕기기


while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:     
    n = t.heading()             
    t.forward(1)
    
    if 250 <= t.ycor():    # 위벽 입사각에 대한 반사각  
        if 0 <= n <= 180:  
             t.seth(360-n)  
             t.forward(1)
                
    if t.ycor() <= -250:  # 밑벽 입사각에 대한 반사각
        if 180 <= n <= 360:  
            t.seth(360-n)  
            t.forward(1)
                                   
    if t.xcor() <= -250:  # 왼쪽벽의 입사각에 대한 반사각 
        if 180 <= n <= 270:  
            t.seth(180-n)  
            t.forward(1)  
        else:  
            t.seth(180-n)  
            t.forward(1)
                
    if 250 <= t.xcor():    # 오른쪽벽의 입사각에 대한 반사각
        if 270 <= n <= 360 :  
            t.seth(180-n)  
            t.forward(1)  
        else:  
            t.seth(180-n)  
            t.forward(1)
