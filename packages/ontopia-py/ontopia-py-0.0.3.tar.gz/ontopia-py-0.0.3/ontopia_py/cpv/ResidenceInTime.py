from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..ti.TimeIndexedEvent import TimeIndexedEvent
from ..clv.Address import Address
from .Person import Person


class ResidenceInTime(TimeIndexedEvent):
    __type__ = CPV["ResidenceInTime"]

    residenceInLocation: Address = None
    isResidenceInTimeOf: Person

    def _addProperties(self, g: Graph):
        if self.residenceInLocation:
            g.add(self.uriRef, CPV["residenceInLocation"],
                  self.residenceInLocation.uriRef)

        if self.isResidenceInTimeOf:
            g.add(self.uriRef, CPV["isResidenceInTimeOf"],
                  self.isResidenceInTimeOf.uriRef)
