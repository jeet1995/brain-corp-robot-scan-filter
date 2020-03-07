import os


def get_file_to_write():
    if os.path.exists("filter_results.txt"):
        os.remove("filter_results.txt")

    return open("filter_results.txt", "a")
