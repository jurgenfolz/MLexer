class StepNode:
    def __init__(self, step_name: str, function_name: str, depends_on_steps:  list[str], used_columns:  list[str], produced_columns: list[str]):
        self.step_name: str = step_name
        self.function_name: str = function_name
        self.depends_on_steps: list[str] = depends_on_steps   # example: ["Changed Type"]
        self.used_columns: list[str] = used_columns           # example: ["Kanton"]
        self.produced_columns: list[str] = produced_columns   # example: ["Kanton.1"]
