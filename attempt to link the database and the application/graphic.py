
import PySimpleGUI as sg 
import random
from main import add,print_base 

layout = [[sg.Button('Добавить задачу',enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
          [sg.Button('Отобразить базу данных',enable_events=True, key='-print-', font='Helvetica 16')], 
        # затем делаем текст
        [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]

# рисуем окно
window = sg.Window('Task-manager', layout, size=(500,200))
# запускаем основной бесконечный цикл
while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event == '-FUNCTION-' : 
        add(sg.PopupGetText('Введите описание задачи'))
    elif event == '-print-' : 
        text = str()
        for i in print_base() : 
            text+= str(i['task_ID']) + '  ' + str(i['Description']) + '\n'
        sg.PopupScrolled('Список задач' , text)
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
# закрываем окно и освобождаем используемые ресурсы
window.close()