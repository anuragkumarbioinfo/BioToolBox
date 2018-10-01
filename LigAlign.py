#a = '  1 4 36.911000 38.936000 41.020000 2 X 14 0.57417 0.57417 "PYL " " C17" 6 0 -1 0.574174665665314 1 4 1'

import sys
comp_pqr_file = sys.argv[-2]
qm_mae_file = sys.argv[-1]

def split2(a):
    d = []
    z = a.split('"')
    for i in range(len(z)):
        m = z[i].split()
        d.append(m)
    x = []
    for i in d:
        for j in i:
                x.append(j)
    return x
    
#print split2(a)


read_key = "m_atom["
start_read = ":::"

BLOCK = False
KEY = False
READ = False

keys = []
complete_block = {}

with open(qm_mae_file) as mae:
    for lines in mae:
        if read_key in lines:
            BLOCK = True
            KEY = True
            READ = False
        
        elif BLOCK == True and KEY == True and READ == False and start_read not in lines:
            keys.append(lines.strip())
            #print "Read key: ", lines.strip()
        elif BLOCK == True and KEY == True and READ == False and start_read in lines:
            BLOCK = True
            KEY = True
            READ = True
        
        elif BLOCK == True and KEY == True and READ == True and start_read not in lines:
            tmp = {}
            x = split2(lines)
            #print "Number of Keys found: ", len(keys)
            #print "Number of line found: ", len(x)
            #print keys
            #print x
            for n, i in enumerate(x):
                tmp[keys[n]] = i
            complete_block[tmp[keys[0]]] = tmp
        
        elif BLOCK == True and KEY == True and READ == True and start_read in lines:
            BLOCK = False
            KEY   = False
            READ  = False

#for key in complete_block:
#    print key
#    print complete_block[key].

qm_new_Charges = {}

for key in complete_block:
    charge = 'r_j_ESP_Charges'
    aname = 's_m_pdb_atom_name'
    rname = 's_m_pdb_residue_name'
    rnum = 'i_m_residue_number'
    new_key = "{}_{}_{}".format(complete_block[key][aname],complete_block[key][rname],complete_block[key][rnum])
    if new_key not in qm_new_Charges: 
        qm_new_Charges[new_key] = float(complete_block[key][charge])

print qm_new_Charges.keys()


#charge_format
cf = "{:6.2f}"
exclude = ["CA", "C", "HA", "O", "N"]
with open("X"+comp_pqr_file, "wb") as output:
    with open(comp_pqr_file) as mm:
        for lines in mm:
            l = lines.split()
            if "ATOM" in lines:
                if l[2] not in exclude:
                    name = "{}_{}_{}".format(l[2],l[3],l[4])
                    if name in qm_new_Charges:
                        mmChar = cf.format(float(l[-3]))
                        qmChar = cf.format(qm_new_Charges[name])
                        print name, mmChar, qmChar
                        lines = lines.replace(mmChar, qmChar)
                        #print "To be replace [{}]: MM = {} QM = {}".format(name, mmChar, qmChar)
                #else: print lines
            output.write(lines)

