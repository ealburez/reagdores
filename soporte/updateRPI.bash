#!/bin/bash
#-----------------------------------------------------------------------------
#			Update from Github
#-----------------------------------------------------------------------------

#variables
repositoryDir="/home/repo/regadores"
wwwDir="/var/www/html"

#Update the iota repository
git -C $repositoryDir reset --hard
git -C $repositoryDir pull

#make all .bash files excecutable
#sudo chmod ugo+x $repositoryDir/*.bash

#move all pages to it position
find $repositoryDir -maxdepth 1 -type f -exec cp {} $wwwDir \;


#Update Crontab
#crontab buCrontab
