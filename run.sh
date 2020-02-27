#!/bin/bash

PYTHON_VERSION=$(python --version 2>&1)
PYTHON_REQUIRED_VERSION="2.7"

if [[ ${PYTHON_VERSION} == *"$PYTHON_REQUIRED_VERSION"* ]]
then
    echo "Welcome to the filter scan project"

    echo "Please enter the no. of samples you wish for the robot to generate"
    read NUM_SAMPLES

    echo "Please enter the size of each sample you wish for the robot to generate"
    read SAMPLE_SIZE

    python runner.py --num_samples ${NUM_SAMPLES} --sample_size ${SAMPLE_SIZE} # 2 command line arguments denoting no. of samples and sample size
else
    echo "The runner.py script can only be run with Python 2.7"
fi

