import sys, getopt
from vhost_creator import Vhost_creator

root_project = ''
opts, args = getopt.getopt(sys.argv[1:], 'r:', ['root-project'])

for opt, ar in opts:
    if(opt == '-r'):
        root_project = ar
vhost_creator = Vhost_creator(root_project)
vhost_creator.create_vhost()
print(vhost_creator.project_name)