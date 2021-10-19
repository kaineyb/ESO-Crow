#!/bin/bash

function get_branch() {
      git branch --no-color | grep -E '^\*' | awk '{print $2}' \
        || echo "default_value"
      # or
      # git symbolic-ref --short -q HEAD || echo "default_value";
}

function deploy_development() {
    # Set Variables
    export DEPLOYPATH=/home/arkus/python/dev_esocrow
    # Clear Dev Directory
    rm -r /home/arkus/python/dev_esocrow/*
    # Copy Files over from local dev repo
    /bin/cp -r /home/arkus/repositories/__DEV__ESO-Crow/* /home/arkus/python/dev_esocrow
    # Delete git folder
    rm -r /home/arkus/python/dev_esocrow/.git
    # Tell me that it worked...!
    echo "Development Deployed!"
}

function deploy_production() {
    # Set Variables
    export DEPLOYPATH=/home/arkus/python/esocrow
    # Clear Dev Directory
    rm -r /home/arkus/python/esocrow/*
    # Copy Files over from local dev repo
    /bin/cp -r /home/arkus/repositories/__LIVE__ESO-Crow/* /home/arkus/python/esocrow
    # Delete git folder
    rm -r /home/arkus/python/esocrow/.git
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

