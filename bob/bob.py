def hey(message):
    line = message.strip()
    if line.isupper():
        return 'Whoa, chill out!'
    elif line.endswith('?'):
        return 'Sure.'
    elif line == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'

