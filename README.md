# BioToolBox
Codes for BioChemist

DESCRIPTION for "itp_atom_num_gro.py"
=====================================
"""
This python script rearranges atom number, atom name and atom coordinates of gro file based on itp file and outputs new gro file named as output.gro.

This script is able to solve the issue of non-matching atoms during MD Simulations of protein-ligand system in GROMACS for small moleucles/ligands.

Most of topologies (itp files) and gromacs coordinates(gro files) for these ligands ar either obtained from PRODRG Server or ATB Server.
These gro files are little optimized to generate topolgies and thus atom numbers, atom names and atomic coordinates are rearranged than required.


Mandatory:
The users should provide gro file in this format:
1. The coordinates should start from first line itself in the gro file
For example:
  565ABC     XX    1  10.859  10.571   2.902
2. The last line of coordinates should be contain this line (Add this line at the end of gro file):
     0.00000   0.00000   0.00000
"""

=====================================

USAGES for "itp_atom_num_gro.py":
=================================

[INPUT]:
1. itp filename
2. gro filename

[HOW TO RUN]:
python itp_atom_num_gro.py itp_filename gro_file_name

[OUTPUT]:
output.gro
