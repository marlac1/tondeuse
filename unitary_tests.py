import InputDatasUpdated as id, TondeuseUpdated as t

#INPUTDATAS TEST
print("INPUTDATAS UNITARY TESTS")
the_file = id.InputDatasUpdated()

input_file = the_file.find_input_file()
print(input_file) # OK input.txt

all_datas = the_file.read_and_return_all_datas(input_file)
print(all_datas) #OK ('55\n', ['44S', 'GADDAAGADAA', '22N', 'AADGGDADGA'])

cleaned_datas = the_file.remove_dg_gd_occurrences(all_datas)
print(cleaned_datas)#OK ['44S', 'GADDAAGADAA', '22N', 'AAAA']

datas = the_file.extract_tondeuse_datas(all_datas)
print(datas) #OK [(4, 4, 'S', 'GADDAAGADAA'), (2, 2, 'N', 'AAAA')]

#TONDEUSE TESTS
print("TONDEUSE UNITARY TESTS")
surface = the_file.read_and_return_all_datas(input_file)[0]

for i in datas:
    x = i[0]
    y = i[1]
    orientation = i[2]
    instructions = i[2] + i[3]
    tondeuse = t.TondeuseUpdated(x, y, orientation, instructions, surface)
    tondeuse.move(instructions) #OK 13W 25N
    print(tondeuse.a_instruction()) #OK (0, 3) (2, 5)


