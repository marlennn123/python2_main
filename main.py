import os
from PIL import Image
from PIL import __version__ as PIL_version
from packaging import version


folder_path = r'photo'
output_folder = r'kk'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

target_size = (28, 28)


if version.parse(PIL_version) >= version.parse("10.0.0"):
    resample_method = Image.Resampling.LANCZOS
else:
    resample_method = Image.ANTIALIAS


for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        try:
            input_path = os.path.join(folder_path, filename)


            with Image.open(input_path) as img:
                img_resized = img.resize(target_size, resample=resample_method)

                output_path = os.path.join(output_folder, filename)


                img_resized.save(output_path)

            print(f"{filename} успешно изменено")
        except Exception as e:
            print(f"Ошибка при обработке {filename}: {e}")
