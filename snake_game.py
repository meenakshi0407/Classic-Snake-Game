# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:55:48 2023

@author: ASUS
"""

import turtle

import random

#program constants 

WIDTH=500
HEIGHT=500
DELAY=400 #miliseconds 
FOOD_SIZE=10

offset={
  "up": (0,20),
  "down": (0,-20),
  "left":(-20,0),
  "right":(20,0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    
def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down": #no self collision simply by pressing wrong key
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "righr":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"
            

def game_loop():
    stamper.clearstamps() #remove existing stamps made by stamper
    
    new_head=snake[-1].copy()
    new_head[0]+=offset[snake_direction][0]
    new_head[1]+=offset[snake_direction][1]
    
      #check collision
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0]> WIDTH/2 or new_head[1] < -HEIGHT/2 or new_head[1]> HEIGHT/2:
        reset()
    else:
        
#add new head to snake
        snake.append(new_head)
        if not food_collision():
        
#keep the snake same length unless fed
            snake.pop(0)
      
#drAW snake for the first time      
    for segment in snake:
      stamper.goto(segment[0],segment[1])
      stamper.stamp()
      
#screen refresh
    screen.title(f'snake game score:{score}')
    screen.update()
#rinse and repeat 
    turtle.ontimer(game_loop,DELAY)
  
def get_random_food_pos():
  x=random.randint(-WIDTH/2+ FOOD_SIZE,WIDTH/2 - FOOD_SIZE)
  y=random.randint(-HEIGHT/2+ FOOD_SIZE,HEIGHT/2 - FOOD_SIZE)
  return(x,y)

def food_collision():
  global food_pos,score
  if get_distance(snake[-1],food_pos) <20:
    score+=1
    food_pos=get_random_food_pos()
    food.goto(food_pos)
    return True
  return False


def get_distance(pos1,pos2):
  x1,y1=pos1
  x2,y2=pos2
  distance = ((y2-y1)**2 + (x2-x1)**2)**0.5
  return distance 

def reset():
    global score,snake,snake_direction,food_pos
    snake=[[0,0],[20,0],[40,0],[60,0]]
    snake_direction= "up"
    score=0
    food_pos=get_random_food_pos()
    food.goto(food_pos)
    game_loop()
    

#game window
screen=turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

#event handlers
screen.listen()
bind_direction_keys()

#create a turtle
stamper= turtle.Turtle()
stamper.shape("circle")
stamper.color("green")
stamper.penup()


#food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE/20)
food.penup()

reset()
turtle.done()
