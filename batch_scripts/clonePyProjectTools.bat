@echo off
setLocal EnableDelayedExpansion

set "url=https://github.com/kconfeiteiro/PyProjectTools"

echo.
echo Cloning PyProjectTools..
git clone "!url!"
echo.
echo. PyProjectTools successfully cloned from "!url!"
echo.
pause
cls
