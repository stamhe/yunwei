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
    cmd = "ldconfig"
    # node web
    #cmd = "(cd /www/web && tar jxvf dbfen_web_node.tar.bz2)"
    # node server
    #cmd = "(cd /www/mulang/server && tar jxvf back_server_20140821.tar.bz2)"
    #cmd = "(cd /www/mulang/server && tar jxvf back_server_20140821.tar.bz2 && ln -s /www/mulang/server/back_server /server)"
    #cmd = "cd /tmp/software && tar zxvf percona-server-5.6.17-65.0.tar.gz && cd percona-server-5.6.17-65.0 && cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local/mysql-5.6.17 -DWITH_EXTRA_CHARSETS=all -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DWITH_SSL=yes -DWITH_INNODB_MEMCACHED=1 -DENABLE_GPROF=1 && make && make install &&  ln -s /usr/local/mysql-5.6.17 /usr/local/mysql"
    #cmd = "yum install cmake -y"
    #cmd = "/usr/local/mysql/bin/mysql --version"
    #cmd = "mkdir /root/hequan"
    #cmd = "cat /server/includes/server_info.cfg"
    #cmd = "mkdir /data_back/conf"
    #cmd = "cp /server/includes/server_info.cfg /data_back/conf/"
    #cmd = "/bin/cp -f /root/datamount /data_back/conf/"
    #cmd = "sed -i 's#cat datamount#cat /data_back/conf/datamount#' /server/misc/moni_info.sh"
    #cmd = "(rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm; rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6; yum clean all; yum makecache; yum install yum-priorities -y)"
    #cmd = "(cd /root/hequan/software; tar jxvf freetds-0.91.tar.bz2; cd freetds-0.91; ./configure --prefix=/usr/local/freetds --with-tdsver=8.0 --enable-msdblib; make; make install;cp include/tds.h /usr/local/freetds/include;cp src/tds/.libs/libtds.a  /usr/local/freetds/lib;)"
    #cmd = "(mkdir /root/hequan/software -p ;cd /root/hequan/software;wget -c 'http://us1.php.net/get/php-5.5.17.tar.bz2/from/this/mirror' -O php-5.5.17.tar.bz2)"
    #cmd = "(cd /root/hequan/software && tar jxvf php-5.5.17.tar.bz2 && cd php-5.5.17 && ./configure --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd  --prefix=/usr/local/php  --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-libxml-dir=/usr --enable-xml --disable-rpath --enable-safe-mode --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --with-curl --with-curlwrappers --enable-mbregex  --enable-fpm --with-fpm-user=www --with-fpm-group=www  --enable-mbstring --with-mcrypt --with-gd --enable-gd-native-ttf --with-openssl --with-mhash --enable-pcntl --enable-sockets --with-xmlrpc --enable-zip --enable-soap  --with-libdir=lib64 --enable-ftp --enable-sysvmsg --enable-sysvsem --enable-sysvshm && make ZEND_EXTRA_LIBS='-liconv' && make install)"
    #cmd = "ps -ef|grep php-fpm|grep master|grep -v grep|awk '{print $2}'|xargs -n 1 kill -USR2"
    #cmd = "/bin/rm -f /usr/local/php/lib/php.ini; ln -s /usr/local/php/etc/php.ini /usr/local/php/lib/php.ini"
    #cmd = "(cd /root/hequan/software && cd /root/hequan/software && tar jxvf php-5.5.12.tar.bz2 && cd php-5.5.12/ext/pdo_dblib && /usr/local/php/bin/phpize && ./configure --with-php-config=/usr/local/php/bin/php-config --with-pdo-dblib=/usr/local/freetds && make && make install)"
    #cmd = "(cd /root/hequan/software && tar zxvf  unixODBC-2.3.0.tar.gz && cd unixODBC-2.3.0 && ./configure --prefix=/usr/local/unixodbc --libdir=/usr/lib64 --sysconfdir=/etc --enable-gui=no --enable-drivers=no --enable-iconv --with-iconv-char-enc=UTF8 --with-iconv-ucode-enc=UTF16LE && ldconfig && make && make install && ldconfig && export PATH=$PATH:/usr/local/unixodbc/bin && cd /root/hequan/software && tar zxvf sqlncli-11.0.1790.0.tar.gz)"
    #cmd = "(cd /root/hequan/software && export PATH=$PATH:/usr/local/unixodbc/bin && tar zxvf sqlncli-11.0.1790.0.tar.gz && cd sqlncli-11.0.1790.0 && /bin/bash install.sh install --accept-license)"
    #cmd = "crontab -l > /data_back/crontab"
    #cmd = "(crontab -l > /data_back/crontab && /bin/cp -f /data_back/crontab /tmp/ && sed -i '/clearlog.sh/d' /data_back/crontab && cat /data_back/crontab|crontab)" 
    #cmd = "(crontab -l > /data_back/crontab; /bin/cp -f /data_back/crontab /tmp/;  echo '*/5 * * * * /bin/bash /server/misc/tmp_check.sh > /dev/null 2>&1 &' >> /tmp/crontab && cat /tmp/crontab|crontab)"
    #cmd = 'ls -al /tmp/'
    #cmd = 'ps -ef|grep filebackup|grep 16185|grep -v grep'
    #cmd = "(cd /root/hequan/software && wget -c \"http://ftp.postgresql.org/pub/source/v9.3.4/postgresql-9.3.4.tar.bz2\")"
    #cmd = "(cd /root/hequan/software && tar jxvf postgresql-9.3.4.tar.bz2 && cd postgresql-9.3.4 && ./configure --prefix=/usr/local/postgresql-9.3.4 --without-readline && make && make install)"
    #cmd = "(ln -s /usr/local/postgresql-9.3.4 /usr/local/postgresql && ldconfig && ln -s /usr/local/postgresql/bin/pg_dump /usr/bin/pg_dump && ln -s /usr/local/postgresql/bin/psql /usr/bin/psql)"
    #cmd = "mkdir -p /data_back/logs/file_back_bh /data_back/logs/db_back_bh"
    #cmd = "/bin/cp -f /server/includes/key.php /data_back/key_20140915.php"
    #cmd = "rpm -q --changelog openssl-1.0.1e | grep CVE-2014-0160"
    #cmd = "rm -fr /data_back/logs/migrationdb /data_back/logs/migrationsite /data_back/logs/redb /data_back/logs/refile /server/logs/migration /server/logs/reback /server/logs/recover"
    #cmd = "/usr/local/mysql/bin/mysqldump --help|grep -i gtid"
    #cmd = "/bin/rm -f /server/misc/keep_dbfen_srvs_alive.log"
    #cmd = "/etc/init.d/iptables restart"
    #cmd = "yum install net-snmp -y"
    #cmd = "/etc/init.d/snmpd start"
    #cmd = "service snmpd start"
    #cmd = "systemctl start snmpd.service"
    #cmd = "mkdir /server/logs/sysmonctl -p"
    #cmd = "netstat -natlpu|grep nrpe"
    #cmd = "(cd /root/hequan/tmp && tar zxvf nagios-plugins-1.4.15.tar.gz && cd nagios-plugins-1.4.15 && ./configure --prefix=/usr/local/nagios && make && make install && cd ../ && tar zxvf nrpe-2.12.tar.gz && cd nrpe-2.12 && ./configure --prefix=/usr/local/nagios --with-nrpe-port=7888 && make && make install)"
    #cmd = "(cd /root/hequan/tmp && tar zxvf nrpe-2.12.tar.gz && cd nrpe-2.12 && ./configure --prefix=/usr/local/nagios --with-nrpe-port=7888 && make && make install)"
    #cmd = "(/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d)"
    #cmd = "(/bin/cp -r  /www/mulang/server/back_server /data_back/server)"
    #cmd = "(tar jxvf /data_back/hequan_20140915d.tar.bz2 -C /; /bin/cp -f /data_back/key_api_20140915.php /server/includes/key.php)"
    #cmd = "(cd /data_back/nginx-v6 && bash nginx-v6-php-5.5-node.sh)"
    #cmd = "(mkdir -p /www/mulang/server ; mkdir -p /www/web)"
    #cmd = "(rm -fr /data_back/logs/filerecovery /data_back/logs/filemovehouse; mkdir /data_back/logs/file_recovery /data_back/logs/file_movehouse)"
   #cmd = "(chkconfig crond on && /etc/init.d/crond restart && chkconfig iptables on && /etc/init.d/iptables restart)"
    #cmd = "service crond restart"
    #cmd = "mkdir /data_back/logs/db_recovery /data_back/logs/db_movehouse"
    #cmd = "(cd /root/hequan/tmp && tar xvf PDO_PGSQL-1.0.2.tgz && cd PDO_PGSQL-1.0.2 && /usr/local/php/bin/phpize && ./configure --with-php-config=/usr/local/php/bin/php-config --with-pdo-pgsql=/usr/local/postgresql && make && make install)"
    #cmd = "ps -ef|grep -i master|grep php-fpm|grep -v grep|awk '{print $2}'|xargs -n 1 kill -USR2"
    #cmd = "ps -ef|grep -i lftp|grep -v grep|awk '{print $2}'|xargs -n 1 kill -9"
    #cmd = "tar jxvf /root/hequan/tmp/hequan_20140610.tar.bz2 -C /"
    #cmd = "mkdir -p /root/hequan/tmp"
    #cmd = "yum --enablerepo=updates install openssl -y"
    #cmd = "(groupadd nagios && useradd -g nagios -d /usr/local/nagios -s /sbin/nologin nagios)"
    #cmd = "(mkdir /tmp/software; cd /tmp/software; /usr/local/php/bin/pecl download channel://pecl.php.net/ssh2-0.12)" 
    #cmd = "(/bin/cp -f /usr/local/php/etc/php.ini /data_back/)"
    #cmd = "(/bin/cp -f /usr/local/php/lib/php.ini /data_back/backup && /bin/cp -f /usr/local/php/etc/php-fpm.conf /data_back/backup/)"
    #cmd = "(chkconfig iptables on)"
    #cmd = "(chkconfig --add  nrped)"
    #cmd = "(chkconfig nrped on)"
    #cmd = "chown -R nagios.nagios /usr/local/nagios/libexec"
    #cmd = "/bin/rm -f /www/web/dbfen/application/controllers/account.php /www/web/dbfen/application/controllers/db.php /www/web/dbfen/application/controllers/guider.php /www/web/dbfen/application/controllers/help.php /www/web/dbfen/application/controllers/home.php /www/web/dbfen/application/controllers/invited.php /www/web/dbfen/application/controllers/news.php /www/web/dbfen/application/controllers/pg.php /www/web/dbfen/application/controllers/spread.php /www/web/dbfen/application/controllers/welcome.php /www/web/dbfen/application/controllers/order.php /www/web/dbfen/application/controllers/site.php /www/web/dbfen/application/controllers/users.php"
    #cmd = "echo '/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d' >> /etc/rc.local"
    #cmd = "service snmpd start >> /etc/rc.local"
    #cmd = "(ps -ef|grep nrpe|grep -v grep|awk '{print $2}'|xargs -n 1 kill -9 && /usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d)"
    #cmd = "(tar jxvf /data_back/tarfile/hequan_20141022a.tar.bz2 -C / && /bin/bash /server/misc/restart_srv.sh dbfen_decrypt)"
    #cmd = "/bin/cp -f /data_back/backup/key.php /server/includes/"
    #cmd = "(cd  /root/hequan/tmp && tar zxvf unixODBC-2.3.0.tar.gz && cd unixODBC-2.3.0 && ./configure --prefix=/usr/local/unixodbc --libdir=/usr/lib64 --sysconfdir=/etc --enable-gui=no --enable-drivers=no --enable-iconv --with-iconv-char-enc=UTF8 --with-iconv-ucode-enc=UTF16LE && make && make install && ldconfig && cd ../ && export PATH=$PATH:/usr/local/unixodbc/bin && tar zxvf sqlncli-11.0.1790.0.tar.gz && cd sqlncli-11.0.1790.0 && /bin/bash install.sh install --accept-license)"
    #cmd = "(/bin/cp -f /server/includes/key.php /data_back/backup/; /bin/cp -rf /data_back/conf /data_back/backup/ ;/bin/cp -rf /data_back/backup /root/)"
    #cmd = "(/bin/cp -f /www/web/dbfen/application/controllers/dl.php /data_back/backup/)"
    #cmd = "(/bin/rm -f /www/mulang/server/back_server/server/oss_sdk_php_*)"
    #cmd = "/usr/local/mysql/bin/mysql --version"
    #cmd = "(service rsyslog restart; /etc/init.d/fail2ban restart; chkconfig fail2ban on)"
    #cmd = "/usr/local/php/bin/pecl install memcache"
    #cmd = "(ps -ef|grep php-fpm|grep master|awk '{print $2}'|xargs -n 1 kill -USR2)"
    #cmd = "(pkill nrpe;/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d)"
    #cmd = "(/bin/bash /server/misc/restart_srv.sh dbfen_cmdrelay dbfen_nodetaskmgr dbfen_sysmonctl dbfen_task_assist)"
    #cmd = "(/bin/bash /server/misc/restart_srv.sh dbfen_decrypt)"
    cmd = "(ps -ef|grep php-fpm|grep master|grep -v grep|awk '{print $2}'|xargs -n 1 kill -QUIT; cd /usr/local/php; sbin/php-fpm -c etc/php.ini -y etc/php-fpm.conf)"
    #cmd = "(/usr/local/nginx/sbin/nginx -s reload)"
    cmd = 'ssh -p %d %s@%s "%s"'%(port, user, ip, cmd)


    # rsync
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /data/software/nginx-v6  %s@%s:/data_back/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/tmp/key.php %s@%s:/server/includes/'%(port, user, ip)
    # node web
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/tmp/dbfen_web_node.tar.bz2  %s@%s:/www/web/'%(port, user, ip)
    # node server
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/tmp/back_server_20140821.tar.bz2 %s@%s:/www/mulang/server/'%(port, user, ip)

    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/yang/nagios_scripts/etc/nrpe.cfg  %s@%s:/usr/local/nagios/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /trunk/application/libraries/ucloud %s@%s:/www/web/dbfen/application/libraries/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /data/software/nginx-v6/unixODBC-2.3.0.tar.gz /data/software/nginx-v6/sqlncli-11.0.1790.0.tar.gz  %s@%s:/root/hequan/tmp/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /trunk/application/controllers/dl.php  %s@%s:/www/web/dbfen/application/controllers/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /trunk/application/controllers/node_svr.php %s@%s:/www/web/dbfen/application/controllers/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /trunk/application/config/constants.php  %s@%s:/www/web/dbfen/application/config/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /trunk/application/helpers/util_helper.php %s@%s:/www/web/dbfen/application/helpers/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/autoload.php %s@%s:/www/web/dbfen/application/config/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /server/libs/ucloud/http.php %s@%s:/server/libs/ucloud/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/config.php %s@%s:/www/web/dbfen/application/config/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/nginx.conf %s@%s:/usr/local/nginx/conf/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/php.ini %s@%s:/usr/local/php/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /application/libraries/Request.php /application/libraries/Response.php %s@%s:/www/web/dbfen/application/libraries/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/hequan_20141022a.tar.bz2 %s@%s:/data_back/tarfile/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /etc/sysctl.conf %s@%s:/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/hequan_20140915d.tar.bz2 %s@%s:/data_back/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /data/software/nrpe/nrpe-2.12.tar.gz  /data/software/nrpe/nagios-plugins-1.4.15.tar.gz %s@%s:/root/hequan/tmp/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /usr/local/nagios/libexec/check_disk2 %s@%s:/usr/local/nagios/libexec/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/.screenrc %s@%s:/root/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /etc/fail2ban/jail.conf %s@%s:/etc/fail2ban/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /etc/resolv.conf %s@%s:/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /etc/snmp/snmpd.conf %s@%s:/etc/snmp/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /tmp/qiniu_20141204.tar.bz2 %s@%s:/data_back/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /tmp/index.php %s@%s:/www/web/dbfen/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/nrpe.cfg %s@%s:/usr/local/nagios/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/tmp_check.sh %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /tmp/key.php %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /tmp/init.php %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /root/hequan/tmp/iptables %s@%s:/etc/sysconfig/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /tmp/database.php %s@%s:/www/web/dbfen/application/config/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /usr/local/nagios/etc/nrpe.cfg %s@%s:/usr/local/nagios/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /data/software/nginx-v6/nrpe.cfg %s@%s:/usr/local/nagios/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/yang/nagios_scripts/libexec/ %s@%s:/usr/local/nagios/libexec/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/libs/ucloud %s@%s:/server/libs/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /trunk/application/libraries/ucloud/ucloud.php %s@%s:/www/web/dbfen/application/libraries/ucloud/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/libs/MsSQLDump.php %s@%s:/server/libs/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/libs/aliconf.inc.php %s@%s:/server/libs/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/libs/alisdk.class.php %s@%s:/server/libs/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/libs/AES.php %s@%s:/server/libs/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/includes/mysqltool.php %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/libs/MsSQLDump.php /server/libs/alirc.class.php /server/libs/RequestCore.class.php %s@%s:/server/libs/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/tmp/moni_info.sh %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/tmp/moni_info.sh %s@%s:/www/mulang/server/back_server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/misc/restart_srv.sh %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/includes/database.class.php %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/includes/config.inc.php %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/includes/function.inc.php %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_serviceframe.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_decrypt.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_cmdrelay.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_eval_latency.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/backup_common.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_sysmonctl.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_scheduler.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_task_assist.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_worker_dbbackup.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_worker_dbbackup_bh.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/backup_common.php /server/server/dbfen_sysmonctl.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_worker_filebackup.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_worker_filerecovery.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_nodetaskmgr.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_cmdrelay.php /server/server/dbfen_sysmonctl.php /server/server/dbfen_nodetaskmgr.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_decrypt.php /server/server/dbfen_worker_dbbackup_bh.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_cmdrelay.php /server/server/dbfen_nodetaskmgr.php /server/server/backup_common.php /server/server/dbfen_sysmonctl.php  %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/misc/dbfen_cleanup.sh  %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/misc/keep_dbfen_srvs_alive.sh %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/misc/moni_info.sh %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_worker_dbbackup_bh.php /server/server/dbfen_worker_filebackup_bh.php /server/server/dbfen_worker_filebackup.php /server/server/dbfen_worker_dbbackup.php /server/server/dbfen_decrypt.php /server/server/dbfen_cmdrelay.php /server/server/dbfen_nodetaskmgr.php /server/server/dbfen_serviceframe.php /server/server/dbfen_sysmonctl.php /server/server/dbfen_worker_filerecovery.php /server/server/dbfen_worker_filemovehouse.php /server/server/backup_common.php /server/server/dbfen_worker_dbmovehouse.php /server/server/dbfen_worker_dbrecovery.php /server/server/dbfen_task_assist.php   %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\'  /server/server/dbfen_decrypt.php  /server/server/dbfen_worker_dbbackup_bh.php /server/server/dbfen_worker_filebackup_bh.php /server/server/dbfen_worker_filebackup.php /server/server/dbfen_worker_dbbackup.php  /server/server/dbfen_worker_filerecovery.php /server/server/dbfen_worker_filemovehouse.php /server/server/dbfen_worker_dbmovehouse.php /server/server/dbfen_worker_dbrecovery.php /server/server/backup_common.php   %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_worker_filebackup.php /server/server/dbfen_worker_dbbackup.php /server/server/dbfen_worker_dbbackup_bh.php /server/server/dbfen_worker_filebackup_bh.php  /server/server/dbfen_worker_filerecovery.php /server/server/dbfen_worker_filemovehouse.php /server/server/dbfen_worker_dbmovehouse.php /server/server/dbfen_worker_dbrecovery.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_sysmonctl.php /server/server/dbfen_worker_filebackup.php /server/server/dbfen_worker_dbbackup.php /server/server/dbfen_worker_dbbackup_bh.php /server/server/dbfen_worker_filebackup_bh.php  /server/server/dbfen_worker_filerecovery.php /server/server/dbfen_worker_filemovehouse.php /server/server/dbfen_worker_dbmovehouse.php /server/server/dbfen_worker_dbrecovery.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/server/dbfen_sysmonctl.php /server/server/backup_common.php %s@%s:/server/server/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/tmp/ssh2.so %s@%s:/usr/local/php/lib/php/extensions/no-debug-non-zts-20121212/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/key.php  %s@%s:/server/includes/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/.vimrc %s@%s:/root/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /server/misc/clearlog.sh %s@%s:/server/misc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /usr/local/freetds/etc/freetds.conf  %s@%s:/usr/local/freetds/etc/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/hequan/software/sqlncli-11.0.1790.0.tar.gz   %s@%s:/root/hequan/software/'%(port, user, ip)
    #cmd = 'rsync -atvP -e \'ssh -p %s\' /root/yang/nagios_scripts/nrped   %s@%s:/etc/rc.d/init.d/'%(port, user, ip)
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
"192.168.1.1"	  : ["192.168.1.1", 22, "root", '123456','ucloud北京C-NODE_UCLOUD_BJ_01'],
}

if __name__ == '__main__':
    threads = []	
    for name, value in serverlist.items():
        a = threading.Thread(target = run_cmd, args = (value[0], value[1], value[2], value[3]))
        a.start()
