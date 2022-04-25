import TondeuseUpdated as t
import InputDatasUpdated as id

#MAIN TEST :

#extract datas from the input text file
file_datas = id.InputDatasUpdated()
input_file = file_datas.find_input_file()
datas = file_datas.read_and_return_all_datas(input_file)
surface = file_datas.read_and_return_all_datas(input_file)[0]
cleaned_datas = file_datas.remove_dg_gd_occurrences(datas)
new_datas = file_datas.extract_tondeuse_datas(datas)
#print(f"NEW DATAS {new_datas}")

#return final orientation and position of the mower
for i in new_datas:
    x = i[0]
    y = i[1]
    orientation = i[2]
    instructions = i[2] + i[3]
    tondeuse = t.TondeuseUpdated(x, y, orientation, instructions, surface)
    tondeuse.move(instructions)
