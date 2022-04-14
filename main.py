import os,time
os.system('cls')
filenames = ['A1.txt','A2.txt']
frames = []

for name in filenames:
    with open(name,'r',encoding='utf8') as f:
        frames.append(f.readlines())

while True:
    for frame in frames:
        print("".join(frame))
        time.sleep(1)
