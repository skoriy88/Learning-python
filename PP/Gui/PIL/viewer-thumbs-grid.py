"""
то же, что и viewer_thumbs, но использует менеджер компоновки grid, чтобы
добиться более стройного размещения миниатюр; того же эффекта можно добиться
с применением фреймов и менеджера pack, если кнопки будут иметь фиксированный
и одинаковый размер;
"""
import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne
def viewer(imgdir, kind=Toplevel, cols=None):
    """
    измененная версия, размещает миниатюры по сетке
    """
    win = kind()
    win.title('Viewer: ' + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))# фиксированное или N x N
    rownum = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        colnum = 0
        for (imgfile, imgobj) in thumbsrow:
            photo   = PhotoImage(imgobj)
            link    = Button(win, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.grid(row=rownum, column=colnum)
            savephotos.append(photo)
            colnum += 1
        rownum += 1
    Button(win, text='Quit', command=win.quit).grid(columnspan=cols, stick=EW)
    return win, savephotos
if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'D:/Projects/python/Gifs/'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()