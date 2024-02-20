class Game:
    total_red = 12
    total_green = 13
    total_blue = 14

    minimum_blue = 0
    minimum_green = 0
    minimum_red = 0

    def __init__(self, game):
        self.game = game.split(":")
        self.id = int(self.game[0].split()[1])
        self.sets = self.game[1]

    def split_sets(self):
        separated_sets = self.sets.split(";")
        for i in range(len(separated_sets)):
            separated_sets[i] = separated_sets[i].split(",")
            for j in range(len(separated_sets[i])):
                separated_sets[i][j] = separated_sets[i][j].strip().split(" ")
        return separated_sets

    def check_validity(self, separated_sets):
        for one_set in separated_sets:
            for color in one_set:
                if color[1] == "blue":
                    if int(color[0]) > self.total_blue:
                        return False
                if color[1] == "red":
                    if int(color[0]) > self.total_red:
                        return False
                if color[1] == "green":
                    if int(color[0]) > self.total_green:
                        return False
        return True

    def set_minimum(self, separated_sets):
        for one_set in separated_sets:
            for color in one_set:
                if color[1] == "blue" and int(color[0]) > self.minimum_blue:
                    self.minimum_blue = int(color[0])
                if color[1] == "red" and int(color[0]) > self.minimum_red:
                    self.minimum_red = int(color[0])
                if color[1] == "green" and int(color[0]) > self.minimum_green:
                    self.minimum_green = int(color[0])




