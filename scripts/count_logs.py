# counts and prints total number of logs
from reduce_logs import reduce_logs


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def count_logs(m, d, h, file_name):
    num_logs = file_len(file_name)
    print('{}:{}:{} | {:<8} logs'.format(m, d, h, num_logs))
    return num_logs


total_logs = reduce_logs(
    (lambda acc, log_file:
        acc + count_logs(*log_file)),
    0)

print('Total Number of Logs: {}'.format(total_logs))
