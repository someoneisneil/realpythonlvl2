import turtle
import random


screen = turtle.Screen()
screen.title("Turtle Tic-Tac-Toe")
screen.setup(width=600, height=600)
screen.bgcolor("white")

screen.setworldcoordinates(0, 0, 3, 3.3)
screen.tracer(0)

board = [" "] * 9
current_player = "X"
game_over = False
game_mode = None  

# Create drawer turtles
grid_drawer = turtle.Turtle()
grid_drawer.hideturtle()
grid_drawer.pensize(5)

piece_drawer = turtle.Turtle()
piece_drawer.hideturtle()
piece_drawer.pensize(7)

text_drawer = turtle.Turtle()
text_drawer.hideturtle()

menu_drawer = turtle.Turtle()
menu_drawer.hideturtle()

def draw_button(x, y, width, height, text, bg_color):
    menu_drawer.penup()
    menu_drawer.goto(x, y)
    menu_drawer.pendown()
    menu_drawer.color("black", bg_color)
    menu_drawer.begin_fill()
    for _ in range(2):
        menu_drawer.forward(width)
        menu_drawer.left(90)
        menu_drawer.forward(height)
        menu_drawer.left(90)
    menu_drawer.end_fill()
    
    menu_drawer.penup()
    menu_drawer.goto(x + width / 2, y + height / 2 - 0.1)
    menu_drawer.color("white")
    menu_drawer.write(text, align="center", font=("Arial", 14, "bold"))

def draw_menu():
    menu_drawer.clear()
    menu_drawer.penup()
    menu_drawer.goto(1.5, 2.3)
    menu_drawer.color("black")
    menu_drawer.write("TIC-TAC-TOE", align="center", font=("Arial", 32, "bold"))
    
    menu_drawer.goto(1.5, 2.0)
    menu_drawer.write("Select a Game Mode:", align="center", font=("Arial", 16, "italic"))
    
    draw_button(0.2, 0.8, 1.2, 0.6, "1 Player (vs Bot)", "#1f77b4")
    draw_button(1.6, 0.8, 1.2, 0.6, "2 Players", "#2ca02c")
    screen.update()

def start_game(mode):
    global game_mode
    game_mode = mode
    menu_drawer.clear()
    draw_grid()
    update_status("Player X's Turn")

def draw_grid():
    grid_drawer.color("black")
    for y in range(1, 3):
        grid_drawer.penup()
        grid_drawer.goto(0, y)
        grid_drawer.pendown()
        grid_drawer.goto(3, y)
    for x in range(1, 3):
        grid_drawer.penup()
        grid_drawer.goto(x, 0)
        grid_drawer.pendown()
        grid_drawer.goto(x, 3)
    screen.update()

def draw_x(col, row):
    piece_drawer.color("blue")
    padding = 0.15
    left = col + padding
    right = col + 1 - padding
    bottom = row + padding
    top = row + 1 - padding

    piece_drawer.penup()
    piece_drawer.goto(left, top)
    piece_drawer.pendown()
    piece_drawer.goto(right, bottom)
    piece_drawer.penup()
    piece_drawer.goto(left, bottom)
    piece_drawer.pendown()
    piece_drawer.goto(right, top)
    screen.update()

def draw_o(col, row):
    piece_drawer.color("red")
    center_x = col + 0.5
    center_y = row + 0.5
    
    piece_drawer.penup()
    piece_drawer.goto(center_x, center_y - 0.35)
    piece_drawer.pendown()
    piece_drawer.circle(0.35, steps=60)
    screen.update()

def check_winner():
    win_conditions = list()
    win_conditions.append((0, 1, 2))
    win_conditions.append((3, 4, 5))
    win_conditions.append((6, 7, 8))
    win_conditions.append((0, 3, 6))
    win_conditions.append((1, 4, 7))
    win_conditions.append((2, 5, 8))
    win_conditions.append((0, 4, 8))
    win_conditions.append((2, 4, 6))
    

    for pos1, pos2, pos3 in win_conditions:
        if board[pos1] == board[pos2] == board[pos3] != " ":
            return board[pos1]
    if " " not in board:
        return "Tie"
    return None

def update_status(text):
    text_drawer.clear()
    text_drawer.penup()
    text_drawer.goto(1.5, 3.08)
    text_drawer.color("black")
    text_drawer.write(text, align="center", font=("Arial", 16, "bold"))
    screen.update()

def bot_move():
    global current_player, game_over
    if game_over:
        return

    available_moves = list()
    for idx in range(9):
        if board[idx] == " ":
            available_moves.append(idx)

    if len(available_moves) > 0:
        bot_choice = random.choice(available_moves)
        
        bot_row = bot_choice // 3
        bot_col = bot_choice % 3

        board[bot_choice] = "O"
        draw_o(bot_col, bot_row)
        
        winner = check_winner()
        if winner:
            end_game(winner)
        else:
            current_player = "X"
            update_status("Player X's Turn")

def handle_click(x, y):
    global current_player, game_over
    

    if game_mode is None:
        if 0.2 <= x <= 1.4 and 0.8 <= y <= 1.4:
            start_game("1")
        elif 1.6 <= x <= 2.8 and 0.8 <= y <= 1.4:
            start_game("2")
        return

    if game_over:
        return
        
    if game_mode == "1" and current_player == "O":
        return
        
    if x < 0 or x > 3 or y < 0 or y > 3:
        return

    col = int(x)
    row = int(y)
    index = row * 3 + col

    if board[index] == " ":
        board[index] = current_player

        if current_player == "X":
            draw_x(col, row)
            winner = check_winner()
            if winner:
                end_game(winner)
            else:
                current_player = "O"
                if game_mode == "1":
                    update_status("Bot is thinking...")
                    screen.ontimer(bot_move, 500)
                else:
                    update_status("Player O's Turn")
        else:
            draw_o(col, row)
            winner = check_winner()
            if winner:
                end_game(winner)
            else:
                current_player = "X"
                update_status("Player X's Turn")

def end_game(winner):
    global game_over
    game_over = True
    if winner == "Tie":
        update_status("It's a Tie! Close window to exit.")
    else:
        if game_mode == "1" and winner == "O":
            update_status("Bot Wins! Close window to exit.")
        else:
            update_status(f"Player {winner} Wins! Close window to exit.")

draw_menu()

screen.onclick(handle_click)
screen.mainloop()
