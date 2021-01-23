#!/bin/bash
DIRECTORY="/opt/panelscripts"
if [ ! -d $DIRECTORY ]
then
	echo "The script needs root permissions to set up the folder" 
	sudo mkdir -p $DIRECTORY
fi
cp */*.py $DIRECTORY
