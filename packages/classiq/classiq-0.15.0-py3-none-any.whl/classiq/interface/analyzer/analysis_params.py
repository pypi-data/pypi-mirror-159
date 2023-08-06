from enum import Enum
from typing import Dict, List, Optional

import pydantic

from classiq.interface.backend.quantum_backend_providers import AnalyzerProviderVendor
from classiq.interface.helpers.custom_pydantic_types import PydanticNonEmptyString


class AnalysisParams(pydantic.BaseModel):
    qasm: PydanticNonEmptyString


class AnalysisHardwareParams(pydantic.BaseModel):
    devices: Optional[List[PydanticNonEmptyString]] = pydantic.Field(
        default=..., description="Devices"
    )
    providers: List[AnalyzerProviderVendor] = pydantic.Field(
        default=..., description="Providers"
    )


class AnalysisTableParams(AnalysisParams, AnalysisHardwareParams):
    pass


class ComparisonProperties(str, Enum):
    DEPTH = "depth"
    MULTI_QUBIT_GATE_COUNT = "multi_qubit_gate_count"
    TOTAL_GATE_COUNT = "total_gate_count"


class AnalysisComparisonParams(pydantic.BaseModel):
    property: ComparisonProperties = pydantic.Field(
        default=...,
        description="The comparison property used to select the best devices",
    )


class AnalysisRBParams(pydantic.BaseModel):
    hardware: str
    counts: List[Dict[str, int]]
    num_clifford: List[int]
