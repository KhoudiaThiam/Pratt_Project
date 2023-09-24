
# PRATT PROJECT 


The purpose of this program is to determine a prosite motif from a set of proteins.A Prosite pattern is used to represent a functional site of a protein.
From a multifasta file, it returns the template created and allows you to search for this pattern in another sequence.

<p align="center">
    <img width="658" alt="image" src="https://github.com/KhoudiaThiam/Pratt_Project/assets/100375394/4d33d76d-29f7-4af7-99a3-6d811b62100b)">
</p>



## Description

This script takes as main arguments:
- a multifasta file that is used to obtain the Prosite model
- a file in which this model will be searched.
  
It also accepts one optional argument that will define a threshold.

If there are only the first two arguments, the model search will be performed on a threshold of four(4) by default.

That is, if this threshold of four amino acids is exceeded on a position, the latter will be considered as an 'x'.


## Extensions


In order to carry out this project, we used several classes


**Multifasta**

The Multifasta class takes a file as input and performs a read.It contains a
*sequences* method who returns the sequences in the multifasta file in a character string list.



**MultipleAlignment**

The MultipleAlignment class takes an instance of the Multifasta class as input and returns the 
alignment as a string. 
It contains a private method *__len__* which return the numbers of amino acids in a sequence.

It also contains :

- a *size* methods which return the number of sequences
- a *all_letters* method for obtaining the list of amino acids present on a given column
- the *letters* method which returns a list of distinct amino acids (without duplicates)
- the *is_conserved method* takes as input a position of the alignment (between 1 and the length of the sequence) 
and returns True if this position is conserved (only one amino acid in all sequences). 
- The *contains_indel* method takes a position (integer)  as input and returns True if the position contains an indel
(insertion or deletion represented by a '-' or a '.')



**PrositePattern**

The Prositepattern class takes as input an instance of the MultipleAlignment class as well as a definition threshold 
(to know from how many amino acids we have an 'x' in the pattern). It refers to the pattern but also contains a private *__re* 
method that allows  to create a regular expression from the pattern and a *search* method that looks in a given sequence as 
a parameter for this regular expression.


We also used the *re* module and the *argparse* module. 




## How to launch the program


PS00028 is the file containing the first known sequences of the prosite pattern PS00028.

The file P28_ex is the file containing a sequence and the purpose will be to find if the pattern is present or not in this sequence.
We will also test the optional argument for setting a threshold 

The command line launched will be

```
python3 .\pratt.py data\PS00028.fasta data\P28_ex.txt -t 8

```


PS00719 is the file containing all the sequences of the prosite pattern PS00028.The file P719_ex is a sequence 
where we except to not find the pattern even if this is the same size as the alignment length.

The commande line launched will be : 

```
 python3 .\pratt.py data\PS00719.txt data\P719_ex.txt -t 5 

```


## Excepted results


Let's take the first file (PS00028). As indicated on the website,the expected pattern is:


**C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H**


The position x(a,b) are re what we are supposed to have if we have indels.
They represent the variation in length between consecutive x's


- After launching the first command line , we'll get :

```
Pattern [CX]-x(2,4)-C-x(3)-[FYILCMVW]-x(8)-H-x(3,5)-H found at position 7 : Cdl..CkagFvrhhdlkrHlri..H
```

At the first position, we realize that we have a list containing 'C' and 'X' or the only element that we must have is 'C. So we checked an X present in our multifasta file and we realized the presence of a sequence at the position 3861 of our alignment (7724 in our multifasta file) :

ZBT32_PANTR/430-450 : PS00028
Xxl..CgagCpslasmqaHmrg..H

This proves that our program is functional but due to the sensitivity of the condition to be an amino acid kept (length of the list ==1 ),
it will take the 'X' element even if it's one in thousand of sequences.This could therefore be a key element in improving our program.

If we take off that specific sequence we'll get : 

```
Pattern C-x(2,4)-C-x(3)-[FYILCMVW]-x(8)-H-x(3,5)-H found at position 7 : Cdl..CkagFvrhhdlkrHlri..H
```


- For the second file(PS00719) , the excepted pattern is :

**N-x-[LIVMFYWD]-R-[STACN](2)-H-Y-P-x(4)-[LIVMFYWS](2)-x(3)-[DN]-x(2)-G-[LIVMFYW](4)**


After launching the second command line, we'll get :

```
Pattern N-x-[VIDFY]-R-[TCN]-[ASC]-H-Y-P-x(4)-[FWLVM]-[YSLM]-x(2)-[caft]-[DN]-x(2)-G-[LFI]-[FYWLV]-[VLM]-[MIVF] not found
```

Once again , the program is functional but we notice that the pattern is the same but the amino acid lists differ. This can be explained by the definition of the amino acid list according to the chemical character of these amino acids.

For example for the third position, we are supposed to have [LIVMFYWD] but instead we have [VIDFY]. After analysis, we realize that the majority of amino acids in [LIVMFYWD] have the particularity of being non-polar. This may therefore explain the fact that there are more amino acids than expected. Lists can also be factored into a single amino acid list. 

This is the case of [LFI]-[FYWLV]-[VLM]-[MIVF] which becomes in the official pattern [LIVMFYW](4)

## Contact

If you found an issue or would like to submit an improvment to this project , you can contact me via [LinkedIn](https://www.linkedin.com/in/ndeye-khoudia-thiam/) or by email (khoudiathiampro@gmail.com)

