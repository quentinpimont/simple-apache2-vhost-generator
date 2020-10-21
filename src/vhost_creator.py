import os
from shutil import copyfile

class Vhost_creator():
    root_project : str
    project_name : str
    self_path = os.path.dirname(os.path.realpath(__file__)) + '/'
    def __init__(self, root_project : str):
        self.root_project = root_project
        root_project_split = self.root_project.split('/')
        self.project_name = root_project_split[root_project_split.count(root_project_split   ) - 1]

    def create_conf_file(self):
        content = '<VirtualHost *:80>\n\tServerName ' + self.project_name + '\n\tServerAlias ' + self.project_name + '\n\tErrorLog /var/log/apache2/' + self.project_name + '-error.log\n\tCustomLog /var/log/apache2/' + self.project_name + '-access.log common\n\tDocumentRoot "' + self.root_project + '/"\n\t<directory ' +  self.root_project + '/>\n\t\tOptions -Indexes +FollowSymLinks +MultiViews\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n</VirtualHost>'
        file_path = self.self_path + self.project_name + '.conf'
        with open(file_path, 'w') as conf_file:
            conf_file.write(content)
            conf_file.close()
        os.rename(file_path, '/etc/apache2/sites-available/' + self.project_name + '.conf')

    def add_in_hosts_file(self):
        hosts_path = '/etc/hosts'
        copyfile(hosts_path, self.self_path + 'hosts.save')
        insert_index = 0
        hosts_file = open(hosts_path, 'r')
        lines = hosts_file.readlines()
        hosts_file.close()
        for i, line in enumerate(lines):
            if(line == '\n' or line[0] == '#'):
                insert_index = i
                break
        lines.insert(insert_index, '127.0.0.1\t' + self.project_name + '\n')
        hosts_content = ''.join(lines)
        hosts_file = open(hosts_path, 'w')
        hosts_file.write(hosts_content)
        hosts_file.close()

    def activate_vhost(self):
        conf_name = self.project_name + '.conf'
        os.system('a2ensite ' + conf_name)
        os.system('systemctl reload apache2')

    def create_vhost(self):
        self.create_conf_file()
        self.add_in_hosts_file()
        self.activate_vhost()