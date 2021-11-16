#!/bin/bash

function get_branch() {
      git branch --no-color | grep -E '^\*' | awk '{print $2}' \
        || echo "default_value"
      # or
      # git symbolic-ref --short -q HEAD || echo "default_value";
}

function deploy_development() {
    # Set Variables
    export DEPLOYPATH=~/python/dev_esocrow
    # Clear Dev Directory
    rm -r ~/python/dev_esocrow/*
    # Copy Files over from local dev repo
    /bin/cp -r ~/repositories/__DEV__ESO-Crow/* ~/python/dev_esocrow
    # Delete git folder
    rm -r ~/python/dev_esocrow/.git
    # Tell me that it worked...!
    echo "Development Deployed!"
}

function deploy_production() {
    # Set Variables
    export DEPLOYPATH=~/python/esocrow
    # Clear Dev Directory
    rm -r ~/python/esocrow/*
    # Copy Files over from local dev repo
    /bin/cp -r ~/repositories/__LIVE__ESO-Crow/* ~/python/esocrow
    # Delete git folder
    rm -r ~/python/esocrow/.git
    # Tell me that it worked...!
    echo "Production Deployed!"
}

function hello_world() {

    echo "Hello World!"

}

branch_name=`get_branch`;
echo $branch_name;

if [ $branch_name == 'master' ]
then 
    deploy_production
fi

if [ $branch_name == 'develop' ]
then 
    deploy_development
    
fi