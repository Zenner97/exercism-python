from re import sub


def encode(line):
    result = sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(1), line)
    return result


def decode(line):
    result = sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), line)
    return result
