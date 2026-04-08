@echo off
REM 사이버범죄 국제공조 위키 — 자동 수집 스크립트
REM Windows Task Scheduler에 등록하여 주기적 실행

cd /d C:\Users\shin1121\Desktop\Cyber_crime_IC
python tools\auto_collect.py >> tools\collect.log 2>&1

REM 수집 결과가 있으면 알림
findstr /c:"new IC-relevant items found" tools\collect.log >nul 2>&1
if %errorlevel%==0 (
    echo [%date% %time%] New items collected. Run /ic-update in Claude Code. >> tools\collect.log
)
