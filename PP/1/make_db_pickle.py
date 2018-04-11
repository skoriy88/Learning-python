from initdata import db
import pickle
dbfile = open('people-pickle', 'wb') # в версии 3.X следует использовать
pickle.dump(db, dbfile)              # двоичный режим работы с файлами, так как
dbfile.close()                       # данные имеют тип bytes, а не str
