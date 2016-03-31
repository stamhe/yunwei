#!/bin/bash
# @hequan
# 解压缩文件，并对压缩包的文件先行备份

if [ $# -ne 1 ] ; then
	echo "$0 <package>"
	exit 1
fi

tar tf $1 > /dev/null 2>&1
if [ $? -ne 0 ] ; then
	echo "unpack $1 failed"
	exit 1
fi

old_filelist=`tar tf $1`
new_filelist=
for filename in ${old_filelist}
do
	new_filelist=${new_filelist}" /${filename}"
done
packagename=`basename $1`
packagename=/data_back/tmp/${packagename}

tar --exclude "*.svn*" -jcvf $packagename ${new_filelist} > /dev/null 2>&1

tar jxvf $1 -C /
