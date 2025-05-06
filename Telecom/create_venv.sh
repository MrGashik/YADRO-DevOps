#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Ошибка: Python 3 не установлен. Установите Python 3 и попробуйте снова."
    exit 1
fi

echo "Создание виртуального окружения..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Ошибка: Не удалось создать виртуальное окружение."
    exit 1
fi

echo "Активация виртуального окружения..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Ошибка: Не удалось активировать виртуальное окружение."
    exit 1
fi

echo "Установка зависимостей (requests, ansible)..."
pip install requests ansible
if [ $? -ne 0 ]; then
    echo "Ошибка: Не удалось установить зависимости."
    exit 1
fi

deactivate
echo "Настройка окружения завершена успешно!"
