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
        if not freeSpace or not blocks:
            break
        freeSpaceIndex, freeSpaceSize = freeSpace.popleft()
        id,index,size = blocks.pop()
        if(freeSpaceIndex> index):
            break
        if freeSpaceSize > size:
            leftover = freeSpaceSize - size
            freeSpace.appendleft([freeSpaceIndex+size, leftover])
            file = file[:index] + [-1] * leftover + file[index + size:]
            file = file[:freeSpaceIndex] + [id] * size + file[freeSpaceIndex+size:]
        elif freeSpaceSize == size:
            file = file[:index] + [-1] * size + file[index + size:]
            file = file[0: freeSpaceIndex] + [id] * size + file[freeSpaceIndex+size:]
        elif freeSpaceSize < size:
            freeSpace.appendleft([freeSpaceIndex,freeSpaceSize])            
            #iterate through free spaces if it wasn't enough
            for space in freeSpace:
                freeSpaceIndex, freeSpaceSize = space
                if(freeSpaceIndex > index):
                    break
                if freeSpaceSize > size:
                    leftover = freeSpaceSize - size
                    space[0] = freeSpaceIndex + size
                    space[1] = leftover
                    file = file[:index] + [-1] * size + file[index + size:]
                    file = file[:freeSpaceIndex] + [id] * size + file[freeSpaceIndex+size:]
                    break
                elif freeSpaceSize == size:
                    file = file[:index] + [-1] * size + file[index + size:]
                    file = file[0: freeSpaceIndex] + [id] * size + file[freeSpaceIndex+size:]
                    freeSpace.remove(space)
                    break
                
        
        while file and file[-1] == -1:
            file.pop()
    
    for i in range(len(file)):
        if file[i] != -1:
            sum += file[i] * i

    return sum

print(Day9())