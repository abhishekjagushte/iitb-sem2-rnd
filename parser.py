import csv

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
