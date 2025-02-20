import csv
from parser import parse_data
from parser import write_csv


columns = [
    "mmu.total_ptw_latency",
    "dtlb.miss",
    "stlb.miss",
    "L2.loads-page_table",
    "L2.load-misses-page_table",
    "L2.loads-tlb_entry",
    "L2.load-misses-tlb_entry",
    "L2.loads-non_page_table",
    "L2.load-misses-non_page_table",
    "nuca-cache.reads",
    "nuca-cache.read-misses",
    "nuca-cache.writes",
    "nuca-cache.write-misses",
    "PTW_0.page_walks",
    "dram.reads",
    "dram.writes",
    "L2.tloads",
    "L2.tload-misses",
    "L2.tstores",
    "L2.tstore-misses",
    "ipc",
    # "L2.tlb-reuse-0",
    # "L2.tlb-reuse-1",
    # "L2.tlb-reuse-2",
    # "L2.tlb-reuse-3",
    # "L2.tlb-reuse-4",
    # "L2.data-reuse-0",
    # "L2.data-reuse-1",
    # "L2.data-reuse-2",
    # "L2.data-reuse-3",
    # "L2.data-reuse-4",
    "L2.metadata-reuse-0",
    "L2.metadata-reuse-1",
    "L2.metadata-reuse-2",
    "L2.metadata-reuse-3",
    "L2.metadata-reuse-4",
    # "L1-D.data-reuse-0",
    # "L1-D.data-reuse-1",
    # "L1-D.data-reuse-2",
    # "L1-D.data-reuse-3",
    # "L1-D.data-reuse-4",
    "nuca-cache.data-reuse-0",
    "nuca-cache.data-reuse-1",
    "nuca-cache.data-reuse-2",
    "nuca-cache.data-reuse-3",
    "nuca-cache.data-reuse-4",
    # "L1-D.loads-page_table",
    # "L1-D.load-misses-page_table",
    # "L1-D.loads-tlb_entry",
    # "L1-D.load-misses-tlb_entry",
    # "L1-D.loads-non_page_table",
    # "L1-D.load-misses-non_page_table",
]

dead_block_cols = [
    "dead_tlb_block_predictor.conf_decrememts",
    "dead_tlb_block_predictor.conf_increments",
    "dead_tlb_block_predictor.deadblocks_predicted",
    "dead_tlb_block_predictor.deadblocks_predicted_correctly",
    "dead_tlb_block_predictor.evictions",
    "dead_tlb_block_predictor.num_entries",
    "dead_tlb_block_predictor.table_hits",
    "dead_tlb_block_predictor.total_correct",
    "dead_tlb_block_predictor.total_incorrect",
    "dead_tlb_block_predictor.total_probes",
    "dead_tlb_block_predictor.unaccounted",
    "stlb.victima_alloc_on_eviction",
    "stlb.victima_alloc_on_ptw"
]

# columns = columns + dead_block_cols


# columns = [
#     "mmu.total_ptw_latency",
#     "L2.loads-page_table",
#     "L2.load-misses-page_table",
#     "L2.loads-tlb_entry",
#     "L2.load-misses-tlb_entry",
#     "L2.loads-non_page_table",
#     "L2.load-misses-non_page_table",
#     "pwc_L2.access",
#     "pwc_L2.miss",
#     "pwc_L3.access",
#     "pwc_L3.miss",
#     "pwc_L4.access",
#     "pwc_L4.miss",
#     "PTW_0.page_walks",
#     "dram.reads",
#     "dram.writes",
#     "L2.tloads",
#     "L2.tload-misses",
#     "L2.tstores",
#     "L2.tstore-misses",
#     "ipc",
#     "next_tlb_block_l2c.gen_prefetch",
#     "next_tlb_block_l2c.pref_called",
#     "next_tlb_block_l2c.prefetch_hits"
# ]

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



datapath = "./bypassing_l2/complete_bypass/victima"
res = parse_data(datapath, workloads)

data_mp = get_data_csv(res)
    
write_csv("data1.csv", data_mp)