# JVME-peer-review
Python scripts and sample data

This material accompanies a submission to the Journal of Veterinary Medical Education.  

Python script "assign_peer_review.py"  generates a HTML file (tasks.HTML) which contains  peer review assignments. The script randomly assigns  a two character student ID with a two digit case number.  This script requires two CSV files and one directory: 

1. "dates.csv" which contains the case numbers to be presented each calender day
2. "student.csv" contains the student two character codes
3. "public_HTML" a directory which receives the output from the python scripts.


Python script "answers_web_page.py"  generates a HTML file (answers.HTML) which contains a text description of a set of diagnostic images. This script requires one CSV file and two directories as follows:

1. "dates.csv" which contains the case numbers to be presented each calender day
2. Directory containing descriptions of case findings as text files written in HTML markup
3. "public_HTML" a directory which receives the output from the python scripts.


To run these files, first download all to a single directory so that after download the directory contains

1. assign_peer_review.py (python script)
2. answers_web_page.py (python script)
3. dates.csv (CSV file)
4. student.csv (CSV file)
5. public_HTML (Directory)

In a UNIX type operating system (Linux or MAC OSX) open a BASH terminal, navigate to the directory containing the above files and run the scripts by typing "python assign_peer_review.py" and then "answers_web_page.py".  Output HTML files will be visible in the public_HTML directory, and can be opened using a standard web browser.

Python is available by default in all Linux distributions and in MAC OSX.  Microsoft Windows users will have to install python.  The code has been tested on Linux and MAC OSX systems, but not in Microsoft Windows.
