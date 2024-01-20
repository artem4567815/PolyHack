import ge_sdk as sdk
import random
import time

def make_choice():
    actions = ["up", "down", "left", "right", "fire_up", "fire_down", "fire_right", "fire_left"]
    return random.choice(actions)

def MoveTanks(result1, result2, game_map, pos_player1, player1Way, pos_player2, player2Way):
    if result1 == 'left' and game_map[pos_player1[0]][pos_player1[1] - 1] not in [1, 3]:
        pos_player1[1] = pos_player1[1] - 1
        player1Way["way"] = "left"
    elif result1 == 'right' and game_map[pos_player1[0]][pos_player1[1] + 1] not in [1, 3]:
        pos_player1[1] = pos_player1[1] + 1
        player1Way["way"] = "right"
    elif result1 == 'down' and game_map[pos_player1[0] + 1][pos_player1[1]] not in [1, 3]:
        pos_player1[0] = pos_player1[0] + 1
        player1Way["way"] = "down"
    elif result1 == 'up' and game_map[pos_player1[0] - 1][pos_player1[1]] not in [1, 3]:
        pos_player1[0] = pos_player1[0] - 1
        player1Way["way"] = "up"

    if result2 == 'left' and game_map[pos_player2[0]][pos_player2[1] - 1] not in [1, 3]:
        pos_player2[1] = pos_player2[1] - 1
        player2Way["way"] = "left"
    elif result2 == 'right' and game_map[pos_player2[0]][pos_player2[1] + 1] not in [1, 3]:
        pos_player2[1] = pos_player2[1] + 1
        player2Way["way"] = "right"
    elif result2 == 'down' and game_map[pos_player2[0] + 1][pos_player2[1]] not in [1, 3]:
        pos_player2[0] = pos_player2[0] + 1
        player2Way["way"] = "down"
    elif result2 == 'up' and game_map[pos_player2[0] - 1][pos_player2[1]] not in [1, 3]:
        pos_player2[0] = pos_player2[0] - 1
        player2Way["way"] = "up"

def Fire(game_map, result1, result2, pos_player1, player1Xp, player1Bullet, pos_player2, player2Xp, player2Bullet, player1Way, player2Way):
    if result1 == 'fire_up':
        player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
        player1Bullet["way"] = "up"
        player1Way['way'] = "up"
    elif result1 == 'fire_down':
        player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
        player1Bullet["way"] = "down"
        player1Way['way'] = "down"
    elif result1 == 'fire_right':
        player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
        player1Bullet["way"] = "right"
        player1Way['way'] = "right"
    elif result1 == 'fire_left':
        player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
        player1Bullet["way"] = "left"
        player1Way['way'] = "left"

    if result2 == 'fire_up':
        player2Bullet["pos"] = [pos_player2[0], pos_player2[1]]
        player2Bullet["way"] = "up"
        player2Way['way'] = "up"
    elif result2 == 'fire_down':
        player2Bullet["pos"] = [pos_player2[0], pos_player2[1]]
        player2Bullet["way"] = "down"
        player2Way['way'] = "down"
    elif result2 == 'fire_right':
        player2Bullet["pos"] = [pos_player2[0], pos_player2[1]]
        player2Bullet["way"] = "right"
        player2Way['way'] = "right"
    elif result2 == 'fire_left':
        player2Bullet["pos"] = [pos_player2[0], pos_player2[1]]
        player2Bullet["way"] = "left"
        player2Way['way'] = "left"


