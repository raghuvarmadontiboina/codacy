import sys,os

root = "/home/patate/directory/"
path = os.path.join(root, "targetdirectory")

for r,d,f in os.walk(path):
    for file in f:
        print os.path.join(root,file)
