import time


class Benchmark:

    @staticmethod
    def benchmark_sequential(table, show_id):

        start = time.perf_counter()

        table.search_by_id(show_id)

        end = time.perf_counter()

        return end - start

    @staticmethod
    def benchmark_hash(hash_index, show_id):

        start = time.perf_counter()

        hash_index.search(show_id)

        end = time.perf_counter()

        return end - start