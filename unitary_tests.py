import InputDatas as id
import Tondeuse as t

#INPUTDATAS TEST
print("INPUTDATAS UNOTARY TESTS")
the_file = id.InputDatas()

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
    instruction = i[3]
    tondeuse = t.Tondeuse(x, y, orientation, instruction, surface)

    fin_or = tondeuse.final_orientation()
    print(fin_or)#OK W #N

    treat_instr = tondeuse.treat_instructions()
    print(treat_instr)  # OK (['S', 'A', 'N', 'A', 'A', 'W', 'A', 'N', 'A', 'A'], 4, 4)
    # (['N', 'A', 'A', 'A', 'A'], 2, 2)

    x, y = tondeuse.get_x_get_y()
    print(f"{x}{y}") #KO ne passe pas : #36 #25
    #OK en test fonctionnel...

    a = tondeuse.a_instruction(['AAAA'])
    print(f"a = {a}")#OK ['AAAA', 'A']
    agd = tondeuse.a_instruction(['ANE'])
    print(f"agd = {agd}")#OK['ANE', 'A']

    k = tondeuse.set_k(['E', 'A', 'S'], 'W')
    print(f"k = {k}")#OK k = ['E', 'A', 'W']


