import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

nsp = parser.parse_args(['-a', '-bval', '-c', '3'])

print(nsp)

for k in list(nsp):
    print(str(k))

