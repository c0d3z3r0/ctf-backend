# CTF-Backend

This is the new backend for the CTF course / project at HS Offenburg.


## Deployment

### Install dependencies

~~~sh
aptitude update
aptitude upgrade
aptitude install python3-pip nginx openssl ssl-cert uwsgi uwsgi-plugin-python3 nodejs-legacy npm
pip3 install virtualenv
~~~

### Set up the server directory

~~~sh
cd /srv
git clone -b stable https://github.com/c0d3z3r0/ctf-backend.git
cd ctf-backend/
npm install bower
virtualenv venv
~~~

### Link config files

This step is optional if you're not the CTF@HSO admin. Feel free to copy the
configs and adapt them for your needs :-)

~~~sh
ln -s /srv/ctf-backend/conf/uwsgi.ini /etc/uwsgi/apps-enabled/ctf-backend.ini
ln -s /srv/ctf-backend/conf/nginx.conf /etc/nginx/sites-enabled/ctf-backend
~~~

### Install git-pull hook and run it manually the first time

The git-hook is used to update the python with pip and js/css libraries with bower, migrate the database, put the static files in the nginx static root and correct the permissions after a `git pull` so you don't need to care about that. After install we need to run it once by hand.

~~~sh
(cd .git/hooks/; ln -f -s ../../git-hooks/post-merge post-merge)
./git-hooks/post-merge
~~~

### Create admin user

This is the first user - you. If you need more admins, just tick `Superuser` for them in the admin interface.

~~~sh
. ./venv/bin/activate
./manage.py createsuperuser
deactivate
~~~

### E-Mail Settings

Do not set the mail settings in `settings.py`. Instead go to the admin interface to `Settings > General Backend Settings`.

## Updating

Since we use a git-hook you just need to do a `git pull` inside the base directory. When there are no errors, that's all you have to do :-)

A backup of your database will be stored at `/srv/ctf-backend/db.sqlite3.bak`.

~~~sh
cd /srv/ctf-backend
git pull
~~~

## Warning

You should ***NOT*** make any changes to the cloned git repo if you do not know how to deal with git merges!

## License

Copyright (C) 2016 Michael Niewöhner

This is open source software, licensed under AGPLv3. See the file LICENSE for details.
