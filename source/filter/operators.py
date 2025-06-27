from .base import BaseFilter

class MoreThanFilter(BaseFilter):
    operator = ">"
    def apply(self, row) -> bool:
        return row[self.column] > self.value

class LessThanFilter(BaseFilter):
    operator = "<"
    def apply(self, row) -> bool:
        return row[self.column] < self.value
            
class EqualsFilter(BaseFilter):
    operator = "="
    def apply(self, row) -> bool:
        return row[self.column] == self.value

FILTERS = { cls.operator: cls for cls in BaseFilter.__subclasses__() }