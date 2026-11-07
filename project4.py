import turtle
import random
import time
from collections import deque

# Set up the screen first
ts = turtle.Screen()
ts.bgcolor("khaki")
ts.title("Snkae Game")


ts.tracer(0)


auto_speed = 50 


shift_x = 40
shift_y = -80
step_size = 20


border = turtle.Turtle()
border.penup()
border.speed(0)
border.pensize(5)
border.color("darkred")
border.goto(-220 + shift_x, -220 + shift_y)
border.pendown()
for _ in range(4):
    border.forward(440)
    border.left(90)
border.ht()


t = turtle.Turtle()
t.shape('square')
t.color("black")
t.penup()
t.goto(shift_x, shift_y)
t.pendown()

n_foods = 100
list_of_foods = []


for kk in range(n_foods):
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    rx = (random.randint(-200, 200) // 20) * 20 + shift_x
    ry = (random.randint(-200, 200) // 20) * 20 + shift_y
    food.goto(rx, ry)
    list_of_foods.append(food)

pen = turtle.Turtle()
pen.penup()
pen.goto(180 + shift_x, 180 + shift_y)
pen.color("black")
pen.ht()


report = turtle.Turtle()
report.penup()
report.goto(shift_x, shift_y)
report.color("black")
report.ht()

started = 0
steps = 0
caught = [False] * n_foods
segments = []
game_over = False

response = ts.textinput("Game Mode", "Enable Autopilot? (Y/N):")
auto_mode = True if response and response.lower() == 'y' else False

def right():
    if t.heading() != 180.0 and not auto_mode:
        t.setheading(0.0)

def left():
    if t.heading() != 0.0 and not auto_mode:
        t.setheading(180.0)

def up():
    if t.heading() != 270.0 and not auto_mode:
        t.setheading(90.0)

def down():
    if t.heading() != 90.0 and not auto_mode:
        t.setheading(-90.0)

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")

ts.listen()


def hits_tail(x, y):
    for seg in segments[2:]:
        if abs(x - seg.xcor()) < 15 and abs(y - seg.ycor()) < 15:
            return True
    return False

def get_safe_next_move(start_x, start_y, target_x, target_y):
    sx, sy = int(round(start_x)), int(round(start_y))
    tx, ty = int(round(target_x)), int(round(target_y))
    
    tail_set = set()
    for seg in segments:
        tail_set.add((int(round(seg.xcor())), int(round(seg.ycor()))))
        
    queue = deque([ (sx, sy, []) ])
    visited = {(sx, sy)}
    
    moves = [
        (0.0, 20, 0),  
        (90.0, 0, 20),  
        (180.0, -20, 0), 
        (270.0, 0, -20) 
    ]
    
    best_fallback = None
    max_fallback_dist = -1
    
    while queue:
        cx, cy, path = queue.popleft()
        
        if cx == tx and cy == ty:
            if path:
                return path[0]  
                
        for heading, dx, dy in moves:
            if path and abs(heading - path[-1]) == 180:
                continue
            if not path and abs(heading - t.heading()) == 180:
                continue

            nx, ny = cx + dx, cy + dy
            if abs(nx - shift_x) <= 200 and abs(ny - shift_y) <= 200:
                if (nx, ny) not in tail_set and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_path = path + [heading]
                    queue.append((nx, ny, new_path))
                    
                    if len(new_path) > max_fallback_dist:
                        max_fallback_dist = len(new_path)
                        best_fallback = new_path
                
    if best_fallback and len(best_fallback) > 0:
        return best_fallback[0] 
    
    for heading, dx, dy in moves:
        if abs(heading - t.heading()) == 180:
            continue
        nx, ny = sx + dx, sy + dy
        if abs(nx - shift_x) <= 200 and abs(ny - shift_y) <= 200:
            if (nx, ny) not in tail_set:
                return heading

    return t.heading()


def game_loop():
    global steps, game_over, started
    
    if game_over:
        return

    steps = steps + 1
    
    
    pen.clear()
    pen.write(len(segments), align="center", font=("Courier", 24, "normal"))
    

    if auto_mode:
        target_x, target_y = shift_x, shift_y
        closest_food = None
        min_distance = float('inf')
        
        for kk in range(len(list_of_foods)):
            if not caught[kk]:
                dist = t.distance(list_of_foods[kk])
                if dist < min_distance:
                    min_distance = dist
                    closest_food = list_of_foods[kk]
        
        if closest_food is not None:
            target_x = closest_food.xcor()
            target_y = closest_food.ycor()
            

        new_heading = get_safe_next_move(t.xcor(), t.ycor(), target_x, target_y)
        t.setheading(new_heading)



    if not auto_mode:
        if abs(t.xcor() - shift_x) > 210 or abs(t.ycor() - shift_y) > 210:
            game_over = True
            report.write("GAME OVER\nHit Boundary!", align="center", font=("Courier", 24, "bold"))
            ts.update()
            return
            
        if hits_tail(t.xcor(), t.ycor()):
            game_over = True
            report.write("GAME OVER\nCrashed into Tail!", align="center", font=("Courier", 24, "bold"))
            ts.update()
            return

    for kk in range(len(list_of_foods)):
        if not caught[kk]:			
            if t.distance(list_of_foods[kk]) < 20:
                caught[kk] = True
                list_of_foods[kk].color('green')
                segments.append(list_of_foods[kk])


    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = t.xcor()
        y = t.ycor()
        segments[0].st()
        segments[0].goto(x, y)
	
    t.forward(20)
	
    if t.xcor() > (shift_x + 10):
        started = 1
		

    if len(segments) == n_foods:
        if abs(t.xcor() - shift_x) < 20 and abs(t.ycor() - shift_y) < 20:
            game_over = True
            t.clear()
            t.ht()
            for kk in range(len(segments)):
                segments[kk].ht()
				
            report_text = f"Victory!\nSteps Taken: {steps}\nFruits Eaten: {len(segments)}"
            report.write(report_text, align="center", font=("Courier", 18, "normal"))
            ts.update()
            return


    ts.update()
    

    delay_ms = auto_speed if auto_mode else 90
    ts.ontimer(game_loop, delay_ms)

game_loop()
turtle.done()
