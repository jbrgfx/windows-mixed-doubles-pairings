@echo off 
cd /d "%USERPROFILE%\Desktop\demo"
cmd /c "%USERPROFILE%\Desktop\demo\.demo_release\bin\demo.bat eval MixedDoubles.assignCourts" | clip
cmd /c notepad
