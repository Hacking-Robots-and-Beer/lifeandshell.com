#!/bin/bash
python get.py

echo "Generate Hugo"
cd hugo
hugo
cd ..
python copyFile.py

echo "Copy data"
