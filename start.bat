    @echo off
cd /d "%~dp0"
echo ==========================================
echo Starte EyeAid... Bitte warten...
echo ==========================================

:: 1. Sicherstellen, dass die Bibliotheken installiert sind
pip install -r requirements.txt

:: 2. Das Programm starten
python app.py

:: 3. Verhindert, dass das Fenster bei einem Fehler einfach abstürzt
echo.
echo Das Programm wurde beendet oder es gab einen Fehler.
pause
