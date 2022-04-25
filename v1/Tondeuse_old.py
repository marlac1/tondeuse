class Tondeuse(object):

    compass = ["N", "S", "E", "W"]
    def __init__(self, x, y, orientation, instructions, surface):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.instructions = instructions
        self.surface = surface

    #this function is called when iterating over "A" character from all_orientations list
    #it aims to assign k to the right orientation, depending on the previous character appended to all_orientations list
    def a_instruction(self, all_orientations):
        k = ""
        for i in all_orientations:
            if len(all_orientations) < 2:
                k = i
            #when the list is composed of several characters, k is the last compass character of
            else:
                a = "A"
                new_all_orientations = [elem for elem in all_orientations if elem != a]
                if len(new_all_orientations) < 1:
                    k = i
                else:
                    k = new_all_orientations[-1]
        all_orientations.append("A")
        return all_orientations


    def set_k(self, all_orientations, k):
        if len(all_orientations) > 1 and all_orientations[-1] in self.compass:
            all_orientations[-1] = k
        else:
            all_orientations.append(k)
        return all_orientations


    #returns a list of characters : orientations (values from compass) and "A" instructions
    #this list is made of values assigned to "k" variables
    #the purpose of this function is to assign the right orientation values to k, then to append them to the list
    def treat_instructions(self):
        all_orientations = []
        k = self.orientation
        for i in range(0, len(self.instructions)):
            if k == "N":
                if self.instructions[i] == "G":
                    k = "W"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "D":
                    k = "E"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "A":
                    self.a_instruction(all_orientations)
            elif k == "S":
                if self.instructions[i] == "G":
                    k = "E"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "D":
                    k = "W"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "A":
                    self.a_instruction(all_orientations)
            elif k == "E":
                if self.instructions[i] == "G":
                    k = "N"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "D":
                    k = "S"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "A":
                    self.a_instruction(all_orientations)
            elif k == "W":
                if self.instructions[i] == "G":
                    k = "S"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "D":
                    k = "N"
                    self.set_k(all_orientations, k)
                elif self.instructions[i] == "A":
                    self.a_instruction(all_orientations)
            elif k == "A":
                self.a_instruction(all_orientations)
            if all_orientations[0] == "A":
                all_orientations.insert(0, self.orientation)
        return all_orientations, self.x, self.y

    #decrement on orientations list to find the previous one
    def find_previous_orientation(self, str_instructions, i):
        for j in range(i - 1, -1, -1):
            if str_instructions[j] in self.compass:
                if str_instructions[j] == "N":
                    self.y += 1
                    break
                elif str_instructions[j] == "S":
                    self.y -= 1
                    break
                elif str_instructions[j] == "E":
                    self.x += 1
                    break
                elif str_instructions[j] == "W":
                    self.x -= 1
                    break
        return self.x, self.y

    #returns final mower's position, self.x and self.y
    #input : list of orientations
    def get_x_get_y(self):
        surface = self.surface
        surfacex = int(surface[0])
        surfacey = int(surface[1])
        all_orientations = self.treat_instructions()[0]
        str_instructions = ""
        for i in all_orientations:
            str_instructions += i
        for i in range(len(str_instructions)):
            if str_instructions[i] == "A":
                if (self.x < surfacex and self.y < surfacey) and str_instructions[i - 1] == "A":
                    self.find_previous_orientation(str_instructions, i)
                elif (self.x < surfacex or self.y < surfacey) and str_instructions[i - 1] in self.compass:
                    if str_instructions[i - 1] == "N":
                        self.y += 1
                    elif str_instructions[i - 1] == "S":
                        self.y -= 1
                    elif str_instructions[i - 1] == "E":
                        self.x += 1
                    elif str_instructions[i - 1] == "W":
                        self.x -= 1
        return self.x, self.y

    #returns final mower's orientation
    def final_orientation(self):
        all_orientations = self.treat_instructions()[0]
        str_orientations = ""
        for i in all_orientations:
            str_orientations += i
        new_str_orientation = str_orientations.replace("A", "")
        if len(new_str_orientation) == 0:
            return self.orientation
        else:
            self.orientation = new_str_orientation[-1]
            return self.orientation