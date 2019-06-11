from setuptools import setup

setup(
  name='snapshotanalyzer-2019',
  version='0.1',
  author="Deborah Cai",
  author_email="deborahcai@outlook.com",
  description="SnapshotAnalyzer 2019 is a tool to manage AWS EC2 snapshots",
  license="GPLv3+",
  packages=['shotty'],
  url="https://github.com/deborahcai/snapshotanalyzer-2019",
  install_requires=[
    'click',
    'boto3',
  ],
  entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
  ''',
)
