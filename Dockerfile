FROM postgres:latest

COPY .env /tmp/.env

RUN cat /tmp/.env >> /etc/environment

ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

EXPOSE 5432

# Используем Python 3.10
FROM python:3.10-slim

# Устанавливаем pip и необходимые пакеты для получения и извлечения предварительно собранных бинарных файлов
RUN apt-get update && apt-get install -y \
    python3-pip \
    xz-utils \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Получаем предварительно собранный бинарный файл от LLVM
RUN curl -SL https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz \
    | tar -xJC . && \
    mv clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04 clang_10

ENV PATH="/clang_10/bin:${PATH}"
ENV LD_LIBRARY_PATH="/clang_10/lib:${LD_LIBRARY_PATH}"

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем приложение в контейнер
COPY . /app

# Создаем виртуальное окружение и устанавливаем зависимости
RUN python3 -m venv .venv & source .venv/bin/activate & pip install -r requirements.txt
RUN chmod -R 777 /app/tmp_files
# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]