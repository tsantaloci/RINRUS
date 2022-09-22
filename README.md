# RINRUS

Residue Interaction Network-based ResidUe Selector (RINRUS) is a QM-cluster model building tool.  Starting from a raw PDB file, after running a series of preparation tasks, the tool will
- select important residues for chemical reactions, and
- generate trimmed PDB files with the corresponding quantum chemical inputs.

## Installation

Clone this repository, then add the library code under `lib3` to your `PYTHONPATH`. For example, in `~/git`:
``` bash
cd ~/git
git clone git@github.com:natedey/RINRUS.git
export PYTHONPATH="~/git/RINRUS/lib3:$PYTHONPATH"
```

### Python dependencies

- Python >= 3.x
- NumPy
- pymol
  - If installing via conda, it's under `-c conda-forge pymol-open-source`.
- openbabel (required for Arpeggio)

For certain scripts (optional),
- matplotlib
- BioPython

### External dependencies

- [probe](https://github.com/rlabduke/probe) - version 2.16.130520 is packaged with RINRUS
- [reduce](https://github.com/rlabduke/reduce) - version 3.23 is packaged with RINRUS
- [arpeggio](http://biosig.unimelb.edu.au/arpeggioweb)

Currently, a precompiled copy of each is present in `bin/`.

which require
- CMake >= 3.10
- Any C/C++ compiler suite with C++11 support

Currently, RINRUS can generate appropriate QM-cluster model input files for  
-Gaussian09/Gaussian16  
-the Gaussian-xTB wrapper developed by the Asparu-Guzik group (https://github.com/aspuru-guzik-group/xtb-gaussian)  
-Q-Chem 5.x/6.x  

TODO:  
-write QM/MM input files with RINRUS-designed QM regions  
-write I/FSAPT input files in PSI4 (scripts to process PSI4 FSAPT calculations and build QM-cluster models of enzymes with non-covalently bonded substrates are available)  
-write ORCA and TURBOMOLE QM-cluster model input files  
-automated network graph visualization of RINRUS models  

Current production-level use cases are described in `bin/` with tutorials in bin/README.md  
The first public release (version 0.2) includes examples 1 and 2 only! Examples 3 - 5 will be available soon.  

## Usage example 1 - generating a single or a few input files with probe interaction count ranking 

## Usage example 2 - generating a single or a few input files with distance-based ranking

## Usage example 3 - generating a single or a few input files with arpeggio interaction-type ranking

## Usage example 4 - generating a single or a few input files with manual ranking (from SAPT, ML, or from some scheme that doesn't yet interface with RINRUS automatically)

## GENERATE ALL THE THINGS!!! Combinatorial model building from arpeggio or probe
## Usage example 5a - Combinatorial model building from arpeggio
## Usage example 5b - Combinatorial model building from probe

## Contributors
This code has been developed by the [DeYonker group](https://www.memphis.edu/chem/faculty-deyonker/index.php) at the University of Memphis Department of Chemistry.  
Dr. Qianyi Cheng is the primary coder, assisted by Prof. Nathan DeYonker, Dr. Thomas Summers (University of Nevada-Reno), Donatus Agbaglo, Tejas Suhagia, and Dr. Eric Berquist (Q-Chem, Inc.)
