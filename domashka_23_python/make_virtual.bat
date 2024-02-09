@echo off

chcp 1251 > nul

rem chcp 65001 > nul

ver | find "Windows" > nul

set "folderPath=.\.venv"

if not exist %folderPath% (
    call check_venv.bat %folderPath%
)

if %errorlevel% equ 0 (
    echo ��� Windows.
    rem rem - ��� �����������
    set "venv_dir=.\.venv\Scripts\"
) else (
    echo ��� �� Windows.
    echo ��� �� ��� ���� ���������?
    set "venv_dir=./.venv/bin/"

    rem �������� ��� ��� ��� Linux �����
)


    rem ����������� ����������
    set "activate_var=activate"
    set "deactivate_var=deactivate"

    rem ����������� ����������
    echo %activate_var%
    echo %deactivate_var%
    echo %venv_dir%

    start "��� ���� ��� ����, ����� ��������, ��� ���������� ����" dir
    echo ������� ����� ������� ��� �����������...
    rem �������� ������� ������
    pause > nul


    if defined VIRTUAL_ENV (
        echo ����������� ��������� Python ������������.
        echo ������������ ����������� ���������
        call virtual_activate.bat %venv_dir% %deactivate_var%
    )

    echo %PYTHONPATH%
    if defined VIRTUAL_ENV (
        echo ����������� ��������� Python ������������.
    ) else (
        echo ����������� ��������� Python �� ������������.
    )


    echo �������� ����������� ���������
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
        echo ����������� ��������� Python ������������.
    ) else (
        echo ����������� ��������� Python �� ������������.
    )

    rem exit()
    echo ������� ����� ������� ��� �����������...
    rem �������� ������� ������
    pause > nul 
rem exit