# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class BaritoneSaxophone(Instrument):
    r'''Baritone saxophone.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> baritone_saxophone = abjad.instrumenttools.BaritoneSaxophone()
            >>> abjad.attach(baritone_saxophone, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { "Baritone saxophone" }
                \set Staff.shortInstrumentName = \markup { "Bar. sax." }
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
        instrument_name='baritone saxophone',
        short_instrument_name='bar. sax.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range='[C2, Ab4]',
        middle_c_sounding_pitch='Eb2',
        ):
        Instrument.__init__(
            self,
            instrument_name=instrument_name,
            short_instrument_name=short_instrument_name,
            instrument_name_markup=instrument_name_markup,
            short_instrument_name_markup=short_instrument_name_markup,
            allowable_clefs=allowable_clefs,
            pitch_range=pitch_range,
            middle_c_sounding_pitch=\
                middle_c_sounding_pitch,
            )
        self._performer_names.extend([
            'wind player',
            'reed player',
            'single reed player',
            'saxophonist',
            ])

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets baritone saxophone's allowable clefs.

        ..  container:: example

            ::

                >>> baritone_saxophone.allowable_clefs
                ClefList([Clef(name='treble')])

            ::

                >>> show(baritone_saxophone.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets baritone saxophone's name.

        ..  container:: example

            ::

                >>> baritone_saxophone.instrument_name
                'baritone saxophone'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets baritone saxophone's instrument name markup.

        ..  container:: example

            ::

                >>> baritone_saxophone.instrument_name_markup
                Markup(contents=['Baritone saxophone'])

            ::

                >>> show(baritone_saxophone.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets baritone saxophone's range.

        ..  container:: example

            ::

                >>> baritone_saxophone.pitch_range
                PitchRange('[C2, Ab4]')

            ::

                >>> show(baritone_saxophone.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets baritone saxophone's short instrument name.

        ..  container:: example

            ::

                >>> baritone_saxophone.short_instrument_name
                'bar. sax.'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets baritone saxophone's short instrument name markup.

        ..  container:: example

            ::

                >>> baritone_saxophone.short_instrument_name_markup
                Markup(contents=['Bar. sax.'])

            ::

                >>> show(baritone_saxophone.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of baritone saxophone's written middle C.

        ..  container:: example

            ::

                >>> baritone_saxophone.middle_c_sounding_pitch
                NamedPitch('ef,')

            ::

                >>> show(baritone_saxophone.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)
