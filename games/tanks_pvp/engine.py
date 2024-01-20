import ge_sdk as sdk
import random
import time

def make_choice():
    actions = ["up", "down", "left", "right", "fire_up", "fire_down", "fire_right", "fire_left"]
    return random.choice(actions)


class PLayer:
    def __init__(self, result, gameMap, player, bullet, enemy):
        self.__result = result
        self.__gameMap = gameMap
        self.__player = player
        self.__bullet = bullet
        self.__enemy = enemy

    def moveTank(self):
        if self.__result == 'left' and self.__gameMap[self.__player['pos'][0]][self.__player['pos'][1] - 1] not in [1, 3]:
            self.__player['pos'][1] = self.__player['pos'][1] - 1
            self.__player["way"] = "left"
        elif self.__result == 'right' and self.__gameMap[self.__player['pos'][0]][self.__player['pos'][1] + 1] not in [1, 3]:
            self.__player['pos'][1] = self.__player['pos'][1] + 1
            self.__player["way"] = "right"
        elif self.__result == 'down' and self.__gameMap[self.__player['pos'][0] + 1][self.__player['pos'][1]] not in [1, 3]:
            self.__player['pos'][0] = self.__player['pos'][0] + 1
            self.__player["way"] = "down"
        elif self.__result == 'up' and self.__gameMap[self.__player['pos'][0] - 1][self.__player['pos'][1]] not in [1, 3]:
            self.__player['pos'][0] = self.__player['pos'][0] - 1
            self.__player["way"] = "up"

    def createBullet(self):
        if self.__result == 'fire_up':
            self.__bullet["pos"] = [self.__player['pos'][0], self.__player['pos'][1]]
            self.__bullet["way"] = "up"
            self.__player['way'] = "up"
        elif self.__result == 'fire_down':
            self.__bullet["pos"] = [self.__player['pos'][0], self.__player['pos'][1]]
            self.__player["way"] = "down"
            self.__bullet['way'] = "down"
        elif self.__result == 'fire_right':
            self.__bullet["pos"] = [self.__player['pos'][0], self.__player['pos'][1]]
            self.__bullet["way"] = "right"
            self.__player['way'] = "right"
        elif self.__result == 'fire_left':
            self.__bullet["pos"] = [self.__player['pos'][0], self.__player['pos'][1]]
            self.__bullet["way"] = "left"
            self.__player['way'] = "left"

    def moveBullet(self):
        if self.__bullet["way"] == "left":
            self.__bullet["pos"][1] -= 1
        elif self.__bullet["way"] == "right":
            self.__bullet["pos"][1] += 1
        elif self.__bullet["way"] == "up":
            self.__bullet["pos"][0] -= 1
        elif self.__bullet["way"] == "down":
            self.__bullet["pos"][0] += 1

        if self.__bullet["pos"] == self.__enemy["pos"]:
            self.__bullet["pos"] = [0, 0]
            self.__bullet["way"] = ""
            self.__enemy['xp'] -= 1
        elif self.__gameMap[self.__bullet["pos"][0]][self.__bullet["pos"][1]] == 1:
            self.__bullet["pos"] = [0, 0]
            self.__bullet["way"] = ""
        elif self.__gameMap[self.__bullet["pos"][0]][self.__bullet["pos"][1]] == 3:
            self.__gameMap[self.__bullet["pos"][0]][self.__bullet["pos"][1]] = 0
            self.__bullet["pos"] = [0, 0]
            self.__bullet["way"] = ""

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

    player1Bullet = {"pos": [0, 0], "way": ""}
    player2Bullet = {"pos": [0, 0], "way": ""}
    playerIn1 = {"pos": [6, 1], "way": "", "xp": 1}
    playerIn2 = {"pos": [6, 6], "way": "", "xp": 1}
    integr = 0
    winners = {"player1": False, "player2": False, "winText": ""}
    while True:
        integr += 1
        result1 = make_choice()
        result2 = make_choice()
        tank1 = PLayer(result1, game_map, playerIn1, player1Bullet, playerIn2)
        tank2 = PLayer(result2, game_map, playerIn2, player2Bullet, playerIn1)

        if integr == 7:
            integr = 0
            player1Bullet["pos"] = [0, 0]
            player2Bullet["pos"] = [0, 0]
            tank1.moveTank()
            tank1.createBullet()
            tank2.moveTank()
            tank2.createBullet()
        tank1.moveBullet()
        tank2.moveBullet()

        if playerIn1['xp'] == 0:
            playerIn1 = {}
            del tank1
            winners['player2'] = True
            print(winners["player2"])
            winners['winText'] = "WINNNNNNNNN red player"
        if playerIn2['xp'] == 0:
            playerIn2 = {}
            del tank2
            winners['player1'] = True
            winners['winText'] = "WINNNNNNNNN blue player"

        frame = {"field": game_map,
                 "player1": playerIn1,
                 "player2": playerIn2,
                 "bullet1": player1Bullet,
                 "bullet2": player2Bullet,
                 "winner": winners}

        engine.send_frame(frame)
        if winners['player1'] or winners['player2']:
            engine.end()
            break
        time.sleep(0.2)

if __name__ == "__main__":
    game()