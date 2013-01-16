from abjad.tools import chordtools
from abjad.tools import leaftools
from abjad.tools import notetools
from abjad.tools.abctools import AbjadObject


class SelectMethodMixin(AbjadObject):
    '''Select-method mix-in.

        >>> from experimental import *

    ::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecification(score_template=score_template)
        >>> red_segment = score_specification.append_segment(name='red')

    Select-method mix-ins are immutable.
    '''
    
    ### PUBLIC METHODS ###

    def select_beats(self, voice_name, time_relation=None):
        '''Select voice ``1`` beats that start during segment ``'red'``::

            >>> selector = red_segment.select_beats('Voice 1')

        ::

            >>> z(selector)
            selectortools.BeatSelector(
                anchor='red',
                voice_name='Voice 1'
                )

        Return beat selector.
        '''
        from experimental.tools import selectortools
        selector = selectortools.BeatSelector(
            anchor=self._anchor_abbreviation,
            voice_name=voice_name,
            time_relation=time_relation
            )
        selector._score_specification = self.score_specification
        return selector

    def select_divisions(self, voice_name, time_relation=None):
        '''Select voice ``1`` divisions that start during segment ``'red'``::

            >>> selector = red_segment.select_divisions('Voice 1')

        ::
            
            >>> z(selector)
            selectortools.DivisionSelector(
                anchor='red',
                voice_name='Voice 1'
                )

        Return division selector.
        '''
        from experimental.tools import selectortools
        selector = selectortools.DivisionSelector(
            anchor=self._anchor_abbreviation,
            voice_name=voice_name,
            time_relation=time_relation
            )
        selector._score_specification = self.score_specification
        return selector

    def select_leaves(self, voice_name, time_relation=None):
        '''Select voice ``1`` leaves that start during segment ``'red'``::

            >>> selector = red_segment.select_leaves('Voice 1')

        ::

            >>> z(selector)
            selectortools.CounttimeComponentSelector(
                anchor='red',
                classes=settingtools.ClassInventory([
                    leaftools.Leaf
                    ]),
                voice_name='Voice 1'
                )

        Return counttime component selector.
        '''
        from experimental.tools import selectortools
        selector = selectortools.CounttimeComponentSelector(
            anchor=self._anchor_abbreviation,
            time_relation=time_relation, 
            classes=(leaftools.Leaf, ), 
            voice_name=voice_name
            )
        selector._score_specification = self.score_specification
        return selector

    def select_measures(self, voice_name, time_relation=None):
        '''Select voice ``1`` measures 
        that start during segment ``'red'``::

            >>> selector = red_segment.select_measures('Voice 1')

        ::

            >>> z(selector)
            selectortools.MeasureSelector(
                anchor='red',
                voice_name='Voice 1'
                )

        Return measure selector.
        '''
        from experimental.tools import selectortools
        selector = selectortools.MeasureSelector(
            anchor=self._anchor_abbreviation,
            voice_name=voice_name,
            time_relation=time_relation
            )
        selector._score_specification = self.score_specification
        return selector

    def select_notes_and_chords(self, voice_name, time_relation=None):
        '''Select voice ``1`` notes and chords that start during segment ``'red'``::

            >>> selector = red_segment.select_notes_and_chords('Voice 1')

        ::

            >>> z(selector)
            selectortools.CounttimeComponentSelector(
                anchor='red',
                classes=settingtools.ClassInventory([
                    notetools.Note,
                    chordtools.Chord
                    ]),
                voice_name='Voice 1'
                )

        Return counttime component selector.
        '''
        from experimental.tools import selectortools
        selector = selectortools.CounttimeComponentSelector(
            anchor=self._anchor_abbreviation,
            time_relation=time_relation, 
            classes=(notetools.Note, chordtools.Chord),
            voice_name=voice_name
            )
        selector._score_specification = self.score_specification
        return selector
