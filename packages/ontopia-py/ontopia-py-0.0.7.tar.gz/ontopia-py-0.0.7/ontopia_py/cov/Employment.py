from rdflib import Graph, Literal

from ..ns import *
from ..ro.TimeIndexedRole import TimeIndexedRole
from .declarations.Organization import Organization


class Employment(TimeIndexedRole):
    __type__ = COV["Employment"]

    employmentFor: Organization = None
    remuneration: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.employmentFor:
            g.add(self.uriRef, COV["employmentFor"],
                  self.employmentFor.uriRef)

        if self.remuneration:
            g.add(self.uriRef, COV["remuneration"],
                  self.remuneration)
