# daily computer log
from time import gmtime, strftime


csvfile = "clog.csv"
def dopisivscv(line,imecsv): #to zapose v csv file nov vspeh
	with open(imecsv,'a') as f:
	    f.write(line)
	    f.write('\n')
while True:
	cas = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	print "wellcome back! write few words about today...:\n (category;santance)"
	stavek = raw_input("type here: ")
	stavek = cas + ';' + stavek
	dopisivscv(stavek,csvfile)
