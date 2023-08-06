from relatable.tabulator import Tabulator
from relatable.table import Table

from copy import copy, deepcopy


class RelationalSchema:

    def __init__(self, docs):
        self.tables = []
        self._docs_list = [(docs, [])]
        self._make()

    def to_list(self):
        return [t.data for t in self.tables]

    def rename_table(self, current_name, new_name):
        current_fk = f"{current_name}_id"
        new_fk = f"{new_name}_id"
        for t in self.tables:
            if t.name == current_name:
                t.rename(new_name)
            elif current_fk in t.foreign_keys:
                t.rename_fk(current_fk, new_fk)

    def rename_column(self, table, current_name, new_name):
        for t in self.tables:
            if t.name == table:
                t.rename_column(current_name, new_name)
                break

    def generate_metadata(self):
        return [{"table": t.name, **d} for i, t in enumerate(self.tables) for d in t.generate_metadata()]

    def _make(self):
        i = 0
        while len(self._docs_list) > 0:
            docs, foreign_keys = self._docs_list.pop()
            tab = Tabulator(deepcopy(docs), f"t{i}", copy(foreign_keys))
            data, more_docs = tab.tabulate()
            new_table = Table(data, tab.name, tab.primary_key, tab.foreign_keys)
            self.tables.append(new_table)
            self._docs_list.extend(more_docs)
            i += 1
