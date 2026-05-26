from tabulate import tabulate


class Table:
    def __init__(self, records):
        self.records = records

    # Display records
    def display(self, limit=5):
        print(
            tabulate(
                self.records[:limit],
                headers="keys",
                tablefmt="grid"
            )
        )

    # Insert new record
    def insert(self, record):
        self.records.append(record)
        print("Record inserted successfully.")

    # Delete record by show_id
    def delete(self, show_id):
        original_length = len(self.records)

        self.records = [
            record
            for record in self.records
            if record["show_id"] != show_id
        ]

        if len(self.records) < original_length:
            print(f"Record with ID {show_id} deleted.")
        else:
            print(f"Record with ID {show_id} not found.")

    # Update a field in a record
    def update(self, show_id, field, value):
        found = False

        for record in self.records:
            if record["show_id"] == show_id:
                if field in record:
                    record[field] = value
                    found = True
                    print(f"{field} updated successfully.")
                else:
                    print(f"Field '{field}' does not exist.")
                break

        if not found:
            print(f"Record with ID {show_id} not found.")

    # Search record by show_id
    def search_by_id(self, show_id):
        for record in self.records:
            if record["show_id"] == show_id:
                print(
                    tabulate(
                        [record],
                        headers="keys",
                        tablefmt="grid"
                    )
                )
                return record

        print(f"Record with ID {show_id} not found.")
        return None

    # Sort records by a field
    def sort_by_field(self, field, reverse=False):
        try:
            self.records.sort(
                key=lambda x: str(x[field]),
                reverse=reverse
            )

            order = "descending" if reverse else "ascending"

            print(f"Records sorted by '{field}' ({order}).")

        except KeyError:
            print(f"Field '{field}' does not exist.")

    # Get total number of records
    def count_records(self):
        return len(self.records)