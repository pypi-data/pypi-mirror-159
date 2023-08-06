from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Description import Description
from .RegisteredFamily import RegisteredFamily


class ParentalRelationshipType(Description):
    __type__ = CPV["ParentalRelationshipType"]

    inRegisteredFamily: List[RegisteredFamily] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.inRegisteredFamily:
            for inRegisteredFamily in self.inRegisteredFamily:
                g.add(
                    (self.uriRef, CPV["inRegisteredFamily"], inRegisteredFamily.uriRef))
