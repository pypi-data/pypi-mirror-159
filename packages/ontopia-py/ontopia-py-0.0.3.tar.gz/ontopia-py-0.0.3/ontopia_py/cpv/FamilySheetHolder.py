from typing import List

from rdflib import Graph

from ..ns import *
from .Person import Person


class FamilySheetHolder(Person):
    __type__ = CPV["FamilySheetHolder"]

    isFamilySheetHolderOf: List[Person] = None

    def _addProperties(self, g: Graph):
        if self.isFamilySheetHolderOf:
            for isFamilySheetHolderOf in self.isFamilySheetHolderOf:
                g.add(
                    (self.uriRef, CLV["isFamilySheetHolderOf"], isFamilySheetHolderOf.uriRef))
