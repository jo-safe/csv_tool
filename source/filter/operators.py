from .base import BaseFilter

class MoreThanFilter(BaseFilter):
    """ Фильтр с заданной нижней границей"""
    operator = ">"
    def apply(self, row) -> bool:
        try:
            return row[self.column] > self.value
        except:
            return False

class LessThanFilter(BaseFilter):
    """ Фильтр с заданной верхней границей"""
    operator = "<"
    def apply(self, row) -> bool:
        try:
            return row[self.column] < self.value
        except:
            return False
            
class EqualsFilter(BaseFilter):
    """ Фильтр проверки равенства"""
    operator = "="
    def apply(self, row) -> bool:
        try:
            return row[self.column] == self.value
        except:
            return False

# Словарь формата { оператор (str) : класс }
FILTERS = { cls.operator: cls for cls in BaseFilter.__subclasses__() } 