# JVME-peer-review
Python scripts and sample data

This material accompanies a peer review exercise used at the University of Copenhagen.  

The folder "python_scripts" contains two files,  "assign_peer_review.py" and "answers_web_page.py".  The first of these,   which generates a HTML file (tasks.HTML) that  contains  peer review assignments. The script randomly assigns  a two character student ID with a two digit case number.  This script requires two CSV files and one directory: 

1. "dates.csv" which contains the case numbers to be presented each calender day
2. "student.csv" contains the student two character codes
3. "public_HTML" a directory which receives the output from the python scripts.


The file "answers_web_page.py"  generates a HTML file (answers.HTML) which contains a text description of a set of diagnostic images. This script requires one CSV file and two directories as follows:

1. "dates.csv" which contains the case numbers to be presented each calender day
2. Directory containing descriptions of case findings as text files written in HTML markup
3. "public_HTML" a directory which receives the output from the python scripts.


To run these python files, first download and expand the zip file for this repository.  Using a terminal window, navigate to the pyhton_scripts directory.  If necessary, change permissions for the python scripts so they are executable on your machine. Run the scripts in the usual way, e.g. by entering "python assign_peer_review.py" at the command prompt. The output for these files can be seen in the "public_html" folder.  These files are called answers.html and tasks.html, old copes are present in the dounload, they are replaced by fresh html files every time the appropriate python script is run.


Python is available by default in all Linux distributions and in MAC OSX.  Microsoft Windows users will have to install python.  The code has been tested on Linux and MAC OSX systems, but not in Microsoft Windows.



When downloaded, the public_html folder als contains a file "motion_chart.html" This is a link to a Google chart.  It require an internet connection go google.com and a browser that runs Adobe Flash.
