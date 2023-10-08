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
    def __init__(self, name, account_sid, api_key, api_secret):
        self.name = name
        self.account_sid = account_sid
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
        self.metric.labels(account.name, account.account_sid).set(getattr(account, self.attribute))

@click.command()
@click.option('-c', '--configuration-file', default="./twilio-exporter.yml", type=click.File('r'))
def exporter(configuration_file):
    accounts = []
    metrics = []
    config = yaml.safe_load(configuration_file)
    print(config)

    metrics.append(TwilioMetric(Gauge('twilio_balance',
                                      'Twilio account balance',
                                      ['name', 'sid']),
                                'balance'))

    for acct in config['accounts']:
        ta = TwilioAccount(**acct)
        print(ta.name)
        accounts.append(ta)

    start_http_server(9130)

    while True:
        for m in metrics:
            for a in accounts:
                m.update(a)
        time.sleep(5)

    print("exporter out")
