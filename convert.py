import ffmpeg
import os

# Список ваших файлов
video_files = ['intro-videokaz.mp4', 'intro-videorus.mp4']


def create_poster(video_input):
    # Формируем имя картинки: заменяем .mp4 на .jpg
    poster_output = video_input.replace('.mp4', '.jpg')

    try:
        (
            ffmpeg
            .input(video_input, ss=0.0)  # Берем кадр на 1.0 сек
            .output(poster_output, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"✅ Готово: {poster_output}")
    except ffmpeg.Error as e:
        print(f"❌ Ошибка в файле {video_input}: {e.stderr.decode()}")


# Запуск обработки
for video in video_files:
    if os.path.exists(video):
        create_poster(video)
    else:
        print(f"⚠️ Файл не найден: {video}")
