from rdflib import Graph, Literal

from ..l0.Location import Location
from ..ns import *
from .Person import Person


class Dead(Person):
    __type__ = CPV["Dead"]

    hasDeathPlace: Location = None
    ageWhenDead: Literal = None
    dateOfDeath: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasDeathPlace:
            g.add(self.uriRef, CPV["hasDeathPlace"],
                  self.hasDeathPlace.uriRef)

        if self.ageWhenDead:
            g.add(self.uriRef, CPV["ageWhenDead"], self.ageWhenDead)

        if self.dateOfDeath:
            g.add(self.uriRef, CPV["dateOfDeath"], self.dateOfDeath)
