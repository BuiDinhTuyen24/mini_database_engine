from tabulate import tabulate


class QueryEngine:

    # =========================
    # EXECUTE QUERY
    # =========================

    @staticmethod
    def execute(records, field, operator, value):

        results = []

        for record in records:

            record_value = str(record[field])

            # =========================
            # EQUAL
            # =========================

            if operator == "=":

                if record_value.lower() == value.lower():

                    results.append(record)

            # =========================
            # GREATER THAN
            # =========================

            elif operator == ">":

                try:

                    if float(record_value) > float(value):

                        results.append(record)

                except:

                    pass

            # =========================
            # LESS THAN
            # =========================

            elif operator == "<":

                try:

                    if float(record_value) < float(value):

                        results.append(record)

                except:

                    pass

        return results

    # =========================
    # DISPLAY RESULTS
    # =========================

    @staticmethod
    def display_results(results, limit=10):

        if len(results) == 0:

            print("\nNo matching records found.")

        else:

            print(f"\nFound {len(results)} matching records.\n")

            print(
                tabulate(
                    results[:limit],
                    headers="keys",
                    tablefmt="grid"
                )
            )