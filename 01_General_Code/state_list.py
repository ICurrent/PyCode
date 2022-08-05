state_south_west = ["lagos","ogun","oyo","ondo","ekiti"]
state_south_east = ["anambra","imo","enugu","abia","ebonyi"]
state_oil_producing = ["rivers","delta","ondo","bayelsa","crossriver"]
print(type(state_south_west))
print(state_south_west.pop())
print(state_south_west)
print(len(state_south_west))
state_south_west.sort()
print(state_south_west)
state_south_west.append("me")
print(state_south_west)
sex = ["male","female"]
sex.append("unknown")
print(sex)
print(sex.insert(1, "anambra"))
print(state_south_west[1:4])

address = [1,2,3,4,5,6,7,8,"nine","ten"]
print(state_oil_producing)
print(state_south_west)
print(state_south_west[1])
print(state_south_west[4])
print(state_south_west[2],state_south_east[2:4],state_oil_producing[1:4])
new_state = [state_south_west[2],state_south_east[2:4],state_oil_producing[1:4]]
print(new_state)
newer_state = [state_south_west[2],state_south_east[2], state_south_east[4],state_oil_producing[1],state_oil_producing[4]]
print(newer_state)
print(new_state[1][1])
print("i am from {} but I live in {}".format(state_south_west[2], state_south_west[0]))
#mr victor
print(address[8], address[9])
#mr bassey
print(address[8], [9])
print(state_oil_producing.index("bayelsa"))
state_oil_producing.insert(3,"ekiti")
print(state_oil_producing)
print(state_oil_producing.index("bayelsa"))



