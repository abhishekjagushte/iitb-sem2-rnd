import csv
from parser import workloads
from parser import parse
from parser import write_csv


def get_data_csv(baseline, victima):
    header = ["workload"]
    baseline_data = []
    victima_data = []

    cols = []
    for k in baseline[workloads[0]].keys():
        if "latency" in k.lower():
            cols.append(k)

    header = header + cols

    baseline_data.append(header)
    victima_data.append(header)

    for wl in workloads:
        rowb = [wl]
        rowv = [wl]
        print(wl, "\n\n")

        for col in cols:
            rowb.append(baseline[wl][col])
            rowv.append(victima[wl][col])


        baseline_data.append(rowb)
        victima_data.append(rowv)

        print(baseline_data)


    return baseline_data, victima_data



basepath = "./normal/baseline"
comparison_path = "./normal/victima"
res = parse(basepath, comparison_path)
baseline = res['baseline']
victima = res['comparison']

baseline_data, victima_data = get_data_csv(baseline, victima)

    
write_csv("baseline.csv", baseline_data)
write_csv("victima.csv", victima_data)