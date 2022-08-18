"""
This is a program written by Qianyi Cheng in DeYonker Research Group
at University of Memphis.
"""

#res_atoms_all = {
#'ALA': ['N', 'CA', 'C', 'O', 'CB', 'H', 'HA', '1HB', '2HB', '3HB'],
#'ARG': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'NE', 'CZ', 'NH1', 'NH2', 'H', 'HA', '2HB', '3HB', '2HG', '3HG', '2HD', '3HD', 'HE', '1HH1', '2HH1', '1HH2', '2HH2'],
#'ASN': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'ND2', 'OD1', 'H', 'HA', '2HB', '3HB', '1HD2', '2HD2'],
#'ASP': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'OD1', 'OD2', 'H', 'HA', '2HB', '3HB'],
#'CYS': ['N', 'CA', 'C', 'O', 'CB', 'SG', 'H', 'HA', '2HB', '3HB', 'HG'],
#'GLN': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'NE2', 'OE1', 'H', 'HA', '2HB', '3HB', '2HG', '3HG', '1HE2', '2HE2'],
#'GLU': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'OE1', 'OE2', 'H', 'HA', '2HB', '3HB', '2HG', '3HG'],
#'GLY': ['N', 'CA', 'C', 'O', 'H', '3HA', 'HA'],
#'HIS': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'H', 'HA', '2HB', '3HB', '2HD', '1HE', '2HE'],
#'ILE': ['N', 'CA', 'C', 'O', 'CB', 'CG1', 'CG2', 'CD1', 'H', 'HA', 'HB', '2HG1', '3HG1', '1HG2', '2HG2', '3HG2', '1HD1', '2HD1', '3HD1'],
#'LEU': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'H', 'HA', '2HB', '3HB', 'HG', '1HD1', '2HD1', '3HD1', '1HD2', '2HD2', '3HD2'],
#'LYS': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'CE', 'NZ', 'H', 'HA', '2HB', '3HB', '2HG', '3HG', '2HD', '3HD', '2HE', '3HE', '1HZ', '2HZ', '3HZ'],
#'MET': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'SD', 'CE', 'H', 'HA', '2HB', '3HB', '2HG', '3HG', '1HE', '2HE', '3HE'],
#'PHE': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'H', 'HA', '2HB', '3HB', '1HD', '2HD', '1HE', '2HE', 'HZ'],
#'PRO': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'HA', '2HB', '3HB', '2HG', '3HG', '2HD', '3HD'],
#'SER': ['N', 'CA', 'C', 'O', 'CB', 'OG', 'H', 'HA', '2HB', '3HB', 'HG'],
#'THR': ['N', 'CA', 'C', 'O', 'CB', 'CG2', 'OG1', 'H', 'HA', 'HB', '1HG', '1HG2', '2HG2', '3HG2'],
#'TRP': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE2', 'CE3', 'NE1', 'CZ2', 'CZ3', 'CH2', 'H', 'HA', '2HB', '3HB', '1HD', '1HE', '3HE', '2HZ', '3HZ', '2HH'],
#'TYR': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH', 'H', 'HA', '2HB', '3HB', '1HD', '2HD', '1HE', '2HE', 'HH'],
#'VAL': ['N', 'CA', 'C', 'O', 'CB', 'CG1', 'CG2', 'H', 'HA', 'HB', '1HG1', '2HG1', '3HG1', '1HG2', '2HG2', '3HG2']
#}
#
#res_atoms_sc = {
#'ALA': ['CB', '1HB', '2HB', '3HB'],
#'ARG': ['CB', 'CG', 'CD', 'NE', 'CZ', 'NH1', 'NH2', '2HB', '3HB', '2HG', '3HG', '2HD', '3HD', 'HE', '1HH1', '2HH1', '1HH2', '2HH2'],
#'ASN': ['CB', 'CG', 'ND2', 'OD1', '2HB', '3HB', '1HD2', '2HD2'],
#'ASP': ['CB', 'CG', 'OD1', 'OD2', '2HB', '3HB'],
#'CYS': ['CB', 'SG', '2HB', '3HB', 'HG'],
#'GLN': ['CB', 'CG', 'CD', 'NE2', 'OE1', '2HB', '3HB', '2HG', '3HG', '1HE2', '2HE2'],
#'GLU': ['CB', 'CG', 'CD', 'OE1', 'OE2', '2HB', '3HB', '2HG', '3HG'],
#'GLY': [],
#'HIS': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', '2HB', '3HB', '2HD', '1HE', '2HE'],
#'ILE': ['CB', 'CG1', 'CG2', 'CD1', 'HB', '2HG1', '3HG1', '1HG2', '2HG2', '3HG2', '1HD1', '2HD1', '3HD1'],
#'LEU': ['CB', 'CG', 'CD1', 'CD2', '2HB', '3HB', 'HG', '1HD1', '2HD1', '3HD1', '1HD2', '2HD2', '3HD2'],
#'LYS': ['CB', 'CG', 'CD', 'CE', 'NZ', '2HB', '3HB', '2HG', '3HG', '2HD', '3HD', '2HE', '3HE', '1HZ', '2HZ', '3HZ'],
#'MET': ['CB', 'CG', 'SD', 'CE', '2HB', '3HB', '2HG', '3HG', '1HE', '2HE', '3HE'],
#'PHE': ['CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', '2HB', '3HB', '1HD', '2HD', '1HE', '2HE', 'HZ'],
#'PRO': ['CB', 'CG', 'CD', '2HB', '3HB', '2HG', '3HG', '2HD', '3HD'],
#'SER': ['CB', 'OG', '2HB', '3HB', 'HG'],
#'THR': ['CB', 'CG2', 'OG1', 'HB', '1HG', '1HG2', '2HG2', '3HG2'],
#'TRP': ['CB', 'CG', 'CD1', 'CD2', 'CE2', 'CE3', 'NE1', 'CZ2', 'CZ3', 'CH2', '2HB', '3HB', '1HD', '1HE', '3HE', '2HZ', '3HZ', '2HH'],
#'TYR': ['CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH', '2HB', '3HB', '1HD', '2HD', '1HE', '2HE', 'HH'],
#'VAL': ['CB', 'CG1', 'CG2', 'HB', '1HG1', '2HG1', '3HG1', '1HG2', '2HG2', '3HG2']
#}


