# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class MezzoSopranoVoice(Instrument):
    r'''Mezzo-soprano voice.

    ::

        >>> import abjad

    ..  container:: example

        ::


            >>> staff = abjad.Staff("c''4 d''4 e''4 fs''4")
            >>> mezzo_soprano = abjad.instrumenttools.MezzoSopranoVoice()
            >>> abjad.attach(mezzo_soprano, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { Mezzo-soprano }
                \set Staff.shortInstrumentName = \markup { Mezz. }
                c''4
                d''4
                e''4
                fs''4
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    performer_abbreviation = 'ms.'

    ### INITIALIZER ###

    def __init__(
        self,
        instrument_name='mezzo-soprano',
        short_instrument_name='mezz.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range='[A3, C6]',
        middle_c_sounding_pitch=None,
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
            'vocalist',
            'mezzo-soprano',
            ])
        self._is_primary_instrument = True

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets mezzo-soprano's allowable clefs.

        ..  container:: example

            ::

                >>> mezzo_soprano.allowable_clefs
                ClefList([Clef(name='treble')])

            ::

                >>> show(mezzo_soprano.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets mezzo-soprano's name.

        ..  container:: example

            ::

                >>> mezzo_soprano.instrument_name
                'mezzo-soprano'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets mezzo-soprano's instrument name markup.

        ..  container:: example

            ::

                >>> mezzo_soprano.instrument_name_markup
                Markup(contents=['Mezzo-soprano'])

            ::

                >>> show(mezzo_soprano.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets mezzo-soprano's range.

        ..  container:: example

            ::

                >>> mezzo_soprano.pitch_range
                PitchRange('[A3, C6]')

            ::

                >>> show(mezzo_soprano.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets mezzo-soprano's short instrument name.

        ..  container:: example

            ::

                >>> mezzo_soprano.short_instrument_name
                'mezz.'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets mezzo-soprano's short instrument name markup.

        ..  container:: example

            ::

                >>> mezzo_soprano.short_instrument_name_markup
                Markup(contents=['Mezz.'])

            ::

                >>> show(mezzo_soprano.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of mezzo-soprano's written middle C.

        ..  container:: example

            ::

                >>> mezzo_soprano.middle_c_sounding_pitch
                NamedPitch("c'")

            ::

                >>> show(mezzo_soprano.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)
