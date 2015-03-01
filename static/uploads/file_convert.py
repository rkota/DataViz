import sys

updated = open ('updated.tsv', 'a')
with open (sys.argv[1], 'r') as f:
	for line in f:
		line = line.strip ()
		updated.write (line + '\n')
f.close ()
updated.close ()
