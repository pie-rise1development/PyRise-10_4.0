from PIL import Image


def image_to_ascii(image_path, output_path, width=100):
    # Открываем изображение по указанному пути
    img = Image.open(image_path)
    # Конвертируем изображение в градации серого ('L' - режим grayscale)
    img = img.convert('L')
    # Вычисляем соотношение сторон изображения
    aspect_ratio = img.height / img.width
    # Определяем новую высоту, сохраняя соотношение сторон
    new_height = int(aspect_ratio * width * 0.55)
    # Изменяем размер изображения согласно новым параметрам
    img = img.resize((width, new_height))

    # Получаем пиксельные данные изображения
    pixels = img.getdata()
    # Определяем набор символов для ASCII
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    # Преобразуем пиксели в ASCII символы
    ascii_str = "".join([chars[pixel // 25] for pixel in pixels])
    # Получаем длину строки ASCII
    ascii_str_len = len(ascii_str)
    # Формируем строку ASCII изображения с нужной шириной
    ascii_img = "\n".join([ascii_str[index: index + width] for index in range(0, ascii_str_len, width)])

    # Формируем файл в режиме для записи
    with open(output_path, "w") as f:
        # Записываем ASCII изображение в файл
        f.write(ascii_img)


image_to_ascii('C:/Users/dmitr/Desktop/PyFilesCDS/instruments/ban.jpg', 'C:/Users/dmitr/Desktop/PyFilesCDS/instruments/word_s.txt')
