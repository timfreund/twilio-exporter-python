from setuptools import setup, find_packages

setup(
    name="twilio-exporter",
    version="0.1",
    packages=find_packages(),

    install_requires=[
        'click',
        'prometheus-client',
        'pyyaml',
        'twilio'
    ],

    # metadata to display on PyPI
    author="Tim Freund",
    author_email="tim@freunds.net",
    description="Twilio Prometheus Exporter",
    url="https://github.com/timfreund/twilio-exporter-python",
    entry_points = """\
    [console_scripts]
    twilio-exporter = twilioexporter:exporter
    """,
)
