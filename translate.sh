#!/bin/bash
if [ -f ~/.virtualenvs/sca2d/bin/python ]; then
    ~/.virtualenvs/sca2d/bin/python getriebe/lang/translate.py
else
    python3 getriebe/lang/translate.py
    if [ $? -ne 0 ]; then
        echo "Install the venv using setup.sh from Poikilos' getriebe repo if you are missing module(s)."
    fi
fi
