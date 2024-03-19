#!/bin/bash

sudo apt-get update

sudo apt-get install -y clang
sudo python3-pip
sudo pip install -r requirements.txt
echo 'export PATH=/usr/bin:$PATH' >> ~/.bashrc

source ~/.bashrc