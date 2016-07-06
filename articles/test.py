#encoding=utf-8

##########################
#by:Gim
##########################

import re,sys,os
# from __future__ import print_function

pattern = re.compile('\d{4}-\d{2}-\d{2}.*')
pattern2 = re.compile(r'id=\d{0,12}')
pattern3 = re.compile(r'positionId=\d{0,12}')
pattern4 = re.compile('"state":[+-]?\d{1}')
urlChecks = ["refresh.json", "savePosition.json", "offline.json","delete.json"]

op_types = {'http://xxxxxxx.xxx.xxx/corpPosition/refresh.json': 'REFRESH',
            'http://xxxxxxx.xxx.xxx/corpPosition/savePosition.json': 'SAVE_OR_UPDATE',
            'http://xxxxxxx.xxx.xxx/offline.json' : "OFFLINE",
            'http://xxxxxxx.xxx.xxx/mcorpPosition/delete.json' : 'DELETE'}

distFile = None

def read(filePath):
    with open(filePath) as infile:

        dateStartLine = infile.next().rstrip('\n')
        while not pattern.match(dateStartLine):
            dateStartLine = infile.next()

        currentLine = infile.next()

        while not pattern.match(currentLine):
            dateStartLine += currentLine
            currentLine = infile.next()


        for line in infile:
            if not pattern.match(line):
                currentLine += line
            else:
                printLine(dateStartLine)
                dateStartLine = currentLine
                currentLine = line

        printLine(dateStartLine)
        printLine(currentLine)

"""
corpPosition/refresh.json
corpPosition/savePosition.json( create , editoronline )
corpPosition/offline.json
corpPosition/delete.json
"""
def printLine(inLine):
    # strHello = "the length of (%s) is %d" %('Hello World',len('Hello World'))
    line = inLine.replace('\n','')
    s = line.split('{|]')
    find = True
    for check in urlChecks:
        if(s[3].__contains__(check) ):
            find = True
            break
        else:
            find = False
    if(find):
        # if(pattern2.match(s[4])):
        #     print s[4]

        id = None
        for match in pattern2.finditer(s[4]):
            id = match.group(0).replace("id=","")

        if id is None:
            for match in pattern3.finditer(s[4]):
                id = match.group(0).replace("positionId=","")

        if id == '' or id == None:
            id = 'null'

        targetId = None
        for match in pattern3.finditer(s[5]):
                targetId = match.group(0).replace("positionId=","")

        if targetId == None:
            targetId = 'null'

        st = None
        for match in pattern4.finditer(s[5]):
                st = match.group(0).replace("\"state\":","")
        if(st is None):
            print s[4]
            print s[5]

        # print "%s \t %s \t %s \t %s \t %s" %(s[1], s[2], op_types.get(s[3]), id, st)
        printSQL(s[1],  s[2],op_types.get(s[3]) , id, targetId, st)


        if id is None:
            print "###### error : pid not fount #######"
            print s[4]
            print "######## end ########"
                #for line in infile:
            # print line
            # while not pattern.match(line):
            #     dateStartLine = dateStartLine + line
            #     line = infile.next()
            # dateStartLine = line
            # print dateStartLine

def printSQL(userId,opTime, opType,positionId,newPositionId,result):
    distFile.writelines("INSERT INTO record(hrId,opTime,opType,sourcePositionId,newPositionId,result) VALUES (%s,'%s','%s',%s,%s,%s);\n" %(userId,opTime, opType,positionId,newPositionId,result))


if __name__ == "__main__":
    print sys.argv
    # sys.exit()
    if sys.argv == None or len(sys.argv) < 2:
		print "params is null"
		print "usage: py [source.py dist_dir]\n"
		sys.exit()
    else:
        files = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
        if files.__len__() == 0:
            print "Not found spaction files ."
            sys.exit(1)
        else:
            print "is good file"
        for file in files:
            with open(sys.argv[1]+"/sql/"+ file+ ".sql","a+") as f:
                print sys.argv[1]+"/"+file
                distFile = f
                read(sys.argv[1] +"/"+file)

