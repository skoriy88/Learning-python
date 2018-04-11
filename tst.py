def tester(start):
    state = start  # Каждый вызов сохраняет отдельный экземпляр state

    def nested(label):
        nonlocal state  # Объект state находится в объемлющей области видимости
        print(label, state)
        state += 1  # Изменит значение переменной, объявленной как nonlocal
    return nested

F = tester(0)
F('spam')

G = tester(5)
G('maps')

F('ham')
G('mah')

import modules.formats
print(dir(modules.formats))


import random
help(random)