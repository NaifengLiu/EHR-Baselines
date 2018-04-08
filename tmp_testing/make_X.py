with open("./data/training/training.csv") as f:
    lines = f.readlines()
    length = len(lines[0].split(","))

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[0] != "" and q <= 5:
            print split[0]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[1] != "" and q <= 5:
            print split[1]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[2] != "" and q <= 5:
            print split[2]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[3] != "" and q <= 5:
            print split[3]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[4] != "" and q <= 5:
            print split[4]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[5] != "" and q <= 5:
            print split[5]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[6] != "" and q <= 5:
            print split[6]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[7] != "" and q <= 5:
            print split[7]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[8] != "" and q <= 5:
            print split[8]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[9] != "" and q <= 5:
            print split[9]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[10] != "" and q <= 5:
            print split[10]
            q += 1

    print "\n\n"

    q = 0
    for line in lines:
        split = line.rstrip().split(",")
        if split[11] != "" and q <= 5:
            print split[11]
            q += 1




