from .base import BaseFilter

class MoreThanFilter(BaseFilter):
    def apply(self, row) -> bool:
        return row[self.column] > self.value

class LessThanFilter(BaseFilter):
    def apply(self, row) -> bool:
        return row[self.column] < self.value
            
class EqualsFilter(BaseFilter):
    def apply(self, row) -> bool:
        return row[self.column] == self.value

FILTERS = {">" : MoreThanFilter,
           "<" : LessThanFilter,
           "=" : EqualsFilter}