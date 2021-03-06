import functools
from .Scheme import Scheme


@functools.total_ordering
class SchemeMoment(Scheme):
    """
    Abjad model of Scheme moment.

    ..  container:: example

        Initializes with two integers:

        >>> abjad.SchemeMoment((2, 68))
        SchemeMoment((2, 68))

    Scheme moments are immutable.
    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(self, duration=(0, 1)):
        import abjad
        duration = abjad.NonreducedFraction(duration)
        pair = duration.pair
        Scheme.__init__(self, pair)

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when ``argument`` is a scheme moment with the same value as
        that of this scheme moment.

        ..  container:: example

            >>> abjad.SchemeMoment((2, 68)) == abjad.SchemeMoment((2, 68))
            True

        ..  container:: example

            Otherwise false:

            >>> abjad.SchemeMoment((2, 54)) == abjad.SchemeMoment((2, 68))
            False

        Returns true or false.
        """
        return super(SchemeMoment, self).__eq__(argument)

    def __hash__(self):
        """
        Hashes scheme moment.

        Returns integer.
        """
        return super(SchemeMoment, self).__hash__()

    def __lt__(self, argument):
        """
        Is true when ``argument`` is a scheme moment with value greater than
        that of this scheme moment.

        ..  container:: example

            >>> abjad.SchemeMoment((1, 68)) < abjad.SchemeMoment((1, 32))
            True

        ..  container:: example

            Otherwise false:

            >>> abjad.SchemeMoment((1, 68)) < abjad.SchemeMoment((1, 78))
            False

        Returns true or false.
        """
        if isinstance(argument, type(self)):
            if self.duration < argument.duration:
                return True
        return False

    ### PRIVATE PROPERTIES ###

    @property
    def _formatted_value(self):
        pair = self.duration.pair
        string = '(ly:make-moment {} {})'
        string = string.format(*pair)
        return string

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        import abjad
        values = [self.value]
        return abjad.FormatSpecification(
            client=self,
            storage_format_args_values=values,
            storage_format_kwargs_names=[],
            )

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        """
        Gets duration of Scheme moment.

        ..  container:: example

            >>> abjad.SchemeMoment((2, 68)).duration
            NonreducedFraction(2, 68)

        Returns nonreduced fraction.
        """
        import abjad
        return abjad.NonreducedFraction(self.value)
