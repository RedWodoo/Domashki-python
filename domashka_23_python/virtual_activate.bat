@echo off

rem ¬ход в локальную область видимости
rem setlocal

set "bat_venv_dir=%1"
echo bat_venv_dir

set "bat_activate_var=%2"
echo bat_activate_var


set "bat_activated_venv=%bat_venv_dir%%bat_activate_var%"

echo %bat_activated_venv%

%bat_activated_venv%

rem ¬ыход из локальной области видимости
rem endlocal