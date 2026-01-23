# m4_project

## 📌 Описание

Это учебный проект, созданный в рамках курса **«Автоматизация тестирования с помощью Selenium и Python»** на платформе Stepik.  
Цель — разработать **набор автотестов с использованием Page Object Model (POM)** для базового UI функционала интернет-магазина.

Сайт, который тестируется:  
https://selenium1py.pythonanywhere.com/

---

## ✅ Структура репозитория
```
text m4_project/ 
├── pages/ # Page Object классы 
├── tests/ # Тестовые сценарии 
├── conftest.py # Фикстуры pytest 
├── pytest.ini # Конфигурация pytest 
├── requirements.txt # Зависимости 
└── README.md # Описание проекта 
``` 

---

## 🚀 Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/eskapandr/m4_project.git
cd m4_project
```
### 2. Создать виртуальное окружение
Linux / macOS / WSL
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows (CMD / PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Установить зависимости
```bash
pip install -r requirements.txt
```
---

## 🧪 Запуск тестов
```bash
pytest -v --tb=line --language=en -m need_review
```
---

## 🛠 Используемые инструменты

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40" height="40"/>
</p>