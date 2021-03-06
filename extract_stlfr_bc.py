#!/usr/bin/env python
import gzip
import sys


def main(argv):
    inFile = argv[1]
    outbc1 = argv[2] + "_bc1.fq"
    outbc2 = argv[2] + "_bc2.fq"
    outbc3 = argv[2] + "_bc3.fq"
    type_bc = argv[3]
    bc1 = open(outbc1, "w")
    bc2 = open(outbc2, "w")
    bc3 = open(outbc3, "w")

    count = 0
    with gzip.open(inFile, "rt") as read2:

        for line in read2:
            count += 1
            if count % 2 == 0:
                b1 = ""
                b2 = ""
                b3 = ""
                if type_bc == "30":
                    b1 = line[100:110] + "\n"
                    b2 = line[110:120] + "\n"
                    b3 = line[120:130] + "\n"
                elif type_bc == "42":
                    b1 = line[100:110] + "\n"
                    b2 = line[116:126] + "\n"
                    b3 = line[132:142] + "\n"
                elif type_bc == "54":
                    b1 = line[100:110] + "\n"
                    b2 = line[116:126] + "\n"
                    b3 = line[144:154] + "\n"
                bc1.write(b1)
                bc2.write(b2)
                bc3.write(b3)
            else:
                bc1.write(line)
                bc2.write(line)
                bc3.write(line)
    bc1.close()
    bc2.close()
    bc3.close()
    read2.close()


if __name__ == "__main__":
    main(sys.argv)
