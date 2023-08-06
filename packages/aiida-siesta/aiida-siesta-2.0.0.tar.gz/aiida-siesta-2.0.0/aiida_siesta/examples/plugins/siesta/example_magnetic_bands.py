#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
import os.path as op
import sys

from aiida.engine import submit
from aiida.orm import load_code
from aiida.plugins import DataFactory
from aiida.tools import get_explicit_kpoints_path

from aiida_siesta.calculations.siesta import SiestaCalculation

# Calculation on Iron, collinear spin polarization applied

################################################################

PsfData = DataFactory('pseudo.psf')
Dict = DataFactory('core.dict')
KpointsData = DataFactory('core.array.kpoints')
StructureData = DataFactory('core.structure')

try:
    dontsend = sys.argv[1]
    if dontsend == "--dont-send":
        submit_test = True
    elif dontsend == "--send":
        submit_test = False
    else:
        raise IndexError
except IndexError:
    print >> sys.stderr, ("The first parameter can only be either "
                          "--send or --dont-send")
    sys.exit(1)

try:
    codename = sys.argv[2]
except IndexError:
    codename = 'Siesta4.0.1@kelvin'

#
#------------------Code and computer options ---------------------------
#
code = load_code(codename)

options = {
#    "queue_name": "debug",
    "max_wallclock_seconds": 1700,
    'withmpi': True,
    "resources": {
        "num_machines": 1,
        "num_mpiprocs_per_machine": 2,
    }
}

#
# Structure -----------------------------------------
#
# BCC
alat = 2.87 # angstrom
cell = [[alat/2, alat/2, alat/2,],
        [alat/2, -alat/2, alat/2,],
        [alat/2, alat/2, -alat/2,],
       ]

#
s = StructureData(cell=cell)
s.append_atom(position=(0.000,0.000,0.000),symbols=['Fe'])
seekpath_parameters = {'reference_distance': 0.04, 'symprec': 0.0001}
result = get_explicit_kpoints_path(s, **seekpath_parameters)
elements = list(s.get_symbols_set())
newstructure = result['primitive_structure']


# The parameters
params_dict= {
'xc-functional': 'GGA',
'xc-authors': 'PBE',
'spin-polarized': True,
'noncollinearspin': False,
'mesh-cutoff': '100.000 Ry',
'max-scfiterations': 40,
'dm-numberpulay': 4,
'dm-mixingweight': 0.1,
'dm-tolerance': 1.e-3,
'electronic-temperature': '300.000 K'
}
parameters = Dict(params_dict)

# The basis
basis_dict = {
    'pao-basistype': 'split',
    'pao-splitnorm': 0.150,
    'pao-energyshift': '0.020 Ry',
    '%block pao-basis-sizes': """
Fe    SZP
%endblock pao-basis-sizes""",
}
#
basis = Dict(basis_dict)


# K ponts mesh
kpoints = KpointsData()
kpoints_mesh = 6
kpoints.set_kpoints_mesh([kpoints_mesh,kpoints_mesh,kpoints_mesh])

# K points for bands
bandskpoints = KpointsData()
# Making use of SeeK-path for the automatic path
# The choice of the distance between kpoints is in the call seekpath_parameters
# All high symmetry points included, labels already included
bandskpoints = result['explicit_kpoints']

#
# Pseudopotentials ----------------------------------------------
#
# This exemplifies the handling of pseudos for different species
# Those sharing the same pseudo should be indicated.
#
pseudos_dict = {}
raw_pseudos = [("Fe.psf", ['Fe'])]
for fname, kinds in raw_pseudos:
    absname = op.realpath(op.join(op.dirname(__file__), "../../fixtures/sample_psf", fname))
    pseudo = PsfData.get_or_create(absname)
    if not pseudo.is_stored:
        print(f"\nCreated the pseudo for {kinds}")
    else:
        print(f"\nUsing the pseudo for {kinds} from DB: {pseudo.pk}")
    for j in kinds:
        pseudos_dict[j]=pseudo


#
#--All the inputs of a Siesta calculations are listed in a dictionary--
#
inputs = {
    'structure': newstructure,
    'parameters': parameters,
    'code': code,
    'basis': basis,
    'pseudos' : pseudos_dict,
    'kpoints' : kpoints,
    'bandskpoints' : bandskpoints,
    'metadata': {
        'options': options,
        'label': "BCC iron",
    }
}

if submit_test:
    inputs["metadata"]["dry_run"] = True
    inputs["metadata"]["store_provenance"] = False
    process = submit(SiestaCalculation, **inputs)
    print(f"Submited test for calculation (uuid='{process.uuid}')")
    print("Check the folder submit_test for the result of the test")

else:
    process = submit(SiestaCalculation, **inputs)
    print(f"Submitted calculation; ID={process.pk}")
    print(f"For information about this calculation type: verdi process show {process.pk}")
    print("For a list of running processes type: verdi process list")
