if not exist %1 (
    start "Установка виртуального окружения python." python -m venv %1
    echo Не закрывайте окно самостоятельно. 
    echo После закрытия окна, 
    echo Нажмите любую клавишу для продолжения...
    pause > nul
    rem exit()
)