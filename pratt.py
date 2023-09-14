from multifasta import Multifasta
from multiplealignment import MultipleAlignment
from prositepattern import Prositepattern
import sys 
import argparse



if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	#Required arguments
	parser.add_argument('file1',help='multifasta file from where we create the new pattern ')
	parser.add_argument('file2',help='sequence where we search the pattern' )
	#Optionnal arguments
	parser.add_argument('-t', dest='threshold',type=int, help="thresholds define")
	args = parser.parse_args()


	f= Multifasta(args.file1)
	m=MultipleAlignment(f)
	

	with open(args.file2, "r") as file2search:
		seq=file2search.read()

	
	if args.threshold: 

		p2=Prositepattern(m,args.threshold)
		p2s=p2.search(seq)
		if p2s != None:
			print("Pattern {} found at position {} : {}".format(p2,p2s[1],p2s[3:-1]))
		else:
			print ("Pattern {} not found".format(p2))


		
	else :
		
		p1= Prositepattern (m,4)
		p1s=p1.search(seq)
		if p1s != None:
			print("Pattern {} found at position {} : {}".format(p1,p1s[1],p1s[3:-1]))
		else:
			print ("Pattern {} not found".format(p1))
	

