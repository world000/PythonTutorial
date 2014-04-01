import os, sys
import string
import re

def main():
    nargs = len(sys.argv)
    if not 2 <= nargs <= 3:
        print "usage: %s infile [outfile]" % os.path.basename(sys.argv[0])
    else:
        inputName = sys.argv[1]
        outputName = inputName[0:-4] + '.srt'
    
        if nargs == 3:
            outputName = sys.argv[2]
    
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

main()
