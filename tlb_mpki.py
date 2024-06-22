import csv
from cache import workloads
from cache import parse
from cache import parse_data
from cache import write_csv


def get_mpki(misses, instructions):
    return (int(misses) / int(instructions)) * 1000

def get_data_csv(baseline):
    header = ["workload", "L1-I TLB MPKI", "L1-D TLB MKPI", "L2 TLB MPKI"]
    
    data = [header]

    for wl in workloads:
        rowv = [wl]

        tlbs = ["itlb", "dtlb", "stlb"]

        for tlb in tlbs:
            mpki = get_mpki(baseline[wl]['%s.miss'%tlb], baseline[wl]['performance_model.instruction_count'])
            rowv.append(mpki)

        data.append(rowv)
    
    return data


datapath = "./normal/baseline"
res = parse_data(datapath)


res_data = get_data_csv(res)

print(res_data)

write_csv("mpki.csv", res_data)
