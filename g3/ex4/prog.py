from subprocess import Popen
from subprocess import PIPE
import sys

proc = Popen("ls -la "+sys.argv[1], stdout=PIPE, shell=True)

return_code = proc.wait()

for line in iter(proc.stdout.readline, b''):
    s = line.decode('utf-8')
    
    if s.find(sys.argv[2]) < 0:
        print(s)
