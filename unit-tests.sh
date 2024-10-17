#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:./src/logger"
python3 -m unittest -v tests/logger_test.py