from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Characteristic import Characteristic


class EducationLevel(Characteristic):
    __type__ = CPV["EducationLevel"]

    educationLevelDesc: List[Literal] = None
    educationLevelID: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.educationLevelDesc:
            for educationLevelDesc in self.educationLevelDesc:
                g.add(
                    (self.uriRef, CPV["educationLevelDesc"], educationLevelDesc))

        if self.educationLevelID:
            g.add(self.uriRef, CPV["educationLevelID"], self.educationLevelID)
