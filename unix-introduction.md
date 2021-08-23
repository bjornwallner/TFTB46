## 1. Unix introduction

Solve these assignments in a terminal window, and perhaps using a browser.
1. Create a directory structure for this lab in your home directory using `mkdir` and `cd`. There should be a directory for the course, and within it a directory for each lab. Also download and unzip the exercises for the video lecture here: (exercises.zip)​ and place them in the course directory. 
2. Use the `man` command to figure out...
	1. what the command `ls -l` does.
	2. how you delete a directory and its contents with `rm`.
3. Find out, perhaps using​​ `man`, what the following commands are for. If you want you can use the file [gpcr.tab], which is in the [exercise.zip] archive, as an example.
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

Here you will need to use Unix redirection of input and output. You can have a look at the (unix_introduction.pdf)​ slides if you want.

The file (gpcr.tab)​​ contains data concerning G-coupled protein receptors from a number of species. We will use it solve the following in the terminal:

	1. Take a look at the gpcr.tab using head. How many columns are there (if you count by eye)? 
	2. How many lines is there in the file?
	3. Use grep and wc to find out how many human GPCRs there are listed. Do you search for "human" or "Homo sapiens"?
	4. How long is the shortest sequence listed in the same file? Use cut and sort!
	5. How many species are named in gpcr.tab?
