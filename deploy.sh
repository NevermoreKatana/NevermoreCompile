#!/bin/bash


apt-get install -y clang

echo 'export PATH=/usr/bin:$PATH' >> ~/.bashrc

source ~/.bashrc
pip install -r requirements.txt
python manage.py collectstatic --no-input