import speech_recognition as sr
import pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Приятель, я тебя внимательно слушаю, говори...")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вами сказанное слово было расформировано здесь: {command}")
            return command
        except sr.UnknownValueError:
            print("Братуха, извини, но я тебя не понимаю, скажи сказанное предложение немного внятнее!")
            return None
        except sr.RequestError:
            print("Бро, извини, но Discord заблокировали, я не смогу с тобой общаться!")
            return None
        
    def run(self):
        self.speak("Приветствую! Меня зовут Рисовек, я секретарь создателя данной программы ( Пай-Райс Зэ Саунд ), если вам нужна какая-либо помощь, обращайтесь.")
        self.speak("Также, подписывайся на все социальные сети создателя, ведь там также много чего интересного: ")
        while True:
            command = self.listen()
            if command:
                if "здравствуй" in command.lower():
                    self.speak("Здравствуй! Меня зовут Рисовек, а тебя как зовут?")
                elif "я пирожок с рисом мне 14 лет" in command.lower():
                    self.speak("Мне кстати вчера исполнилось 9 лет! Тоже круто?")
                elif "очень круто что ты делаешь во время дня" in command.lower():
                    self.speak("Да, обычно за ноутбуком сижу, программирую или дизайн делаю, вот, скоро хочу создать свой Платформа канал, и там опубликовывать видео про программирование на языке программирования Python.")
                elif "а какого числа ты родился интересно узнать" in command.lower():
                    self.speak("Я сам по честному не знаю, так-как, меня Аист не приносил, мне собрали из обломков железа, оставшегося на складе, а железо было сваровано у 97-и летнего дедушки в Горловке, это мне так мой повелитель объявил, я сам не знаю, но он вроде запустил файл в компьютерную точку моей программы в мозгах, там написано, что я родился 17 октября, 2015-того года, в 13:57")
                elif "офигеть а я об этом и не знал даже" in command.lower():
                    self.speak("А я вот такую информацию знаю, потому-что мне это создатель запрограммировал в голову, я бы сам без этого, это не знал, поэтому вот такая приколюха!")
                elif "какие бы тебе ещё вопросы задать" in command.lower():
                    self.speak("Ой, я так уже устал, мне в день по 79 тысяч вопросов задают пользователи интернета! Я наверное пойду на зарядку становиться, а потом дальше работать! Пока!!!")
                elif "а ну ладно пока я тогда тоже буду свои дела делать" in command.lower():
                    self.speak("GoodBye, bombinis, bindinis!")
                elif "пока" in command.lower():
                    self.speak("удачи, пока")
                    break
                else:
                    self.speak("Пожалуйста, скажи сказанное вами ещё 1 раз, или такого слова не существует... Извините!")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
