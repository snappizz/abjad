from abjad import *


def test_seqtools_remove_consecutive_duplicates_from_sequence_01( ):

   l = [0, 0, 1, 1, 2, 2, 3, 4, 5, 5]
   t = list(seqtools.remove_consecutive_duplicates_from_sequence(l))
   
   assert t == [0, 1, 2, 3, 4, 5]


def test_seqtools_remove_consecutive_duplicates_from_sequence_02( ):

   l = [0, 0, 0, 0, 0, 0, 0]
   t = list(seqtools.remove_consecutive_duplicates_from_sequence(l))
   
   assert t == [0]
   

def test_seqtools_remove_consecutive_duplicates_from_sequence_03( ):
   '''Empty list and length-1 list boundary cases.'''

   assert list(seqtools.remove_consecutive_duplicates_from_sequence([ ])) == [ ]
   assert list(seqtools.remove_consecutive_duplicates_from_sequence([99])) == [99]
