def read(path):
    data = []
    for line in open(path):
        edge = []
        for i in line.split(" "):
            if i.startswith("0."):
                edge.append(float(i))
            else:
                edge.append(int(i))
            #print(edge[-1])

        data.append(edge)

    return data