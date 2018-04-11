from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']                # извлекает объект sue
sue['pay'] *= 1.50
db['sue'] = sue                # изменяет объект sue
db['tom'] = tom                # добавляет новую запись
db.close()
