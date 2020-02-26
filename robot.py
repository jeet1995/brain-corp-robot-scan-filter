import random

MIN_RANGE_VAL = 0.03
MAX_RANGE_VAL = 50


class Robot:
    """
    A Robot which can generate scan results based on the
    no. of samples provided (D) with a sample size (N)
    """

    def __init__(self):
        pass

    def generate_scan(self, num_samples, sample_size):
        samples = []

        for i in range(num_samples):
            sample = []
            for j in range(sample_size):
                sample.append(random.uniform(MIN_RANGE_VAL, MAX_RANGE_VAL))
            samples.append(sample)

        return samples
