#!/bin/bash

git clone git@github.com:ayomodu/terrk.git

cd terrk

python3 -m venv .
source bin/activate
pip install -r requirements.txt
pint install .

pyinstaller --name terrk --onefile --console src/terrk/__main__.py