from abjad.tools import scoretools
from experimental.tools.scoremanagertools.selectors.Selector import Selector


class ScoreToolsPerformerNameSelector(Selector):

    ### CLASS VARIABLES ###

    space_delimited_lowercase_target_name = 'performer'

    ### INITIALIZER ###

    def __init__(self, is_keyed=True, **kwargs):
        Selector.__init__(self, **kwargs)
        self.is_keyed = is_keyed

    ### PUBLIC METHODS ###

    def _make_main_menu(self, head=None):
        menu_tokens = self.make_menu_tokens(head=head)
        menu, menu_section = self._io.make_menu(where=self._where,
            is_keyed=self.is_keyed,
            is_numbered=self.is_numbered,
            is_ranged=self.is_ranged,
            menu_tokens=menu_tokens,
            return_value_attribute='body',
            )
        return menu

    def make_menu_tokens(self, head=None):
        performer_names, performer_abbreviations = [], []
        performer_pairs = scoretools.list_primary_performer_names()
        performer_pairs = [(x[1].split()[-1].strip('.'), x[0]) for x in performer_pairs]
        performer_pairs.append(('perc', 'percussionist'))
        performer_pairs.sort(lambda x, y: cmp(x[1], y[1]))
        return performer_pairs
