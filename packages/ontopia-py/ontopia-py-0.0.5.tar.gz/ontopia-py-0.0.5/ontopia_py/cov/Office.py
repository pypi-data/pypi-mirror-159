from rdflib import Graph, Literal

from ..ns import *
from .eInvoiceService import eInvoiceService
from .HomogeneousOrganizationalArea import HomogeneousOrganizationalArea
from .SupportUnit import SupportUnit


class Office(SupportUnit):
    __type__ = COV["Office"]

    hasEInvoiceService: eInvoiceService = None
    isPartOf: HomogeneousOrganizationalArea = None
    officeIdentifier: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasEInvoiceService:
            for hasEInvoiceService in self.hasEInvoiceService:
                g.add(
                    (self.uriRef, COV["hasEInvoiceService"], hasEInvoiceService.uriRef))

        if self.isPartOf:
            for isPartOf in self.isPartOf:
                g.add((self.uriRef, COV["isPartOf"], isPartOf.uriRef))

        if self.officeIdentifier:
            g.add((self.uriRef, COV["officeIdentifier"],
                  self.officeIdentifier))
