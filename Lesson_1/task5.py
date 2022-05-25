import subprocess
import sys

args = ['ping', 'yandex.ru', '-c 1']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
encoding = sys.getdefaultencoding()

for line in subproc_ping.stdout:
    print(line.decode(encoding))


args = ['ping', 'youtube.com', '-c 1']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
encoding = sys.getdefaultencoding()

for line in subproc_ping.stdout:
    print(line.decode(encoding))
