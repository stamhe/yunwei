#!/bin/bash

if [ $# -ne 1 ] ; then
	echo $0" <filelist>"
	exit 1
fi

workpath=/root/hequan
deploy_path=/data/htdocs/
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
        /bin/cp -fr $filename_path2 $deploy_path$filepath
	else
		if [ -d ${filepath} ] ; then
			if [ ! -d $deploy_path$filepath ] ; then
				mkdir -pv $deploy_path$filepath
				if [ $? -ne 0 ] ; then
					echo "mkdir $deploy_path$filepath failed"
					exit
				fi
			fi

			if [ -f $filename_path ] ; then
				/bin/cp -f $filename_path $deploy_path$filename_path
            else
                /bin/cp -fr $filename_path $dst_project_path$filepath
            fi		
		fi
	fi

	if [ $? -ne 0 ] ; then
		echo "${filename_path} failed"
		exit 1
    else
        echo $filename_path
	fi
done
