from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Characteristic import Characteristic


class LegalStatus(Characteristic):
    __type__ = COV["LegalStatus"]

    legalStatusCode: List[Literal] = None
    legalStatusDesc: List[Literal] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.legalStatusCode:
            for legalStatusCode in self.legalStatusCode:
                g.add((self.uriRef, COV["legalStatusCode"], legalStatusCode))

        if self.legalStatusDesc:
            for legalStatusDesc in self.legalStatusDesc:
                g.add((self.uriRef, COV["legalStatusDesc"], legalStatusDesc))
