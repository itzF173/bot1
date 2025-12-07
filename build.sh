#!/bin/bash
# build.sh

echo "=== Setting up Python 3.12.11 ==="

# Принудительно устанавливаем Python 3.12
pyenv install 3.12.11 -s
pyenv global 3.12.11

# Проверяем версию
python --version

# Обновляем pip
pip install --upgrade pip setuptools wheel

# Устанавливаем зависимости в правильном порядке
pip install numpy==1.24.3
pip install pandas==2.1.4
pip install -r requirements.txt

echo "=== Build complete ==="