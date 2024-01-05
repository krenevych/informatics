import sys

infile = sys.argv[1]
outfile = sys.argv[2]


f = open(infile, 'r')
lines = f.readlines()
f.close()


f_out = open(outfile, 'w')
f_out.writelines(lines)
f_out.close()




