#!/bin/bash
#-----------------------------------------------------------------------------
#                       Change branch from Github
#                          !!!DO NOT DEPLOY !!!
#pasar el como argumento el nombre de la branch a ala que se quiere cambiar
# ejemplo:
# ./changeBranch.bash master
#-----------------------------------------------------------------------------

#variables
repositoryDir="/home/repo/regadores"
branch=$1

#delete all files in the repository
rm $repositoryDir/*

#Update the repository
git -C $repositoryDir reset --hard
git -C $repositoryDir fetch --all
git -C $repositoryDir fetch -p origin
git -C $repositoryDir checkout $branch
git -C $repositoryDir pull

#make all .bash files excecutable
#sudo chmod ugo+x $repositoryDir/*.bash

#Run updateRPI to delete sourcefiles
#bash $repositoryDir/updateRPI.bash