def Bullet_up(player1Bullet, player2Bullet, pos_player1, pos_player2, game_map, player1Xp, player2Xp, winners):
    global finish
    if player1Bullet["way"] == "left":
        player1Bullet["pos"][1] -= 1
    elif player1Bullet["way"] == "right":
        player1Bullet["pos"][1] += 1
    elif player1Bullet["way"] == "up":
        player1Bullet["pos"][0] -= 1
    elif player1Bullet["way"] == "down":
        player1Bullet["pos"][0] += 1

    if player1Bullet["pos"] == pos_player2:
        player1Bullet["pos"] = [0, 0]
        player1Bullet["way"] = ""
        player2Xp -= 1
        print(player2Xp)
        if player2Xp == 0:
            pos_player2 = []
            winners["players1"] = True
            finish = True
            print("WINNNNNNNNN player 1")
    elif game_map[player1Bullet["pos"][0]][player1Bullet["pos"][1]] == 1:
        player1Bullet["pos"] = [0, 0]
        player1Bullet["way"] = ""
    elif game_map[player1Bullet["pos"][0]][player1Bullet["pos"][1]] == 3:
        game_map[player1Bullet["pos"][0]][player1Bullet["pos"][1]] = 0
        player1Bullet["pos"] = [0, 0]
        player1Bullet["way"] = ""

    if player2Bullet["way"] == "left":
        player2Bullet["pos"][1] -= 1
    elif player2Bullet["way"] == "right":
        player2Bullet["pos"][1] += 1
    elif player2Bullet["way"] == "up":
        player2Bullet["pos"][0] -= 1
    elif player2Bullet["way"] == "down":
        player2Bullet["pos"][0] += 1

    if player2Bullet["pos"] == pos_player1:
        player2Bullet["pos"] = [0, 0]
        player2Bullet["way"] = ""
        player1Xp -= 1
        if player1Xp == 0:
            pos_player1 = []
            winners["players2"] = True
            finish = True
            print("WINNNNNNNNN player 2")
    elif game_map[player2Bullet["pos"][0]][player2Bullet["pos"][1]] == 1:
        player2Bullet["pos"] = [0, 0]
        player2Bullet["way"] = ""
    elif game_map[player2Bullet["pos"][0]][player2Bullet["pos"][1]] == 3:
        game_map[player2Bullet["pos"][0]][player2Bullet["pos"][1]] = 0
        player2Bullet["pos"] = [0, 0]
        player2Bullet["way"] = ""

