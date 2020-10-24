# Apache2 vhost generator
generate simple apache2 vhost for developement

## prerequisite
- Python 3
- Linux (Only tested on debian based system)
- Apache2

## Install
clone repository

`git clone https://github.com/quentinpimont/simple-apache2-vhost-generator.git`

Create *.bash_aliases* at your home directory

`touch /home/your_username/.bash_aliases`

Add this line in *.bash_aliases*

`alias vhost="sh /home/your_username/path/to/simple-apache2-vhost-generator/src/vhost.sh"`

you must restart the terminal to finish install

## How to use
Go to the folder where index.php is located and type this command

`vhost`

you can access your project in your browser with this url

`name_root_porject_directory/`
