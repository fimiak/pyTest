def letters(*args):
    for arg in args:
        morphed = arg.split()
        upper = arg.upper()
        print(morphed[0] + upper)


def nums(*args):
    args = list(args)

    letters(*args)

nums('air', 'water', 'earth', 'fire')
