from abjad import *


def test_PitchArrayCell_matches_cell_01( ):

   array = pitchtools.PitchArray([[1, 2, 1], [2, 1, 1]])
   array[0].cells[0].pitches.append(Pitch(0))
   array[0].cells[1].pitches.extend([Pitch(2), Pitch(4)])

   '''
   [c'] [d' e'    ] [ ]
   [          ] [ ] [ ]
   '''

   assert array[0].cells[0].matches_cell(array[0].cells[0])
   assert not array[0].cells[0].matches_cell(array[0].cells[1])
   assert not array[0].cells[0].matches_cell(array[0].cells[2])
   assert not array[0].cells[0].matches_cell(array[1].cells[0])
   assert not array[0].cells[0].matches_cell(array[1].cells[1])
   assert not array[0].cells[0].matches_cell(array[1].cells[2])

   assert not array[0].cells[2].matches_cell(array[0].cells[0])
   assert not array[0].cells[2].matches_cell(array[0].cells[1])
   assert array[0].cells[2].matches_cell(array[0].cells[2])
   assert not array[0].cells[2].matches_cell(array[1].cells[0])
   assert array[0].cells[2].matches_cell(array[1].cells[1])
   assert array[0].cells[2].matches_cell(array[1].cells[2])
