import sys
from collections import deque

def Day9(input = "input.txt"):
    l=[]
    sum=0
    with open(input, "r") as f:
        for line in f:
            try:
                l = list(line.strip())
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    

    freeSpace = deque([])   #FIFO
    blocks = deque([])      #LIFO
    emptySpace = 0
    usedSpace = 0
    id = 0
    isBlock = True
    file = []
    id = 0
    for i in range(len(l)):
        char = l[i]
        size = int(char)
        if isBlock:
            usedSpace += size
            blocks.append([id,len(file),size])
            file.extend([id] * size )
            id += 1
            isBlock = False
        else:
            emptySpace += size
            freeSpace.append([len(file),size])
            file.extend([-1] * size) ## empty spaces represented by a -1
            isBlock = True
        
    while len(file) > usedSpace:
        freeSpaceIndex, freeSpaceSize = freeSpace.popleft()
        id,index,size = blocks.pop()
        used = 0
        if freeSpaceSize > size:
            used = size
            leftover = freeSpaceSize - size
            file = file[0: freeSpaceIndex] + [id] * size + file[freeSpaceIndex+size:] 
            freeSpace.appendleft([freeSpaceIndex+size, leftover])
        elif freeSpaceSize == size:
            used = size
            file = file[0: freeSpaceIndex] + [id] * size + file[freeSpaceIndex+size:] 
        elif freeSpaceSize < size:
            used=freeSpaceSize
            leftover = size - freeSpaceSize
            file = file[0: freeSpaceIndex] + [id] * freeSpaceSize + file[freeSpaceIndex+freeSpaceSize:] 
            blocks.append([id,index,leftover])
        
        file = file[:len(file)-used]
        while file and file[-1] == -1:
            file.pop()
        
        
        
    
    for i in range(len(file)):
        sum += file[i] * i
        
        
    
    return sum

print(Day9())