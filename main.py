import time
import keyboard
import random

game = []
score = 0

def pick_ran():
    return [random.randint(0, 8), random.randint(0, 8)]

def write_game_to_win(game, b = 0):
    global score
    if b == 1:
        win = open("window.txt", "w")
        win.write("   Snake Game")
        win.write("\n\n")
        for i in range(9):
            for j in range(9):
                win.write(game[i][j])
                win.write(" ")
            win.write("\n")
        win.write("\n")
        win.write(f"Score: {score}")
        win.write("\nYou lose!")
        win.close()
        return
    elif b == 2:
        win = open("window.txt", "w")
        win.write("   Snake Game")
        win.write("\n\n")
        for i in range(9):
            for j in range(9):
                win.write(game[i][j])
                win.write(" ")
            win.write("\n")
        win.write("\n")
        win.write(f"Score: {score}")
        win.write("\nYou win!")
        win.close()
        return
    win = open("window.txt", "w")
    win.write("   Snake Game")
    win.write("\n\n")
    for i in range(9):
        for j in range(9):
            win.write(game[i][j])
            win.write(" ")
        win.write("\n")
    win.write("\n")
    win.write(f"Score: {score}")
    win.close()

for i in range(9):
    game.append([])
    for j in range(9):
        game[i].append('.')

game[4][1] = "*"
game[4][2] = "*"
game[4][3] = "*"

game[4][6] = "a"

head = [4,3]

tail = [[4,1], [4,2], [4,3]]

write_game_to_win(game)

rotation = "right"

while True:
    if keyboard.is_pressed("right") and rotation != "left":
        rotation = "right"
    elif keyboard.is_pressed("up") and rotation != "down":
        rotation = "up"
    elif keyboard.is_pressed("left") and rotation != "right":
        rotation = "left"
    elif keyboard.is_pressed("down") and rotation != "up":
        rotation = "down"
    
    if rotation == "right":
        if not (head[1] + 1 <= 8 and game[head[0]][head[1] + 1] != "*"):
            write_game_to_win(game, 1)
            break
        if game[head[0]][head[1] + 1] == "a":
            score += 1
            if score == 78:
                write_game_to_win(game, 2)
                break
            game[head[0]][head[1] + 1] = "*"
            head[1] += 1
            tail.append([head[0], head[1]])
            
            while True:
                apple = pick_ran()
                if (game[apple[0]][apple[1]] == "."):
                    break
            game[apple[0]][apple[1]] = "a"
        else:
            game[head[0]][head[1] + 1] = "*"
            head[1] += 1
            tail.append([head[0], head[1]])
            last = tail.pop(0)
            game[last[0]][last[1]] = "."
        write_game_to_win(game)
        time.sleep(0.5)
        continue
    elif rotation == "left":
        if not (head[1] - 1 >= 0 and game[head[0]][head[1] - 1] != "*"):
            write_game_to_win(game, 1)
            break
        if game[head[0]][head[1] - 1] == "a":
            score+= 1
            if score == 78:
                write_game_to_win(game, 2)
                break
            game[head[0]][head[1] - 1] = "*"
            head[1] -= 1
            tail.append([head[0], head[1]])

            while True:
                apple = pick_ran()
                if (game[apple[0]][apple[1]] == "."):
                    break
            game[apple[0]][apple[1]] = "a"
        else:
            game[head[0]][head[1] - 1] = "*"
            head[1] -= 1
            tail.append([head[0], head[1]])
            last = tail.pop(0)
            game[last[0]][last[1]] = "."
        write_game_to_win(game)
        time.sleep(0.5)
        continue
    elif rotation == "up":
        if not (head[0] - 1 >= 0 and game[head[0] - 1][head[1]] != "*"):
            write_game_to_win(game, 1)
            break
        if game[head[0] - 1][head[1]] == "a":
            score += 1
            if score == 78:
                write_game_to_win(game, 2)
                break
            game[head[0] - 1][head[1]] = "*"
            head[0] -= 1
            tail.append([head[0], head[1]])
            
            while True:
                apple = pick_ran()
                if (game[apple[0]][apple[1]] == "."):
                    break
            game[apple[0]][apple[1]] = "a"
        else:
            game[head[0] - 1][head[1]] = "*"
            head[0] -= 1
            tail.append([head[0], head[1]])
            last = tail.pop(0)
            game[last[0]][last[1]] = "."
        write_game_to_win(game)
        time.sleep(0.5)
        continue
    elif rotation == "down":
        if not (head[0] + 1 <= 8 and game[head[0] + 1][head[1]] != "*"):
            write_game_to_win(game, 1)
            break
        if game[head[0] + 1][head[1]] == "a":
            score += 1
            if score == 78:
                write_game_to_win(game, 2)
                break
            game[head[0] + 1][head[1]] = "*"
            head[0] += 1
            tail.append([head[0], head[1]])

            while True:
                apple = pick_ran()
                if (game[apple[0]][apple[1]] == "."):
                    break
            game[apple[0]][apple[1]] = "a"
        else:
            game[head[0] + 1][head[1]] = "*"
            head[0] += 1
            tail.append([head[0], head[1]])
            last = tail.pop(0)
            game[last[0]][last[1]] = "."
        write_game_to_win(game)
        time.sleep(0.5)
        continue
