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

    data = read_csv(filePath)
    dataRes = []
    if filterExpr:
        try:
            filter = parse_filter_expression(filterExpr)
        except Exception:
            print(f"Invalid filter format: {filterExpr}")
            return
        for line in data:
            if filter.apply(line):
                dataRes.append(line)
    else:
        dataRes = data
    
    if aggregateExpr:
        try:
            aggregator = parse_aggregator_expression(aggregateExpr)
        except Exception:
            print(f"Invalid aggregate format: {aggregateExpr}")
            return
        for line in dataRes:
            aggregator.add(line)
        res = [{aggregator.identifier : aggregator.calc()}]
    else:
        res = dataRes
    
    if res:
        print(tabulate(res, headers="keys", tablefmt="fancy_grid"))
    else:
        print("Empty table")

if __name__ == "__main__":
    main()