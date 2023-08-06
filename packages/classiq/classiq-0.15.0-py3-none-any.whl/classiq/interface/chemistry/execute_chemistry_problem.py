from pydantic import BaseModel

from classiq.interface.chemistry.ground_state_problem import GroundStateProblem
from classiq.interface.executor.execution_preferences import ExecutionPreferences
from classiq.interface.generator.model import Model


class GroundStateProblemExecution(BaseModel):
    molecule: GroundStateProblem
    model: Model
    preferences: ExecutionPreferences
