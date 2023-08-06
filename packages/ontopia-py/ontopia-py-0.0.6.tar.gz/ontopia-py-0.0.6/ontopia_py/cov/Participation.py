from rdflib import Graph, Literal

from ..ns import *
from ..ti.TimeIndexedEvent import TimeIndexedEvent
from .Organization import Organization
from .ParticipationType import ParticipationType


class Participation(TimeIndexedEvent):
    __type__ = COV["Participation"]

    participated: Organization = None
    hasParticipationType: ParticipationType = None
    participationPercentage: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.participated:
            for participated in self.participated:
                g.add((self.uriRef, COV["participated"], participated.uriRef))

        if self.hasParticipationType:
            for hasParticipationType in self.hasParticipationType:
                g.add(
                    (self.uriRef, COV["hasParticipationType"], hasParticipationType.uriRef))

        if self.participationPercentage:
            for participationPercentage in self.participationPercentage:
                g.add(
                    (self.uriRef, COV["participationPercentage"], participationPercentage))
