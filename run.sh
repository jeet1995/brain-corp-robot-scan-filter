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

    echo "Please enter the lower limit of the filter"
    read RANGE_FILTER_LOWER_LIMIT

    echo "Please enter the upper limit of the filter"
    read RANGE_FILTER_UPPER_LIMIT

    echo "Please enter the temporal neighbour size"
    read TEMPORAL_NEIGHBOUR_SIZE

    python runner.py --num_samples ${NUM_SAMPLES} --sample_size ${SAMPLE_SIZE} --range_filter_lower_limit ${RANGE_FILTER_LOWER_LIMIT} --range_filter_upper_limit ${RANGE_FILTER_UPPER_LIMIT} --temporal_neighbour_size ${TEMPORAL_NEIGHBOUR_SIZE}
else
    echo "The runner.py script can only be run with Python 2.7"
fi

