# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class ClarinetInA(Instrument):
    r'''Clarinet in A.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> clarinet = abjad.instrumenttools.ClarinetInA()
            >>> abjad.attach(clarinet, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { "Clarinet in A" }
                \set Staff.shortInstrumentName = \markup {
                    Cl.
                    A
                    \natural
                }
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
        instrument_name='clarinet in A',
        short_instrument_name=r'cl. A \natural',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range='[Db3, A6]',
        middle_c_sounding_pitch='A3',
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
            'clarinettist',
            'clarinetist',
            ])

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets clarinet in A's allowable clefs.

        ..  container:: example

            ::

                >>> clarinet.allowable_clefs
                ClefList([Clef(name='treble')])

            ::

                >>> show(clarinet.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets clarinet in A's name.

        ..  container:: example

            ::

                >>> clarinet.instrument_name
                'clarinet in A'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets clarinet in A's instrument name markup.

        ..  container:: example

            ::

                >>> clarinet.instrument_name_markup
                Markup(contents=['Clarinet in A'])

            ::

                >>> show(clarinet.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets clarinet in A's range.

        ..  container:: example

            ::

                >>> clarinet.pitch_range
                PitchRange('[Db3, A6]')

            ::

                >>> show(clarinet.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets clarinet in A's short instrument name.

        ..  container:: example

            ::

                >>> clarinet.short_instrument_name
                'cl. A \\natural'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets clarinet in A's short instrument name markup.

        ..  container:: example

            ::

                >>> clarinet.short_instrument_name_markup
                Markup(contents=['Cl.', 'A', MarkupCommand('natural')])

            ::

                >>> show(clarinet.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of clarinet in A's written middle C.

        ..  container:: example

            ::

                >>> clarinet.middle_c_sounding_pitch
                NamedPitch('a')

            ::

                >>> show(clarinet.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)
