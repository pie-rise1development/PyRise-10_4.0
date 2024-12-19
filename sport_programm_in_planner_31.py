class Workout:
    def __init__(self, name, duration, calories):
        self.name = name
        self.duration = duration    # Время в минутах
        self.calories = calories      # Сожжённые калории

class FitnessApp:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)
        print(f'Новый комплекс упражнений в одной тренировке был добавлен: {workout.name}')

    def show_workouts(self):
        print('\nКоличество добавленных вами тренировок: ')
        for idx, workout in enumerate(self.workouts, start=1):
            print(f'{idx}. {workout.name} - {workout.duration} минут, {workout.calories} сожжённых калорий')

    def total_calories_burned(self):
        total_calories = sum(workout.calories for workout in self.workouts)
        print(f'\nКоличество калорий, которые вы сожгли: {total_calories}')

def main():
    app = FitnessApp()

    while True:
        print("\nПожалуйста выберите действие, с чего хотите начать:")
        print("- 1. } Создать новый комплекс упражнений в вашей тренировке.")
        print("- 2. } Просмотреть все добавленные вами тренировки.")
        print("- 3. } Показать общее количество сожжённых вами калорий.")
        print("- 4. } Выйти из программы!")

        choice = input("Напишите номер раздела, который хотите открыть:  ")

        if choice == '1':
            name = input("Напишите название тренировки: ")
            duration = int(input("Сколько по времени будет проходить ваша тренировка ( в минутах ): "))
            calories = int(input("Введите количество сожжённых вами калорий: "))
            workout = Workout(name, duration, calories)
            app.add_workout(workout)
        elif choice == '2':
            app.show_workouts()
        elif choice == '3':
            app.total_calories_burned()
        elif choice == '4':
            print("Вы успешно покинули мою Fitness программу, приходите ещё, тренироваться никогда не поздно!")
            break
        else:
            print("Эй! Вы ввели неправильный номер пункта, попробуйте ещё раз...")

if __name__ == '__main__':
    main()