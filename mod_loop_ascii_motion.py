import os,time
os.system('clear')
files = ["frame1","frame2","frame3","frame4"]

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
animator(files,delay = 0.2, repeats = 5)

animator(files,delay = 0.5, repeats = 2)

animator(files,delay = 0.14, repeats = 10)

