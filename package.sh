#!/bin/bash

if [ $# -ne 2 ] ; then
	echo $0" <filelist> <packagename>"
	exit 1
fi

filelist_old=`cat $1|sort|uniq`

filelist_new=""

excludelist='/trunk/server/includes/key.php /trunk/application/config/production/config.php /trunk/application/config/production/database.php'

for filename in ${filelist_old} ; 
do
	if [ -d ${filename} ] ; then
		continue
	fi
    if [ $filename == '/trunk/server/includes/init.php' ] ; then
        continue
    fi

    if [ $filename == '/trunk/server/includes/key.php' ] ; then
        continue
    fi

    if [ $filename == '/trunk/application/config/production/config.php' ] ; then
        continue
    fi

    if [ $filename == '/trunk/application/config/production/database.php' ] ; then
        continue
    fi
    if [ ${filename##*.} == 'sass' ] ; then
        filename=${filename%.*}.css
    fi
	filelist_new=$filelist_new" "$filename
done


tar --exclude "*.svn*" -jcvf $2 $filelist_new
