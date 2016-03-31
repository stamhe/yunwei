#!/usr/bin/python2.6
#coding=utf-8

import pexpect
import threading
import sys
import os
import struct
import fcntl
import termios
import signal



if len(sys.argv) != 2:
    print "%s 192.168.1.1"%(sys.argv[0])
    sys.exit(1)


def sigwinch_passthrough(sig, data):
    winsize = getwinsize()
    global ssh
    ssh.setwinsize(winsize[0], winsize[1])

def getwinsize():
    if 'TIOCGWINSZ' in dir(termios):
        TIOCGWINSZ = termios.TIOCGWINSZ
    else:
        TIOCGWINSZ = 1074295912L

    s = struct.pack('HHHH', 0, 0, 0, 0)
    x = fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ, s)
    return struct.unpack("HHHH", x)[0:2]

serverlist = {
"192.168.1.4"		  : ["192.168.1.4", 22, "root", '123456',          'aliyun青岛-web服务器'],
}

if __name__ == '__main__':
    if serverlist.has_key(sys.argv[1]):
        serverinfo = serverlist[sys.argv[1]]
        cmd = 'ssh -p %s %s@%s'%(serverinfo[1], serverinfo[2], serverinfo[0])
        print cmd
        ssh = pexpect.spawn(cmd, [], 300)
        signal.signal(signal.SIGWINCH, sigwinch_passthrough)
        try:
            while True:
                i = ssh.expect(['password', 'continue connecting'])
                if i == 0:
                    ssh.sendline(serverinfo[3])
                    break
                elif i == 1:
                    ssh.sendline('yes')
                else:
                    break
        except pexpect.EOF:
            ssh.close()
        else:
            winsize = getwinsize()
            ssh.setwinsize(winsize[0], winsize[1])
            ssh.interact()
            pass
    else:
        print '%s 192.168.1.1'%(sys.argv[0])
