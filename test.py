import unittest

from filter import RangeFilter, TemporalMedianFilter


class RangeAndMedianFilterUnitTest(unittest.TestCase):
    range_filter_input = [[10, 12, 3], [19, 7, 8]]
    expected_range_filtered_output = [[10, 10, 5], [10, 7, 8]]
    range = [5, 10]

    temporal_median_filter_input = [[0, 1, 2, 1, 3], [1, 5, 7, 1, 3], [2, 3, 4, 1, 0], [3, 3, 3, 1, 3],
                                    [10, 2, 4, 0, 0]]
    expected_temporal_median_filter_output = [[0.0, 1.0, 2.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0],
                                              [1.0, 3.0, 4.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0],
                                              [2.5, 3.0, 4.0, 1.0, 1.5]]
    temporal_scan_size = 3

    def test_range_filter(self):
        range_filter = RangeFilter(self.range)
        range_filtered_output = range_filter.filter(self.range_filter_input)
        self.assertEquals(range_filtered_output, self.expected_range_filtered_output)

    def test_median_filter(self):
        median_filter = TemporalMedianFilter(self.temporal_scan_size)
        temporal_median_filtered_output = median_filter.filter(self.temporal_median_filter_input)
        self.assertEquals(temporal_median_filtered_output, self.expected_temporal_median_filter_output)


if __name__ == '__main__':
    unittest.main()
