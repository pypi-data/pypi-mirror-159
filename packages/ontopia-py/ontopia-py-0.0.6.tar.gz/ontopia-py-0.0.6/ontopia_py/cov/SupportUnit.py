from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .Organization import Organization


class SupportUnit(Organization):
    __type__ = COV["SupportUnit"]

    isSupportUnitOf: List[Organization] = None
    officeIdentifier: List[Literal] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isSupportUnitOf:
            for isSupportUnitOf in self.isSupportUnitOf:
                g.add(
                    (self.uriRef, COV["isSupportUnitOf"], isSupportUnitOf.uriRef))

        if self.officeIdentifier:
            for officeIdentifier in self.officeIdentifier:
                g.add((self.uriRef, COV["officeIdentifier"], officeIdentifier))
