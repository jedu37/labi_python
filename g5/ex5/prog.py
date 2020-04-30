#encode utf-8
import sys, time, json, psutil

def main():
    fout = open("g5/ex5/log.json","w")
    data = []
    for i in range(0,10):
        cpu = psutil.cpu_percent(interval=1)
        tm = time.time()
        net = psutil.net_io_counters()
        t_data = {'stats' : [{'time': tm, 'cpu': cpu, 'network': net},]}
        data.append(t_data)
        time.sleep(1)
    
    json.dump(data,fout,ensure_ascii=False,indent=2)
    fout.close()

main()