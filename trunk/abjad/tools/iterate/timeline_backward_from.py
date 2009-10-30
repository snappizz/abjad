from abjad.leaf.leaf import _Leaf
from abjad.tools.iterate.timeline_backward_in import timeline_backward_in as \
   iterate_timeline_backward_in


def timeline_backward_from(expr, klass = _Leaf):
   r'''.. versionadded:: 1.1.2

   Yield `klass` instances in score of `expr`, 
   sorted backward by score offset stop time,
   starting from `expr`. ::

      abjad> score = Score([ ])
      abjad> score.append(Staff(construct.run(4, Rational(1, 4))))
      abjad> score.append(Staff(construct.run(4)))
      abjad> pitchtools.diatonicize(score)
      abjad> f(score)
      \new Score <<
              \new Staff {
                      c'4
                      d'4
                      e'4
                      f'4
              }
              \new Staff {
                      g'8
                      a'8
                      b'8
                      c''8
              }
      >>
      abjad> for leaf in iterate.timeline_backward_from(score[1][2]):
      ...     leaf
      ... 
      Note(b', 8)
      Note(c', 4)
      Note(a', 8)
      Note(g', 8)

   .. todo:: optimize to avoid behind-the-scenes full-score traversal.
   '''

   root = expr.parentage.root
   component_generator = iterate_timeline_backward_in(root, klass = klass)

   yielded_expr = False
   for component in component_generator:
      if yielded_expr:
         yield component
      elif component is expr:
         yield component
         yielded_expr = True
