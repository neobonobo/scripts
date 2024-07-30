#!/bin/sh
# Linux users have to change $8 to $9
awk '
BEGIN 	{ print "File\t\t\tOwner" } 
		{ print $9, "\t", $3}	
END   	{ print " - DONE -" } 
'
