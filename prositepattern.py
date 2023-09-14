import re
class Prositepattern:

	"""
	A class to create a pattern from a set of proteins
	...

	Attributes
	----------
	align : 
		object : instance of the class Multifasta
	threshold : 
		int

	

	Methods
	-------
	__re :
		Return the regular expression from a prosite pattern

	search:
		Find a regular expression in a sequence
	

	"""
	
	def __init__(self,align,threshold):

		"""
		Constructs all the necessary attributes for creating the pattern.

		Parameters
		----------
		align : 
			object : contains a multifasta sequence format
		threshold : 
			int 
			
		"""
		self.__align=align
		self.__threshold=threshold
	   
		patt=[]
		
		for i in range(len(self.__align)):
			l=self.__align.letters(i+1)

            #if this column is conserved
			if self.__align.is_conserved(i+1) is True:
				patt.append(l[0])
				
			elif len(l) <= self.__threshold and self.__align.contains_indel(i+1) is False:
				patt.append('[' +''.join(l)+ ']')
			
			elif len(l)<= self.__threshold and self.__align.contains_indel(i+1) is True:
				patt.append('x')

			elif len(l) > self.__threshold :
				patt.append('x')
			
		#initializing the list of the final pattern 	
		patt2=[]

		
		for i in range(len(patt)):
			
	       #for the first x encountered
			if patt[i] == 'x' and patt[i-1]!= 'x' :
				ct=0
				#count x's number
				while i < len(patt) and patt[i]=='x':
			   
					ct+=1
					i+=1
				#case of one x
				if ct == 1 : 
					patt2.append('x')
				# case where number of x are superior to one	
				elif ct > 1 :
                    #we want to know if there is an indel in the successive positions of x
					indel=[]
                    #i is the position of the last x
					for a in range ((i-ct),i):
						ind=self.__align.contains_indel(a+1)
						indel.append(ind)

					if True in indel:
					#List_aa contains true if there is an indel or false if no indel in the line
                    #nb_aa contains the number of amino acids in each line of the columns
						list_aa=[]
						nb_aa=[]

						for k in range(i-ct,i):
							pos=self.__align.all_letters(k+1)
                            #for each amino acids in pos, if this is not a indel , we add to pos2 the boolean True
							pos2=[(x!='-' and x!= '.') for x in pos]
						
							list_aa.append(pos2)
						for p in range(len(list_aa[0])):
                            #initializing the number of amino acid to 0 for each line
							aa=0
							for k in range(len(list_aa)):
								aa=aa+list_aa[k][p]
							nb_aa.append(aa)
                        #adding the x(a,b) in case of indel   
						patt2.append('x'+'('+str(min(nb_aa))+','+str(ct)+')' )		
					
                    #adding the number of x if there is not indels
					else :
						patt2.append('x'+ '('+str(ct)+ ')')
						
			  
			#For conserved amino acids or list of amino acids   
			elif patt[i]!='x':
				patt2.append(patt[i])
			
			
			
		pattern='-'.join(patt2)
			
	
		#Final pattern
		self.__patt=pattern
	   
		
							
		
	def __re(self):

		"""
		return the regular expression
		

		Parameters
		----------
		None

		Returns
		-------
		String 
			The regular expression from the pattern : str

		"""		
		regex=''
		
		for i in self.__patt:   
			if i == 'x':
				regex += '.'   
			elif i == '-':   
				regex += ''   
			elif i == "(":   
				regex += '{'   
			elif i == ")":
				regex += '}'
			else :
				regex += i
				
		return regex
   
		
	def search(self,sequence) : 

		"""
		Find a match of the regex (regular expression) in a sequence
		

		Parameters
		----------
		sequence
			string

		Returns
		-------
		String 
			The match on the sequence 

		""" 
		r=self.__re()
		ok=re.search(r,sequence)
        #if the method find a match
		if ok: 
			return '('+ str(ok.start())+','+ ok.group()+ ')'
		else:
			return None
		
		
		
	
	def __str__(self):

		"""
		print the regular expression
		

		Parameters
		----------
		None

		Returns
		-------
		String 
			The pattern : str
			 
		"""	 
		
		return self.__patt
