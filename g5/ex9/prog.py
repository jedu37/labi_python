#encode utf-8
import sys, time, psutil
from lxml import etree

def main():
    root = etree.Element("stats")

    for i in range(1,10):
        value = etree.SubElement(root,'value')
        value.set('time', str(int(time.time())))
        value.text = str(i)
        cpu = etree.SubElement(value,'cpu')
        cpu.text = format("%f"%(psutil.cpu_percent(interval=1)))
        ram = etree.SubElement(value,'ram')
        ram.text = format("%f"%(psutil.virtual_memory()[1]))
        net = etree.SubElement(value,'net')
        nets = psutil.net_io_counters()
        net.text = format("sent:%s,recv:%s"%(nets[0],nets[1]))
        time.sleep(1)
    
    et = etree.ElementTree(root)
    et.write("g5/ex9/log.xml", pretty_print = True)

main()