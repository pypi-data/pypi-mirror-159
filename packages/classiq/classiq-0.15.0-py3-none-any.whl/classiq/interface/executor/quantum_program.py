from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Union

import pydantic
from pydantic import BaseModel

from classiq.interface.backend.ionq import ionq_quantum_program
from classiq.interface.backend.pydantic_backend import PydanticArgumentNameType
from classiq.interface.executor.quantum_instruction_set import QuantumInstructionSet

Arguments = Dict[PydanticArgumentNameType, float]


class QuantumProgram(BaseModel):
    syntax: QuantumInstructionSet = pydantic.Field(
        QuantumInstructionSet.QASM, description="The syntax of the program."
    )
    code: Union[str, ionq_quantum_program.IonqQuantumCircuit] = pydantic.Field(
        ..., description="The textual representation of the program"
    )
    arguments: Optional[Arguments] = pydantic.Field(
        None,
        description="The parameters dictionary for a parametrized quantum program. "
        "Relevant for Q# programs only.",
    )

    @pydantic.validator("code")
    def load_quantum_program(cls, code: str, values: Dict[str, Any]):
        if not isinstance(code, str):
            return code

        syntax = values.get("syntax")
        if syntax == QuantumInstructionSet.IONQ:
            return ionq_quantum_program.IonqQuantumCircuit.from_string(code)

        return code

    @pydantic.validator("arguments")
    def validate_arguments(cls, arguments: Optional[Arguments], values: Dict[str, Any]):
        if arguments and values.get("syntax") not in (
            QuantumInstructionSet.QSHARP,
            QuantumInstructionSet.QASM,
        ):
            raise ValueError("Only QASM or Q# programs support arguments")
        return arguments

    @staticmethod
    def from_file(
        file_path: Union[str, Path],
        syntax: Optional[Union[str, QuantumInstructionSet]] = None,
        arguments: Optional[Arguments] = None,
    ) -> QuantumProgram:
        path = Path(file_path)
        code = path.read_text()
        if syntax is None:
            syntax = path.suffix.lstrip(".")
        return QuantumProgram(syntax=syntax, code=code, arguments=arguments)
