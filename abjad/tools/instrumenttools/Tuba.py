# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class Tuba(Instrument):
    r'''Tuba.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> clef = abjad.Clef(name='bass')
            >>> abjad.attach(clef, staff[0])
            >>> tuba = abjad.instrumenttools.Tuba()
            >>> abjad.attach(tuba, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { Tuba }
                \set Staff.shortInstrumentName = \markup { Tb. }
                \clef "bass"
                c'4
                d'4
                e'4
                fs'4
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        name='tuba',
        short_name='tb.',
        name_markup=None,
        short_name_markup=None,
        allowable_clefs=('bass',),
        middle_c_sounding_pitch=None,
        pitch_range='[D1, F4]',
        ):
        Instrument.__init__(
            self,
            name=name,
            short_name=short_name,
            name_markup=name_markup,
            short_name_markup=short_name_markup,
            allowable_clefs=allowable_clefs,
            middle_c_sounding_pitch=middle_c_sounding_pitch,
            pitch_range=pitch_range,
            )
        self._performer_names.extend([
            'brass player',
            'tubist',
            ])
        self._is_primary_instrument = True

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets tuba's allowable clefs.

        ..  container:: example

            ::

                >>> tuba.allowable_clefs
                ClefList([Clef(name='bass')])

            ::

                >>> show(tuba.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of tuba's written middle C.

        ..  container:: example

            ::

                >>> tuba.middle_c_sounding_pitch
                NamedPitch("c'")

            ::

                >>> show(tuba.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        r'''Gets tuba's name.

        ..  container:: example

            ::

                >>> tuba.name
                'tuba'

        Returns string.
        '''
        return Instrument.name.fget(self)

    @property
    def name_markup(self):
        r'''Gets tuba's instrument name markup.

        ..  container:: example

            ::

                >>> tuba.name_markup
                Markup(contents=['Tuba'])

            ::

                >>> show(tuba.name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets tuba's range.

        ..  container:: example

            ::

                >>> tuba.pitch_range
                PitchRange('[D1, F4]')

            ::

                >>> show(tuba.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_name(self):
        r'''Gets tuba's short instrument name.

        ..  container:: example

            ::

                >>> tuba.short_name
                'tb.'

        Returns string.
        '''
        return Instrument.short_name.fget(self)

    @property
    def short_name_markup(self):
        r'''Gets tuba's short instrument name markup.

        ..  container:: example

            ::

                >>> tuba.short_name_markup
                Markup(contents=['Tb.'])

            ::

                >>> show(tuba.short_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_name_markup.fget(self)
