if not exist %1 (
    start "��������� ������������ ��������� python." python -m venv %1
    echo �� ���������� ���� ��������������. 
    echo ����� �������� ����, 
    echo ������� ����� ������� ��� �����������...
    pause > nul
    rem exit()
)