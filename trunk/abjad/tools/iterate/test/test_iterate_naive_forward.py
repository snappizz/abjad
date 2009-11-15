from abjad import *
from abjad.component import _Component
from abjad.leaf import _Leaf
from abjad.tuplet import _Tuplet


def test_iterate_naive_forward_01( ):
   '''Yield nothing when class not present.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   iter = iterate.naive_forward(t, Rest)
   assert len(list(iter)) == 0


def test_iterate_naive_forward_02( ):
   '''Yield topmost node only.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   iter = iterate.naive_forward(t, Staff)
   assert len(list(iter)) == 1


def test_iterate_naive_forward_03( ):
   '''Yield internal nodes only.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   #from abjad.tuplet.tuplet import _Tuplet
   iter = iterate.naive_forward(t, _Tuplet)
   assert len(list(iter)) == 3


def test_iterate_naive_forward_04( ):
   '''Yield exact leaves.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   iter = iterate.naive_forward(t, Note)
   assert len(list(iter)) == 9


def test_iterate_naive_forward_05( ):
   '''Yield leaves based on names higher in inheritence hierarchy.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   #from abjad.leaf import _Leaf
   iter = iterate.naive_forward(t, _Leaf)
   assert len(list(iter)) == 9


def test_iterate_naive_forward_06( ):
   '''Yield all nodes in tree.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   #from abjad.component.component import _Component
   iter = iterate.naive_forward(t, _Component)
   assert len(list(iter)) == 13


def test_iterate_naive_forward_07( ):
   '''Yield all python objects.'''
   t = Staff(FixedDurationTuplet((2, 4), Note(0, (1, 4)) * 3) * 3)
   iter = iterate.naive_forward(t, object)
   assert len(list(iter)) == 13


def test_iterate_naive_forward_08( ):
   '''From start index.'''

   t = Staff(FixedDurationTuplet((2, 8), construct.run(3)) * 2)
   pitchtools.diatonicize(t)

   r'''
   \new Staff {
           \times 2/3 {
                   c'8
                   d'8
                   e'8
           }
           \times 2/3 {
                   f'8
                   g'8
                   a'8
           }
   }
   '''

   leaves = list(iterate.naive_forward(t, _Leaf, 3))

   assert leaves[0] is t.leaves[3]
   assert leaves[1] is t.leaves[4]
   assert leaves[2] is t.leaves[5]


def test_iterate_naive_forward_09( ):
   '''To stop index.'''

   t = Staff(FixedDurationTuplet((2, 8), construct.run(3)) * 2)
   pitchtools.diatonicize(t)

   r'''
   \new Staff {
           \times 2/3 {
                   c'8
                   d'8
                   e'8
           }
           \times 2/3 {
                   f'8
                   g'8
                   a'8
           }
   }
   '''

   leaves = list(iterate.naive_forward(t, _Leaf, 0, 3))

   assert leaves[0] is t.leaves[0]
   assert leaves[1] is t.leaves[1]
   assert leaves[2] is t.leaves[2]
   assert len(leaves) == 3


def test_iterate_naive_forward_10( ):
   '''From start index to stop index.'''

   t = Staff(FixedDurationTuplet((2, 8), construct.run(3)) * 2)
   pitchtools.diatonicize(t)

   r'''
   \new Staff {
           \times 2/3 {
                   c'8
                   d'8
                   e'8
           }
           \times 2/3 {
                   f'8
                   g'8
                   a'8
           }
   }
   '''

   leaves = list(iterate.naive_forward(t, _Leaf, 1, 5))

   assert leaves[0] is t.leaves[1]
   assert leaves[1] is t.leaves[2]
   assert leaves[2] is t.leaves[3]
   assert leaves[3] is t.leaves[4]
   assert len(leaves) == 4
