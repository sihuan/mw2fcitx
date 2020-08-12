#!/bin/bash
python setup.py install
pip install pytest pytest-cov coverage
coverage erase
coverage run --source=mw2fcitx -m pytest tests/lib
coverage run -a --source=mw2fcitx -m mw2fcitx.main -c tests/cli/conf_one.py
coverage html