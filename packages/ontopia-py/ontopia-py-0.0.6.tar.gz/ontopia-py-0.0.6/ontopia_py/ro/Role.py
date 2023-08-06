from typing import List

from rdflib import Graph, Literal

from ..l0.Entity import Entity
from ..ns import *
from ..ro.TimeIndexedRole import TimeIndexedRole
from .declarations.Role import Role


class Role(Role):
    __type__ = RO["Role"]

    isRoleIn: List[TimeIndexedRole] = None
    isRoleOf: List[Entity] = None
    name: List[Literal] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isRoleIn:
            for isRoleIn in self.isRoleIn:
                g.add((self.uriRef, RO["isRoleIn"], isRoleIn.uriRef))

        if self.isRoleOf:
            for isRoleOf in self.isRoleOf:
                g.add((self.uriRef, RO["isRoleOf"], isRoleOf.uriRef))

        if self.name:
            for name in self.name:
                g.add((self.uriRef, L0["name"], name))
