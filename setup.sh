#!/bin/bash

# Python 버전 설정
PYTHON_VERSION="3.9"

# Pipenv 설치 확인 및 설치
if ! command -v pipenv &> /dev/null
then
    echo "pipenv가 설치되어 있지 않습니다. 설치를 진행합니다..."
    pip install pipenv
fi

# pyenv 설치 확인 및 설치
if ! command -v pyenv &> /dev/null
then
    echo "pyenv가 설치되어 있지 않습니다. 설치를 진행합니다..."
    curl https://pyenv.run | bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
fi

# 가상 환경 설정 및 의존성 설치
PIPENV_VENV_IN_PROJECT=true PIPENV_IGNORE_VIRTUALENVS=1 pipenv install --python "$PYTHON_VERSION"

# pre-commit hook 설치
pipenv run pre-commit install

echo "설치가 완료되었습니다!"