res_atoms_all = {
'ALA': ['N', 'CA', 'C', 'O', 'CB', 'H', 'HA', 'HB1', 'HB2', 'HB3'],
'ARG': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'NE', 'CZ', 'NH1', 'NH2', 'H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3', 'HE', 'HH11', 'HH12', 'HH21', 'HH22'],
'ASN': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'ND2', 'OD1', 'H', 'HA', 'HB2', 'HB3', 'HD21', 'HD22'],
'ASP': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'OD1', 'OD2', 'H', 'HA', 'HB2', 'HB3'],
'ASH': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'OD1', 'OD2', 'H', 'HA', 'HB2', 'HB3', 'HD2'],
'CYS': ['N', 'CA', 'C', 'O', 'CB', 'SG', 'H', 'HA', 'HB2', 'HB3', 'HG'],
'GLN': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'NE2', 'OE1', 'H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HE21', 'HE22'],
'GLH': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'NE2', 'OE1', 'OE2','H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HE21', 'HE22'],
'GLU': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'OE1', 'OE2', 'H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3'],
'GLY': ['N', 'CA', 'C', 'O', 'H', 'HA3', 'HA'],
'HIS': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'H', 'HA', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2','HD1'],
'HIP': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'H', 'HA', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2','HD1'],
'HID': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'H', 'HA', 'HB2', 'HB3', 'HD2', 'HE1', 'HD1'],
'HIE': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'H', 'HA', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2'],
'ILE': ['N', 'CA', 'C', 'O', 'CB', 'CG1', 'CG2', 'CD1', 'H', 'HA', 'HB', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23', 'HD11', 'HD12', 'HD13'],
'LEU': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'H', 'HA', 'HB2', 'HB3', 'HG', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23'],
'LYS': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'CE', 'NZ', 'H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3', 'HE2', 'HE3', 'HZ1', 'HZ2', 'HZ3'],
'MET': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'SD', 'CE', 'H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HE1', 'HE2', 'HE3'],
'MSE': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'SE', 'CE', 'H', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HE1', 'HE2', 'HE3'],
'PHE': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'H', 'HA', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2', 'HZ'],
'PRO': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'HA', 'HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3'],
'SER': ['N', 'CA', 'C', 'O', 'CB', 'OG', 'H', 'HA', 'HB2', 'HB3', 'HG'],
'THR': ['N', 'CA', 'C', 'O', 'CB', 'CG2', 'OG1', 'H', 'HA', 'HB', 'HG1', 'HG21', 'HG22', 'HG23'],
'TRP': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE2', 'CE3', 'NE1', 'CZ2', 'CZ3', 'CH2', 'H', 'HA', 'HB2', 'HB3', 'HD1', 'HE1', 'HE3', 'HZ2', 'HZ3', 'HH2'],
'TYR': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH', 'H', 'HA', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2', 'HH'],
'VAL': ['N', 'CA', 'C', 'O', 'CB', 'CG1', 'CG2', 'H', 'HA', 'HB', 'HG11', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23']
}


