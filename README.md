# snapshotanalyzer-2019

DEMO project to manage AWS EC2 Instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 Instance snapshots

## Configuring

Shotty uses the configuration file created by the AWS cli e.g. 

`aws configure --profile shotty`

## running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes, or snapshots 
*subcommand* - depends on command
*project* is optional
