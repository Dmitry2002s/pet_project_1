from kivy.app import App
from kivy.uix.widget import Widget



class Menu(Widget) : 
    pass 

class MenuApp(App): 
    def build(self) : 
        return Menu() 

class Task_manager(Widget) : 
    pass 

class Task_managerApp(App) :  # Когда вызываешь отсюда определение приложения он ищет всё, что до app  с с форматом kv 
    def build(self) : 
        return Task_manager()


if __name__ == '__main__':
    #тут должна быть функция, которая будет открывать то или иное окно при нажатии 
    if (False) : 
         MenuApp().run() 
    # Пока будем думать, что мы кнопкой вызываем окно, которое позволяет посмотреть раздел посвященный задачам
    # То есть -- 
    # 1. Посмотреть список задач 
    # 2. Быстро добавить ещё задачу (Пока без дат, баллов и прочего) 
    # ДЛЯ БЭКА 
    # НЕобходимо прописать логику хранения задач  
    if(True) : 
        Task_managerApp().run() 
        
