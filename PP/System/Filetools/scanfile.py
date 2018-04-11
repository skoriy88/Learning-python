def scanner(name, function):
    [function(line) for line in open(name, 'r')]

