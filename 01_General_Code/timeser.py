def times_table_wey_dey_jump_5():
    for i in range(2, 13):
        if i == 5:
            continue
        for j in range(1, 13):
            print("{} times {} is {}".format(i, j, i * j))