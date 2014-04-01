import os, sys
import string

# 01:01:01 -> 3661
def time2Second(time):
    timeComp = time.split(':')
    second = int(timeComp[0]) * 3600 + int(timeComp[1]) * 60 + int(timeComp[2])
    return second

def second2Time(second):
    hour = second / 3600
    second = second % 3600
    minute = second / 60
    second = second % 60
    return ('%02d:%02d:%02d' % (hour, minute, second))

def timePlus(time, plus):
    timeComp = time.split(',')
    second = time2Second(timeComp[0])
    second = second + plus
    timeComp[0] = second2Time(second)
    return (timeComp[0] + ',' + timeComp[1])

nargs = len(sys.argv)
if not nargs == 3:
    print "usage: %s infile time" % os.path.basename(sys.argv[0])
else:
    inputName = sys.argv[1]
    plus = int(sys.argv[2])
    inputFile = open(inputName)
    outputFile = open(inputName[0:-4] + '(1).srt', 'w')
    
    for line in inputFile:
        timeList = line.split(' --> ')
        
        if len(timeList) == 2:
            start = timePlus(timeList[0], plus)
            end = timePlus(timeList[1], plus)
            outputFile.write('%s --> %s' % (start, end))
        else:
            outputFile.write(line)

    outputFile.close()
    inputFile.close()
