#!/usr/bin/python2.6
#coding=utf-8

import pexpect
import threading
import sys
import os


if len(sys.argv) != 2 or sys.argv[1] != 'confirm':
    print "%s confirm"%(sys.argv[0])
    sys.exit(1)


def run_cmd(ip, port, user, passwd):
    # remote cmd
    #cmd = "ls /"
    #cmd = "ldconfig"
    # rsync
    cmd = 'rsync -atvP -e \'ssh -p %s\' /www/web/new_dbfen/  %s@%s:/www/web/new_dbfen/'%(port, user, ip)
    print "cmd = %s"%(cmd)
    ssh = pexpect.spawn(cmd, [], 6000)
    fp = file("%s"%(ip), 'w')
    ssh.logfile = fp
    r = ''
    try:
        while True:
            i = ssh.expect(['assword: ', 'continue connecting (yes/no)?'])
            if i == 0:
                ssh.sendline(passwd)
                break
            elif i == 1:
                ssh.sendline('yes')
    except pexpect.EOF:
        ssh.close()
    else:
        r = ssh.read()
        #ssh.expect(pexpect.EOF)
        ssh.close()

    print r

serverlist = {
"192.168.1.1"		: ["192.168.1.1", 22, "root", '123456',         'aliyun青岛-web1'],
"192.168.1.2"		: ["192.168.1.2", 22, "root", '123456',           'aliyun青岛-web2'],
}

if __name__ == '__main__':
    threads = []	
    for name, value in serverlist.items():
        a = threading.Thread(target = run_cmd, args = (value[0], value[1], value[2], value[3]))
        a.start()
