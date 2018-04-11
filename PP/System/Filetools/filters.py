import sys
def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line)) # записать измененную строку

def filter_stream(function):
    for line in sys.stdin:         # автоматически выполняет построчное чтение
        print(function(line), end='')

if __name__ == '__main__':
    filter_stream(lambda line: line)   # копировать stdin в stdout, если
                                       # запущен как самостоятельный сценарий
