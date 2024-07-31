import csv
from cache import parse_data
from cache import write_csv


columns = [
    "mmu.total_ptw_latency",
    "dtlb.miss",
    "stlb.miss",
    "L1-D.loads-page_table",
    "L1-D.load-misses-page_table",
    "L1-D.loads-tlb_entry",
    "L1-D.load-misses-tlb_entry",
    "L1-D.loads-non_page_table",
    "L1-D.load-misses-non_page_table",
    "L2.loads-page_table",
    "L2.load-misses-page_table",
    "L2.loads-tlb_entry",
    "L2.load-misses-tlb_entry",
    "L2.loads-non_page_table",
    "L2.load-misses-non_page_table",
    "pwc_L2.access",
    "pwc_L2.miss",
    "pwc_L3.access",
    "pwc_L3.miss",
    "pwc_L4.access",
    "pwc_L4.miss",
    "PTW_0.page_walks",
    "dram.reads",
    "dram.writes",
    "L2.tloads",
    "L2.tload-misses",
    "L2.tstores",
    "L2.tstore-misses",
    "ipc",
]

workloads = [
    "bc",
    "bfs",
    "cc",
    "dlrm",
    "gc",
    "gen",
    "pr",
    "rnd",
    "sssp",
    "tc",
    "xs"
]

def get_data_csv(results):
    data = [["workload"] + columns]
 
    for wl in workloads:
        row = []
        row.append(wl)

        res = results[wl]

        for col in columns:
            row.append(res[col])

        data.append(row)


    return data



datapath = "./staging/radix"
res = parse_data(datapath)

data_mp = get_data_csv(res)
    
write_csv("data.csv", data_mp)