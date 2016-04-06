#!/bin/bash

if [ $# -ne 1 ] ; then
	echo $0" <filelist>"
	exit 1
fi

workpath=/root/hequan
cd $workpath
cd irulu
git checkout master
git pull origin master

cat ${workpath}/$1 | while read filename_path ; 
do
	if [ $filename_path"X" = "X" ] ; then
		continue
	fi

    filename_path2=${filename_path#*/}
	filepath=`dirname ${filename_path}`

	if [ -d $filename_path2 ] ; then
        /bin/cp -fr $filename_path2 /data0/htdocs/$filepath
	else
		if [ -d ${filepath} ] ; then
            /bin/cp -f $filename_path2 /data0/htdocs/$filename_path
		else
            /bin/cp -rf `dirname $filename_path2` /data0/htdocs/$filepath
		fi
	fi

	if [ $? -ne 0 ] ; then
		echo "${filename_path} failed"
		exit 1
    else
        echo $filename_path
	fi
done
