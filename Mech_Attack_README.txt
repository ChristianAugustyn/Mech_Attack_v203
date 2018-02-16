******************************************************************************
Author: Austin Witherall and Christian Augustyn
******************************************************************************
Class: ICS3U1 – 01
******************************************************************************
Date: 2016-05-27
******************************************************************************
Version: 1.4.0
******************************************************************************
Unit: CPT
Question: Create a text based game or application
******************************************************************************
Programming Language: The programming language used is Python 3.5.1
******************************************************************************
Problem Description: 
Mech Attack is a text based game that is based on a mech battle sequence. 
Mech's are large robots that are used in battle and are typically in anime or 
video games. The battle style of Mech Attack is a turn based game that is in 
the fashion of a tournament. The objective is to beat all of the competition
while upgrading your mech's stats throughout, increasing the strength of your
mech. 
******************************************************************************
Problem Assumptions:
This problem assume that the player knows how to input different commands and 
will read the help menu and stat definitions so that they know how to play the 
game and what each stat mean. The program also assumes that the player knows 
how to play a turn based game and knows what to expect when they play this 
style of game. The problem also assumes that the user knows to press enter 
after each time they are asked to enter a value or option.
******************************************************************************
Features of the Program:
Mech Attack features a help menu that gives the user the option to view the 
rules or see the definitions of each stat, these definitions will give the 
meaning and implementation of each stat type. The program also uses ascii art 
that gives a visual of what is occurring and some visual of the different types 
of mechs that they will be fighting in the tournament. The program also 
features an option for the user to quit at anytime when they have given up or 
if they no longer want to play.
******************************************************************************
Restrictions:
The program is restricted to a turn based game with a battle phase that 
involves an attack turn, a special attack turn or an inventory. The program 
does not have an option to move position.
******************************************************************************
Known Errors:
Occasionally when the user uses an incendiary it will do double damage rather 
than damage over 2 turns. The CPU also had this option of the incendiary but 
when used, it would switch some of the stats so this option had to be taken 
out of the program.
******************************************************************************
Implementation Details:
The program implements ascii art to create a more appealing player interface. 
The program also uses various if statements to differentiate what the user is 
inputting into the program and to verify that what they have entered was 
correct or invalid. The program also uses Exception Handling to verify that 
the user is entering the correct type of value and to determine whether the 
user has won or loss. The program uses lists to carry the stats of each mech 
and the opponent mech, lists are also used to return multiple values and later 
sliced to separate the different values. Uses random library to determine the 
CPU's turns and what they choose.
