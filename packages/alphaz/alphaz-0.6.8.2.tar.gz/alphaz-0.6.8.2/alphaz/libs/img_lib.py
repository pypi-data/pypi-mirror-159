from PIL import Image, ImageDraw

import requests, imghdr

def resize_image(path: str):
    standard_height = 100
    image = Image.open(path)
    width, height = image.size
    ratio = standard_height / height
    new_width, new_height = int(width * ratio), int(height * ratio)
    new_image = image.resize((new_width, new_height))
    new_image.save(path)
    
def get_image_from_src(src: str, save: bool = False):
    webs = requests.get(src)
    file_name = src.split("/")[-1].split("?")[0]
    if not "." in file_name:
        ext = imghdr.what(None, h=webs.content)
        file_name += f".{ext}"
    else:
        ext = file_name.split(".")[-1]
    path = f"tmp/images/{file_name}"

    if save:
        try:
            open(path, "wb").write(webs.content)
        except Exception as ex:
            print(ex)
            return file_name
        resize_image(path)
    return file_name