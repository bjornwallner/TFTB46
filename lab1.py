#!/usr/bin/env python3
import sys
#import re
#extra modules
import random


# Code skeleton for the first lab in Advanced Bioinformatics
# The idea is to force you think in terms of defining functions that can be reused

# Go down to the function called "main". This is the function that will be used when the program starts.
# You will have to
#       * Add code to the main function to call the right function
#       * Add code to the function to do the actual work.


# ASSIGNMENT 3
def random_DNA(N):
    random_dna_seq=""

    ### ADD CODE HERE START ###
    return random_dna_seq


# This function prints the nucleotide composition
def print_nucleotide_composition(seq):
    (Afrac,Cfrac,Tfrac,Gfrac)=(0.0,0.0,0.0,0.0)

    ### ADD CODE HERE START ###
     
    print('Composition: A:' + str(Afrac) + ' C:'  + str(Cfrac) + ' T:'  + str(Tfrac) + ' G:'  + str(Gfrac)) 
    
# Should generate DNA sequences with a composition similar to real DNA
def real_DNA(N):
    dna_seq=""
    
    ### ADD CODE HERE START ###
    
     
    return dna_seq

    

def read_fasta(filename):
    names=[] # will contain a list of the name/id of the sequence
    seqs=[] # will contain a list of sequences

    ### ADD CODE HERE START ###

    
    return (names,seqs)

#This function takes a sequence, returns true if the sequence is most likely DNA, false otherwise
def isDNA(seq):
    dna=False

    ### ADD CODE HERE START ###

    return dna
#This function takes a sequence, returns true if the sequence is most likely RNA, false otherwise

def isRNA(seq):

    rna=False
    ### ADD CODE HERE START ###

    return rna
#This function takes a sequence, returns true if the sequence is most likely is a Protein, false otherwise
def isProtein(seq):

    protein=False
    ### ADD CODE HERE START ###

    return protein




def read_stockholm(filename):
    names=[] # will contain a list of the name/id of the sequence
    seqs=[] # will contain a list of sequences

    ### ADD CODE HERE START ###
    
    return (names,seqs)

def string60(seq):
    str60=""  #This string will contain the seq string formatted so that no lines is longer than 60 chars.

    ### ADD CODE HERE START ###
    return str60


def translate_seq(seq):
    translated_seq=""

    ### ADD CODE HERE START ###
    return translated_seq

#This function takes a translated sequence like returned from translate_seq and returns the longest ORF.
def find_longest_orf(seq):
    longest_orf=""

    ### ADD CODE HERE START ###
    


    return longest_orf


def usage():
    print("Usage: python lab1.py --lab number [addtional args...].")
    sys.exit(1)
            


def main():

    if len(sys.argv)> 2 and sys.argv[1] == "--lab":
        lab_number=int(sys.argv[2])
#        print "I will try to run lab number: 1." + str(lab_number)

        # Each lab_number corresponds to the different exercise in Lab 1 that you can find in Lisam. Look there to find more details what is needed
        if lab_number == 3:
            print("Lab 1.3 Random DNA")
                
            ### Called by: python lab1.py --lab 3 N, where N is the number of nucleotides you want
            ### The following code will read the third argument you are passing to the program and convert it to an integer and place it in the variable N:

            N=int(sys.argv[3]) 
            ### ADD CODE HERE START ###

        elif lab_number == 4:
            #Now do the same thing for realDNA
            print("1.4 Real DNA")
            N=int(sys.argv[3]) 
            ### ADD CODE HERE START ###
            
        elif lab_number == 6:
            print("1.6 DNA, RNA or Protein")
            filename=sys.argv[3]
            ### ADD CODE HERE START###              
                
        elif lab_number == 7:
            print("1.7 Reformatting Sequences")

            ### ADD CODE HERE START ###


        elif lab_number == 9:
            print("1.9 Translate DNA")
            ### ADD CODE HERE START ###

        elif lab_number < 9:
            print("ERROR: This number is associated with a google excerise")
        else:
            print("ERROR: Allowed numbers are 3,4,6,7, or 9")
    else:
        usage()
    

if __name__ == '__main__':
  main()
