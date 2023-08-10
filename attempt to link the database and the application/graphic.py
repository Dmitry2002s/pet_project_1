
import PySimpleGUI as sg 
import random
from main import add,print_base, authentification 

start_layout = [ [sg.Button('Аутентификация', enable_events=True, key = '-authentification-', font = 'Helvetica 16')], 
                [sg.Button('Регистрация', enable_events=True, key = '-registration-', font = 'Helvetica 16')] ] 

layout = [[sg.Button('Добавить задачу',enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
          [sg.Button('Отобразить базу данных',enable_events=True, key='-print-', font='Helvetica 16')], 
        # затем делаем текст
        [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]

# рисуем окно
window = sg.Window('Task-manager', layout, size=(500,200))
start_window = sg.Window('Task-manager', start_layout, size=(500,200))
User_ID = 1
# запускаем основной бесконечный цикл
Login_succes = True 
while True :
    # получаем события, произошедшие в окне
    event, values = start_window.read()
    if event == '-authentification-' : 
        nick = sg.PopupGetText('Введите логин ')
        password  = sg.PopupGetText('Введите пароль ')
        User_ID = authentification(nick, password , False )
        if (User_ID == -2 ) : 
            sg.PopupError('Логин/пароль не подходят')
        elif (User_ID > -1 ) : 
            sg.PopupError('Авторизация успешна')
            break 
    elif event == '-registration-' : 
        nick = sg.PopupGetText('Введите логин создаваемого пользователя  ')
        password  = sg.PopupGetText('Введите пароль создаваемого пользователя')
        User_ID = authentification(nick, password, True )
        if User_ID == -1 : 
            print('Такой пользователь уже существует ')
            sg.PopupError('Такой пользователь уже существует')
    elif event in (sg.WIN_CLOSED, 'Exit'): # Выходим из цикла 
        Login_succes = False 
        break
while Login_succes : 
    event, values = window.read()
    # если нажали на крестик
    if event == '-FUNCTION-' : 
        add(sg.PopupGetText('Введите описание задачи'), User_ID)
    elif event == '-print-' : 
        text = str()
        for i in print_base(User_ID) : 
            text+= str(i['task_ID']) + '  ' + str(i['Description']) + '\n'
        sg.PopupScrolled('Список задач' , text)
    elif event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
# закрываем окно и освобождаем используемые ресурсы
window.close()