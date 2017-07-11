def is_isogram(line):
    line = line.lower().translate(None, ";\"!_:- ")
    if len(line) == len(set(line)):
        return True
    return False
