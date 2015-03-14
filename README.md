# CTF@HSO Backend
This is the backend which should have been developed but we decided to use CTFd. Maybe this will be useful at some time later.

## Package managers
I used bower for all js related things and composer for php stuff.

## Dependencies
Make sure to have npm (node.js package manager), php and curl installed.

## Deployment
Install all dependencies inside the project directory and build a tar file with `./build.sh`.
Copy the file to your webserver, create `/var/www/backend` and untar it there.
You will ned to allow FollowSymlinks in your webserver configuration.
