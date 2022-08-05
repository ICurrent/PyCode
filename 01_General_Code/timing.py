
def time():
    import time
    secomd = 1
    while (secomd < 120):
        if (secomd < 60):
            print("{}s".format(secomd))
            secomd +=1
            time.sleep(1)
        elif(secomd >= 60):
            print("1mins: {}s".format(secomd % 60))
            secomd += 1
            time.sleep(1)

time()