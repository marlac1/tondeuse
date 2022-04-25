class TondeuseUpdated(object):

    def __init__(self, x, y, orientation, instructions, surface):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.instructions = instructions
        self.surface = surface

    def a_instruction(self):
        if self.orientation == "N" and self.y < int(self.surface[1]):
            self.y += 1
        elif self.orientation == "S":
            self.y -= 1
        elif self.orientation == "E" and self.x < int(self.surface[0]):
            self.x += 1
        elif self.orientation == "W":
            self.x -= 1
        return self.x, self.y


    def move(self, ins):
        self.orientation = ins[0]
        for i in range(len(ins)):
            if self.orientation == "N":
                if ins[i] == "G":
                    self.orientation = "W"
                if ins[i] == "D":
                    self.orientation = "E"
            elif self.orientation == "S":
                if ins[i] == "G":
                    self.orientation = "E"
                if ins[i] == "D":
                    self.orientation = "W"
            elif self.orientation == "E":
                if ins[i] == "G":
                    self.orientation = "N"
                if ins[i] == "D":
                    self.orientation = "S"
            elif self.orientation == "W":
                if ins[i] == "G":
                    self.orientation = "S"
                if ins[i] == "D":
                    self.orientation = "N"
            if ins[i] == "A":
                self.a_instruction()
        print(f"{self.x}{self.y}{self.orientation}")
        return self.x, self.y, self.orientation
