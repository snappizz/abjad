from abjad.tools.containertools.Container import Container
from abjad.tools import componenttools


def get_first_container_in_proper_parentage_of_component(component):
   r'''.. versionadded:: 1.1.2

   Get first container in proper parentage of `component`::

      abjad> staff = Staff("c'8 d'8 e'8 f'8")

   ::

      abjad> f(staff)
      \new Staff {
         c'8
         d'8
         e'8
         f'8
      }

   ::

      abjad> containertools.get_first_container_in_proper_parentage_of_component(staff[1])
      Staff{4}

   Return container or none.
   '''

   return componenttools.get_first_instance_of_klass_in_proper_parentage_of_component(
      component, Container)
