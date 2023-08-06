import abc
from typing import Any, Dict, Optional

import pydantic

from classiq.interface.generator.arith.arithmetic import DEFAULT_ARG_NAME
from classiq.interface.generator.arith.fix_point_number import FixPointNumber
from classiq.interface.generator.arith.register_user_input import RegisterUserInput
from classiq.interface.generator.function_params import FunctionParams

_DEFAULT_GARBAGE_OUT_NAME = "extra_qubits"


class UnaryOpParams(FunctionParams):
    arg: RegisterUserInput
    output_size: Optional[pydantic.PositiveInt]
    output_name: str
    inplace: bool = False
    garbage_output_name: str = _DEFAULT_GARBAGE_OUT_NAME

    @pydantic.validator("arg")
    def _validate_argument(cls, arg: RegisterUserInput) -> RegisterUserInput:
        if arg.name is None:
            arg.name = DEFAULT_ARG_NAME
        return arg

    @classmethod
    @abc.abstractmethod
    def _expected_result_size(cls, arg: RegisterUserInput) -> int:
        pass

    def _create_io_names(self) -> None:
        arg_name: str = self.arg.name  # type: ignore[assignment]
        self._input_names = [arg_name]
        self._output_names = [self.output_name]

        if not self.inplace:
            self._output_names.append(arg_name)

        if (
            self.output_size == 1
            and self.inplace
            and self.output_size < self._expected_result_size(self.arg)
        ):
            self._output_names.append(self.garbage_output_name)

    class Config:
        arbitrary_types_allowed = True


class BitwiseInvert(UnaryOpParams):
    output_name: str = "inverted"

    @classmethod
    def _expected_result_size(cls, arg: RegisterUserInput) -> int:
        return arg.size


class Negation(UnaryOpParams):
    output_name: str = "negated"

    @classmethod
    def _expected_result_size(cls, arg: RegisterUserInput) -> int:
        return arg.size + int(arg.size > 1 and not arg.is_signed)

    @pydantic.validator("output_size", always=True)
    def _validate_output_size(
        cls, output_size: Optional[pydantic.PositiveInt], values: Dict[str, Any]
    ) -> pydantic.PositiveInt:
        if output_size is not None:
            return output_size
        arg: RegisterUserInput = values.get("arg")  # type: ignore[assignment]
        return (
            FixPointNumber.bounds_to_integer_part_size(
                lb=-max(arg.bounds), ub=-min(arg.bounds)  # type: ignore[arg-type]
            )
            + arg.fraction_places
        )
