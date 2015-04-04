#!/bin/bash
[ "$(which npm)" == "" ] && echo Please install npm first. && exit 1
[ "$(which php)" == "" ] && echo Please install php first. && exit 1
[ "$(which curl)" == "" ] && echo Please install curl first. && exit 1

npm install bower
curl -sS https://getcomposer.org/installer | php
./node_modules/.bin/bower install -p
./composer.phar install --no-dev
