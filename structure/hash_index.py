class HashIndex:

    def __init__(self, records, key):

        self.index = {}

        self.key = key

        self.build_index(records)

    # =========================
    # BUILD HASH INDEX
    # =========================

    def build_index(self, records):

        for record in records:

            self.index[record[self.key]] = record

    # =========================
    # SEARCH USING HASH TABLE
    # =========================

    def search(self, value):

        return self.index.get(value, None)