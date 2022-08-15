#!/bin/bash

read -p "This script may open a large number of browser windows. Continue? [yN] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborting script"
    exit 1
fi

echo -n "Checking this script is executed from the correct directory..."

if [ ${PWD##*/} != "tests" ]; then
    echo
    echo "❌ This script must be run from the 'tests' directory"
    exit 1
fi

echo " ☑️"
echo -n "Checking for necessary folder structure..."

required_dirs=(../../data ../../data/raw ../../data/interim ../../data/processed ../../models)

for dir in ${required_dirs[@]}; do
    if [ ! -d $dir ]; then
        echo
        echo "❌ '$dir' must exist before running this script"
        exit 1
    fi
done

echo " ☑️"

echo "Generating fake data..."
cd ../fake_data_generation
python generate_fake_data.py

echo "Running through notebooks..."
cd ../notebooks

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for n in $(ls *.ipynb | grep -v .nbconvert); do
    echo "Converting '$n' to a python script..."
    jupyter nbconvert --to script $n
    script=${n%.ipynb}.py
    echo "Removing ipython code..."
    sed -i '' -e '/ipython/d' $script
    echo "Executing '$script'"
    python "$script"
done

echo "Integration test complete. Please check output of notebooks above for any errors."

IFS=$SAVEIFS
