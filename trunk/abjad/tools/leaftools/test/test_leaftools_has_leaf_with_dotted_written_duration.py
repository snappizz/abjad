from abjad import *


def test_leaftools_has_leaf_with_dotted_written_duration_01( ):

   notes = construct.notes([0], [(1, 16), (2, 16), (3, 16)])
   assert leaftools.has_leaf_with_dotted_written_duration(notes)


def test_leaftools_has_leaf_with_dotted_written_duration_02( ):

   notes = construct.notes([0], [(1, 16), (2, 16), (4, 16)])
   assert not leaftools.has_leaf_with_dotted_written_duration(notes)


def test_leaftools_has_leaf_with_dotted_written_duration_03( ):
   '''Empty iterable boundary case.'''

   assert not leaftools.has_leaf_with_dotted_written_duration([ ])
