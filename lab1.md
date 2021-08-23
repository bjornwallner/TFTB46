---
title: Labs in Advanced Bioinformatics
permalink: /lab1/
---


# ​​Lab 1: Unix and Python programming
In the Python assignments you are expected to use Python and no additional libraries. The goal is to practice writing "pure" Python for those occasions when libraries or other good tools are not available for one reason or another. Assignment 1 can be completed after the first lecture and 2-3 after the Video Lecture 1, 4-6 after Video Lecture 2, 7-9 after Video Lecture 3.

To help you get organized the assignment (not related to a Video Lecture)​ should be solved by adding code to the following code skeleton: [lab1.py]​(lab1.py)

## Assignments

1. [Unix introduction](#unix-introduction)
2. [Data type: strings​](#data-type-strings) (Video Lecture 1, string_exercise.py)
3. [Random DNA sequences](#random-dna-sequences)
4. [Real DNA sequences​](#real-dna-sequences​)
5  [Data type: lists](#data-type-lists) (Video Lecture 2, list_exercise.py)
6. [DNA, RNA or Protein](#dna-rna-or-protein)
7. [Re-formatting sequences](​re-formatting-sequences)
8. [Data type: dictionaries​](#data-type-dictionaries​) (Video Lecture 3, organismcount.py)
9. [Translate DNA](#translate-dna)§


## 1. Unix introduction

Solve these assignments in a terminal window, and perhaps using a browser.
1. Create a directory structure for this lab in your home directory using `mkdir` and `cd`. There should be a directory for the course, and within it a directory for each lab. Also download and unzip the exercises for the video lecture here: (exercises.zip)​ and place them in the course directory. 
2. Use the `man` command to figure out...
	1. what the command `ls -l` does.
	2. how you delete a directory and its contents with `rm`.
3..Find out, perhaps using​​ `man`, what the following commands are for. If you want you can use the file (gpcr.tab)​, which is in the (exercise.zip) archive, as an example.
	* cat
   * more or less
   * head
   * tail
   * wc
   * grep
   * sort​
   * uniq
   *cut​
​​
4. Working in Unix
Here you will need to use Unix redirection of input and output. You can have a look at the (unix_introduction.pdf)​ slides if you want..

The file gpcr.tab​​ contains data concerning G-coupled protein receptors from a number of species. We will use it solve the following in the terminal:

Take a look at the gpcr.tab using head. How many columns are there (if you count by eye)? 
How many lines is there in the file?
Use grep and wc to find out how many human GPCRs there are listed. Do you search for "human" or "Homo sapiens"?
How long is the shortest sequence listed in the same file? Use cut and sort!
How many species are named in gpcr.tab?

## 2. Data type: strings​ 
(Video Lecture 1, string_exercise.py)

## 3. Random DNA sequences ​​

## 4. Real DNA sequences​ ​ 

## 5. Data type: lists


## 6. DNA, RNA or Protein

## 7. Re-formatting sequences​

## 8. Data type: dictionaries​
(Video Lecture 3, organismcount.py)

## 9. Translate DNA


