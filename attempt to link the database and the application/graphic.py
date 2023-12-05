
import PySimpleGUI as sg 
import random
import webbrowser
import requests 
import time

from main import add,print_base, authentification, delete_user, delete_task
import webview as wv

def get_current_url(window):
    sg.PopupError('Не закрывайте окно после авторизации до надписи "ID записан"')
    time.sleep(30)
    global string
    string = (window.get_current_url())
    sg.PopupError('URL записан')
    

def UI_print(User_ID : int, all_users : bool ) : 
    text = str()
    None_base = print_base(User_ID, all_users)
    if None_base != None : 
        for i in None_base : 
            text+= str(i['Person_ID']) + ' ' + str(i['task_ID']) + ' ' + str(i['Nickname']) + '  ' + str(i['Description']) + '\n'
        sg.PopupScrolled('Список задач' , text)
    else : 
        sg.PopupScrolled('Список задач пуст!')


start_layout = [ [sg.Button('Аутентификация', enable_events=True, key = '-authentification-', font = 'Helvetica 16')],
                [sg.Button('Аутентификация через ВК', enable_events=True, key = '-vk_authentification-', font = 'helvetica16')],
                [sg.Button('Регистрация', enable_events=True, key = '-registration-', font = 'Helvetica 16')] ] 

layout = [[sg.Button('Добавить задачу',enable_events=True, key='-add_task-', font='Helvetica 16')],
          [sg.Button('Отобразить базу мои задачи',enable_events=True, key='-print-', font='Helvetica 16')], 
        # затем делаем текст
        ]

admin_layout = [ 
               [sg.Button('Добавить задачу',enable_events=True, key='-add_task-', font='Helvetica 16')],
               [sg.Button('Отобразить базу мои задачи',enable_events=True, key='-print-', font='Helvetica 16')],
               [sg.Button('Отобразить базу данных всех задач',enable_events=True, key='-print_admin-', font='Helvetica 16')],
               [sg.Button('Удалить пользователя по ID', enable_events = True, key = '-delete_user-', font = 'Helvetca 16')],
               [sg.Button('Удалить задачу по ID', enable_events = True, key = '-delete_task-', font = 'Helvetca 16')]
]

# рисуем окно
window = sg.Window('Task-manager', layout, size=(500,200))
admin_window = sg.Window('Admin Task-manager', admin_layout, size =(600, 300))
start_window = sg.Window('Task-manager', start_layout, size=(500,200))
User_ID = 1
Admin = False 
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
        elif (User_ID[0] > -1 ) : 
            sg.PopupError('Авторизация успешна')
            Admin = User_ID[1] 
            User_ID = User_ID[0]
            break 
    elif event == '-vk_authentification-' : 
        #print(webbrowser.open('https://oauth.vk.com/authorize?client_id=51727595&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131&state=asihiohoih', 1) ) 
        k = 0 
        local_window = wv.create_window('После авторизации закройте окно!', 'https://oauth.vk.com/authorize?client_id=51727595&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131&scope=offline')
        string = 'я пустой'
        wv.start(get_current_url, local_window)
        print(string)
        for i in range(0,len(string)) : 
            if string[-i] == '=' : 
                i-=1 
                break 
        id_token = '' 
        while (i > 0 )  : 
            id_token+= string[-i] 
            i-= 1
        print(id_token)
        User_ID = authentification(id_token, 'lksj5dfwe1234iojf', True )
        if User_ID == -1 : 
            User_ID = authentification(id_token, 'lksj5dfwe1234iojf', False )
            if (User_ID == -2 ) : 
                sg.PopupError('Логин/пароль не подходят')
            elif (User_ID[0] > -1 ) : 
                sg.PopupError('Авторизация успешна')
                Admin = User_ID[1] 
                User_ID = User_ID[0]
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


if Admin == False : 
    while Login_succes : 
        event, values = window.read()
        # если нажали на крестик
        if event == '-add_task-' : 
            add(sg.PopupGetText('Введите описание задачи'), User_ID)
        elif event == '-print-' : 
            UI_print(User_ID, False)
        elif event in (sg.WIN_CLOSED, 'Exit'):
            # выходим из цикла
            break
else : 
    while Login_succes : 
        event, values = admin_window.read() 
        if event == '-add_task-' : 
            add(sg.PopupGetText('Введите описание задачи'), User_ID)
        elif event == '-print_admin-': 
            UI_print(User_ID, True)
        elif event == '-print-' : 
            UI_print(User_ID, False)
        elif event == '-delete_task-' :
            task_ID = sg.PopupGetFile('Введите номер удаляемой задачи')
            if (delete_task(task_ID ) == 1 ) : 
                sg.PopupError("Удаление успешно!")
            else : 
                sg.PopupError("Ошибка!")
        elif event == '-delete_user-' : 
            delete_user(sg.PopupGetText('Введите номер удаляемого пользователя'))
        elif event in (sg.WIN_CLOSED, 'Exit'):
            # выходим из цикла
            break 




# закрываем окно и освобождаем используемые ресурсы
window.close()