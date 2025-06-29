from tabulate import tabulate

from reader import read_csv
from argparser import parse_args
from filter import parse_filter_expression
from aggregators import parse_aggregator_expression

def main():
    args = parse_args()
    filePath = args.file
    filterExpr = args.where
    aggregateExpr = args.aggregate

    # Чтение csv-файла
    try:
        data = read_csv(filePath)
    except Exception as e:
        print(f"Can't open file ({filePath}): {e}")
        return

    dataRes = []

    # При указанном фильтре - фильтрация
    if filterExpr:
        try:
            filter = parse_filter_expression(filterExpr)
        except Exception as e:
            print(f"Invalid filter format ({filterExpr}): {e}")
            return
        for line in data:
            if filter.apply(line):
                dataRes.append(line)
    else:
        dataRes = data
    
    # При указанном методе агрегации - поиск подходящих значений
    if aggregateExpr:
        try:
            aggregator = parse_aggregator_expression(aggregateExpr)
        except Exception as e:
            print(f"Invalid aggregate format ({aggregateExpr}): {e}")
            return
        for line in dataRes:
            try:
                aggregator.add(line)
            except Exception as e:
                print(f"Failed adding value to aggregator: {e}")
        try:
            res = [{aggregator.identifier : aggregator.calc()}]
        except:
            res = []

    else:
        res = dataRes
    
    if res:
        print(tabulate(res, headers="keys", tablefmt="fancy_grid"))
    else:
        print("Empty table")

if __name__ == "__main__":
    main()