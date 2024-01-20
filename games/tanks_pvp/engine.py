import ge_sdk as sdk
import random
import time

def make_choice():
    actions = ["up", "down",
               "left", "right", "fire_up", "fire_down", "fire_left", "fire_right"]
    return random.choice(actions)

def MoveTanks(result1, game_map, pos_player1):
    if result1 == 'left' and game_map[pos_player1[0]][pos_player1[1] - 1] not in [1, 3]:
        pos_player1[1] = pos_player1[1] - 1
    elif result1 == 'right' and game_map[pos_player1[0]][pos_player1[1] + 1] not in [1, 3]:
        pos_player1[1] = pos_player1[1] + 1
    elif result1 == 'down' and game_map[pos_player1[0] + 1][pos_player1[1]] not in [1, 3]:
        pos_player1[0] = pos_player1[0] + 1
    elif result1 == 'up' and game_map[pos_player1[0] - 1][pos_player1[1]] not in [1, 3]:
        pos_player1[0] = pos_player1[0] - 1

def Fire(game_map, result1, pos_player1, player1Xp, player1Bullet, pos_player2, player2Xp):
    if result1 == 'fire_up':
        player1Bullet["pos"] = [pos_player1[0], pos_player1[0] - 1]
        player1Bullet["way"] = "up"
    elif result1 == 'fire_down':
        player1Bullet["pos"] = [pos_player1[0], pos_player1[0] + 1]
        player1Bullet["way"] = "down"
    elif result1 == 'fire_right':
        player1Bullet["pos"] = [pos_player1[1] + 1, pos_player1[1]]
        player1Bullet["way"] = "right"
    elif result1 == 'fire_left':
        player1Bullet["pos"] = [pos_player1[1] - 1, pos_player1[1]]
        player1Bullet["way"] = "left"

def Bullet_up(player1Bullet):
    if player1Bullet["way"] == "left":
        player1Bullet["pos"][1] = player1Bullet["pos"][1] - 1
    if player1Bullet["way"] == "right":
        player1Bullet["pos"][1] = player1Bullet["pos"][1] + 1
    if player1Bullet["way"] == "up":
        player1Bullet["pos"][0] = player1Bullet["pos"][0] - 1
    if player1Bullet["way"] == "down":
        player1Bullet["pos"][0] = player1Bullet["pos"][0] + 1

def game():
    engine = sdk.GameEngineClient()

    game_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
                [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 3, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
                [1, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 1],
                [1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    engine.start()

    team1 = engine.teams[0]
    team1.name = 'first'
    left_history = []
    rotation = 0
    player1 = team1.players[0]
    player1.name = 1

    team2 = engine.teams[1]
    team2.name = 'second'

    player2 = team2.players[0]
    player2.name = 2
    pos_player2 = [0, 0]
    coordsBul = [0, 0]

    player2Xp = 5
    player1Xp = 5

    player1Bullet = {"pos": [0, 0], "way": ""}
    integr = 0


    pos_player1 = [6, 1]
    baseCoords = [6, 1]

    while True:
        integr += 1
        #result1 = sdk.timeout_run(0.4, player1.script, "make_choice", [left_history])
        result1 = make_choice()
        if integr == 4:
            integr = 0
            MoveTanks(result1, game_map, pos_player1)
            print(result1)
        Fire(game_map, result1, pos_player1, player1Xp, player1Bullet, pos_player2, player2Xp)
        Bullet_up(player1Bullet)

        frame = {"field": game_map,
                 "rotate": rotation,
                 "x": pos_player1[0],
                 "y": pos_player1[1],
                 "baseX": baseCoords[0],
                 "baseY": baseCoords[1],
                 "bx": player1Bullet["pos"][0],
                 "by": player1Bullet["pos"][1]}
        engine.send_frame(frame)
        time.sleep(0.7)

    engine.end()


if __name__ == "__main__":
    game()
