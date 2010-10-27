from abjad.tools import seqtools


def iterate_named_chromatic_pitch_pairs_forward_in_expr(expr):
   r'''.. versionadded:: 1.1.2

   Iterate left-to-right, top-to-bottom pitch pairs in `expr`. ::

      abjad> score = Score([ ])
      abjad> notes = macros.scale(4) + [Note(7, (1, 4))]
      abjad> score.append(Staff(notes))
      abjad> notes = [Note(x, (1, 4)) for x in [-12, -15, -17]]
      abjad> score.append(Staff(notes))
      abjad> contexttools.ClefMark('bass')(score[1])

   ::

      abjad> f(score)
      \new Score <<
              \new Staff {
                      c'8
                      d'8
                      e'8
                      f'8
                      g'4
              }
              \new Staff {
                      \clef "bass"
                      c4
                      a,4
                      g,4
              }
      >>

   ::

      abjad> for pair in pitchtools.iterate_named_chromatic_pitch_pairs_forward_in_expr(score):
      ...     pair
      ... 
      (NamedChromaticPitch(c, 4), NamedChromaticPitch(c, 3))
      (NamedChromaticPitch(c, 4), NamedChromaticPitch(d, 4))
      (NamedChromaticPitch(c, 3), NamedChromaticPitch(d, 4))
      (NamedChromaticPitch(d, 4), NamedChromaticPitch(e, 4))
      (NamedChromaticPitch(d, 4), NamedChromaticPitch(a, 2))
      (NamedChromaticPitch(c, 3), NamedChromaticPitch(e, 4))
      (NamedChromaticPitch(c, 3), NamedChromaticPitch(a, 2))
      (NamedChromaticPitch(e, 4), NamedChromaticPitch(a, 2))
      (NamedChromaticPitch(e, 4), NamedChromaticPitch(f, 4))
      (NamedChromaticPitch(a, 2), NamedChromaticPitch(f, 4))
      (NamedChromaticPitch(f, 4), NamedChromaticPitch(g, 4))
      (NamedChromaticPitch(f, 4), NamedChromaticPitch(g, 2))
      (NamedChromaticPitch(a, 2), NamedChromaticPitch(g, 4))
      (NamedChromaticPitch(a, 2), NamedChromaticPitch(g, 2))
      (NamedChromaticPitch(g, 4), NamedChromaticPitch(g, 2))

   Chords are handled correctly. ::

      abjad> chord_1 = Chord([0, 2, 4], (1, 4))
      abjad> chord_2 = Chord([17, 19], (1, 4))
      abjad> staff = Staff([chord_1, chord_2])

   ::

      abjad> f(staff)
      \new Staff {
              <c' d' e'>4
              <f'' g''>4
      }

   ::

      abjad> for pair in pitchtools.iterate_named_chromatic_pitch_pairs_forward_in_expr(staff):
      ...   print pair
      (NamedChromaticPitch(c, 4), NamedChromaticPitch(d, 4))
      (NamedChromaticPitch(c, 4), NamedChromaticPitch(e, 4))
      (NamedChromaticPitch(d, 4), NamedChromaticPitch(e, 4))
      (NamedChromaticPitch(c, 4), NamedChromaticPitch(f, 5))
      (NamedChromaticPitch(c, 4), NamedChromaticPitch(g, 5))
      (NamedChromaticPitch(d, 4), NamedChromaticPitch(f, 5))
      (NamedChromaticPitch(d, 4), NamedChromaticPitch(g, 5))
      (NamedChromaticPitch(e, 4), NamedChromaticPitch(f, 5))
      (NamedChromaticPitch(e, 4), NamedChromaticPitch(g, 5))
      (NamedChromaticPitch(f, 5), NamedChromaticPitch(g, 5))

   .. versionchanged:: 1.1.2
      renamed ``iterate.pitch_pairs_forward_in( )`` to
      ``pitchtools.iterate_named_chromatic_pitch_pairs_forward_in_expr( )``.

   .. versionchanged:: 1.1.2
      renamed ``iterate.pitch_pairs_forward_in_expr( )`` to
      ``pitchtools.iterate_named_chromatic_pitch_pairs_forward_in_expr( )``.

   .. versionchanged:: 1.1.2
      renamed ``pitchtools.iterate_pitch_pairs_forward_in_expr( )`` to
      ``pitchtools.iterate_named_chromatic_pitch_pairs_forward_in_expr( )``.
   '''
   from abjad.tools.leaftools.iterate_leaf_pairs_forward_in_expr import iterate_leaf_pairs_forward_in_expr

   from abjad.tools import pitchtools
   for leaf_pair in iterate_leaf_pairs_forward_in_expr(expr):
      leaf_pair_list = list(leaf_pair)
      ## iterate chord pitches if first leaf is chord
      for pair in pitchtools.list_unordered_named_chromatic_pitch_pairs_in_expr(leaf_pair_list[0]):
         yield pair
      if isinstance(leaf_pair, set):
         for pair in pitchtools.list_unordered_named_chromatic_pitch_pairs_in_expr(leaf_pair):
            yield pair
      elif isinstance(leaf_pair, tuple):
         for pair in pitchtools.list_ordered_named_chromatic_pitch_pairs_from_expr_1_to_expr_2(*leaf_pair):
            yield pair
      else:
         raise TypeError('leaf pair must be set or tuple.')
      ## iterate chord pitches if last leaf is chord
      for pair in pitchtools.list_unordered_named_chromatic_pitch_pairs_in_expr(leaf_pair_list[1]):
         yield pair
