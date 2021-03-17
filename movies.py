import os
import random


# get a random movie folder
# return the name of a folder in the "movies/" folder
def get_random_folder():
    # change dir name to whatever
    choice = random.choice(os.listdir("movies/"))
    print(choice)
    return choice

# get a random screen from the chosen random folder (movie)
# return a random screen file name
#def get_one_random_screen(folder):
#    screen = random.choice(os.listdir("movies/"+folder+"/screens/"))
#    print(screen)
#    return screen

# get random folder from the screens folder (so one random movie)
# returns a combination of ["name of the movie", screens_path]
# first element is a string, second element is a list of paths
def get_four_random_screens(folder):
    i = 0
    screens = [1, 2, 3, 4]
    while(i < 4):
        screens[i] = random.choice(os.listdir("movies/"+folder+"/screens/"))
        print(screens[i])
        i = i + 1
    return screens

# get one, two, three, or four random screens in a folder
def get_x_random_screens(folder):
    i = 0
    y = random.randint(1, 4)
    screens = []
    while(i < y):
        screens.append(random.choice(os.listdir("movies/"+folder+"/screens/")))
        print(screens[i])
        i = i + 1
    return screens

# get a random movie quote from the chosen random folder (movie)
def get_movie_quote(file):
    if(os.stat(file).st_size != 0):
        chosen_line = random_line(file)
        return chosen_line
    else:
        print("The file is empty")
        return " "

# remove a movie quote from the chosen random folder (movie), in the quotes file
def remove_movie_quote(file):
    return True


def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line


# remove the used files (can be one file or multiple images depending on
# the tweet)
def remove_files(choices):
    try:
        os.remove("images/"+choices)
        print("file has been removed")
        return True
    except:
        print("Error while trying to remove the current image")


# remove the folder if empty, else just let it stay
def remove_folder_ifempty(folder):
    return True
