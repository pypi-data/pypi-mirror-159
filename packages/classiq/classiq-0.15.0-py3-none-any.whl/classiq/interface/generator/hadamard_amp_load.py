from typing import List

import pydantic

from classiq.interface.generator import function_params
from classiq.interface.generator.complex_type import Complex
from classiq.interface.generator.sparse_amp_load import amplitudes_sum_to_one
from classiq.interface.generator.state_preparation import is_power_of_two

OUTPUT_STATE = "OUTPUT_STATE"
EXTRA_QUBITS = "EXTRA_QUBITS"


class HadamardAmpLoad(function_params.FunctionParams):
    """
    loads a amplitudes vector using hadamard decomposition
    """

    num_qubits: pydantic.PositiveInt = pydantic.Field(
        description="The number of qubits in the circuit."
    )
    amplitudes: List[Complex] = pydantic.Field(description="amplitudes vector to load")

    cutoff: pydantic.PositiveInt = pydantic.Field(
        description="The number of hadamard coefficients to keep. "
        "The largest cutoff_num coefficients are used to load the amplitudes"
    )

    _is_power_of_two = pydantic.validator("amplitudes", allow_reuse=True)(
        is_power_of_two
    )
    _is_sum_to_one = pydantic.validator("amplitudes", allow_reuse=True)(
        amplitudes_sum_to_one
    )

    @pydantic.root_validator()
    def cutoff_validator(cls, values):
        amp = values.get("amplitudes")
        cutoff = values.get("cutoff")
        if cutoff > len(amp):
            raise ValueError(
                "cutoff number should be smaller or equal to the length of the amplitudes vector "
            )
        return values

    @property
    def state_qubits_num(self) -> int:
        return len(self.amplitudes).bit_length() - 1

    @property
    def has_extra_qubits(self) -> bool:
        return self.num_qubits > self.state_qubits_num

    def _create_io_names(self) -> None:
        self._input_names = list()
        self._output_names = [OUTPUT_STATE]
        if self.has_extra_qubits:
            self._output_names.append(EXTRA_QUBITS)
