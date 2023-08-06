from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .SupportUnit import SupportUnit


class HomogeneousOrganizationalArea(SupportUnit):
    __type__ = COV["HomogeneousOrganizationalArea"]

    AOOIdentifier: List[Literal] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.AOOIdentifier:
            for AOOIdentifier in self.AOOIdentifier:
                g.add((self.uriRef, COV["AOOIdentifier"], AOOIdentifier))
