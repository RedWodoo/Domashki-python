@echo off

chcp 1251 > nul

rem chcp 65001 > nul

ver | find "Windows" > nul

set "folderPath=.\.venv"

if not exist %folderPath% (
    call check_venv.bat %folderPath%
)

if %errorlevel% equ 0 (
    echo Это Windows.
    rem rem - это комментарий
    set "venv_dir=.\.venv\Scripts\"
) else (
    echo Это не Windows.
    echo Как ты это смог запустить?
    set "venv_dir=./.venv/bin/"

    rem Добавьте ваш код для Linux здесь
)


    rem Определение переменной
    set "activate_var=activate"
    set "deactivate_var=deactivate"

    rem Отображение переменной
    echo %activate_var%
    echo %deactivate_var%
    echo %venv_dir%

    start "Это окно для того, чтобы показать, как вызывается окно" dir
    echo Нажмите любую клавишу для продолжения...
    rem Ожидание нажатия кнопки
    pause > nul


    if defined VIRTUAL_ENV (
        echo Виртуальное окружение Python активировано.
        echo Останавливаю виртуальное окружение
        call virtual_activate.bat %venv_dir% %deactivate_var%
    )

    echo %PYTHONPATH%
    if defined VIRTUAL_ENV (
        echo Виртуальное окружение Python активировано.
    ) else (
        echo Виртуальное окружение Python не активировано.
    )


    echo Запускаю виртуальное окружение
    call virtual_activate.bat %venv_dir% %activate_var%

    python -m pip install -U pip
    rem pip uninstall openpyxl -y
    rem pip install openpyxl -y

    rem pip uninstall auto-py-to-exe -y
    pip install auto-py-to-exe
    pip list
    pip freeze > requirements.txt

    auto-py-to-exe calculator_input.py

    if defined VIRTUAL_ENV (
        echo Виртуальное окружение Python активировано.
    ) else (
        echo Виртуальное окружение Python не активировано.
    )

    rem exit()
    echo Нажмите любую клавишу для продолжения...
    rem Ожидание нажатия кнопки
    pause > nul 
rem exit