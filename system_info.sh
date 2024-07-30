#!/bin/bash

# sysinfo_page - A script to produce an HTML file
#Functions
$(system_info)
{
	echo "function system_info"
}
$(show_uptime)
{
echo "function show_uptime"
}
$(drive_space)
{
    echo "function drive_space"
}
$(home_space)
{
    echo "function home_space"
}
title="System Information for $HOSTNAME"
RIGHT_NOW=$(date +"%x %r %Z")
TIME_STAMP="Updated on $RIGHT_NOW by $USER"

cat <<- _EOF_
<html>
    <head>
    <title>
        $title
    </title>
    </head>

    <body>
	    <h1>$title</h1>
	    <p>$TIME_STAMP</p>
		$(system_info)
		$(show_uptime)
		$(drive_space)
		$(home_space)
    </body>
</html>
_EOF_
