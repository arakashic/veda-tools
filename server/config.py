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
    if len(section) == 0:
        sechead = re.compile(sectionhead)
        sectail = re.compile(sectiontail)
        for i in range(0, len(lines)):
            if sechead.search(lines[i]):
                head = i
            if sectail.search(lines[i]):
                tail = i
    for i in rang(head, tail):
        if lines[i][0] == '#':
            continue
        if token.search(line):
            temp = lines[i].split(' ')
            config_value = temp[len(temp)-1]
            break
    
    return config_value
            