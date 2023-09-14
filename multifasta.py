
class Multifasta:

	"""
	A class to represent a multifasta file.

	...

	Attributes
	----------
	seq : file
		contains a multifasta sequence format
	

	Methods
	-------
	sequence:
		Prints the list of the sequences contained in seq.
	"""
  
	def __init__(self,seq):

		"""
		Constructs all the necessary attributes for the multifasta file.

		Parameters
		----------
			seq : file
				contains a multifasta sequence format 
			
		"""
	
		with open(seq,'r') as fileIn:
        #initializing the list containing the sequences
			liste_seq=[]
			lines=fileIn.readlines()	
			for i in lines: 
                #Add to the list only sequences
				if '>' not in i :
					i=i.strip()
					liste_seq.append(i)
			self.__seq=liste_seq
  
	def sequences(self):

		"""
		prints the list of sequences contained in the file
		

		Parameters
		----------
		    None

		Returns
		-------
		    List 
		"""
		return self.__seq
	
	
		

	  
