class Table:

    def __init__(self, data, name, primary_key, foreign_keys):
        self.data = data
        self.name = name
        self.primary_key = primary_key
        self.foreign_keys = foreign_keys
        self.all_keys = [self.primary_key] + self.foreign_keys
        self.columns = list(self.data.keys())

    def rename(self, name):
        self.name = name
        old_pk = self.primary_key
        self.primary_key = f"{self.name}_id"
        self.all_keys = [self.primary_key] + self.foreign_keys
        self.data = {(self.primary_key if k == old_pk else k): v for k, v in self.data.items()}
        self.columns = list(self.data.keys())

    def rename_fk(self, current_fk, new_fk):
        for i in range(len(self.foreign_keys)):
            if self.foreign_keys[i] == current_fk:
                self.foreign_keys[i] = new_fk
        self.all_keys = [self.primary_key] + self.foreign_keys
        self.data = {(new_fk if k == current_fk else k): v for k, v in self.data.items()}
        self.columns = list(self.data.keys())

    def rename_column(self, current_name, new_name):
        self.data = {(new_name if k == current_name else k): v for k, v in self.data.items()}
        self.columns = list(self.data.keys())

    def generate_metadata(self):
        metadata = []
        for c in self.columns:
            values = self.data[c]
            nullable = any(v is None for v in values)
            non_null_values = [v for v in values if v is not None]
            data_type = self._determine_type(non_null_values)
            unique = len(non_null_values) == len(set(non_null_values))
            metadata.append({"field": c, "type": data_type, "nullable": nullable, "unique": unique})
        return metadata

    def _determine_type(self, values):
        if self._castable(int, values):
            return "Integer"
        elif self._castable(float, values):
            return "Float"
        elif all(type(v) is str for v in values):
            return "String"
        else:
            return "Any"

    @staticmethod
    def _castable(type_, values):
        try:
            [type_(v) for v in values]
            return True
        except ValueError:
            return False
