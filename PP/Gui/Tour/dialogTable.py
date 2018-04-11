# определяет таблицу имя:обработчик с демонстрационными примерами
from tkinter.filedialog   import askopenfilename # импортировать стандартные
from tkinter.colorchooser import askcolor        # диалоги из Lib\tkinter
from tkinter.messagebox   import askquestion, showerror
from tkinter.simpledialog import askfloat
demos = {
    'Открыть':  askopenfilename,
    'Цвет': askcolor,
    'Запрос': lambda: askquestion('Внимание', 'Вы ввели "rm *"\nПодтвердить?'),
    'Ошибка': lambda: showerror('Ошибка!', "Оно мертво!"),
    'Ввод': lambda: askfloat('Ввод', 'Введите номер')
}
