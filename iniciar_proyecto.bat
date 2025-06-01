@echo off
setlocal

REM 📁 Definición de rutas del proyecto
set PROJECT_DIR=.
set VENV_DIR=%PROJECT_DIR%\venv
set REQ_FILE=%PROJECT_DIR%\config\requirements.txt
set MAIN_FILE=%PROJECT_DIR%\main.py

echo 🚀 Iniciando el proyecto CASINO...

REM 🧠 Verificar si el entorno virtual existe
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo ⚙️  Creando entorno virtual...
    where python >nul 2>&1 && (
        python -m venv "%VENV_DIR%"
    ) || (
        echo ❌ No se encontró Python en el sistema. Abortando.
        exit /b 1
    )
)

REM ✅ Activar entorno virtual
call "%VENV_DIR%\Scripts\activate.bat"

REM 📦 Verificar existencia del archivo de requerimientos
if not exist "%REQ_FILE%" (
    echo ❌ No se encontró el archivo de dependencias: %REQ_FILE%. Abortando.
    exit /b 1
)

echo 📦 Instalando dependencias desde requirements.txt...
python -m pip install --upgrade pip
pip install -r "%REQ_FILE%"

REM 🧾 Verificar existencia del archivo principal
if not exist "%MAIN_FILE%" (
    echo ❌ No se encontró el archivo principal: %MAIN_FILE%. Abortando.
    exit /b 1
)

echo 🌐 Iniciando Streamlit...
start streamlit run "%MAIN_FILE%"

echo.
echo ✅ Aplicación lanzada correctamente.
echo 📎 URL por defecto: http://localhost:8501
echo.

endlocal
pause
