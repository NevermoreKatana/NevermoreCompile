#!/bin/bash

apt-get update && apt-get install -y \
    python3-pip \
    xz-utils \
    curl \
    && rm -rf /var/lib/apt/lists/*


curl -SL https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz \
    | tar -xJC . && \
    mv clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04 clang_10

export PATH="/clang_10/bin:${PATH}"
export LD_LIBRARY_PATH="/clang_10/lib:${LD_LIBRARY_PATH}"

pip install -r requirements.txt
python manage.py collectstatic --no-input