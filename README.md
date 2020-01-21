# Bright-Mark

## Authors - Gavin Mesz, Faizaan Qureshi

Date - June 19 2019

Version - 1.0

Programming Language - Python 3.x

Program Assumptions - Windows OS, Mac OSX, Linux installed with and capable of running Python 3.x

Features of Program - Store classes, students, assignments, and grades into files. Access these variables anytime and edit them. Calculate total class averages and individual 
student averages in a easy to understand graphical interface.

Restrictions - Cannot input individual strands of marks for each assignment (knowledge, application, communication, thinking)

Known Errors - If a non integer is inputed in an integerbox, the user is prompted that what he/she has entered is not a number and the program asks for the users input again

Implementation Details/How to build the program - Install the latest version of easygui and follow the installation steps in the easygui documentation. Ask the user to open 
or create a class which creates a program file where variables are stored. User can select a class which leads to a choicebox. Through file management, the user can delete
students and add students which are either appended or removed to a class file. The user can calculate the average of each student using the formula of (mark * weight ) / weight
and the program prints the average to a msgbox. The user can view each student's markbook where all the assignments are viewed through a choicebox. User can add and remove
assignments through file management.

Additional Files - Program files included in application folder are required. All files created by program are also stored here. It contains data of classes, students, etc.
