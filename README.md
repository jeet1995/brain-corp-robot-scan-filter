Goal: To design filters which reduce noise of data generated by a LIDAR sensor attached to a robot.
--
Name : Abhijeet Mohanty
--
### Overview
* In this take home assignment, I implement two kinds of filters - `RangeFilter` and `TemporalMedianFilter`.
* The scan result to be generated by a robot are randomly generated.

### Development environment
* **OS :** MacOS Mojave
* **IDE :** PyCharm 2019.1.2
* **Language used :** Python 2.7
* **Libraries used :** `numpy`, `argparse`, `unittest`, `random`

### Running the application
* Navigate to **abhijeet-mohanty** by executing `cd abhijeet-mohanty/`
* Add permission to execute `run.sh` by executing `chmod u + x run.sh`
* Run the bash script by executing the command `./run.sh`
* **NOTE :** Please enter *integral* values when prompted by the program to enter values on the standard input.

### Dependencies to download

* numpy
* argparse
* unittest

### Classes used in the application
* The `Robot` class :
    * This class generates a matrix with random values.
    * These values fall within the range of `[0.03, 50]`.
    * The size and no. of samples are 
    taken as user inputs which are in turn taken as command line arguments.
* The `RangeFilter` and `TemporalMedianFilter` classes :
    * An instance of the `RangeFilter` class is created with some user defined
    range.
    * Then the randomized matrix generated by an instance of `Robot` is passed to the `filter` method
    defined on `RangeFilter`.
    * An instance of the `TemporalMedianFilter` class is created with the `temporal_scan_size`. 
    * The `temporal_scan_size` is basically the no. of previous values to be considered in order to determine the 
    median.
* The `RangeAndMedianFilterUnitTest` consists of 2 unit tests to check for correctness of the two filters.

### Algorithm
* Range based filtering
    * For range filtering, if the value in the input matrix 
      happens to be greater than the upper limit of the range, then the value is updated to the upper limit.
    * Analogously, if the value in the input matrix happens to be lower than the lower limit of the range, then the va;ue is updated to
      store the lower limit of the range.
* Temporal median filtering
    * The transpose of the input matrix is taken.
    * Once the transpose is taken, each row is iterated.
    * Two cases arise :
        * If the row index is lesser than the `temporal_scan_size`
            * Take the array starting from index `0` to index `i` for a given column j
            * Find the median of the array for all such columns `j`
        * Else
            * Take the array starting from index `i - temporal_scan_size`  to index `i` for a given column `j`
            * Find the median of the array for all such columns `j`
       

### Results

* The following results were obtained with a range of `[4, 9]`, on a randomly generated `4 x 5` matrix from the 
instance of a `Robot`. The `D` value or temporal median neighbourhood was chosen as `3`.
* The results are saved in `filter_results.txt` :
*
```
Generated samples by robot : 
[[12.762631795879246, 7.488884256619713, 0.75164381740593, 34.38291673790682, 9.83371964056372, 43.90822213986414], [4.513687517658108, 24.8500167427099, 15.65210515755051, 12.484071756255286, 26.15227427173945, 18.346323375081386], [12.430701183539641, 30.50780010375611, 22.270739192796437, 41.306717957122395, 46.177837353042584, 38.639411115909596], [26.917015229724303, 39.168001688242555, 16.250486254563583, 25.883183455145605, 13.976046339810118, 10.896946141624834]]
Range filtered output : 
[[9, 7.488884256619713, 4, 9, 9, 9], [4.513687517658108, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9]]
Temporal median filtered output : 
[[12.762631795879246, 7.488884256619713, 0.75164381740593, 34.38291673790682, 9.83371964056372, 43.90822213986414], [8.638159656768677, 16.169450499664805, 8.20187448747822, 23.43349424708105, 17.992996956151586, 31.12727275747276], [12.430701183539641, 24.8500167427099, 15.65210515755051, 34.38291673790682, 26.15227427173945, 38.639411115909596], [12.596666489709444, 27.678908423233004, 15.951295706057046, 30.133050096526212, 20.064160305774784, 28.49286724549549]]
```

### Future improvements and ideas
* To read robot generated inputs from an external file.
* To add visualization for generated outputs.
* Enhance my shell script to check if required dependencies exist before starting execution.

