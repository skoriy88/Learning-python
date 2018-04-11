"""
выводит все изображения, имеющиеся в каталоге, в виде миниатюр на кнопках,
щелчок на которых приводит к выводу полноразмерного изображения; требует
наличия пакета PIL для отображения JPEG-файлов и создания миниатюр; что сделать:
добавить прокрутку, если в окне выводится слишком много миниатюр!
"""

import os, sys, math
from tkinter import *
from PIL import Image # <== required for thumbs
from PIL.ImageTk import PhotoImage # <== required for JPEG display

def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    """
    создает миниатюры для всех изображений в каталоге; для каждого изображения
    создается и сохраняется новая миниатюра или загружается существующая;
    при необходимости создает каталог thumb;
    возвращает список кортежей (имя_файла_изображения, объект_миниатюры);
    для получения списка файлов миниатюр вызывающая программа может также
    воспользоваться функцией listdir в каталоге thumb; для неподдерживаемых
    типов файлов может возбуждать исключение IOError, или другое;
    ВНИМАНИЕ: можно было бы проверять время создания файлов;
    """
    thumbdir = os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)
    thumbs = []
    for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir, imgfile)
        if os.path.exists(thumbpath):
            thumbobj = Image.open(thumbpath)                # использовать существующую
            thumbs.append((imgfile, thumbobj))
        else:
            print('making', thumbpath)
            imgpath = os.path.join(imgdir, imgfile)
            try:
                imgobj = Image.open(imgpath)                # создать новую миниатюру
                imgobj.thumbnail(size, Image.ANTIALIAS)     # фильтр, дающий
                                                            # лучшее качество при
                                                            # уменьшении размеров
                imgobj.save(thumbpath)                      # тип определяется расширением
                thumbs.append((imgfile, imgobj))
            except:                                         # не всегда IOError
                print("Skipping: ", imgpath)
    return thumbs

class ViewOne(Toplevel):
    """
    открывает одно изображение в новом окне; ссылку на объект PhotoImage
    требуется сохранить: изображение будет утрачено при утилизации объекта;
    """

    def __init__(self, imgdir, imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)
        imgobj = PhotoImage(file=imgpath)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())  # размер в пикселях
        self.savephoto = imgobj  # сохранить ссылку на изображение


def viewer(imgdir, kind=Toplevel, cols=None):
    """
     создает окно с миниатюрами для каталога с изображениями: по одной кнопке с
    миниатюрой для каждого изображения;
    используйте параметр kind=Tk, чтобы вывести миниатюры в главном окне, или
    Frame (чтобы прикрепить к фрейму); значение imgfile изменяется в каждой
    итерации цикла: ссылка на значение должна сохраняться по умолчанию;
    объекты PhotoImage должны сохраняться: иначе при утилизации изображения
    будут уничтожены;
    компонует в ряды фреймов (в противоположность сеткам, фиксированным
    размерам, холстам);
    """
    win = kind()
    win.title('Viewer: ' + imgdir)
    quit = Button(win, text='Quit', command = win.quit, bg ='beige')    # добавить
    quit.pack(fill=X, side=BOTTOM)                                      # первой, чтобы урезалась последней
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))  # фиксированное или N x N
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)
    return win, savephotos
if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'D:/Projects/python/Gifs/'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()


