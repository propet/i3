import os
import shutil
import random

images = os.listdir(os.path.expanduser('~') + "/Pictures/wallpapers")


# Rename files to avoid spaces
#for i in os.list():
#    os.rename(i, i.replace(' ', ''))

rnd_img = random.choice(images)

# Try to remove the previous wallpaper if there was any
os.system("touch ~/Pictures/wallpaper/tmp")
os.system("rm ~/Pictures/wallpaper/*")


# copia la imagen aleatoria a la carpeta de wallpaper como wallpaper.jpg
os.system("cp " + "~/Pictures/wallpapers/" + rnd_img + " ~/Pictures/wallpaper/wallpaper.jpg")
