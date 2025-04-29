from drain3 import TemplateMiner
from drain3.file_persistence import FilePersistence
import json

persistence = FilePersistence("drain3_state.bin")
template_miner = TemplateMiner(persistence)

log_file_path = "../data/HDFS.log"

with open(log_file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        result = template_miner.add_log_message(line)
        if result["change_type"] is not None:
            print(f"Cluster created: {result['cluster_id']}, Template: {result['template_mined']}")

template_miner.drain.save_state()