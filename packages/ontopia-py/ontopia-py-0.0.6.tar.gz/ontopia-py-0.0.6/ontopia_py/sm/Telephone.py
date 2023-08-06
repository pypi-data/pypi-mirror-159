from rdflib import Graph, Literal

from ..ns import *
from .declarations.OnlineContactPoint import OnlineContactPoint
from .declarations.Telephone import Telephone
from .TelephoneType import TelephoneType


class Telephone(Telephone):
    __type__ = SM["Telephone"]

    hasTelephoneType: TelephoneType = None
    isTelephoneOf: OnlineContactPoint = None
    telephoneNumber: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasTelephoneType:
            g.add((self.uriRef, SM["hasTelephoneType"],
                  self.hasTelephoneType.uriRef))

        if self.isTelephoneOf:
            g.add((self.uriRef, SM["isTelephoneOf"],
                  self.isTelephoneOf.uriRef))

        if self.telephoneNumber:
            g.add((self.uriRef, SM["telephoneNumber"], self.telephoneNumber))
