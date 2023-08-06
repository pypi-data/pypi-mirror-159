from typing import Dict

from pydantic import BaseModel

from classiq.interface.executor.vqe_result import VQESolverResult
from classiq.interface.generator.complex_type import Complex


class GroundStateExactResult(BaseModel):
    energy: float
    nuclear_repulsion_energy: float
    total_energy: float
    hartree_fock_energy: float
    ground_state: Dict[str, Complex]


class GroundStateResult(GroundStateExactResult, VQESolverResult):
    pass
