import os
import shutil
from bank import CheckedNumber

def test_CheckedNumber():
    for i in ('1', '100', '154', '205', '458'):
      num = CheckedNumber(i)
      assert isinstance(num, float)


def test_copy():
    shutil.copy('test_python.py','test_pythonana.py')
    files = os.listdir()
    assert 'test_pythonana.py' in files
    os.remove('test_pythonana.py')

def test_mkdir():
    """Тест для функции с побочным эффектом"""
    # Если папка есть, то удалям ее
    if 'ффф' in os.listdir(): os.rmdir('ффф')

    # создаем папку
    os.mkdir('ффф')
    # проверяем есть ли папка на диске
    assert 'ффф' in os.listdir()
    # удаляем папку после проверки
    os.rmdir('ффф')