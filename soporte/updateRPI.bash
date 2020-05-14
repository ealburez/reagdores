#!/bin/bash
#-----------------------------------------------------------------------------
#			Update from Github
#-----------------------------------------------------------------------------

#variables
repositoryDir="/home/repo/regadores"

#Update the iota repository
git -C $repositoryDir reset --hard
git -C $repositoryDir pull

#make all .bash files excecutable
sudo chmod ugo+x $repositoryDir/*.bash

#Update Crontab
#crontab buCrontab
