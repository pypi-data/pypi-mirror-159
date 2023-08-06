import enum
from typing import Any, Dict, List, Optional, Union

import pydantic
from pydantic import BaseModel

from classiq.interface.chemistry.ground_state_result import (
    GroundStateExactResult,
    GroundStateResult,
)
from classiq.interface.executor.vqe_result import (
    OptimizationResult,
    SolverResult,
    VQESolverResult,
)


class ExecutionStatus(str, enum.Enum):
    SUCCESS = "success"
    ERROR = "error"


class VaRResult(BaseModel):
    var: Optional[float] = None
    alpha: Optional[float] = None


class FinanceSimulationResults(BaseModel):
    var_results: Optional[VaRResult] = None
    result: Optional[float] = None

    @pydantic.root_validator()
    def validate_atleast_one_field(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        is_var_results_defined = values.get("var_results") is not None
        is_result_defined = values.get("result") is not None

        if not is_var_results_defined and not is_result_defined:
            raise ValueError(
                "At least one of var_results and result should be defined."
            )

        return values


class GroverSimulationResults(BaseModel):
    result: Dict[str, Union[float, int]]


class ExecutionDetails(BaseModel):
    vendor_format_result: Dict[str, Any] = pydantic.Field(
        ..., description="Result in proprietary vendor format"
    )
    counts: Dict[str, pydantic.NonNegativeInt] = pydantic.Field(
        default_factory=dict, description="Number of counts per state"
    )
    histogram: Optional[Dict[str, pydantic.NonNegativeFloat]] = pydantic.Field(
        None,
        description="Histogram of probability per state (an alternative to counts)",
    )


class GroverAdaptiveSearchResult(BaseModel):
    opt_x_string: List[int] = pydantic.Field(
        ..., description="Result in proprietary vendor format"
    )
    min_value: float = pydantic.Field(
        ..., description="Result in proprietary vendor format"
    )


ExecutionData = Union[
    ExecutionDetails,
    FinanceSimulationResults,
    GroverSimulationResults,
    OptimizationResult,
    GroundStateResult,
    VQESolverResult,
    GroundStateExactResult,
    SolverResult,
    GroverAdaptiveSearchResult,
    str,
]


class ExecutionResult(BaseModel):
    status: ExecutionStatus
    details: ExecutionData
