#!/bin/bash

rm -r ./dist/
python -m build
python3 -m twine upload dist/*
