from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('text', type=str, help='an integer for the accumulator')
args = parser.parse_args()
text = args.text



print(f'{text} (0.1.1)')
