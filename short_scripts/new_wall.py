import os
import random

home = os.path.expanduser('~')
images = os.listdir(home + "/Pictures/wallpapers")


rnd_img = random.choice(images)

# Try to remove the previous wallpaper if there was any
wallpaper_folder = home + "/Pictures/wallpaper/"
os.system("touch {}tmp".format(wallpaper_folder))
os.system("rm {}*".format(wallpaper_folder))
# os.system("touch ~/Pictures/wallpaper/tmp")
# os.system("rm ~/Pictures/wallpaper/*")


# copia la imagen aleatoria a la carpeta de wallpaper como wallpaper.jpg
wallpapers_folder = home + "/Pictures/wallpapers/"
os.system("cp " + wallpapers_folder + rnd_img + " {}wallpaper.jpg".format(wallpaper_folder))
