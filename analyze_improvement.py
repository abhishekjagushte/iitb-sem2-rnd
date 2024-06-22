import csv
from cache import workloads
from cache import parse
from cache import write_csv
import pprint


def get_cols_with_difference(baseline, comparison):
    res = {}
    
    for wl in workloads:

        res[wl] = {}

        for col in baseline[wl]:
            if baseline[wl][col].isnumeric() and float(baseline[wl][col]) != 0:
                ratio = float(comparison[wl][col])/float(baseline[wl][col])

                if ratio > 1.5 or ratio < 0.5:
                    res[wl][col] = ratio

    return res



basepath = "./victima/baseline"
comparison_path = "./victima/pl2real"
res = parse(basepath, comparison_path)
baseline = res['baseline']
victima = res['comparison']

victima_data = get_cols_with_difference(baseline, victima)

pprint.pprint(victima_data)

# write_csv("speedup_normal.csv", victima_data)
