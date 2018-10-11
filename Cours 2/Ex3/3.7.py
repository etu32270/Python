fileA = open("fileA")
fileB = open("fileB")
fileC = open("fileC","w")

for lineA, lineB in zip(fileA,fileB):
    fileC.write(lineA)
    fileC.write(lineB)

fileA.close()
fileB.close()
fileC.close()

