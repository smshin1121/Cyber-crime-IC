@echo off
REM Cybercrime IC auto-collector - runs via Windows Task Scheduler
REM ASCII-only: Korean comments corrupt parsing under cp949 codepage (see LESSONS.md L8)

cd /d C:\Users\shin1121\Desktop\Cyber_crime_IC
python tools\auto_collect.py >> tools\collect.log 2>&1

REM Notify if new items were collected
findstr /c:"new IC-relevant items found" tools\collect.log >nul 2>&1
if %errorlevel%==0 (
    echo [%date% %time%] New items collected. Run /ic-update in Claude Code. >> tools\collect.log
)
