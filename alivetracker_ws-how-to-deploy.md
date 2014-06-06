How to deploy alivetracker_ws ?
===============================

Firstable, if your sever is clean, you need to install the following softwate:

        sudo apt-get install apache2 unzip zip mysql git-core

Then you need to copy the compress file from our local machine to the server using scp. For example

         scp /home/myName/Spuras01.zip root@198.199.110.37:/home

Copy the compress file to public apache folder.

        sudo cp Spuras01.zip /var/www/html
        
Uncompress the file.

        unzip Spuras01.zip

Just to be sure, apply the permissions to files and folders.

        sudo find /html -type d -exec chmod 755 {} \;

        sudo find /html -type f -exec chmod 644 {} \;

To install python download the "compressed source tarball" from the oficial web page. [http://python.org/download/](http://python.org/download/)

        wget https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz

Then uncompress the python.
        
        tar -xvf  Python-2.7.6.tgz


Before compile, we need to install some tools. 

        sudo apt-get install build-essential

Execute the following command.
        
        ./configure

Ok ready, compile python !

        make
        sudo make altinstall

Check the python version.

        python --version

Now install the setuptools.

        sudo apt-get install python-setuptools python-pip

Teh to install pip and the setuptools, is easier install django.

        sudo pip install django

The project needs django rest-framework, so we can install it using pip.

        pip install djangorestframework
        pip install markdown  # Markdown support for the browseable API.
        pip install pyyaml    # YAML content-type support.
        pip install django-filter  # Filtering support

To run the app, we are going to use gunicorn.

        sudo pip install gunicorn 

After that, we must create a file called 'gunicorn.conf.py' inside of the project. 

        nano gunicorn.conf.py


Writte the following lines, for example:

        bind = "127.0.0.1:8000"
        workers = 2

Install mysql server.

        sudo apt-get install mysql-server

Install mysql drivers for python.

        sudo apt-get install python-mysqldb

The settings.py should use the mysql driver, 'DATABASE' section may looks like these:

        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'mysql'
            'NAME': 'mydb',
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': 'localhost', # or IP
            'PORT': '3606'                 
        }

Then syncronize the database.

        python manage.py syncdb

If you want to use a remote access, change your bind param.

        sudo nano /etc/mysql/my.cnf     

        #skip-external-locking
        #
        # Instead of skip-networking the default is now to listen only on
        # localhost which is more compatible and is not less secure.
        
        # old one
        #bind-address           = 127.0.0.1
        
        #new one
        bind-address           = 0.0.0.0

Restart the mysql service, and syncronize againg.

        sudo /etc/init.d/mysql reload
        sudo /etc/init.d/mysql restart
        python manage.py syncdb
        
Next we can run the project using unicorn.

        gunicorn_django -c gunicorn.conf.py
    
Add a "-D" to convert the process in a deamon.

        gunicorn_django -c gunicorn.conf.py -D

