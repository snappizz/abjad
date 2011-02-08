def remove_elements_at_indices_cyclic(sequence, indices, period, offset = 0):
   '''.. versionadded:: 1.1.2

   Remove `sequence` elements at `indices` mod `period` plus `offset`::

      abjad> list(seqtools.remove_elements_at_indices(range(20), [0, 1], 5, 3)
      [0, 1, 2, 5, 6, 7, 10, 11, 12, 15, 16, 17]

   Ignore negative indices.

   Return generator.
   '''

   for i, element in enumerate(sequence):
      if (i - offset) % period not in indices:
         yield element
