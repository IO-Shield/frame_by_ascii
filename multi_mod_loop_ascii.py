import os
import time
os.system('clear')

# multi layer ascii pool (using more than set of frames)
dance = ["frame1","frame2","frame3","frame4"]
ascii_pool = ["test.txt", "test2.txt"]

# using a function instead of the basic setup
def animator(files, delay = .125,repeats = 10):
    frames = []
    for name in files:
        with open(name, "r") as f:
            frames.append(f.readlines())

    for i in range(repeats):
	for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('clear')

# set each frame witi a different delay (change speed between each one)
# edit "files with the desired animation from the multi layer ascii pool
'''
exmaple;
animator(files,delay = 0.54, repeat = 20)
'''
# NOTE this will pull the delay and repeat time from these animator lines
# instead from the def animator function

animator(dance,delay = 0.2, repeat = 5)

animator(ascii_pool,delay = 0.5, repeat = 2)

animator(dance,delay = 0.14, repeat = 10)

