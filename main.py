import pandas as pd

from structures.table import Table
from structures.hash_index import HashIndex
from benchmark.benchmark import Benchmark
from algorithm.sorting import SortingAlgorithms
from engine.query_engine import QueryEngine


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    r"C:\Users\Admin\Desktop\mini data engine\data.csv",
    encoding="latin-1"
)


# =========================
# SELECT USEFUL COLUMNS
# =========================

df = df[
    [
        "show_id",
        "type",
        "title",
        "director",
        "country",
        "release_year",
        "rating",
        "duration"
    ]
]


# =========================
# HANDLE MISSING VALUES
# =========================

df = df.fillna("Unknown")


# =========================
# CONVERT TO LIST OF DICTIONARIES
# =========================

records = df.to_dict(orient="records")


# =========================
# CREATE TABLE OBJECT
# =========================

table = Table(records)


# =========================
# CREATE HASH INDEX
# =========================

hash_index = HashIndex(records, "show_id")


# =========================
# MAIN MENU LOOP
# =========================

while True:

    print("\n========== MINI DATABASE ENGINE ==========")
    print("1. Display Records")
    print("2. Insert Record")
    print("3. Search Record (Sequential)")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Count Records")
    print("7. Hash Search")
    print("8. Benchmark Search")
    print("9. Sort Records")
    print("10. Query Engine")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    # =========================
    # DISPLAY RECORDS
    # =========================

    if choice == "1":

        limit = int(input("How many records to display? "))

        table.display(limit)

    # =========================
    # INSERT RECORD
    # =========================

    elif choice == "2":

        new_record = {
            "show_id": input("Show ID: "),
            "type": input("Type (Movie/TV Show): "),
            "title": input("Title: "),
            "director": input("Director: "),
            "country": input("Country: "),
            "release_year": input("Release Year: "),
            "rating": input("Rating: "),
            "duration": input("Duration: ")
        }

        table.insert(new_record)

        # Update hash index
        hash_index.index[new_record["show_id"]] = new_record

    # =========================
    # SEARCH RECORD
    # =========================

    elif choice == "3":

        show_id = input("Enter Show ID: ")

        table.search_by_id(show_id)

    # =========================
    # UPDATE RECORD
    # =========================

    elif choice == "4":

        show_id = input("Enter Show ID: ")

        field = input("Enter field to update: ")

        value = input("Enter new value: ")

        table.update(show_id, field, value)

        # Rebuild hash index
        hash_index = HashIndex(table.records, "show_id")

    # =========================
    # DELETE RECORD
    # =========================

    elif choice == "5":

        show_id = input("Enter Show ID to delete: ")

        table.delete(show_id)

        # Rebuild hash index
        hash_index = HashIndex(table.records, "show_id")

    # =========================
    # COUNT RECORDS
    # =========================

    elif choice == "6":

        print("\nTotal Records:")

        print(table.count_records())

    # =========================
    # HASH SEARCH
    # =========================

    elif choice == "7":

        show_id = input("Enter Show ID: ")

        result = hash_index.search(show_id)

        if result:

            print("\nRecord Found:\n")

            print(result)

        else:

            print("\nRecord not found.")

    # =========================
    # BENCHMARK SEARCH
    # =========================

    elif choice == "8":

        show_id = input("Enter Show ID for benchmark: ")

        sequential_time = Benchmark.benchmark_sequential(
            table,
            show_id
        )

        hash_time = Benchmark.benchmark_hash(
            hash_index,
            show_id
        )

        print("\n===== BENCHMARK RESULTS =====")

        print(f"Sequential Search Time: {sequential_time:.10f} seconds")

        print(f"Hash Search Time: {hash_time:.10f} seconds")

    # =========================
    # SORT RECORDS
    # =========================

    elif choice == "9":

        print("\nAvailable fields:")
        print("1. title")
        print("2. release_year")
        print("3. country")

        field_choice = input("\nChoose field: ")

        if field_choice == "1":
            field = "title"

        elif field_choice == "2":
            field = "release_year"

        elif field_choice == "3":
            field = "country"

        else:
            print("Invalid field.")
            continue

        print("\nSorting Algorithms:")
        print("1. Quick Sort")
        print("2. Merge Sort")

        algorithm_choice = input("\nChoose algorithm: ")

        print("\nOrder:")
        print("1. Ascending")
        print("2. Descending")

        order_choice = input("Choose order: ")

        # QUICK SORT

        if algorithm_choice == "1":

            table.records = SortingAlgorithms.quick_sort(
                table.records,
                field
            )

            if order_choice == "2":
                table.records.reverse()

            print("\nQuick Sort completed.")

        # MERGE SORT

        elif algorithm_choice == "2":

            table.records = SortingAlgorithms.merge_sort(
                table.records,
                field
            )

            if order_choice == "2":
                table.records.reverse()

            print("\nMerge Sort completed.")

        else:

            print("Invalid algorithm.")
            continue

        print("\nFirst 10 sorted records:\n")

        table.display(10)

    # =========================
    # QUERY ENGINE
    # =========================

    elif choice == "10":

        print("\nAvailable fields:")
        print("title")
        print("country")
        print("release_year")
        print("rating")

        field = input("\nEnter field: ")

        print("\nOperators:")
        print("=")
        print(">")
        print("<")

        operator = input("\nEnter operator: ")

        value = input("Enter value: ")

        results = QueryEngine.execute(
            table.records,
            field,
            operator,
            value
        )

        QueryEngine.display_results(results)

    # =========================
    # EXIT
    # =========================

    elif choice == "11":

            print("\nExiting program...")

            break

    # =========================
    # INVALID CHOICE
    # =========================

    else:
        print("Invalid choice. Please try again.")