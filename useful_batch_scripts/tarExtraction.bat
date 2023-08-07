@echo off
setlocal EnableDelayedExpansion

:redo
echo TAR EXTRACT PROCEDURE
echo ----------------------
echo 1. continue
echo 2. terminate operation
echo 3. surprise

echo.
choice /c 123 /n /m "Enter number: "

if errorlevel 3 goto option3
if errorlevel 2 goto option2
if errorlevel 1 goto option1

:option1
echo ---------
echo Proceeding with extraction...
echo.

echo ======= Directory Input =========

:dir_input
set /p "tar_save_dir=Enter the name of the new directory: "
echo.
echo You entered: !tar_save_dir!

:validate_dir
set /p "yes_no=Do you wish to proceed? (Y/N): "
if /i "!yes_no!"=="N" (
    goto dir_input
) else if /i "!yes_no!"=="Y" (
    echo Proceeding...
) else (
    goto validate_dir
)

echo ----------
if not "!tar_save_dir!"=="" (
    if not exist "!tar_save_dir!" (
        mkdir "!tar_save_dir!"
        echo Directory created: "!cd!\!tar_save_dir!"
    ) else (
        echo Directory already exists: "!cd!\!tar_save_dir!"
        set /p "use_dir=Do you want to use an existing directory? (Y/N): "
        if /i "!use_dir!"=="N" (
            goto dir_input
        ) else if /i "!use_dir!"=="Y" (
            echo Proceeding...
            goto git_ignore
        ) else (
            goto dir_input
        )
        echo Enter a new directory for extraction
        goto dir_input
    )
)

:git_ignore
echo.
set /p "git_ignore=Add the directory to .gitignore file? (Y/N): "
if /i "!git_ignore!"=="Y" (
    REM Check if the .gitignore file exists, create it if it doesn't
    echo Proceeding...
    if not exist .gitignore (
        echo Creating .gitignore file...
        type nul > .gitignore
    ) 

    REM Append the file to .gitignore
    echo Adding !tar_save_dir! to .gitignore
    echo.>>.gitignore
    echo !tar_save_dir!/>>.gitignore
    echo.
    echo Displaying .gitignore...
    type .gitignore

    goto file_input
) else if /i "!git_ignore!"=="N" (
    echo Skipping .gitignore...
    goto file_input
) else (
    goto git_ignore
)

:file_input
echo.
echo ========= File Input ============
set /p "tar_file=Enter the tar file you would like to extract (Press E to explore directory): "
if "!tar_file!"=="E" (
    goto :explore
) else (
    echo Filename entered: "!tar_file!"

    :validate_file
    echo.
    set /p "yes_no2=Do you wish to proceed? (Y/N): "
    if /i "!yes_no2!"=="N" (
        goto file_input
    ) else if /i "!yes_no2!"=="Y" (
        echo Proceeding...
    ) else (
        goto validate_file
    )
)

:explore
echo.
set /p "tar_dir=Enter directory of the tar files (or enter CWD): "
if /i "%tar_dir%"=="CWD" (
    set "dir=%CD%"
) else if "%tar_dir%"=="" (
    set "dir=%CD%"
) else (
    set "dir=%tar_dir%"
)

REM Enumerate all .tar.gz files and store them in an array
set /a count=0
for %%F in ("%dir%\*.tar.gz") do (
    set /a count+=1
    set "file[!count!]=%%F"
)

REM Prompt the user with the enumerated list of files
echo Listing '.tar.gz' files in %dir%...
echo ----------
if %count%==0 (
    echo No files found in directory. Returning to the previous step...
    timeout /t 1 > nul
    goto explore
) else (
    echo Found %count% files:
    for /l %%i in (1,1,%count%) do (
        echo [%%i] !file[%%i]!
    )
    goto choice_prompt
)

REM Prompt the user to select a file
:choice_prompt
echo.
set /p "choice=Enter the number of the file you want to choose: "

REM Verify if the choice is valid (between 1 and the count of files)
echo.
if %choice% geq 1 if %choice% leq %count% (
    REM Set the chosen file name to a variable
    set "tar_file=!file[%choice%]!"
    goto extraction
) else (
    echo Invalid choice. Please select a valid number.
    goto choice_prompt
)

:extraction
echo Extracting !tar_file! into !tar_save_dir!
set /p "yes_no3=Do you wish to proceed? (Y/N): "
if /i "!yes_no3!"=="N" (
    echo Starting over...
    goto file_input
) else if /i "!yes_no3!"=="Y" (
    echo Proceeding...
)

echo ----------
echo Now extracting...
tar -xvzf "!tar_file!" -C "!tar_save_dir!"
echo --
echo Extraction complete
set /p "more=Would you like to extract another file? (Y/N): "
if /i "!more!"=="N" (
    timeout /t 1 > nul
    goto end
) else if /i "!more!"=="Y" (
    timeout /t 1 > nul
    echo Starting over...
    timeout /t 1 > nul
    cls
    timeout /t 1 > nul
    goto redo
)

:option2
echo ---------
echo You chose to end the operation
timeout /t 1 > nul
echo Goodbye
timeout /t 1 > nul
goto end

:option3
timeout /t 1 > nul
echo ----------------------------------------------------------------------------------------
echo --------------------                                      ------------------------------
echo ------------                                                           -----------------
echo                           oooo$$$$$$$$$$$$oooo
echo                       oo$$$$$$$$$$$$$$$$$$$$$$$$o
echo                    oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
echo    o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
echo oo $ $ $      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
echo $$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
echo   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
echo   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$     $$$
echo    $$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      $$$
echo     $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      $$$o
echo    o$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
echo    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$ooooo$$$$o
echo   o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
echo   $$$$$$$$ $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$
echo             $$$$    *$$$$$$$$$$$$$$$$$$$$$$$$$$$$*       o$$$
echo              $$$o     ***$$$$$$$$$$$$$$$$$$*$$*         $$$
echo               $$$o          *$$**$$$$$$*****           o$$$
echo                $$$$o                                o$$$*
echo                 *$$$$o      o$$$$$$o*$$$$o        o$$$$
echo                   **$$$$$oo     **$$$$o$$$$$o   o$$$$**e
echo                      **$$$$$oooo  *$$$o$$$$$$$$$***
echo                         **$$$$$$$oo $$$$$$$$$$
echo                                 ****$$$$$$$$$$$
echo                                     $$$$$$$$$$$$
echo                                      $$$$$$$$$$*
echo                                       *$$$***     
timeout /t 2 > nul
pause
echo See you later, alligator ;)
timeout /t 1 > nul
goto end

:end
echo Now closing terminal window...
timeout /t 2 > nul
exit