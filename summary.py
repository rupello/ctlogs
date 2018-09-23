import requests
import json
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

ctl_log = requests.get('https://www.gstatic.com/ct/log_list/log_list.json').json()

total_certs = 0

human_format = lambda x: locale.format('%d', x, grouping=True)

for log in ctl_log['logs']:
    log_url = log['url']
    try:
        log_info = requests.get('https://{}/ct/v1/get-sth'.format(log_url), timeout=3).json()
        total_certs += int(log_info['tree_size'])
    except:
        continue

    print("{} has {} certificates".format(log_url, human_format(log_info['tree_size'])))

print("Total certs -> {}".format(human_format(total_certs)))
