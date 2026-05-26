class SortingAlgorithms:

    # =========================
    # QUICK SORT
    # =========================

    @staticmethod
    def quick_sort(records, key):

        if len(records) <= 1:
            return records

        pivot = records[len(records) // 2][key]

        left = [
            record
            for record in records
            if str(record[key]) < str(pivot)
        ]

        middle = [
            record
            for record in records
            if str(record[key]) == str(pivot)
        ]

        right = [
            record
            for record in records
            if str(record[key]) > str(pivot)
        ]

        return (
            SortingAlgorithms.quick_sort(left, key)
            + middle
            + SortingAlgorithms.quick_sort(right, key)
        )

    # =========================
    # MERGE SORT
    # =========================

    @staticmethod
    def merge_sort(records, key):

        if len(records) <= 1:
            return records

        mid = len(records) // 2

        left_half = records[:mid]

        right_half = records[mid:]

        left_sorted = SortingAlgorithms.merge_sort(
            left_half,
            key
        )

        right_sorted = SortingAlgorithms.merge_sort(
            right_half,
            key
        )

        return SortingAlgorithms.merge(
            left_sorted,
            right_sorted,
            key
        )

    # =========================
    # MERGE FUNCTION
    # =========================

    @staticmethod
    def merge(left, right, key):

        merged = []

        i = 0

        j = 0

        while i < len(left) and j < len(right):

            if str(left[i][key]) <= str(right[j][key]):

                merged.append(left[i])

                i += 1

            else:

                merged.append(right[j])

                j += 1

        merged.extend(left[i:])

        merged.extend(right[j:])

        return merged