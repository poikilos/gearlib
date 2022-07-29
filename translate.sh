#!/bin/bash
if [ -f ~/.virtualenvs/sca2d/bin/python ]; then
    ~/.virtualenvs/sca2d/bin/python pyopenscad/lang/translate.py
else
    python3 pyopenscad/lang/translate.py
fi

if [ $? -ne 0 ]; then
    echo "Install the venv using setup.sh from Poikilos' pyopenscad repo if you are missing module(s)."
fi
