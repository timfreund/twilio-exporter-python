from setuptools import setup, find_packages

setup(
    name="twilio-exporter",
    version="0.1",
    packages=find_packages(),

    install_requires=[
        'click',
        'prometheus-client',
        'pyyaml'
    ],

    # metadata to display on PyPI
    author="Tim Freund",
    author_email="tim@freunds.net",
    description="Prometheus Exporter for Twilio",
    url="",
    entry_points = """\
    [console_scripts]
    twilio-exporter = twilioexporter:exporter
    """,
)
