from kivy.app import App
from kivy.uix.widget import Widget



class Menu(Widget) : 
    pass 

class MenuApp(App): 
    def build(self) : 
        return Menu() 

class Task_manager(Widget) : 
    pass 

class Task_managerApp(App) :  # ����� ��������� ������ ����������� ���������� �� ���� ��, ��� �� app  � � �������� kv 
    def build(self) : 
        return Task_manager()


if __name__ == '__main__':
    #��� ������ ���� �������, ������� ����� ��������� �� ��� ���� ���� ��� ������� 
    if (False) : 
         MenuApp().run() 
    # ���� ����� ������, ��� �� ������� �������� ����, ������� ��������� ���������� ������ ����������� �������
    # �� ���� -- 
    # 1. ���������� ������ ����� 
    # 2. ������ �������� ��� ������ (���� ��� ���, ������ � �������) 
    # ��� ���� 
    # ���������� ��������� ������ �������� �����  
    if(True) : 
        Task_managerApp().run() 
        
