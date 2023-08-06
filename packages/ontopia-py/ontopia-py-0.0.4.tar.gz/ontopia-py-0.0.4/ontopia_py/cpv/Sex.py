from typing import List

from rdflib import Graph, Literal

from ..l0.Characteristic import Characteristic
from ..ns import *


class Sex(Characteristic):
    __type__ = CPV["Sex"]

    sexDesc: List[Literal] = None
    sexID: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.sexDesc:
            for sexDesc in self.sexDesc:
                g.add((self.uriRef, CLV["sexDesc"], sexDesc))

        if self.sexID:
            g.add(self.uriRef, CPV["sexID"], self.sexID)
