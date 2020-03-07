from file_setup import get_file_to_write
from filter import RangeFilter, TemporalMedianFilter
from robot import Robot
import argparse

# Instantiate a parser to parse command line arguments
runner_parser = argparse.ArgumentParser(
    description='This parser parses command line arguments for the runner.py script')

# Add command line arguments to be parsed
runner_parser.add_argument('--num_samples', type=int, default=30, required=False)
runner_parser.add_argument('--sample_size', type=int, default=20, required=False)
runner_parser.add_argument('--range_filter_lower_limit', type=int, default=2, required=False)
runner_parser.add_argument('--range_filter_upper_limit', type=int, default=25, required=False)
runner_parser.add_argument('--temporal_neighbour_size', type=int, default=3, required=False)


def generate_samples(robot, num_samples, sample_size):
    return robot.generate_scan(num_samples, sample_size)


def generate_range_filtered_results(range_filter, unfiltered_samples):
    return range_filter.filter(unfiltered_samples)


def generate_temporal_median_filtered_results(temporal_median_filter, unfiltered_samples):
    return temporal_median_filter.filter(unfiltered_samples)


def write_results_to_file(generated_samples, generated_range_filtered_results,
                          generated_temporal_median_filtered_results):
    results_file = get_file_to_write()
    results_file.write("Generated samples by robot : \n")
    results_file.write(generated_samples.__str__())
    results_file.write("\nRange filtered output : \n")
    results_file.write(generated_range_filtered_results.__str__())
    results_file.write("\nTemporal median filtered output : \n")
    results_file.write(generated_temporal_median_filtered_results.__str__())
    results_file.close()


if __name__ == '__main__':
    # Get all parsed arguments
    parsed_arguments = runner_parser.parse_args()

    # Instantiate a sample robot
    sample_robot = Robot()

    # Generate scan samples from robot
    samples_generated = generate_samples(sample_robot, parsed_arguments.num_samples, parsed_arguments.sample_size)

    # Instantiate a sample range filter
    sample_range_filter = RangeFilter(
        [parsed_arguments.range_filter_lower_limit, parsed_arguments.range_filter_upper_limit])

    # Generate range filtered sample
    range_filtered_samples = generate_range_filtered_results(sample_range_filter, samples_generated)

    # Instantiate a sample temporal median filter
    sample_temporal_median_filter = TemporalMedianFilter(parsed_arguments.temporal_neighbour_size)

    # Generate temporal median filtered results
    temporal_median_filtered_results = generate_temporal_median_filtered_results(sample_temporal_median_filter,
                                                                                 samples_generated)

    # Write results to filter_results.txt
    write_results_to_file(samples_generated, range_filtered_samples, temporal_median_filtered_results)
