---
title: Lab 3 in Advanced Bioinformatics
permalink: /lab3/
---


# ​​Lab 3

​​​​​These assignments are meant to introduce you to Biopython and some other useful Python modules.

The online documentation of Biopython might be useful and can be found here: [http://biopython.org](http://biopython.org)

Here you need to use: module initadd courses/TFTB46 to get access to biopython on the school's computers.

If you want install biopython on your own computer it is easiest to install [Anaconda python package handler](http://anaconda.com/downloads), 
​once installed you should be able to install biopython. On mac or linux you can write: conda install biopython in the terminal


### ​Assignments
1. [Translate DNA 2.0](#1-translate-dna-20)
2. [Running external programs](#2-running-external-programs) (Video Lecture 6, pipeline.py)​​
3. [Remote Blast](#3-remote-blast)
4. [Blast ​parsing​​](#4-blast-​parsing​​)



## 1. Translate DNA 2.0
Use BioPython to write a program that reads a Fasta file containing genes and writes their translations to stdout.

You may not re-use any code from lab 1. Input, output, and translation must be done using BioPython.

### Test data
[This file](translationtest.dna) contains interesting tests.​
[Here](empty.fa) is an empty​ file.

### Requirements
Your program must handle all test files gracefully.

Example session:
```
bash$ python translation2.py translationtest.dna
>stopcodons
***************************
>alphabet_gene
ARNDCQEGHILKMFPSTWYV
>alphabet_gene2
ARNDCQEGHILKMFPSTWYV​
```


## 2. Running external programs
Do this assignment after Video Lecture 6. The assignment is to complete the code in the `pipeline.py` file from the `exercise.zip` archive. 

## 3. Remote Blast
In this assignment, you will use BioPython to run a Blast job at NCBI.

### Data
Download the human CST3 protein sequence.


### Preliminaries
* Figure out what Blast does and how it works.
* Go to the NCBI Blast web page (find it yourself...) and start a Blast comparison with CST3 against the so-called non-redundant protein database: nr. This means that you comparison should use the "blastp" subprogram (protein query against protein DB).
* Find the highest scoring hit in mouse
* What is the E-value, and what does that mean?
* Look at the actual alignment. How alike are the sequences?


### Programming
* Write a Python program that conducts a Blast search of a given protein sequence against the nr database at NCBI. There is good support for this in BioPython.

### Requirements
* Your program is a Python script taking one input: a file containing a protein sequence in FASTA format.
* Save the results and output the blast report given in XML format to a file (you will use it the last assignment) and also output it to stdout.

### To present:
* You should be able to give a brief explanation of Blast.
* What is the E-value, and what does that mean?
* You should understand the online output from a Blast run.
* Your code for the remoteblast program.
* Demonstrate a successful run of remoteblast.

Example session
Usage of your program should be something like this:

```
bash$ python remoteblast.py cst3.fa
<?xml version="1.0"?>
<!DOCTYPE BlastOutput PUBLIC "-//NCBI//NCBI BlastOutput/EN" "NCBI_BlastOutput.dtd">
<BlastOutput>
  <BlastOutput_program>blastx</BlastOutput_program>
  <BlastOutput_version>blastx 2.2.6 [Apr-09-2003]</BlastOutput_version>
  <BlastOutput_reference>~Reference: Altschul, Stephen F., et al (1997), "Gapped
BLAST and PSI-BLAST: a new generation of protein database search~programs",
Nucleic Acids Res. 25:3389-3402.</BlastOutput_reference>
  <BlastOutput_db>sprot</BlastOutput_db>
  <BlastOutput_query-ID>lcl|QUERY</BlastOutput_query-ID>
  <BlastOutput_query-def>CST3</BlastOutput_query-def>
...
```

Output is trimmed. 

## 4. Blast ​parsing​​

Use BioPython to filter the results from a Blast run. You want to be able to specify a substring that will match the accession, and you can assume that you always want to remove any hits with an E-value larger than 1e-20. The input is a Blast report in XML format.

### Data
Here is some sample test data. You should however also manage to handle the output of the previous assignment.
Please note: Browsers get confused if you try to look at these XML files in the browser. Right click and download the files directly!

[test1.xml](test1.xml) contains 3 hits and none is from mouse.
[test2.xml](test2.xml) contains 11 hits, of which one is from mouse.
[Blast result file](cst_blast.xml) is in XML format.


### Requirements
Write a Python program that fulfills the following.

* Your Python script takes two inputs:
  1. A command line argument with a string that should match "accession", "title" field in the Blast hit list, e.g., "mouse". 
  2. A file to read input from. The file contains Blast XML data.

Output goes to stdout and is a table with four columns:
1. Query accession
2. Target accession
3. Score
4. E-value
where only sequences with an accession matching the input substring are listed, and each sequence pair is listed only once.

### Example session
In this example, the first column has been simplified. The actual accession can be more complicated!
```
bash$ python blastparse.py MOUSE test1.xml
Warning: No hits
bash$ python blastparse.py MOUSE test2.xml
CST3 24130 469.0 3.45493e-47​
```

