import easygui
import json
import collections
import os
import random

title="Bright Mark"

def removeNone(list): #Removes type NONE if NONE in list
    while None in list:
        list.remove(None)

def delete_del_and_add(list):
    list.remove("Delete a student")
    list.remove("Add a student")

def add_del_and_add(list):
    list.append("Add a student")
    list.append("Delete a student")

def delete_del_and_add_ASSIGN(list):
    list.remove("Delete an assignment")
    list.remove("Add an assignment")

def add_del_and_add_ASSIGN(list):
    list.append("Add an assignment")
    list.append("Delete an assignment")

a=0
f=0
k=0

#MENU
while k==0:
    #OPEN CLASS OR ADD NEW
    oioi=["Open","Add"]
    a=0
    choice=easygui.buttonbox("Hello! Do you want to open or add a file?",title,oioi) ##open file or add a file
    while choice==None:
        quit()
        break
    while choice=='Add':
        file=open("goodfiles.txt",'r') #reads classes before they are erased
        nardfiles=file.readlines(1-100)
        file.close()
        with open("goodfiles.txt",'w+') as goodfile: #list of actual class files in a txt
            #TEACHER ENTER
            newfile=easygui.enterbox("Create a new file name.",title) ##create new file name
            if newfile==None:
                newfile = ""
                break
            for root, dirs, files in os.walk('.'): #finds all files in the directory this file is stored in
                for p in files:
                    while p in newfile+".txt": #if file has same name as another, will create file with a number
                        coolionumber=random.randint(10,99)
                        newfile=newfile+str(coolionumber)
            nardfiles.append(newfile+".txt")
            for newfile in nardfiles:
                goodfile.write(newfile+"\n") #Files to be shown in the pick a file area as to not pick a student file
            file=open(newfile,"w+") ##opens new file under the new file name
            teacher=easygui.enterbox("What's the teacher's name?",title) ##teacher's name
            while teacher==None:
                break
            while teacher!=None:
                file.write(teacher+"\n") ##Writes teacher's name at top of file
                #STUDENT NAMES
                num=1 #student counter to 0
                f=0
                ques="How many students?"
                names=[]
                numberofstudents=easygui.integerbox(ques, title) #asks for number of students in class
                while numberofstudents==None:
                    break
                if numberofstudents!=None:
                    n=1
                    for i in range(numberofstudents): #writes each student in file
                        while n!=numberofstudents:
                            y=easygui.enterbox("First name of student "+str(num)+"? ",title)
                            if ' ' in y:
                                py=easygui.msgbox("Only the student's first name",title)
                                y=''
                            else:
                                num+=1
                                for root, dirs, files in os.walk('.'): #finds all files in the directory this file is stored in
                                    for p in files:
                                        if p in y+".txt":
                                            coollastname=easygui.enterbox("Enter the student's last name", "Markbook")
                                            y=y+' '+coollastname
                                newfilelol=open(y+".txt",'w') #Adding files for each student
                                newfilelol.close()
                                file.write(y+"\n")
                                names.append(y+"\n")
                                break
                        if n==numberofstudents:
                            break
                    num=1
                    file.close()
                    choice=''
                    break
    while choice=='Open': #OPENING FILE
        file=open("goodfiles.txt",'r')
        nardfiles=file.readlines(1-100)
        file.close()
        if len(nardfiles)==0:
            p=easygui.msgbox("You cannot view classes as you do not have any.",title)
            choice=''
            break
        else:
            file=[] #txt files (one we want)
            fileno=[] #will be the files that are part of the list in the goodfiles.txt file
            classfiles=open("goodfiles.txt",'r')
            filestohave=classfiles.readlines(1-100) #new list of the classes we want
            for i in filestohave:
                filestohave2=i.replace("\n",'')
                fileno.append(filestohave2)
            classfiles.close()
            print(filestohave)
            for root, dirs, files in os.walk('.'): #finds all files in the directory this file is stored in
                for p in files:
                    if p in fileno: #append wanted files to a list
                        file.append(p)
                print(file)
                file.append(">Delete a file<")
                openfile=easygui.choicebox("Choose the file you want to open.",title,file) #user chooses which file to open
                file.remove(">Delete a file<")
                while openfile==">Delete a file<": #DELETE FILE
                    removefile=easygui.choicebox("Choose a file to delete.",title,file)
                    if removefile==None:
                        openfile=''
                        break
                    else:
                        file3=open(removefile,'r')
                        teacherssss=file3.readlines(1)
                        studentsremoval=file3.readlines(2-100)
                        print(studentsremoval)
                        for i in studentsremoval:
                            if i not in teacherssss:
                                p=i.replace("\n",'')
                                os.remove(p+".txt")
                        file3.close()
                        file2=open("goodfiles.txt",'r')
                        filestoremove=file2.readlines(1-100)
                        file2.close()
                        file.remove(removefile)
                        os.remove(removefile)
                        file2=open("goodfiles.txt",'w')
                        for i in filestoremove:
                            if i==removefile+"\n":
                                print("nope")
                            else:
                                file2.write(i+"\n")
                        openfile=None
                        choice=''
                        break
                if openfile==None:
                    choice=''
                    break
                a=0
                #STUDENT NAME LIST/MAIN PROGRAM
                while a==0:
                    print(openfile)
                    with open(openfile,"r+") as f: #open the file in read and write mode
                        for i in f.readlines(1): #finds the teachers name in the file
                            teacher=i
                        teachernew=teacher.replace("\n","")
                        olderstudents=f.readlines(2-100) #Reads everything after the first line (all of the students)
                        students=[]
                        for i in olderstudents: #checks if number is in student name
                            y=i.replace("\n",'')
                            if '1' in y[-2:] or '2' in y[-2:] or '3' in y[-2:] or '4' in y[-2:] or '5' in y[-2:] or '6' in y[-2:] or '7' in y[-2:] or '8' in y[-2:] or '9' in y[-2:] or '0' in y[-2:]:
                                pp=y[:-2]+"\n"
                                students.append(pp)
                            else:
                                pp=y+"\n"
                                students.append(pp)
                        classavg=''
                        graderino=0
                        totallen=0
                        print(students)
                        for avg in students: #START OF CLASS AVG CALCULATOR
                            y=avg.replace("\n",'')
                            print(y)
                            lol=open(y+".txt")
                            newavg=lol.readlines(1-100)
                            print(lol.readlines(1-100))
                            lol.close()
                            totallen+=len(newavg)
                            if len(newavg)==0:
                                print("Nope")
                            elif len(newavg)>0:
                                for plox in newavg:
                                    ll=plox.replace("\n",'')
                                    y=ll[-2:]
                                    print(y)
                                    if '00' in y:
                                        y=100
                                    elif ':' in ll[-2:]:
                                        y=ll[-1:]
                                    graderino+=int(y)
                                print(graderino)
                                print(totallen)
                        if totallen==0:
                            classavg="None"
                        else:
                            print(totallen)
                            print(graderino)
                            classavg=int(graderino)//totallen #END OF CLASS AVG CALCULATOR
                        students.append(">Add a student<")
                        students.append(">Delete a student<")
                        classmainpage = easygui.choicebox("Welcome to " + teachernew + "'s class! The class average is "+str(classavg)+"%", title, students)
                        while classmainpage == None: #IF USER PRESSES CANCEL ON MAIN PAGE////TO BE REPLACED BY GAVIN'S CODE TO MAIN SCREEN OF SAVED CLASSES
                            choice=''
                            a=1
                            break
                        while classmainpage == ">Add a student<": #ADD
                            newstudent = easygui.enterbox("Enter the name of the new student", title)
                            if newstudent == None or newstudent=='': #If user clicks cancel
                                classmainpage=''
                                break
                            elif newstudent!=None or newstudent!='':
                                newfilelol=open(newstudent+".txt",'w') #makes a new file for the student
                                newfilelol.close()
                                f.write(newstudent+"\n")
                                classmainpage=''
                                break
                        while classmainpage == ">Delete a student<": #DELETE
                            students.remove(">Add a student<")
                            students.remove(">Delete a student<")
                            delstudent = easygui.choicebox("Select student to delete", title ,students)
                            if delstudent == None: #If user presses cancel while deleting a student
                                students.append(">Add a student<")
                                students.append(">Delete a student<")
                                classmainpage=''
                                break
                            if delstudent != None: #If the user does not press "Add more choices"
                                students.remove(delstudent)
                                with open(openfile,'w') as f_new:
                                    f_new.write(teacher)
                                    for i in students: #writes new set of students into the class file
                                        f_new.write(i)
                                    y=delstudent.replace("\n",'')
                                    os.remove(y+".txt") #deletes student's file
                                    students.append(">Add a student<")
                                    students.append(">Delete a student<")
                                    classmainpage=''
                                    break
                        if classmainpage in students: #STUDENT MARKBOOKS
                            choices = ["Compute Average", "Insert Mark", "View Markbook", "Back"] #Choices for button box
                            studentguy=classmainpage.replace("\n",'')
                            f=open(studentguy+".txt",'r')
                            grades=f.readlines(1-100)
                            f.close()
                            kd=0
                            while kd==0:
                                with open(studentguy+".txt",'w+') as a: #OPEN STUDENT FILE
                                    for newgradesyeet in grades: #writes students grades into a file
                                        a.write(newgradesyeet)
                                    userchoice = easygui.buttonbox("What would you like to do with " + studentguy, title, choices=choices)
                                    while userchoice == "Back" or userchoice==None: #If user presses back while at button box
                                        classmainpage=''
                                        userchoice=''
                                        kd=1
                                        a=0
                                        break
                                    while userchoice == "Insert Mark": #Gavin's Work: Find a way to save all these variables by student in a file #If user presses "insert mark"
                                        assignment = easygui.enterbox("Enter assignment name", title)
                                        if assignment == None: #If user presses cancel
                                            while assignment == None:
                                                break
                                            break
                                        newass=assignment+' '
                                        if assignment!=None:
                                            year = easygui.integerbox("Enter the year of completion", title, lowerbound=0, upperbound=3000)
                                        if year == None: #If user presses cancel
                                            while year == None:
                                                break
                                            break
                                        newye=newass+str(year)+'/'
                                        month = easygui.integerbox("Enter the month of completion", title, lowerbound=0, upperbound=12)
                                        if month == None: #If user presses cancel
                                            while month == None:
                                                break
                                            break
                                        newmon=newye+str(month)+'/'
                                        day = easygui.integerbox("Enter the day of completion", title, lowerbound=0, upperbound=31)
                                        if day == None: #If user presses cancel
                                            while day == None:
                                                break
                                            break
                                        newday=newmon+str(day)+' '
                                        grade = easygui.enterbox("Enter grade", title)
                                        if grade == None: #If user presses cancel
                                            while grade == None:
                                                break
                                            break
                                        k=0
                                        while k==0:
                                            newgrade=newday+':'+str(grade) #Add grade to markbook and display
                                            grades.append(newgrade+"\n")
                                            a.write(newgrade+"\n") #writes new grades into students file
                                            userchoice=''
                                            k=1
                                            break
                                    while userchoice == "View Markbook": #Gavin's Work: Find a way to save files again but use my GUI foundation (Do this for all buttons in buttonbox of student)
                                        grades.append(">Add new mark<")
                                        grades.append(">Delete a mark<")
                                        allassignments = easygui.choicebox("All assignments of " + studentguy, title,grades) #Choicebox menu
                                        grades.remove(">Add new mark<")
                                        grades.remove(">Delete a mark<")
                                        if allassignments == ">Add new mark<": #If user adds more choices at assignment screen
                                            userchoice='Insert Mark'
                                            break
                                        elif allassignments==">Delete a mark<":
                                            delassign=easygui.choicebox("Which assignment do you want to delete?",title,grades)
                                            if delassign==None:
                                                userchoice=''
                                                break
                                            elif delassign!=None: #deletes mark from mark list and from file
                                                grades.remove(delassign)
                                                fnewye=open(studentguy+".txt",'w')
                                                print(grades)
                                                for getridof in grades:
                                                    print(getridof)
                                                    fnewye.write(getridof)
                                                fnewye.close()
                                                userchoice=''
                                                break
                                        elif allassignments==None:
                                            userchoice=''
                                            break
                                    while userchoice == "Compute Average": #Calculates average
                                        if len(grades)==0:
                                            easygui.msgbox("You cannot calculate an average with no marks",title)
                                            userchoice=''
                                            break
                                        totalweight = 0
                                        for i in grades:
                                            y=i[-3:]
                                            print(y)
                                            if '00' in y:
                                                y=100
                                            elif ':' in y:
                                                y=i[-2:]
                                            totalweight+=int(y)
                                        length=len(grades)
                                        avg=totalweight//length
                                        p=easygui.msgbox(studentguy+"'s average is "+str(avg),title)
                                        userchoice=''
                                        break
                                        
                            
        

