import argparse
parser = argparse.ArgumentParser()
parser.add_argument('address', nargs="?", default='localhost')
parser.add_argument('port', nargs="?", default=8888)
args = parser.parse_args()
