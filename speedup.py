import csv
from cache import workloads
from cache import parse
from cache import write_csv


def get_data_csv(baseline, comparison):
    header = ["workload", "speedup"]
    comparison_data = []
    comparison_data.append(header)

    for wl in workloads:
        rowv = [wl]

        ipc_b = float(baseline[wl]["ipc"])
        ipc_c = float(comparison[wl]["ipc"])

        rowv.append(ipc_c / ipc_b)

        comparison_data.append(rowv)

    return comparison_data



basepath = "./victima/baseline"
comparison_path = "./victima/pl2real"
res = parse(basepath, comparison_path)
baseline = res['baseline']
victima = res['comparison']

victima_data = get_data_csv(baseline, victima)

print(victima_data)

write_csv("speedup_normal.csv", victima_data)
