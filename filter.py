import numpy as np


class AbstractFilter:

    def filter(self, samples):
        raise NotImplementedError('The method filter has to be implemented')


class RangeFilter(AbstractFilter):

    def __init__(self, range_array):
        self.range_array = range_array

    def filter(self, samples):

        filter_samples = []

        for i in range(len(samples)):

            filter_sample = []

            for j in range(len(samples[i])):

                if samples[i][j] < self.range_array[0]:
                    filter_sample.append(self.range_array[0])

                elif samples[i][j] > self.range_array[1]:
                    filter_sample.append(self.range_array[1])

                else:
                    filter_sample.append(samples[i][j])

            filter_samples.append(filter_sample)

        return filter_samples


class TemporalMedianFilter(AbstractFilter):

    def __init__(self, temporal_scan_size):
        self.temporal_scan_size = temporal_scan_size

    def filter(self, samples):

        temporal_median_filtered_samples = []

        samples_as_np = np.array(samples)
        columns = samples_as_np.transpose()

        for i in range(len(samples)):

            temporal_median_filtered_sample = []

            if self.temporal_scan_size > i:
                for j in range(len(columns)):
                    median_val = np.median(np.sort(columns[j][:i + 1]))
                    temporal_median_filtered_sample.append(median_val)
            else:
                for j in range(len(columns)):
                    median_val = np.median(np.sort(columns[j][i - self.temporal_scan_size:i + 1]))
                    temporal_median_filtered_sample.append(median_val)

            temporal_median_filtered_samples.append(temporal_median_filtered_sample)

        return temporal_median_filtered_samples
