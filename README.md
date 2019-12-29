# Численные методы. Лабораторная работы номер 1

## Структура директорий

- [differential_equation](differential_equation) - проект с решением дифференциального уравнения методом РК 4 порядка
- [differential_equation_system](differential_equation_system) - проект с решением системы дифференциальных уравнений методом РК 4 порядка

## Зависимости
- PyQt5
- Matplotlib

## Установка

1. Установка [Python3.x.x](http://www.python.org/downloads/)
   Рекомендуемая версия Python 3.7, так же рекомендуется добавить Python в параметры окружения (нажать галочку при установке)
2. Открыть командную строку
3. Установка Python QT5
   В командной строке ввести:
   ```bash
   pip install pyqt5
   ```
4. Установка Python matplotlib
   В командной строке ввести:
   ```bash
   pip install matplotlib
   ```
 ## Запуск приложений

- Windows
    1. Открыть командную строку
    2. Перейти в директорию numerical-methods-lab1
    3. Для запуска программы с решением ДУ:
        ```bash
        cd .\differential_equation
        python differential_equation.py
        ```
       Для запуска программы с решением системы ДУ:
        ```bash
        cd .\differential_equation_system
        python differential_equation_system.py
        ```

- Linux
    1. Открыть командную строку
    2. Перейти в директорию numerical-methods-lab1
    3. Для запуска программы с решением ДУ:
        ```bash
        cd ./differential_equation
        python3 differential_equation.py
        ```
       Для запуска программы с решением системы ДУ:
        ```bash
        cd ./differential_equation_system
        python3 differential_equation_system.py
        ```
