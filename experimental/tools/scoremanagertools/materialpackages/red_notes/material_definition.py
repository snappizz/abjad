# -*- encoding: utf-8 -*-
from abjad import *
output_material_module_import_statements = ['from abjad import *']


red_notes = scoretools.make_notes(6 * [2, 4, 5], [(1, 16), (1, 8)])
