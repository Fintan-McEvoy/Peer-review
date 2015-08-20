import random

import csv
f=open('../csv_files/students.csv')
student_list=list()

r=csv.reader(f)
r.next()
for students in r:
	student_list.append(students[0])
f.close()
#print(student_list)


import datetime
now=datetime.datetime.now()
one_day=datetime.timedelta(days=1)
print 'One day:', one_day
print 'Today:',now
yesterday=now - one_day
print 'yesterday:',yesterday.day



g=open('../csv_files/dates3.csv','r')
h=open('../csv_files/dates3.csv','r')

t=csv.reader(g)
t.next()
t.next()
case_list=list()
case_list_old=list()

for row in t:
	casenum_last=row[yesterday.day]
	if casenum_last !="":
		case_list_old.append(row[yesterday.day])
print(case_list_old)



s=csv.reader(h)
s.next()
s.next()


for row in s:
	casenum = row[now.day]
	if casenum !="":
		case_list.append(row[now.day])


task_list=list()

print('equality')
if (case_list==case_list_old) is True:
	print('equlity done....that was true')
else:
	print 'equality done ... that was not true'

for name in student_list:
		for case in case_list:
			task_list.append(name+case)
random.shuffle(task_list)
print 'her comes the task list'
print(task_list)
ln_task=len(task_list)
ln_student=len(student_list)

print(ln_task)
print(ln_student)
max=(ln_task/ln_student)
remainder=(ln_task % ln_student)
print(remainder) 


assignments = {}

for task in task_list:
	assignments[task]=None

student_index = 0
while(None in assignments.values()):
	student = student_list[student_index]
	print("--------------")
	task_index=0
	task=task_list[task_index]
	task_author=task[0:2]
	
	print("Looking at student:" + student)
	while (task_index < ( len(task_list)-1 ) and (student == task_author or assignments[task] is not None)):
		task_index=task_index+1
		task=task_list[task_index]
		task_author=task[0:2]
		task_author=task_author + ";"
	if student != task_author:
		assignments[task] = student
		print("assigning task:" + task + " to student")
		print("task author:" + task_author)
		print (task_author + ";;")
		print (student)
		print(task)
		print 'kkkkkkkkk'
		print (student)


# If the main while loop has reached the end of the student list. Reset the student index
	if student_index == (len(student_list) - 1):
		student_index = 0
	else:
		student_index = student_index + 1
 


print("=========== ASSIGNMENTS =======")
print("STUDENT\tTASK")

result_list=list()
for  k,v in assignments.iteritems():
	result_list.append("student "+v+"...please evaluate report by your colleague " +k[0:2]+" on case " +k[2:]+ "<br/>")
	print(v + "\t" + k)

#print(sorted(result_list))

header=("<b>Peer review assignments.</b></br>Here is the list of current peer review assignments.  It was created at 4pm on "+(datetime.date.today().strftime("%A"))+" "+(datetime.date.today().strftime("%d/%m/%Y"))+"<br/><br/>Please complete these assignments within the next 24 hours. <br/><br/>Student IDs were assigned at random to give some degree of anonymity.  You will find the reports you are to evaluate on the course web site on absolon. Go to the file 'studentReports', then open the folder with the name of the student your have been assigned to assess, e.g. 'aa, or ba, or ca ...etc.'. There you will find your colleague's reports named by case number, 'n.docx', where and 'n' is the case number for the case your are to evaluate.  You can see which student / reports you have been assigned to review below.</br></br>You should wait until you have heard the cases discussed at case rounds and have read the web comments for the cases before you start your evaluations.</br></br>We ask you to evaluate the reports using the form available <a href=https://docs.google.com/a/mcevoy.se/forms/d/19EgqZ5ixQAtPaoE73Z0RXtKWIyEqm4X86Qy5tECtHNY/viewform?usp=send_form>HERE</a> . When you open this form you will be reminded of the evaluation criteria to apply.</br></br></br>")


if (case_list==case_list_old) is True:
	print('equlity done....that was true')
else:
	print 'equality done ... that was not true'

if (case_list!=case_list_old) is True:
	output_file = open("../public_html/tasks.html","w")
	html_string = header
	for item in sorted(result_list):
		html_string = html_string + item
	output_file.write(html_string)
	output_file.close()
else:
	print 'no change in case list so review assignments not updated'
		
print(max)
print(ln_task)	
print(ln_student)


