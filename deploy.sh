#!/bin/bash

apt-get update

apt-get install -y clang
apt-get install python3-pip
pip install -r requirements.txt
echo 'export PATH=/usr/bin:$PATH' >> ~/.bashrc

source ~/.bashrc
python3 manage.py collectstatic --no-input