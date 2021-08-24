---
title: Lab 3 in Advanced Bioinformatics
permalink: /lab3/
---


# ​​Lab 3

​​​​​These assignments are meant to introduce you to Biopython and some other useful Python modules.

The online documentation of Biopython might be useful and can be found here: http://biopython.org

Here you need to use: module initadd courses/TFTB46 to get access to biopython on the school's computers.

If you want install biopython on your own computer it is easiest to install [Anaconda python package handler](http://anaconda.com/downloads), 
​once installed you should be able to install biopython. On mac or linux you can write: conda install biopython in the terminal


### ​Assignments
1. [Translate DNA 2.0](#1-translate-dna-20)
2. [Running external programs](#2-running-external-programs) (Video Lecture 6, pipeline.py)​​
3. [Remote Blast](#3-remote-blast)
4. [Blast ​parsing​​](#4-blast-​parsing​​)



## 1. Translate DNA 2.0

## 2. Running external programs
Do this assignment after Video Lecture 6. The assignment is to complete the code in the `pipeline.py` file from the `exercise.zip` archive. 

## 3. Remote Blast

## 4. Blast ​parsing​​


In these assignments you are expected to use Python and no additional libraries (except for standard libraries). The goal is to practice writing "pure" Python for those occasions when libraries or other good tools are not available for one reason or another.



## Assignments


1. [Regular expressions](#1-regular-expressions) (Video Lecture 4, regexp.py) 
2. [Download genomes](#2-download-genomes)
3. [Computing GC content](#3-computing-gc-content)
4. [Comparing base composition](#4-comparing-base-composition)
5. [Addition modules, URL and Exception](#5-addition-modules-url-and-exception) (Video Lecture 5, fetch_sequences.py)​ 



## 1. Regular expressions 
Do this assignment after Video Lecture 4. The assignment is to complete the code in the `regexp.py` file from the `exercise.zip` archive. 

## 2. Download genomes

Find the NCBI website and use it to download genome sequences for 

* *Chlamydophila pneumoniae*
* *Thermosynechococcus elongatus*
* *Bacillus subtilis*
* *Legionella pneumophila*
* *Haemophilus influenzae*

Be sure to download the chromosomal genome sequences and not any plasmid DNA. Store the data using one file per genome. 

* What sequence format are you using?
* How large are the different genomes? (use unix command, code you have written previously in the course, or new/adapted code)


## 3. Computing GC content
Write a program `gccontent for computing [GC content](http://en.wikipedia.org/wiki/GC-content) for a genome.

### Requirements
Your program must read any number of files from the command line arguments, compute GC for file after file, and write them to standard out in order.
All sequences (chromosomes and/or contigs) from a genome should be included in the analysis.

You program must be structured so that:
* one function is in charge of reading a genome sequence,
* one function is computing the GC content of a sequence.

Example usage:

A typical session running you program must look like this:
```
> ./gccontent genome1
0.406
> ./gccontent genome1 genome2 genome3
0.406
0.539
0.435
> ./gccontent genome1 genome2 genome3 | sort -n
0.406
0.435
​0.539
```

Print using any precision you like.
 
* Test runs on the five downloaded genomes. 
* Why do people care about GC content?​​
  

## 4. Comparing base composition

Computing phylogenies for specie​s based on whole genomes is hard for several reasons. Do you work with genes only? How do you then pick the genes? You cannot, in general, align whole genomes because of recombination events that cause large scale differences. 

One solution that has been tried is comparing the difference in nucleotide composition. Let πX be the nucleotide composition vector for species X. If all nucleotides have the same frequence in X (which would be surprising), then πX=(0.25, 0.25, 0.25, 0.25). 

If genome Y we are looking at is GC rich, then the composition vector might be πY = (0.2, 0.3, 0.3, 0.2), assuming that the nucleotide frequencies are in the order A, C, G, and T.

### Measuring difference in composition
To be able to use composition for distances, we want to have a measure for the difference. In this assignment, we use the root-mean-square distance: 
* Take the elementwise differences. 
* Square the differences and add them up.
* Divide the sum by 4 and take the square root.
* diff(πX,πY) = √ (0.25 * ((0.25-0.2)2 + (0.25-0.3)2 + (0.25-0.3)2 + (0.25-0.2)2))

### Assignment
Write a Python program that takes as input a number of filenames, each pointing to a file containing one genomic sequence in Fasta format, and output a distance matrix using the composition difference above.

#### Suggested solution structure
* Define a function dist that takes two composition vectors as arguments and returns a difference.
* Loop over all pairs to generate the distance matrix for all pairs

#### Test data
[simple1.fa](simile1.fa) and [simple2.fa](simile2.fa) have composition vectors (0.25, 0.25, 0.25, 0.25) and (0.3, 0.2, 0.2, 0.3), respectively, and their composition distance should therefore be 0.05.

Some actual data:
* [human.fa](human.fa)
* [mouse.fa](mouse.fa) 
* [fly.fa](fly.fa)
* [yeast.fa](yeast.fa)
* [ecoli.fa](ecoli.fa)
* [plasmodium.fa](plasmodium.fa)
* [thermus.fa](thermus.fa)
For efficiency reasons, this is just parts of the chromosomes/genomes.


#### Requirements
If your Python file is named "basedist" then you should be able to run it like in the example below.
All files are read from the command line (`*.fa` will run it for all files matching `*.fa`)

Output is written to stdout, any errors or warnings go to stderr, using sys.stdout.write and sys.stderr.write (print also writes to stdout)
The output is a distance matrix in Phylip format. Note: The accessions are limited to 10 characters in this format!.
You can use the format module to print matrix in the right format, right more about it here: https://pyformat.info​
​ A typical session looks like (the numbers are made up!) this:

```
prompt> python basedist human.fa mouse.fa fly.fa yeast.fa ecoli.fa plasmodium.fa thermus.fa
   7
Hsapiens  0.0   0.009   0.014   0.041   0.042   0.073   0.126
Mus_muscul0.009	0.0     0.017   0.044   0.039   0.079   0.126
Fly       0.014	0.017	0.0     0.054   0.031   0.081   0.112
Yeast     0.041	0.044	0.054	0.0     0.083   0.048   0.112
Ecoli     0.042	0.039	0.031	0.083	0.0     0.111   0.088
Plasmodium0.073	0.079	0.081	0.048	0.111	0.0     0.182
Thermus_th0.126	0.126	0.112	0.166	0.088	0.182	0.0
```


#### Clarifications
You do not need to change the accessions (name of the from the fasta file) to look "nice", but you do have to limit their length to 10 characters.
The numbers in the example are made up. But should be printed with 3 decimals.


## 5. Addition modules, URL and Exception 
Do this assignment after Video Lecture 5. The assignment is to complete the code in the `fetch_sequences.py` file from the `exercise.zip` archive. 







