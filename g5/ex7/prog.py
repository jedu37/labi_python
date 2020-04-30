#encode utf-8
import sys, time, csv, psutil
from lxml import etree

def main():
    root = etree.parse("g5/ex7/conf.xml")
    interval = root.findall("./interval")[0]
    output_csv = root.findall("./output/csv")[0]
    monitor_cpu = root.findall("./monitor/cpu")[0]
    monitor_net = root.findall("./monitor/network")[0]
    monitor_ram = root.findall("./monitor/ram")[0]
    
    if output_csv.attrib["active"]  == "true":
        fout = open("g5/ex7/log.csv","w")
        writer = csv.DictWriter(fout,delimiter = output_csv.attrib["separator"],fieldnames = ["time","sent","recv","cpu","ram"])
        writer.writeheader()

    for i in range(0,10):
        cpu = "Not Monitored"
        ram = "Not Monitored"
        net = ["Not Monitored","Not Monitored"]

        if monitor_cpu.attrib['active'] == "true":
            cpu = psutil.cpu_percent(interval=int(interval.text))
        
        tm = time.time()
        
        if monitor_net.attrib['active']  == "true":
            net = psutil.net_io_counters()
        
        if monitor_ram.attrib['active']  == "true":
            ram = psutil.virtual_memory()[1]

        data = {'time':tm, 'sent':net[0],'recv':net[1], 'cpu':cpu,'ram':ram }
        
        print(data)
        
        writer.writerow(data)
        
        time.sleep(int(interval.text))
    
    fout.close()

main()