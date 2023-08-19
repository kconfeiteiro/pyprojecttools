@echo off
setlocal EnableDelayedExpansion

echo.
echo =======================
echo Updating PyProjectTools
echo =======================
echo.
echo Changing directories...
cd PyProjectTools
echo Pulling from main branch...
git pull
echo.
echo Returning to working directory...
cd ..
echo.
echo PyProjectTools is updated ready for use...
echo.
pause
goto exit_menu

:exit_menu
set /p "yes_no=Do want to exit the terminal? (Y/N): "
if /i "!yes_no!"=="N" (
    echo.
	timeout /t 2 > nul
	echo Clearing terminal..
	cls
) else if /i "!yes_no!"=="Y" (
	echo Closing terminal window
	timeout /t 2 > nul
	echo Goodbye
	cls
	exit
)
