import sys
class InputDatas(object): #représente les données fichier

    #returns input_file
    def find_input_file(self):
        input_file = sys.argv[1]
        return input_file

    #returns surface and mower datas
    def read_and_return_all_datas(self, input_file):
        datas = []
        with open(input_file, 'r') as f:
            all_datas = f.readlines()
            surface = all_datas[0]
            for i in range(1, len(all_datas)):
                datas.append(str(all_datas[i]).replace("\n", ""))
        return surface, datas

    #returns a cleaned list data representing the mower, without "GD" and "DG" occurrences
    def remove_dg_gd_occurrences(self, datas):
        datas = datas[1]
        for i in range(len(datas)):
            if datas[i].find("DG") > -1:
                datas[i] = datas[i].replace("DG", "")
            if datas[i].find("GD") > -1:
                datas[i] = datas[i].replace("GD", "")
        return datas

    #returns a formatted representation of the meower : [(x, y, orientation, instructions]
    def extract_tondeuse_datas(self, datas):
        datas = datas[1]
        datas_tup = []
        for i in range(0, len(datas), 2):
            datas_tup.append((int(datas[i][0]), int(datas[i][1]), datas[i][2], datas[i + 1]))
        return datas_tup
