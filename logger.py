def log(user, string):
    with open('lab.log', "a") as f:
        f.write(user + ":" + string + "\n")
