from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.graphics import Color, Rectangle

class RiseFormat(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Название приложения.
        title_label = Label(text="Rise-TrueFormat1 ™", font_size=24, size_hint_y=None, height=50)
        self.layout.add_widget(title_label)

        # Элементы ввода
        self.name_input = self.create_input("[Фамилия] [Имя] [Отчество] ^_^: ")
        self.nickname_input = self.create_input("Введите ваше прозвише [начальный символ @] 🥰: ")
        self.email_input = self.create_input("[E-Mail] Yandex | E-Mail | другие мессенджеры... ✨: ")
        self.phone_input = self.create_input("Введите свой номер телефона [Tele2 | МегаФон | MTS и другие...] 📞: ")
        self.address_input = self.create_input("Местоположение [Адрес проживания (Страна, Область, Город) 🐱‍👓: ")

        # Кнопка.
        submit_button = Button(text="$ Отправить составленное. 🎈")
        submit_button.bind(on_press=self.submit)

        # Добавление всех элементов в пакет.
        self.layout.add_widget(self.name_input)
        self.layout.add_widget(self.nickname_input)
        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(self.address_input)
        self.layout.add_widget(submit_button)

        # Место для сообщения.
        self.thank_you_label = Label(text="", size_hint_y=None, height=40)
        self.layout.add_widget(self.thank_you_label)

        # Водяной знак.
        self.watermark = Label(text="Developed by Pie-Rise The Sound | [Developed] 🐍", size_hint_y=None, height=40)
        self.watermark.color = (1, 1, 1, 0.5) #Полупрозрачный
        self.layout.add_widget(self.watermark)

        return self.layout

    def create_input(self, placeholder):
        return TextInput(hint_text=placeholder, multiline=False)

    def submit(self, instance):
        # Получение ввода.
        name = self.name_input.text
        nickname = self.nickname_input.text
        email = self.email_input.text
        phone = self.phone_input.text
        address = self.address_input.text

        # Проверка пустых полей.
        if name and nickname and email and phone and address:
            self.thank_you_label.text = "Большое спасибо за тестирование! :-)"
            # Очистка полей.
            self.name_input.text = ""
            self.nickname_input.text = ""
            self.email_input.text = ""
            self.phone_input.text = ""
            self.address_input.text = ""
        else:
            self.thank_you_label.text = "Ошибка! Заполните все поля приложения..."

if __name__ == '__main__':
    RiseFormat().run()

