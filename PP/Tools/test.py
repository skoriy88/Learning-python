from visitor import FileVisitor
import sys
dolist   = 1
dosearch = 2                             # 3 = список и поиск
donext   = 4                             # при добавлении следующего теста


#visitor = FileVisitor(trace=2)
path = sys.argv[2]
print(path)
#visitor.run(path)
#print('Visited %d files and %d dirs' % (visitor.fcount, visitor.dcount))
