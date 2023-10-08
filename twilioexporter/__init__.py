import click
import random
import time
import yaml

from prometheus_client import start_http_server, Gauge

class TwilioMetric:
    def __init__(self, metric, attribute):
        self.metric = metric
        self.attribute = attribute

class TwilioAccount:
    def __init__(self, name, sid, api_key, api_secret):
        self.name = name
        self.sid = sid
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def balance(self):
        return random.random() * random.randint(0, 1000)

class TwilioMetric:
    def __init__(self, metric, attribute):
        self.metric = metric
        self.attribute = attribute

    def update(self, account):
        self.metric.labels(account.name, account.sid).set(getattr(account, self.attribute))

@click.command()
@click.option('-c', '--configuration-file', default="./twilio-exporter.yml", type=click.File('r'))
@click.option('-i', '--interval', default=0, type=int)
@click.option('-p', '--port', default=0, type=int)
def exporter(configuration_file, interval, port):
    exporter_config = {}
        'interval': interval,
        'port': port,
    }
    accounts = []
    metrics = []
    config = yaml.safe_load(configuration_file)
    for k, v in config['exporter']:
        exporter_config[k] = v

    if exporter_config['interval'] == 0:
        exporter_config['interval'] = 60
    if exporter_config['port'] == 0:
        exporter_config['port'] = 9130

    metrics.append(TwilioMetric(Gauge('twilio_balance',
                                      'Twilio account balance',
                                      ['name', 'sid']),
                                'balance'))

    for acct in config['accounts']:
        ta = TwilioAccount(**acct)
        print(ta.name)
        accounts.append(ta)

    start_http_server(port)

    while True:
        print("updating metrics")
        for m in metrics:
            for a in accounts:
                m.update(a)
        time.sleep(interval)

    print("exporter out")
