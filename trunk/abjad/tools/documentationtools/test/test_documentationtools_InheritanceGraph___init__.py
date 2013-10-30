# -*- encoding: utf-8 -*-
import abjad
from abjad import *
import py


def test_documentationtools_InheritanceGraph___init___01():
    graph = documentationtools.InheritanceGraph(
        addresses=(
            abjad,
        )
        )


def test_documentationtools_InheritanceGraph___init___02():
    graph = documentationtools.InheritanceGraph(
        addresses=(
            abjad,
        ),
        root_addresses=(abctools.AbjadObject,)
        )


def test_documentationtools_InheritanceGraph___init___03():
    graph = documentationtools.InheritanceGraph(
        addresses=(
            Container,
            scoretools,
            scoretools,
        )
        )


def test_documentationtools_InheritanceGraph___init___04():
    graph = documentationtools.InheritanceGraph(
        addresses=(
            'abjad',
        )
        )


def test_documentationtools_InheritanceGraph___init___05():
    graph = documentationtools.InheritanceGraph(
        addresses=(
            'abjad',
        ),
        root_addresses=(('abjad.tools.abctools.AbjadObject', 'AbjadObject'),)
        )


def test_documentationtools_InheritanceGraph___init___06():
    graph = documentationtools.InheritanceGraph(
        addresses=(
            ('abjad.tools.containertools.Container', 'Container'),
            'abjad.tools.scoretools',
            'abjad.tools.scoretools',
        ),
        root_addresses=(('abjad.tools.abctools.AbjadObject', 'AbjadObject'),)
        )


def test_documentationtools_InheritanceGraph___init___07():
    graph = documentationtools.InheritanceGraph(
        lineage_addresses=(containertools.Container,),
        root_addresses=(('abjad.tools.abctools.AbjadObject', 'AbjadObject'),)
        )
