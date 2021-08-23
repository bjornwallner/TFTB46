---
title: Labs in Advanced Bioinformatics
permalink: /lab1/
---


# ​​Lab 1: Unix and Python programming
In the Python assignments you are expected to use Python and no additional libraries. The goal is to practice writing "pure" Python for those occasions when libraries or other good tools are not available for one reason or another. Assignment 1 can be completed after the first lecture and 2-3 after the Video Lecture 1, 4-6 after Video Lecture 2, 7-9 after Video Lecture 3.

To help you get organized the assignments (except those related to a Video Lecture)​ should be solved by adding code to the following code skeleton: [lab1.py](lab1.py)

It is important that you do the assignments in the order presented here. You will not gain time by skipping the initial assignments. 

## Assignments

1. [Unix introduction](#unix-introduction)
2. [Data type: strings​](#data-type-strings) (Video Lecture 1, string_exercise.py)
3. [Random DNA sequences](#random-dna-sequences)
4. [Real DNA sequences​](#real-dna-sequences​)
5. [Data type: lists](#data-type-lists) (Video Lecture 2, list_exercise.py)
6. [DNA, RNA or Protein](#dna-rna-or-protein)
7. [Re-formatting sequences](​re-formatting-sequences)
8. [Data type: dictionaries​](#data-type-dictionaries​) (Video Lecture 3, organismcount.py)
9. [Translate DNA](#translate-dna)

[hej](link)

## 1. Unix introduction

Solve these assignments in a terminal window, and perhaps using a browser.
1. Create a directory structure for this lab in your home directory using `mkdir` and `cd`. There should be a directory for the course, and within it a directory for each lab. Also download and unzip the exercises for the video lecture here: (exercises.zip)​ and place them in the course directory. 
2. Use the `man` command to figure out...
	1. what the command `ls -l` does.
	2. how you delete a directory and its contents with `rm`.
3. Find out, perhaps using​​ `man`, what the following commands are for. If you want you can use the file [gpcr.tab](gpcr.tab), which is in the [exercise.zip](exercise.zip) archive, as an example.
   * cat
   * more or less
   * head
   * tail
   * wc
   * grep
   * sort​
   * uniq
   * cut​
​​
4. Working in Unix

Here you will need to use Unix redirection of input and output. You can have a look at the [Unix introduction](unix_introduction.pdf)​ slides if you want.

The file [gpcr.tab](gpcr.tab)​​ contains data concerning G-coupled protein receptors from a number of species. We will use it solve the following in the terminal:
1. Take a look at the gpcr.tab using head. How many columns are there (if you count by eye)? 
2. How many lines is there in the file?
3. Use grep and wc to find out how many human GPCRs there are listed. Do you search for "human" or "Homo sapiens"?
4. How long is the shortest sequence listed in the same file? Use cut and sort!
5. How many species are named in gpcr.tab?

## 2. Data type: strings​ 
Do this assignment after Video Lecture 1. The assignment is to complete the code in the `string_exercise.py` file from the `exercise.zip` archive. 

## 3. Random DNA sequences ​​
To help you get organized the assignment (not related to a Video Lecture)​ should be solved by adding code to the following code skeleton: `lab1.py​

Random DNA sequences
Add the functionality to your software to generate random DNA sequence in Fasta format, and to calculate the nucleotide composition (i.e. the frequence of each nucleotide) of the random DNA sequence.

You should add your code to the functions: "random_DNA(N)" and "print_nucleotide_composition", and adapt the main() function so it will run your code.

Requirements
Your program should get the length of the sequence from the command line and use the name "myrandomsequence" 
The session should look something like:​

bash$ python lab1.py --lab 3 40
I will try to run lab number: 1.3
Random DNA
>myrandomsequence
CCTCGCTCTGACTTAGCTTTGATACTAATATACATACAAT
Composition: A: 0.3 C:0.25 T:0.35 G:0.1
The output must be in valid Fasta format, and contain the nucleotide composition. It should also be able to handle the case where the user specifies zero length.​​

​The Python module random is suitable to use in this assignment. Take a look at the online documentation the random module! Which function do you find most useful for this assignment?​


## 4. Real DNA sequences​ ​ 

## 5. Data type: lists
Do this assignment after Video Lecture 2. The assignment is to complete the code in the `list_exercise.py` file from the `exercise.zip` archive. 


## 6. DNA, RNA or Protein

## 7. Re-formatting sequences​

## 8. Data type: dictionaries​
Do this assignment after Video Lecture 3. The assignment is to complete the code in the `organismcount.py` file from the `exercise.zip` archive. 


## 9. Translate DNA


