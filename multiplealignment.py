class MultipleAlignment:
	"""
	A class to represent a multifasta alignment.

	...

	Attributes
	----------
	seq : file
		contains a multifasta sequence format
	

	Methods
	-------
	len :
		Return the length of amino acids

	letters:
		Return the list of distinct amino acids at a given position
	
	size:
		Return the number of sequences
	
	all_letters:
		Return the list of all amino acids at a given position

	is_conserved:
		Return True if there is a conserved amino acids at a given position
	
	contains_indel:
		Return True if there is a indel at a given position

	"""
	
	def __init__(self,seq):

		"""
		Constructs all the necessary attributes for the multifasta file.

		Parameters
		----------
			seq : file
				contains a multifasta sequence format 
			
		"""
		seq2=seq.sequences()
		self.__seq=seq2
		  
		
		
	def __len__(self):

		"""
		return the length of amino acids
		

		Parameters
		----------
			None

		Returns
		-------
			Int 
		"""
		return len(self.__seq[0])
	
	def size(self):

		"""
		return the number of sequences
		

		Parameters
		----------
			None

		Returns
		-------
			Int 

		"""
		return len(self.__seq)


	
	def letters(self,k):

		"""
		Return the list of distinct amino acids at a given position
		

		Parameters
		----------
		k : int 
			position of the alignment

		Returns
		-------
		list 
			list of distinct amino acids at position k
			
		"""

		#verify if k is between 1 and alignment's length
		assert k>= 1 and k <= len(self.__seq[0]) , "{} is not in the range of 1 and {}".format(k,len(self.__seq[0]))
		
		prot=[]
        #Goes through each sequence and adds the element if it is not already in Prot
		for i in range(self.size()):
			if self.__seq[i][k-1] not in prot:
				prot.append(self.__seq[i][k-1])
				
		return prot
	
	def all_letters(self,k):

		"""
		Return the list of all amino acids at a given position
		

		Parameters
		----------
		k : int 
			position on the alignment

		Returns
		-------
		list 
			list of all amino acids at position k
			
		"""
		assert k>= 1 and k <= len(self.__seq[0]) , "{} is not in the range of 1 and {}".format(k,len(self.__seq[0]))

		lett=[]
		for i in range(self.size()):
			lett.append(self.__seq[i][k-1])
		return lett
	
	def is_conserved(self,k):

		"""
		Return True if there is a conserved amino acid at a given position 

		Parameters
		----------
		k : int 
			position on the alignment

		Returns
		-------
		boolean 
			True or False


		"""
		assert k>= 1 and k <= len(self.__seq[0]) , "{} is not in the range of 1 and {}".format(k,len(self))
        #The length of the list equals one if the column is conserved
		if len(self.letters(k)) == 1 :
			return True
		else:
			return False
	   
	def contains_indel(self,k):
		"""
		Return True if there is a indel at a given position

		Parameters
		----------
		k : int 
			position on the alignment

		Returns
		-------
		boolean 
			True or False
		"""
		assert k>= 1 and k <= len(self.__seq[0]) , "{} is not in the range of 1 and {}".format(k,len(self))
        #The presence of full stops and hyphen means there is a indel in the alignment
		if '.' in self.letters(k) :
			return True

		elif '-' in self.letters(k):
			return True

		else:
			return False
	
	def __str__(self):

		"""
		print the alignment 
		

		Parameters
		----------
			None

		Returns
		-------
		String 

		"""
		
		alignment=''
		for line in self.__seq:
			alignment += line+"\n"
		return alignment
	
