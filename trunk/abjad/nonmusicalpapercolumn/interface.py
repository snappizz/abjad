from abjad.core.grobhandler import _GrobHandler
from abjad.core.interface import _Interface


class NonMusicalPaperColumnInterface(_Interface, _GrobHandler):
   r'''.. versionadded:: 1.1.2.

   Handle the LilyPond NonMusicalPaperColumn grob. ::

      abjad> t = Score([Staff(construct.scale(4))])
      abjad> t.nonmusicalpapercolumn.line_break_permission = False
      abjad> t.nonmusicalpapercolumn.page_break_permission = False

   ::

      abjad> print t.format
      \new Score \with {
              \override NonMusicalPaperColumn #'line-break-permission = ##f
              \override NonMusicalPaperColumn #'page-break-permission = ##f
      } <<
              \new Staff {
                      c'8
                      d'8
                      e'8
                      f'8
              }
      >>
   '''

   def __init__(self, client):
      _Interface.__init__(self, client)
      _GrobHandler.__init__(self, 'NonMusicalPaperColumn')
