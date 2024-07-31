import csv

columns = [
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



def get_results_map(fodler_path, workload):
    filename = fodler_path + "/" + workload + ".txt" 
    d = {}
    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            splits = line.split(" ")
            d[splits[0]] = splits[2]

    # print(d)

    return d

def get_data_csv(results):
    data = [["workload"] + columns + ["dram.acceeses"]]
 
    for wl in workloads:
        row = []
        row.append(wl)

        res = results[wl]

        for col in columns:
            row.append(res[col])

        row.append(int(res["dram.reads"]) + int(res["dram.writes"]))

        data.append(row)


    return data



def write_csv(filename, data):
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)


def parse_data(data_folder):
    data = {}

    for wl in workloads:
        baseline_res = get_results_map(data_folder, wl)
        data[wl] = baseline_res

    return data


def parse(base_folder, comparison_folder):
    baseline = {}
    comparison = {}

    for wl in workloads:
        baseline_res = get_results_map(base_folder, wl)
        comparison_res = get_results_map(comparison_folder, wl)

        baseline[wl] = baseline_res
        comparison[wl] = comparison_res

    return {
        "baseline": baseline,
        "comparison": comparison
    }
