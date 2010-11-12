import os, sys, time
import re

def apply_config_line(config_file='', config_name='', config_line=''):
    cmdline = 'sed -e \'/%s/c%s\' %s > %s' \
                % (config_name, config_line, config_file, config_file)
    os.system(cmdline)
    
def get_config(config_file='', config_name='', sectionhead='', sectiontail=''):
    fp = file(config_file, 'r')
    lines = fp.readlines()
    fp.close()
    head = 0
    tail = len(lines)
    token = re.compile(config_name)
    if len(sectionhead) == 0:
        sechead = re.compile(sectionhead)
        sectail = re.compile(sectiontail)
        for i in range(0, len(lines)):
            if sechead.search(lines[i]):
                head = i
            if sectail.search(lines[i]):
                tail = i
    for i in range(head, tail):
        if lines[i][0] == '#':
            continue
        if token.search(lines[i]):
            temp = lines[i].strip().split(' ')
            config_value = temp[len(temp)-1]
            break
    
    return config_value

if __name__ == "__main__":
    print get_config("/etc/apache2/apache2.conf", "MaxClients", "_prefork_", "IfModule")
    # apply_config_line("/etc/apache2/apache2.conf", "MaxClients", "MaxCliens -99")
            