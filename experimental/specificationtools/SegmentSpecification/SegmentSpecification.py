from abjad.tools import *
from experimental.specificationtools.exceptions import *
from experimental.specificationtools.AttributeRetrievalIndicator import AttributeRetrievalIndicator
from experimental.specificationtools.AttributeRetrievalRequest import AttributeRetrievalRequest
from experimental.specificationtools.Callback import Callback
from experimental.specificationtools.HandlerRequest import HandlerRequest
from experimental.specificationtools.Specification import Specification
from experimental.specificationtools.StatalServer import StatalServer
from experimental.specificationtools.StatalServerRequest import StatalServerRequest
from experimental.handlertools.Handler import Handler
import copy


class SegmentSpecification(Specification):
    r'''.. versionadded:: 1.0

    ::

        >>> from abjad.tools import scoretemplatetools
        >>> from experimental import specificationtools
        >>> from experimental.specificationtools import ScoreSpecification

    The examples below reference the following segment specification::

        >>> template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(n=1)
        >>> specification = specificationtools.ScoreSpecification(score_template=template)
        
    ::
    
        >>> segment = specification.append_segment('red')

    ::
            
        >>> segment
        SegmentSpecification('red')

    ``SegmentSpecification`` properties are read-only.
    '''

    ### INITIALIZER ###

    def __init__(self, score_template, name):
        from experimental import settingtools
        assert isinstance(name, str), name
        Specification.__init__(self, score_template)
        self._score_model = self.score_template()
        self._name = name
        self._directives = settingtools.SettingInventory()

    ### SPECIAL METHODS ###

    def __getitem__(self, expr):
        if isinstance(expr, int):
            return self.directives.__getitem__(expr)
        else:
            return self.payload_context_dictionary.__getitem__(expr) 
        
    def __repr__(self):
        return '{}({!r})'.format(self._class_name, self.name)

    ### READ-ONLY PUBLIC ATTRIBUTES ###

    @property
    def directives(self):
        '''Segment specification directives.

            >>> segment.directives
            SettingInventory([])

        Return directive inventory.
        '''
        return self._directives

    @property
    def duration(self):
        '''Segment specification duration.

            >>> segment.duration is None
            True

        Derived during interpretation.

        Return rational or none.
        '''
        if self.time_signatures is not None:
            return sum([durationtools.Duration(x) for x in self.time_signatures])        

    @property
    def name(self):
        '''Segment name.

            >>> segment.name
            'red'

        Return string.
        '''
        return self._name

    @property
    def score_model(self):
        '''Segment score model specified by user.

            >>> segment.score_model
            Score-"Grouped Rhythmic Staves Score"<<1>>

        Return Abjad score object.
        '''
        return self._score_model

    @property
    def selector(self):
        '''Segment selector::

            >>> segment.selector
            SegmentSelector(index='red')

        Return segment selector.
        '''
        from experimental import selectortools
        return selectortools.SegmentSelector(index=self.name)
        
    @property
    def start(self):
        '''Segment start.

            >>> segment.start
            Timepoint(anchor=SegmentSelector(index='red'), edge=Left)

        Return timepoint.
        '''
        from experimental import timespantools
        return timespantools.Timepoint(anchor=self.selector, edge=Left)

    @property
    def stop(self):
        '''Segment stop.

            >>> segment.stop
            Timepoint(anchor=SegmentSelector(index='red'), edge=Right)

        Return timepoint.
        '''
        from experimental import timespantools
        return timespantools.Timepoint(anchor=self.selector, edge=Right)

    @property
    def time_signatures(self):
        '''Segment time signatures::

            >>> segment.time_signatures is None
            True

        Derived during interpretation.

        Return list or none.
        '''
        try:
            setting = self.resolved_settings_context_dictionary.score_context_proxy.get_setting(
                attribute='time_signatures')
        except MissingContextSettingError:
            return None
        assert isinstance(setting.value, list), setting.value
        return setting.value

    @property
    def timespan(self):
        '''Segment timespan.

            >>> segment.timespan
            SingleSourceTimespan(selector=SegmentSelector(index='red'))

        Return timespan.
        '''
        from experimental import timespantools
        return timespantools.SingleSourceTimespan(selector=self.selector)

    ### PUBLIC METHODS ###

    def add_time_signatures(self, score):
        time_signatures = self.time_signatures
        if self.time_signatures is not None:
            measures = measuretools.make_measures_with_full_measure_spacer_skips(time_signatures)
            context = componenttools.get_first_component_in_expr_with_name(score, 'TimeSignatureContext')
            context.extend(measures)

    def annotate_source(self, source, callback=None, count=None, offset=None):
        from experimental import selectortools
        assert isinstance(callback, (Callback, type(None))), callback
        assert isinstance(count, (int, type(None))), count
        assert isinstance(offset, (int, type(None))), offset
        if isinstance(source, StatalServer):
            if count is not None or offset is not None:
                source = StatalServerRequest(source, count=count, offset=offset)
        elif isinstance(source, Handler):
            if offset is not None:
                assert count is None
                source = HandlerRequest(source, offset=offset)
        elif isinstance(source, AttributeRetrievalIndicator):
            if any([x is not None for x in (callback, count, offset)]):
                source = AttributeRetrievalRequest(source, callback=callback, count=count, offset=offset)
        elif isinstance(source, selectortools.SingleContextDivisionSliceSelector):
            if any([x is not None for x in (callback, count, offset)]):
                source = copy.copy(source)
                source.callback = callback
                source.count = count
                source.offset = offset
        elif any([x is not None for x in (callback, count, offset)]):
            raise ValueError("'callback', 'count' or 'offset' set on nonstatal source: {!r}.".format(source))
        return source

    def get_directives(self, target=None, attribute=None):
        result = []
        for directive in self.directives:
            if target is None or directive.target == target:
                if attribute is None or directive.attribute == attribute:
                    result.append(directive)
        return result

    def get_divisions_value_with_fresh_and_truncate(self, context_name, timespan=None):
        '''Return value found in context tree or else default to segment time signatures.
        '''
        value, fresh, truncate = self.get_resolved_value_with_fresh('divisions', context_name, 
            include_truncate=True, timespan=timespan)
        if value is None:
            value, fresh = self.get_resolved_value_with_fresh('time_signatures', context_name, 
            timespan=timespan)
            truncate = False
        return value, fresh, truncate

    def get_resolved_value_with_fresh(self, attribute, context_name, include_truncate=False, timespan=None):
        '''Return value from resolved setting because context proxy stores resolved settings.
        '''
        from experimental import settingtools
        #self._debug((attribute, context_name))
        context = componenttools.get_first_component_in_expr_with_name(self.score_model, context_name)
        for component in componenttools.get_improper_parentage_of_component(context):
            #self._debug(component)
            context_proxy = self.resolved_settings_context_dictionary[component.name]
            settings = context_proxy.get_settings(attribute=attribute, timespan=timespan)
            #self._debug(settings, 'settings')
            if not settings:
                continue
            elif len(settings) == 1:
                setting = settings[0]
                assert isinstance(setting, settingtools.ResolvedContextSetting)
                if include_truncate:
                    return setting.value, setting.fresh, setting.truncate
                else:
                    return setting.value, setting.fresh
            else:
                raise Exception('multiple {!r} settings found.'.format(attribute))
        if include_truncate:
            return None, None, False
        else:
            return None, None
    
    def get_rhythm_value(self, context_name, timespan=None):
        '''Default to rest-filled tokens if explicit rhythm not found.
        '''
        from experimental.specificationtools import library
        value, fresh = self.get_resolved_value_with_fresh('rhythm', context_name, timespan=timespan)
        if value is not None:
            return value, fresh
        return library.rest_filled_tokens, True

    def retrieve_attribute(self, attribute, **kwargs):
        return Specification.retrieve_attribute(self, attribute, self.name, **kwargs)

    def retrieve_resolved_value(self, attribute, **kwargs):
        return Specification.retrieve_resolved_value(self, attribute, self.name, **kwargs)

    def select_background_measures(self, start=None, stop=None):
        '''Select the first five background measures that start during segment::

            >>> selector = segment.select_background_measures(stop=5)

        ::

            >>> z(selector)
            selectortools.BackgroundMeasureSliceSelector(
                inequality=timespantools.TimespanInequality(
                    timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                    timespantools.SingleSourceTimespan(
                        selector=selectortools.SegmentSelector(
                            index='red'
                            )
                        )
                    ),
                stop=5
                )

        Return selector.
        '''
        from experimental import selectortools
        from experimental import timespantools
        inequality = timespantools.expr_starts_during_timespan(self.timespan)
        selector = selectortools.BackgroundMeasureSliceSelector(inequality=inequality, start=start, stop=stop)
        return selector
    
    def select_divisions(self, contexts=None, start=None, stop=None):
        '''Select the first five divisions that start during segment::

            >>> contexts = ['Voice 1', 'Voice 3']
            >>> selector = segment.select_divisions(contexts=contexts, stop=5)

        ::
            
            >>> z(selector)
            selectortools.MultipleContextDivisionSliceSelector(
                contexts=['Voice 1', 'Voice 3'],
                inequality=timespantools.TimespanInequality(
                    timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                    timespantools.SingleSourceTimespan(
                        selector=selectortools.SegmentSelector(
                            index='red'
                            )
                        )
                    ),
                stop=5
                )

        Return selector.
        '''
        from experimental import selectortools
        from experimental import timespantools
        inequality = timespantools.expr_starts_during_timespan(self.timespan)
        selector = selectortools.MultipleContextDivisionSliceSelector(
            contexts=contexts, inequality=inequality, start=start, stop=stop)
        return selector

    def select_duration_ratio(self, ratio, index, contexts=None):
        '''Select the last third of the timespan of segment::

            >>> selector = segment.select_duration_ratio((1, 1, 1), -1, contexts=['Voice 1', 'Voice 3'])

        ::

            >>> z(selector)
            selectortools.DurationRatioItemSelector(
                selectortools.MultipleContextTimespanSelector(
                    contexts=['Voice 1', 'Voice 3'],
                    timespan=timespantools.SingleSourceTimespan(
                        selector=selectortools.SegmentSelector(
                            index='red'
                            )
                        )
                    ),
                mathtools.Ratio(1, 1, 1),
                index=-1
                )

        Return selector.
        '''
        from experimental import selectortools
        selector = selectortools.MultipleContextTimespanSelector(contexts=contexts, timespan=self.timespan)
        selector = selectortools.DurationRatioItemSelector(selector, ratio, index)
        return selector

    def select_leaves(self, contexts=None, start=None, stop=None):
        '''Select the first ``40`` leaves that start during segment::

            >>> contexts = ['Voice 1', 'Voice 3']
            >>> selector = segment.select_leaves(contexts=contexts, stop=40)

        ::

            >>> z(selector)
            selectortools.MultipleContextCounttimeComponentSliceSelector(
                contexts=['Voice 1', 'Voice 3'],
                inequality=timespantools.TimespanInequality(
                    timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                    timespantools.SingleSourceTimespan(
                        selector=selectortools.SegmentSelector(
                            index='red'
                            )
                        )
                    ),
                klass=leaftools.Leaf,
                stop=40
                )

        Return selector.
        '''
        from experimental import selectortools
        from experimental import timespantools
        inequality = timespantools.expr_starts_during_timespan(self.timespan)
        selector = selectortools.MultipleContextCounttimeComponentSliceSelector(
            contexts=contexts, inequality=inequality, klass=leaftools.Leaf, 
            start=start, stop=stop)
        return selector

    def select_notes_and_chords(self, contexts=None, start=None, stop=None):
        '''Select the first ``40`` notes and chords that start during segment.
        Do this for ``'Voice 1'`` and ``'Voice 3'``::

            >>> contexts = ['Voice 1', 'Voice 3']
            >>> selector = segment.select_notes_and_chords(contexts=contexts, stop=40)

        ::

            >>> z(selector)
            selectortools.MultipleContextCounttimeComponentSliceSelector(
                contexts=['Voice 1', 'Voice 3'],
                inequality=timespantools.TimespanInequality(
                    timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                    timespantools.SingleSourceTimespan(
                        selector=selectortools.SegmentSelector(
                            index='red'
                            )
                        )
                    ),
                klass=selectortools.KlassInventory([
                    notetools.Note,
                    chordtools.Chord
                    ]),
                stop=40
                )

        Return selector.
        '''
        from experimental import selectortools
        from experimental import timespantools
        inequality = timespantools.expr_starts_during_timespan(self.timespan)
        selector = selectortools.MultipleContextCounttimeComponentSliceSelector(
            contexts=contexts, inequality=inequality, klass=(notetools.Note, chordtools.Chord),
            start=start, stop=stop)
        return selector

    def select_ratio_of_background_measures(self, ratio, index=0, count=True):
        r'''Select the first third of background measures starting during segment::

            >>> selector = segment.select_ratio_of_background_measures((1, 1, 1), 0)

        ::

            >>> z(selector)
            selectortools.CountRatioItemSelector(
                selectortools.BackgroundMeasureSliceSelector(
                    inequality=timespantools.TimespanInequality(
                        timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                        timespantools.SingleSourceTimespan(
                            selector=selectortools.SegmentSelector(
                                index='red'
                                )
                            )
                        )
                    ),
                mathtools.Ratio(1, 1, 1),
                index=0
                )

        Return selector.
        '''
        from experimental import selectortools
        selector = self.select_background_measures()
        if count:
            selector = selectortools.CountRatioItemSelector(selector, ratio, index=index)
        else:
            selector = selectortools.DurationRatioItemSelector(selector, ratio, index=index)
        return selector

    def select_ratio_of_divisions(self, ratio, index, contexts=None, count=True):
        r'''Select the first third of divisions starting during segment::

            >>> selector = segment.select_ratio_of_divisions((1, 1, 1), 0, contexts=['Voice 1', 'Voice 3'])

        ::

            >>> z(selector)
            selectortools.CountRatioItemSelector(
                selectortools.MultipleContextDivisionSliceSelector(
                    contexts=['Voice 1', 'Voice 3'],
                    inequality=timespantools.TimespanInequality(
                        timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                        timespantools.SingleSourceTimespan(
                            selector=selectortools.SegmentSelector(
                                index='red'
                                )
                            )
                        )
                    ),
                mathtools.Ratio(1, 1, 1),
                index=0
                )

        Return selector.
        '''
        from experimental import selectortools
        selector = self.select_divisions(contexts=contexts)
        if count:
            selector = selectortools.CountRatioItemSelector(selector, ratio, index=index)
        else:
            selector = selectortools.DurationRatioItemSelector(selector, ratio, index=index)
        return selector

    def select_ratio_of_leaves(self, ratio, index, contexts=None, count=True):
        r'''Select the first third of leaves starting during segment::

            >>> selector = segment.select_ratio_of_leaves((1, 1, 1), 0, contexts=['Voice 1', 'Voice 3'])

        ::

            >>> z(selector)
            selectortools.CountRatioItemSelector(
                selectortools.MultipleContextCounttimeComponentSliceSelector(
                    contexts=['Voice 1', 'Voice 3'],
                    inequality=timespantools.TimespanInequality(
                        timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                        timespantools.SingleSourceTimespan(
                            selector=selectortools.SegmentSelector(
                                index='red'
                                )
                            )
                        ),
                    klass=leaftools.Leaf
                    ),
                mathtools.Ratio(1, 1, 1),
                index=0
                )

        Return selector.
        '''
        from experimental import selectortools
        selector = self.select_leaves(contexts=contexts)
        if count:
            selector = selectortools.CountRatioItemSelector(selector, ratio, index=index)
        else:
            selector = selectortools.DurationRatioItemSelector(selector, ratio, index=index)
        return selector

    def select_ratio_of_notes_and_chords(self, ratio, index, contexts=None, count=True):
        r'''Select the first third of notes and chords starting during segment::

            >>> selector = segment.select_ratio_of_notes_and_chords((1, 1, 1), 0, contexts=['Voice 1', 'Voice 3'])

        ::

            >>> z(selector)
            selectortools.CountRatioItemSelector(
                selectortools.MultipleContextCounttimeComponentSliceSelector(
                    contexts=['Voice 1', 'Voice 3'],
                    inequality=timespantools.TimespanInequality(
                        timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                        timespantools.SingleSourceTimespan(
                            selector=selectortools.SegmentSelector(
                                index='red'
                                )
                            )
                        ),
                    klass=selectortools.KlassInventory([
                        notetools.Note,
                        chordtools.Chord
                        ])
                    ),
                mathtools.Ratio(1, 1, 1),
                index=0
                )

        Return selector.
        '''
        from experimental import selectortools
        selector = self.select_notes_and_chords(contexts=contexts)
        if count:
            selector = selectortools.CountRatioItemSelector(selector, ratio, index=index)
        else:
            selector = selectortools.DurationRatioItemSelector(selector, ratio, index=index)
        return selector

    def select_timespan(self, contexts=None):
        '''Select contexts::

            >>> selector = segment.select_timespan()

        ::

            >>> z(selector)
            selectortools.MultipleContextTimespanSelector(
                contexts=['Grouped Rhythmic Staves Score'],
                timespan=timespantools.SingleSourceTimespan(
                    selector=selectortools.SegmentSelector(
                        index='red'
                        )
                    )
                )

        Return selector.
        '''
        from experimental import selectortools
        contexts = self.context_token_to_context_names(contexts)
        return selectortools.MultipleContextTimespanSelector(contexts=contexts, timespan=self.timespan)

    def set_aggregate(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'aggregate'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_articulations(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'articulations'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_attribute(self, attribute, contexts, source, 
        callback=None, count=None, offset=None, persistent=True, timespan=None, truncate=False):
        from experimental import settingtools
        from experimental import timespantools
        assert attribute in self.attributes, repr(attribute)
        assert isinstance(count, (int, type(None))), repr(count)
        assert isinstance(persistent, type(True)), repr(persistent)
        assert isinstance(timespan, (timespantools.SingleSourceTimespan, type(None))), repr(timespan)
        assert isinstance(truncate, type(True)), repr(truncate)
        target = self.select_timespan(contexts=contexts)
        source = self.annotate_source(source, callback=callback, count=count, offset=offset)
        directive = settingtools.Setting(target, attribute, source, 
            persistent=persistent, truncate=truncate)
        self.directives.append(directive)
        return directive

    def set_chord_treatment(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'chord_treatment'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_divisions(self, contexts, source, 
        callback=None, count=None, offset=None, persistent=True, truncate=False):
        attribute = 'divisions'
        return self.set_attribute(attribute, contexts, source, 
            callback=callback, count=count, offset=offset, persistent=persistent, truncate=truncate)

    def set_duration_in_seconds(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'duration_in_seconds'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_dynamics(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'dynamics'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_marks(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'marks'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_markup(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'markup'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_pitch_classes(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'pitch_classes'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_pitch_class_application(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'pitch_class_application'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_pitch_class_transform(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'pitch_class_transform'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_register(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'register'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_rhythm(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'rhythm'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_retrograde_divisions(self, contexts, source,
        count=None, offset=None, persistent=True, truncate=True):
        r'''.. versionadded:: 1.0

        Set `contexts` divisions from `source` taken in retrograde.
        '''
        string = 'sequencetools.reverse_sequence'
        callback = Callback(eval(string), string)
        return self.set_divisions(contexts, source, 
            callback=callback, count=count, offset=offset, persistent=persistent, truncate=truncate)

    def set_rotated_divisions(self, contexts, source, n, 
        count=None, offset=None, persistent=True, truncate=True):
        r'''.. versionadded:: 1.0

        Set `contexts` divisions from `source` rotated by integer `n`.
        '''
        assert isinstance(n, int), repr(n)
        string = 'lambda x: sequencetools.rotate_sequence(x, {})'.format(n)
        callback = Callback(eval(string), string)
        return self.set_divisions(contexts, source, 
            callback=callback, count=count, offset=offset, persistent=persistent, truncate=truncate)

    def set_tempo(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'tempo'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_time_signatures(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'time_signatures'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def set_written_duration(self, contexts, source, 
        count=None, persistent=True, offset=None):
        attribute = 'written_duration'
        return self.set_attribute(attribute, contexts, source, 
            count=count, offset=offset, persistent=persistent)

    def unpack_directives(self):
        for directive in self.directives:
            self.settings.extend(directive.unpack())
        return self.settings
