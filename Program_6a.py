import os.path
import sys
fname=input("enter the filename: ")
if not os.path.isfile(fname):
    print("File",fname,"doesn't exists")
    sys.exit(0)
infile=open(fname,"r")
lineList=infile.readlines()
for i in range(20):
    print(i+1,":",lineList[i])
word=input("enter a word: ")
cnt=0
for linr in lineList:
    cnt+=line.count(word)
print("the word",word,"appears",cnt,"times in the file")

