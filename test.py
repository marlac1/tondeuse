import Tondeuse as t
import InputDatas as id

#MAIN TEST :

#extract datas from the input text file
file_datas = id.InputDatas()
input_file = file_datas.find_input_file()
datas = file_datas.read_and_return_all_datas(input_file)
surface = file_datas.read_and_return_all_datas(input_file)[0]
cleaned_datas = file_datas.remove_dg_gd_occurrences(datas)
new_datas = file_datas.extract_tondeuse_datas(datas)

#return final orientation and position of the mower
for i in new_datas:
    x = i[0]
    y = i[1]
    orientation = i[2]
    instruction = i[3]
    tondeuse = t.Tondeuse(x, y, orientation, instruction, surface)
    x, y = tondeuse.get_x_get_y()
    print(f"{x}{y}{tondeuse.final_orientation()}")


#UNITARY TESTS
file_datas = id.InputDatas()
input_file = file_datas.find_input_file()
datas = file_datas.read_and_return_all_datas(input_file)
surface = file_datas.read_and_return_all_datas(input_file)[0]
cleaned_datas = file_datas.remove_dg_gd_occurrences(datas)
new_datas = file_datas.extract_tondeuse_datas(datas)

#return final orientation and position of the mower
for i in new_datas:
    x = i[0]
    y = i[1]
    orientation = i[2]
    instruction = i[3]
    tondeuse = t.Tondeuse(x, y, orientation, instruction, surface)
    x, y = tondeuse.get_x_get_y()
    print(f"{x}{y}{tondeuse.final_orientation()}")