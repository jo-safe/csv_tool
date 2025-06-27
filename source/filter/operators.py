from .base import BaseFilter

class MoreThanFilter(BaseFilter):
    operator = ">"
    def apply(self, row) -> bool:
        try:
            return row[self.column] > self.value
        except:
            return False

class LessThanFilter(BaseFilter):
    operator = "<"
    def apply(self, row) -> bool:
        try:
            return row[self.column] < self.value
        except:
            return False
            
class EqualsFilter(BaseFilter):
    operator = "="
    def apply(self, row) -> bool:
        try:
            return row[self.column] == self.value
        except:
            return False

FILTERS = { cls.operator: cls for cls in BaseFilter.__subclasses__() }