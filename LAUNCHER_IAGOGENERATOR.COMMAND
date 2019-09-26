#!/bin/sh
echo Starting Generator New
export PYTHONPATH=.:$(dirname $0)/src/
cd $(dirname $0)/src
python3.7 -W ignore ./generator.py
echo Done