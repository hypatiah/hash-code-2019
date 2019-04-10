def read():
    N = int(input())
    out = []
    for i in range(N):
        line = raw_input()
        lineData = line.split()
        data = []
        data.append(lineData[0])
        tags = []
        for i in range(int(lineData[1])):
            tags.append(lineData[i+2])
        data.append(tags)
        out.append(data)
    return out

def description(photos):
    print('The collection has %d photos' % len(photos))
    for i in range(len(photos)):
        orient = 'vertical'
        if photos[i][0] == 'V':
            orient = 'horizontal'
        print('Photo %d is %s and has tags %s' % (i, orient, photos[i][1]))
description(read())