res_atoms_sc = {
'ALA': ['CB', 'HB1', 'HB2', 'HB3'],
'ARG': ['CB', 'CG', 'CD', 'NE', 'CZ', 'NH1', 'NH2', 'HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3', 'HE', 'HH11', 'HH12', 'HH21', 'HH22'],
'ASN': ['CB', 'CG', 'ND2', 'OD1', 'HB2', 'HB3', 'HD21', 'HD22'],
'ASP': ['CB', 'CG', 'OD1', 'OD2', 'HB2', 'HB3'],
'ASH': ['CB', 'CG', 'OD1', 'OD2', 'HB2', 'HB3', 'HD2'],
'CYS': ['CB', 'SG', 'HB2', 'HB3', 'HG'],
'GLN': ['CB', 'CG', 'CD', 'NE2', 'OE1', 'HB2', 'HB3', 'HG2', 'HG3', 'HE21', 'HE22'],
'GLH': ['CB', 'CG', 'CD', 'NE2', 'OE1', 'OE2','HB2', 'HB3', 'HG2', 'HG3', 'HE21', 'HE22'],
'GLU': ['CB', 'CG', 'CD', 'OE1', 'OE2', 'HB2', 'HB3', 'HG2', 'HG3'],
'GLY': [],
'HIS': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2','HD1'],
'HIP': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2','HD1'],
'HID': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'HB2', 'HB3', 'HD2', 'HE1', 'HD1'],
'HSD': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'HB2', 'HB3', 'HD2', 'HE1', 'HD1','HB1'], #in charmm
'HIE': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2'],
'HSE': ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2', 'HB2', 'HB3', 'HD2', 'HE1', 'HE2','HB1'], #in charmm
'ILE': ['CB', 'CG1', 'CG2', 'CD1', 'HB', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23', 'HD11', 'HD12', 'HD13'],
'LEU': ['CB', 'CG', 'CD1', 'CD2', 'HB2', 'HB3', 'HG', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23','HB1'],
'LYS': ['CB', 'CG', 'CD', 'CE', 'NZ', 'HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3', 'HE2', 'HE3', 'HZ1', 'HZ2', 'HZ3'],
'MET': ['CB', 'CG', 'SD', 'CE', 'HB2', 'HB3', 'HG2', 'HG3', 'HE1', 'HE2', 'HE3'],
'MSE': ['CB', 'CG', 'SE', 'CE', 'HB2', 'HB3', 'HG2', 'HG3', 'HE1', 'HE2', 'HE3'],
'PHE': ['CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2', 'HZ'],
'PRO': ['CB', 'CG', 'CD', 'HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3'],
'SER': ['CB', 'OG', 'HB2', 'HB3', 'HG'],
'THR': ['CB', 'CG2', 'OG1', 'HB', 'HG1', 'HG21', 'HG22', 'HG23'],
'TRP': ['CB', 'CG', 'CD1', 'CD2', 'CE2', 'CE3', 'NE1', 'CZ2', 'CZ3', 'CH2', 'HB2', 'HB3', 'HD1', 'HE1', 'HE3', 'HZ2', 'HZ3', 'HH2'],
'TYR': ['CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2', 'HH'],
'VAL': ['CB', 'CG1', 'CG2', 'HB', 'HG11', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23']
}
