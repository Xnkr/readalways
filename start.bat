subl
python manage.py runserver
@ECHO OFF
CHOICE /C YN /M "git push?"
IF ERRORLEVEL ==2 exit
IF ERRORLEVEL ==1 goto push

:PUSH
echo "hello"