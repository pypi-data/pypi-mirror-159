from rdflib import Graph, Literal

from ..l0.Object import Object
from ..ns import *
from ..ti.Year import Year


class BalanceSheet(Object):
    __type__ = COV["BalanceSheet"]

    hasYear: Year = None
    totalAmount: Literal = None
    totalTaxBurden: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasYear:
            g.add(self.uriRef, TI["hasYear"], self.hasYear.uriRef)

        if self.totalAmount:
            g.add(self.uriRef, COV["totalAmount"], self.totalAmount)

        if self.totalTaxBurden:
            g.add(self.uriRef, COV["totalTaxBurden"], self.totalTaxBurden)
