import os
import sys
from normalize_neologd import normalize_neologd

infile = sys.argv[1]
print("Counting line number...")
num_lines = sum(1 for line in open(infile))

outfile = os.path.splitext(infile)[0].replace("_extracted", "_normalized") + ".txt"
with open(outfile, 'w') as fout, open(infile) as fin:
    for i, line in enumerate(fin):
        if i > 0 and i % 20000 == 0:
            print("{0:10} / {1:10} lines ({2:1.1f} percent) done".format(i, num_lines, 100.0 * i / num_lines))
            sys.stdout.flush()
        if line.startswith('<doc') or line.startswith('</doc'):
            fout.write(line)
        else:
            fout.write(normalize_neologd(line) + "\n")
