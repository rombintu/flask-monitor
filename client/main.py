import psutil
import json

data = []
help_data = ['cpu_min', 'mem_min', 'hard_min', 'cpu_max', 'mem_max', 'hard_max']

def bytes_to_gb(n):
    # из байт в ГБ
    return round(n*9.31*pow(10,-10))

def get_hard():
    mps = []
    hard_min = 0
    hard_max = 0
    for disk in psutil.disk_partitions():
        mps.append(disk[1])
    for mp in mps:
        storage = psutil.disk_usage(mp)
        hard_min += storage[1]
        hard_max += storage[0]
    return [bytes_to_gb(hard_min), bytes_to_gb(hard_max)]


data.append(round(sum(psutil.getloadavg()))) # get CPU_MIN
data.append(bytes_to_gb(psutil.virtual_memory()[3])) # GET MEM_MIN
data.append(get_hard()[0]) # GET HARD_MIN
data.append(psutil.cpu_count()) # get CPU_MAX
data.append(bytes_to_gb(psutil.virtual_memory()[0])) # GET MEM_MAX
data.append(get_hard()[1]) # GET HARD_MAX

with open('info.json', 'w') as f:
    pre_data = dict(zip(help_data, data))
    f.write(json.dumps(pre_data))