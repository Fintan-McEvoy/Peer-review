#This script should run daily at (15.30: i.e. when student case round end) 
import datetime
now=datetime.datetime.now()

import csv
import os

f= open('../csv_files/dates3.csv', 'r')

r =csv.reader(f)
r.next()#ignores first row for headers: 
r.next()#ignores next row for headers: 
reports_str=""
for row in r:
	casenum = row[now.day]
	if casenum != "":
		report_file=open("../case_reports/" + casenum + ".txt")
		reports_str=reports_str+report_file.read()
f.close()

#print reports_str

header_str="<b>Teaching points from our most recently completed cases.</b> <br/><br/>Below you will find some comments on the cases discussed at the most recent rounds session.<br/><br/><br/>"
footer_str='These cases will be available for review on the PACS until replaced by the next set of cases.  These new cases will be posted just after midnight on our next course day.  These new cases will be discussed at our next case rounds and this web page will be updated with comments immediately afterwards.' 

output_file = open('../public_html/answers.html','w')
output_file.write(header_str + reports_str + footer_str)
output_file.close()


