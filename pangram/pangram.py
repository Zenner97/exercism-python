def is_pangram(line):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(letter in line.lower() for letter in alphabet)
    # for letter in alphabet:
    #     if letter not in line:
    #         return False
    # return True
    #
