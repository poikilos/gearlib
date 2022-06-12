#!/bin/bash
if [ ! -d ~/.virtualenvs/sca2d ]; then
    python3 -m venv ~/.virtualenvs/sca2d
fi

source ~/.virtualenvs/sca2d/bin/activate
code=$?
if [ $code -ne 0 ]; then
    echo "'source ~/.virtualenvs/sca2d/bin/activate' failed."
    exit $code
fi
python3 -m pip install --upgrade https://gitlab.com/bath_open_instrumentation_group/sca2d/-/archive/master/sca2d-master.zip
echo "* Use ~/.virtualenvs/sca2d/bin/python to run the translate script since it requires sca2d."
