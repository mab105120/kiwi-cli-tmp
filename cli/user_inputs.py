from typing import Dict
from rich.console import Console

_console = Console()

def get_user_inputs(vars: Dict[str, str]) -> Dict[str, str]:
    inputs = {}
    for var, label in vars.items():
        inputs[var] = _console.input(label)
    _console.print("\n")
    return inputs