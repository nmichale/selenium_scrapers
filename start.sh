#!/bin/bash
#set -x

docker rm selenium_scrapers
docker build -t selenium_scrapers . 
docker run --name selenium_scrapers -i -d  selenium_scrapers
