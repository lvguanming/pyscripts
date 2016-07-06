#encoding=utf-8

##########################
#by:Gim
##########################

import sys,os,re

def read(filePath):
    with open(filePath, "rb") as f:
        line = f.readline()
        print line



def find_file_by_pattern(regexStr=".*",base=".",circle=True):
	if base == ".":
		base = os.getcwd();
	final_file_list = [];
	if os.path.isfile(base):
		if re.match(regexStr,base):
			final_file_list.append(base)
		return final_file_list
	cur_list = os.listdir(base)
	for item in cur_list:
		if item == "." or item == "..":
			continue
		full_path = os.path.join(base,item)
		if os.path.isfile(full_path):
			if re.match(regexStr,item):
				final_file_list.append(full_path)
			else:
				print full_path + "not good path"
		elif circle:
			final_file_list += find_file_by_pattern(regexStr, full_path, True)
	return final_file_list

if __name__ == "__main__":

	if sys.argv == None or len(sys.argv) < 1:
		print "usage: ....py [src_dir src_dir src_dir...dest_dir]\n"
		sys.exit()
	dirList = [sys.argv[1]]
	if len(dirList) < 1:
		print 'Specify at least one source directory'
		sys.exit()
	for fileName in dirList:
		if (fileName == ''):
			print 'Source directory or file %s must not be empty' %(fileName)
			sys.exit()
		if (not os.path.isdir(fileName)) and (not os.path.isfile(fileName)):
			print 'Invalid destination directory or file %s' &(fileName)
			sys.exit()
	result = []
	for srcDirPath in dirList:
		result += find_file_by_pattern(".*",srcDirPath, True)
	for filesname in result:
		fp = open(filesname)
		eachline = fp.readlines()
		fp.close()
		length=len(eachline)
		if length>500:
			length=500
		for line in eachline[1:length]:
			removePattern = re.compile('<[^>]+>|&#\d*;|&nbsp;')
			text = (removePattern.sub("",line)).strip()
			print "before ", line
			print "after ", text