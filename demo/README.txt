Installation:
	Download and copy the "demo" directory and its
	contents to %USERPROFILE%\Desktop\

Participants:
	To change participants, edit or replace either 
	or both of the files in the data directory:

	%USERPROFILE%\Desktop\demo\data\females.csv
	%USERPROFILE%\Desktop\demo\data\males.csv

Note: This operation is best done using the 
%USERPROFILE%\Desktop\demo\MD App CMD
Shortcut which launches all of the
applications, as the file names, file type (CSV), data 
format, and path to the data files must not change.
(move this anywhere that you find convenient, 
e.g., the Desktop)


Use (including application paths to moving parts):

%USERPROFILE%\Desktop\demo\MD App CMD
	Shortcut that runs a Python programming language script.
	This "runner" includes use instructions, so
	it is recommended for first time use.
	(move this anywhere that you find convenient, 
	 e.g., the Desktop)

%USERPROFILE%\Desktop\demo\show-script-output.py 
	(Python script that runs:
		notepad (used to edit females.csv and males.csv)
		run.bat

%USERPROFILE%\Desktop\demo\Assign Courts Mixed Doubles
	A shortcut that can be used to run an Elixir programming 
	language application using the Erlang Virtual Machine and
	runtime environment.
	The program assigns pairs of females and males to courts 
	and builds waitlists
	(move this anywhere that you find convenient, 
	 e.g., the Desktop, for use when no adjustment 
	 to the data files is required -- that is, no 
	 need to adjust participants).

%USERPROFILE%\Desktop\demo\run.bat
	runs the elixir app that builds mixed doubles
	rosters and waitlists and copies output
	to the Windows clipboard
	runs notepad into which clipboard can be pasted
	(Note: Save the notepad file where you wish and
	 close notepad before exiting the main program.
	 note: the clipboard still holds the rosters and
	 the waitlists in case pasting into another program
	 is what is desired).

%USERPROFILE%\Desktop\demo\data contains these data files:
	females.csv
	males.csv

%USERPROFILE%\Desktop\demo\.demo_release\bin\demo.bat
	run.bat runs this script when the "Assign Courts"
	button is clicked
	
	demo.bat runs the elixir app which assigns courts
	and waitlists

%USERPROFILE%\Desktop\demo\.demo_release\*
	contains all that a Windows users needs to run the
	Erlang Virual Machine and Erlang runtime as well as
	the Elixir app itself (no need to install anything).

%USERPROFILE%\Desktop\demo\README.txt
	this file