def game():
    engine = sdk.GameEngineClient()

    game_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
                [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 3, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
                [1, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    engine.start()

    team1 = engine.teams[0]
    team1.name = 'first'

    player1 = team1.players[0]
    player1.name = 1

    team2 = engine.teams[1]
    team2.name = 'second'

    player2 = team2.players[0]
    player2.name = 2
    player2Bullet = {"pos": [0, 0], "way": ""}
    pos_player2 = [6, 6]
    player2Way = {"way": " "}
    finish = False
    player2Xp = {"xp": 1}
    player1Xp = {"xp": 1}

    player1Bullet = {"pos": [0, 0], "way": ""}
    integr = 0

    pos_player1 = [6, 1]
    player1Way = {"way": " "}
    winners = {"players1": False, "players2": False}

    while True:
        integr += 1
        # result1 = sdk.timeout_run(0.4, player1.script, "make_choice", [left_history])
        result1 = make_choice()
        result2 = make_choice()
        if integr == 4:
            integr = 0
            player1Bullet["pos"] = [0, 0]
            player2Bullet["pos"] = [0, 0]
            MoveTanks(result1, result2, game_map, pos_player1, player1Way, pos_player2, player2Way)
            print("player1: ", result1, "player2: ", result2, "xp1: ", player1Xp['xp'], "xp2: ", player2Xp['xp'])
            Fire(game_map, result1, result2, pos_player1, player1Xp['xp'], player1Bullet, pos_player2, player2Xp['xp'],
                 player2Bullet, player1Way, player2Way)

        Bullet_up(player1Bullet, player2Bullet, pos_player1, pos_player2, game_map, player1Xp['xp'], player2Xp['xp'], winners)
        frame = {"field": game_map,
                 "x": pos_player1[0],
                 "y": pos_player1[1],
                 "x2": pos_player2[0],
                 "y2": pos_player2[1],
                 "bullet":
                     {"bx": player1Bullet["pos"][0],
                      "by": player1Bullet["pos"][1],
                      "way": player1Bullet["way"]},
                 "bullet2":
                     {"bx": player2Bullet["pos"][0],
                      "by": player2Bullet["pos"][1],
                      "way": player2Bullet["way"]},
                 "way1": player1Way['way'],
                 "way2": player2Way['way'],
                 "finish": winners}

        engine.send_frame(frame)

        time.sleep(0.2)
        print(winners['players1'], winners['players2'])
        if winners['players1'] == True or winners['players2'] == True:
            engine.end()
            break

if __name__ == "__main__":
    game()









#########################################
# import ge_sdk as sdk
# import random
# import time
#
# def make_choice():
#     actions = ["up", "down",
#                "left", "right", "fire_up", "fire_down", "fire_right", "fire_left"]
#     # actions = ["left", "fire_right", "fire_left"]
#     return random.choice(actions)
#
# def MoveTanks(result1, game_map, pos_player1, player1Way):
#     if result1 == 'left' and game_map[pos_player1[0]][pos_player1[1] - 1] not in [1, 3]:
#         pos_player1[1] = pos_player1[1] - 1
#         player1Way["way"] = "left"
#     elif result1 == 'right' and game_map[pos_player1[0]][pos_player1[1] + 1] not in [1, 3]:
#         pos_player1[1] = pos_player1[1] + 1
#         player1Way["way"] = "right"
#     elif result1 == 'down' and game_map[pos_player1[0] + 1][pos_player1[1]] not in [1, 3]:
#         pos_player1[0] = pos_player1[0] + 1
#         player1Way["way"] = "down"
#     elif result1 == 'up' and game_map[pos_player1[0] - 1][pos_player1[1]] not in [1, 3]:
#         pos_player1[0] = pos_player1[0] - 1
#         player1Way["way"] = "up"
#
# def Fire(game_map, result1, pos_player1, player1Xp, player1Bullet, pos_player2, player2Xp, player1Way):
#     if result1 == 'fire_up':
#         player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
#         player1Bullet["way"] = "up"
#         player1Way['way'] = "up"
#     elif result1 == 'fire_down':
#         player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
#         player1Bullet["way"] = "down"
#         player1Way['way'] = "down"
#     elif result1 == 'fire_right':
#         player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
#         player1Bullet["way"] = "right"
#         player1Way['way'] = "right"
#     elif result1 == 'fire_left':
#         player1Bullet["pos"] = [pos_player1[0], pos_player1[1]]
#         player1Bullet["way"] = "left"
#         player1Way['way'] = "left"
#
# def Bullet_up(player1Bullet, pos_player2, game_map, player2Xp):
#     if player1Bullet["way"] == "left":
#         player1Bullet["pos"][1] -= 1
#     elif player1Bullet["way"] == "right":
#         player1Bullet["pos"][1] += 1
#     elif player1Bullet["way"] == "up":
#         player1Bullet["pos"][0] -= 1
#     elif player1Bullet["way"] == "down":
#         player1Bullet["pos"][0] += 1
#
#     if player1Bullet["pos"] == pos_player2:
#         player1Bullet["pos"] = [0, 0]
#         player1Bullet["way"] = ""
#         player2Xp -= 1
#     elif game_map[player1Bullet["pos"][0]][player1Bullet["pos"][1]] == 1:
#         player1Bullet["pos"] = [0, 0]
#         player1Bullet["way"] = ""
#     elif game_map[player1Bullet["pos"][0]][player1Bullet["pos"][1]] == 3:
#         game_map[player1Bullet["pos"][0]][player1Bullet["pos"][1]] = 0
#         player1Bullet["pos"] = [0, 0]
#         player1Bullet["way"] = ""
#
# def game():
#     engine = sdk.GameEngineClient()
#
#     game_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
#                 [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 3, 0, 1],
#                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
#                 [1, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 1, 0, 0, 1],
#                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 1],
#                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
#
#     engine.start()
#
#     team1 = engine.teams[0]
#     team1.name = 'first'
#     left_history = []
#     rotation = 0
#     player1 = team1.players[0]
#     player1.name = 1
#
#     team2 = engine.teams[1]
#     team2.name = 'second'
#
#     player2 = team2.players[0]
#     player2.name = 2
#     pos_player2 = [0, 0]
#
#     player2Xp = 5
#     player1Xp = 5
#
#     player1Bullet = {"pos": [0, 0], "way": ""}
#     integr = 0
#
#     pos_player1 = [6, 2]
#     player1Way = {"way": "up"}
#
#     while True:
#         integr += 1
#         #result1 = sdk.timeout_run(0.4, player1.script, "make_choice", [left_history])
#         result1 = make_choice()
#         if integr == 4:
#             integr = 0
#             player1Bullet["pos"] = [0, 0]
#             MoveTanks(result1, game_map, pos_player1, player1Way)
#             print(result1)
#             Fire(game_map, result1, pos_player1, player1Xp, player1Bullet, pos_player2, player2Xp, player1Way)
#
#         Bullet_up(player1Bullet, pos_player1, game_map, player2Xp)
#         frame = {"field": game_map,
#                  "x": pos_player1[0],
#                  "y": pos_player1[1],
#                  "bullet":
#                      {"bx": player1Bullet["pos"][0],
#                       "by": player1Bullet["pos"][1],
#                       "way": player1Bullet["way"]},
#                  "ways": player1Way['way']}
#
#         engine.send_frame(frame)
#         time.sleep(0.7)
#
#     engine.end()
#
#
# if __name__ == "__main__":
#     game()
