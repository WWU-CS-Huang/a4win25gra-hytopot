% CSCI 497B - Assignment 3  % Fuqun Huang  % Spring 2024

### Problem Description

The problem description can be found [here](https://drive.google.com/file/d/1K8PD4VeOiNc8FCR5xBOt9M12qG17DRgb/view?usp=sharing)

### Setup

For this assignment, you must be able to write & run code in the language of your choice on your laptop. If Linux features are required that your laptop's OS does not support, you may either SSH into WWU's lab machines using [this guide](https://support.cs.wwu.edu/home/survival_guide/tools/SSH.html) or you may install Windows Subsystem for Linux using [this guide](https://learn.microsoft.com/en-us/windows/wsl/install).

## Walkthrough

Complete the following steps.

1.  Log into Canvas, find Assignment 3, and click the GitHub Classroom invitation link found there. You will need to log into your GitHub account if you haven't already.

2.  Once you have accepted the GitHub Classroom invitation, you will be given a link to your repository for this assignment. This link should be in the form of:

        https://github.com/WWU-CS-Huang/a3-username

    You should be able to click this link and see the repository on GitHub.

3. Create a working copy of your code by cloning the repository from GitHub. You can copy the command from the green button that says \"clone or download\" on GitHub, or type it yourself:

         # replace username with your github username
         git clone https://github.com/WWU-CS-Huang/a3-username

4. Now you will create a blank file to write your code in and tell git to track it (that is, include it in your repository). Note that spelling, spacing and capitalization matter in the following commands. If writing in a different language, use the appropriate file extension.

         touch Fractal.java
         git add Fractal.java # run "git help add" for details

5.  Begin working on your program. The problem description can be found [at this link](https://drive.google.com/file/d/1K8PD4VeOiNc8FCR5xBOt9M12qG17DRgb/view?usp=sharing).

6.  After working on your program for **30 minutes**, you will submit your first version. Commit your changes to the local repository:

        git commit -m "XX minute submission"

    Please specify the timing of your submission in the commit message. Commit a new version of your code after **40 minutes**, **50 minutes**, and **60 minutes**.

7.  To synchronize your local repo with the version on GitHub, push your changes from the local repository to the original one. You do not need to do this after every commit, but you must do so after the final commit.

        git push

## Submission

Make sure that you've followed all of the steps above, all of your latest changes are committed to your repository (check this using `git status`), and push your submission to Github.

## Grading

This assignment is worth 10 points, assigned as follows:

-   4 points: Initial 30-minute commit.
-   2 points each: Each following commit (40-, 50-, and 60-minute commit)

2 bonus points may be earned by spending more time to improve your code within the next 7 days.

##

*The materials are for the use of the students and instructors of CSCI497B and CSCI597B only. Copyrighted materials of Dr. Fuqun Huang and Owen Wright may not be further disseminated.*
