from abjad.tools import seqtools
from abjad.tools.pitchtools.MelodicChromaticIntervalSegment import MelodicChromaticIntervalSegment
from abjad.tools.pitchtools.list_named_chromatic_pitches_in_expr import list_named_chromatic_pitches_in_expr
from abjad.tools.pitchtools.calculate_melodic_chromatic_interval_from_pitch_carrier_to_pitch_carrier import calculate_melodic_chromatic_interval_from_pitch_carrier_to_pitch_carrier


def expr_to_melodic_chromatic_interval_segment(expr):
   '''.. versionadded:: 1.1.2

   Return melodic chromatic interval segment corresponding to
   arbitrary input `expr`.  ::

      abjad> staff = Staff(macros.scale(8))
      abjad> pitchtools.expr_to_melodic_chromatic_interval_segment(staff)
      MelodicChromaticIntervalSegment(+2, +2, +1, +2, +2, +2, +1)
   '''

   pitches = list_named_chromatic_pitches_in_expr(expr)
   mcis = [ ]
   for left, right in seqtools.iterate_sequence_pairwise_strict(pitches):
      mci = calculate_melodic_chromatic_interval_from_pitch_carrier_to_pitch_carrier(left, right)
      mcis.append(mci)

   return MelodicChromaticIntervalSegment(mcis)
