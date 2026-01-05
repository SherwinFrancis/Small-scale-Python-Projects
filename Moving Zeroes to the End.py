def move_zeros(lst):
    output = []
    count = 0
    for i in range(0,len(lst)):
        if str(lst[i]) == "0":
            count += 1
        else:
            output.append(lst[i])
    for i in range (0, count):
        output.append(0)
    return output