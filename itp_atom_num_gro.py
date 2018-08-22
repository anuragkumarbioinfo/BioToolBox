#updated from pycharm
import os, sys
#from operator import itemgetter
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("i", help="itp file name")
parser.add_argument("g", help="gro file name")
args = parser.parse_args()

ref_itp = args.i
print ref_itp
query_gro = args.g
print query_gro

def itpReader(p):
    itp_atom_num = []    
    marker = False
    with open(p) as itpname:
        for lines in itpname:
            if ";  nr" in lines:
                marker = True     
            elif "; total" in lines:
                marker = False
            elif marker:
                lines = lines.split()[4]
                #lines = "_".join(itemgetter(4)(lines))
                itp_atom_num.append(lines)
    return itp_atom_num
a = itpReader(ref_itp)

def gro_to_change(query_gro):
    gro_dict = {}
    with open(query_gro) as gro_name:
        checker = False
        for linesX in gro_name:
            #print linesX.split()[2].strip().isdigit()
            if linesX.split()[2].strip().isdigit():
                checker = True
            elif '0.00000' in linesX:
                checker = False
            if checker:
                linesZ = linesX.split()[1]
                print linesZ
                #name = "_".join(itemgetter(1,2)(linesZ))
                name = linesZ
                print name
                print linesX
                gro_dict[name] = linesX.rstrip('\n')
    return gro_dict

b = gro_to_change(query_gro)
if b == {}:
    print "Dictionary is empty"
def write_gro(a,b):
    counter = 0
    with open("output.gro","w") as out:
        for i in a:
            counter+=1
            out.write(b[i][:16]+"{:4}".format(counter)+b[i][20:]+"\n")
    print("Modified gro file has been succesfully made!")

write_gro(a,b) 
