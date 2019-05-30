# helper to deal with looking at every log chronologically
import os
import fnmatch
import glob
import json
from functools import reduce

path = '../gem-log-export/winston_log/2019'

files = []
for month in os.listdir(path):
    if ('.' not in month):
        for day in os.listdir(path + '/' + month):
            if ('.' not in day):
                for file_name in os.listdir(path + '/' + month + '/' + day):
                    hour = file_name[0: 2]
                    file = {}
                    file['month'] = month
                    file['day'] = day
                    file['hour'] = hour
                    file['file_name'] = file_name
                    files.append(file)

chronological_files = sorted(
    files, key=lambda i: (i['month'], i['day'], i['hour']))


def clean_chron_file(f):
    m = f['month']
    d = f['day']
    h = f['hour']
    name = f['file_name']
    cur_file_name = '{}/{}/{}/{}'.format(path, m, d, name)
    return (m, d, h, cur_file_name)


def reduce_logs(function, initializer):
    return reduce((lambda acc, file: function(acc, clean_chron_file(file))), chronological_files, initializer)
