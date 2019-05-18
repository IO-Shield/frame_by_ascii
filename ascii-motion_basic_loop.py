import os
import time
os.system('clear')
files = ["frame1","frame2","frame3","frame4"]
frames = []

for name in files:
    with open(name, "r") as f:
        frames.append(f.readlines())

while True:
    for frame in frames:
        print("".join(frame))
        time.sleep(.125)
        os.system('clear')


'''
# instead of a white true just loop only 10 times

for i in range(10):
    for frame in frames:
        print("".join(frame))
        time.sleep(.2)
        os.system('clear')
'''
