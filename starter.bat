@echo off
REM ============================================
REM AedeonAI Starter Script - by Collins Akoja Nathaniels
REM Automatically activates virtual environment and runs Flask app
REM ============================================

echo.
echo --------------------------------------------
echo  Launching AedeonAI Basic Flask App...
echo --------------------------------------------
echo.

REM Step 1: Activate virtual environment
call venv\Scripts\activate

REM Step 2: Run the Flask app
python app.py

echo.
echo --------------------------------------------
echo AedeonAI Flask App Closed.
echo --------------------------------------------
pause
