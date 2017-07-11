# def distance(line1, line2):
#     count = 0
#     if line1 == line2:
#         return 0
#     while line1 != line2:
#         count = count + 1
#         return count


def distance(line1, line2):
    count = 0
    index = 0

    if len(line1) != len(line2):
        raise ValueError

    while index < len(line1):
        if line1[index] != line2[index]:
            count += 1
        index += 1
    return count
