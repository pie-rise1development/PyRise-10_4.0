from moviepy.editor import VideoFileClip

# Загружаем видеофайл
video = VideoFileClip("Вводите путь к скачанному вами видео-ролику [ со звуком ]")

# Создаём видео без звука
silent_video = video.without_audio()

# Сохраняем видео без звука
silent_video.write_videofile("Впишите путь сохранения файла, например: [ Page/finished_audio.mp4 ]")