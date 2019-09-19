#!/bin/bash

docker run --name configtool -p 5000:5000 -v /usr/dynas/deploy-configTool:/code/tool --restart always --privileged=true -it configtool
