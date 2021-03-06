import bisect
import collections
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject


class MeterFittingSession(AbjadValueObject):
    """
    Meter-fitting session.

    Used internally by Meter.fit_meters().
    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_cached_offset_counters',
        '_kernel_denominator',
        '_kernels',
        '_longest_kernel',
        '_maximum_run_length',
        '_meters',
        '_offset_counter',
        '_ordered_offsets',
        )

    KernelScore = collections.namedtuple(
        'KernelScore',
        ('kernel', 'score'),
        )

    ### INITIALIZER ###

    def __init__(
        self,
        kernel_denominator=32,
        maximum_run_length=None,
        meters=None,
        offset_counter=None,
        ):
        import abjad
        self._cached_offset_counters = {}
        if maximum_run_length is not None:
            maximum_run_length = int(maximum_run_length)
            assert 0 < maximum_run_length
        self._maximum_run_length = maximum_run_length
        if offset_counter:
            self._offset_counter = abjad.MetricAccentKernel.count_offsets(
                    offset_counter)
        else:
            self._offset_counter = {}
        self._ordered_offsets = tuple(sorted(self.offset_counter))
        meters = meters or ()
        self._meters = tuple(abjad.Meter(_) for _ in meters)
        self._kernel_denominator = abjad.Duration(kernel_denominator)
        self._kernels = {}
        for meter in self._meters:
            kernel = meter.generate_offset_kernel_to_denominator(
                self._kernel_denominator)
            self._kernels[kernel] = meter
        if self.kernels:
            self._longest_kernel = sorted(
                self._kernels,
                key=lambda x: x.duration,
                )[-1]
        else:
            self._longest_kernel = None

    ### SPECIAL METHODS ###

    def __call__(self):
        """
        Fits meters.

        Returns meter list.
        """
        import abjad
        selected_kernels = []
        current_offset = abjad.Offset(0)
        while current_offset < self.ordered_offsets[-1]:
            kernel_scores = []
            kernels = self._get_kernels(selected_kernels)
            offset_counter = self._get_offset_counter_at(current_offset)
            if not offset_counter:
                winning_kernel = self.longest_kernel
                if selected_kernels:
                    winning_kernel = selected_kernels[-1]
            else:
                for kernel in kernels:
                    if self.maximum_run_length and \
                        1 < len(kernels) and \
                        self.maximum_run_length <= len(selected_kernels):
                        last_n_kernels = \
                            selected_kernels[-self.maximum_run_length:]
                        if len(set(last_n_kernels)) == 1:
                            if kernel == last_n_kernels[-1]:
                                continue
                    initial_score = kernel(offset_counter)
                    lookahead_score = self._get_lookahead_score(
                        current_offset,
                        kernel,
                        kernels,
                        )
                    score = initial_score + lookahead_score
                    kernel_score = self.KernelScore(
                        kernel=kernel,
                        score=score,
                        )
                    kernel_scores.append(kernel_score)
                kernel_scores.sort(key=lambda kernel_score: kernel_score.score)
                winning_kernel = kernel_scores[-1].kernel
            selected_kernels.append(winning_kernel)
            current_offset += winning_kernel.duration
        selected_meters = (self.kernels[_] for _ in selected_kernels)
        selected_meters = abjad.MeterList(selected_meters)
        return selected_meters

    ### PRIVATE METHODS ###

    def _get_kernels(self, selected_kernels):
        return tuple(self.kernels)

    def _get_lookahead_score(self, current_offset, kernel, kernels):
        lookahead_scores = []
        lookahead_offset = current_offset + kernel.duration
        lookahead_offset_counter = self._get_offset_counter_at(
            lookahead_offset)
        for lookahead_kernel in kernels:
            lookahead_scores.append(
                lookahead_kernel(lookahead_offset_counter)
                )
        lookahead_score = sum(lookahead_scores)  # / len(lookahead_scores)
        return lookahead_score

    def _get_offset_counter_at(self, start_offset):
        if start_offset in self.cached_offset_counters:
            return self.cached_offset_counters[start_offset]
        offset_counter = {}
        stop_offset = start_offset + self.longest_kernel.duration
        index = bisect.bisect_left(self.ordered_offsets, start_offset)
        if index == len(self.ordered_offsets):
            return offset_counter
        offset = self.ordered_offsets[index]
        while offset <= stop_offset:
            count = self.offset_counter[offset]
            offset_counter[offset - start_offset] = count
            index += 1
            if index == len(self.ordered_offsets):
                break
            offset = self.ordered_offsets[index]
        self.cached_offset_counters[start_offset] = offset_counter
        return offset_counter

    ### PUBLIC PROPERTIES ###

    @property
    def cached_offset_counters(self):
        """
        Gets cached offset counters

        Returns dictionary.
        """
        return self._cached_offset_counters

    @property
    def kernel_denominator(self):
        """
        Gets kernel denominator.

        Returns duration.
        """
        return self._kernel_denominator

    @property
    def kernels(self):
        """
        Gets kernels-to-meter dictionary.

        Returns dictionary.
        """
        return self._kernels

    @property
    def longest_kernel(self):
        """
        Gets longest kernel.

        Returns kernel.
        """
        return self._longest_kernel

    @property
    def maximum_run_length(self):
        """
        Gets maximum meter repetitions.

        Returns integer or none.
        """
        return self._maximum_run_length

    @property
    def meters(self):
        """
        Gets meters.

        Returns meters.
        """
        return self._meters

    @property
    def offset_counter(self):
        """
        Gets offset counter.

        Returns offset counter.
        """
        return self._offset_counter

    @property
    def ordered_offsets(self):
        """
        Gets ordered offsets.

        Returns offsets.
        """
        return self._ordered_offsets
