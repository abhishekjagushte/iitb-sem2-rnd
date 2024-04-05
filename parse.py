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
    "PTW_0.page_walks"
    
]

workloads = [
    "pr",
    "bc",
    "rnd",
    "bfs"
]



def get_results_map(folder, workload):
    filename = "./" + folder + "/" + workload + ".txt" 
    d = {}
    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            splits = line.split(" ")
            d[splits[0]] = splits[2]

    print(d)
    return d

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

def write_csv(filename, data):
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)


baseline = {}
victima = {}

for wl in workloads:
    baseline_res = get_results_map("baseline", wl)
    victima_res = get_results_map("victima", wl)

    baseline[wl] = baseline_res
    victima[wl] = victima_res


baseline_data = get_data_csv(baseline)
victima_data = get_data_csv(victima)
    
write_csv("baseline.csv", baseline_data)
write_csv("victima.csv", victima_data)