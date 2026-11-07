import turtle

# Set up the screen
screen = turtle.Screen()
screen.title(" Tic-Tac-Toe ")
screen.setup(width=600, height=600)
screen.bgcolor("white")


screen.setworldcoordinates(0, 0, 3, 3.3)
screen.tracer(0)


board = [" "] * 9
current_player = "X"
game_over = False

grid_drawer = turtle.Turtle()
grid_drawer.hideturtle()
grid_drawer.pensize(5)

piece_drawer = turtle.Turtle()
piece_drawer.hideturtle()
piece_drawer.pensize(7)

text_drawer = turtle.Turtle()
text_drawer.hideturtle()

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
    text_drawer.goto(1.5, 3.03)
    text_drawer.color("black")
    text_drawer.write(text, align="center", font = ("times new roman", 27, "bold"))
    screen.update()

def handle_click(x, y):
    global current_player, game_over
    
    if game_over:
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
        update_status(f"Player {winner} Wins! Close window to exit.")

# Run the game layout sequence instantly
draw_grid()
update_status("Player X's Turn")

screen.onclick(handle_click)
screen.mainloop()
