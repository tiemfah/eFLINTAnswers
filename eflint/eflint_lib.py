import json
import subprocess
from typing import Union


def _parse_to_dict(json_string: str):
    return json.loads(json_string)


def _to_eflint_value(python_value: Union[int, str]) -> dict:
    """Get the fact type from a fact dictionary"""
    return {
        "tagged-type": "string" if isinstance(python_value, str) else "int",
        "fact-type": "string" if isinstance(python_value, str) else "int",
        "value": python_value,
        "textual": python_value
    }


class EF:
    def __init__(self):
        self.HOST = "localhost"
        self.PORT = 8080

    def send_eflint_command(self, command_obj: dict) -> str:
        """Send a command to the eFLINT server and return the response"""
        command_json = json.dumps(command_obj)
        full_cmd = f"echo '{command_json}' | nc {self.HOST} {self.PORT}"
        return subprocess.check_output(full_cmd, shell=True, text=True)

    def status(self) -> dict:
        """Send a status command to the eFLINT server"""
        command = {"command": "status"}
        return _parse_to_dict(self.send_eflint_command(command))

    def phrase(self, phrase_text: str) -> dict:
        """Send a phrase to the eFLINT server"""
        command = {
            "command": "phrase",
            "text": phrase_text
        }
        return _parse_to_dict(self.send_eflint_command(command))

    def types(self) -> dict:
        """Get all types from the eFLINT server"""
        command = {"command": "types"}
        return _parse_to_dict(self.send_eflint_command(command))

    def create(self, fact_type: str, fact_value: Union[int, str, list]) -> dict:
        """Create a fact instance in eFLINT.

        Args:
            fact_type: The type of fact to create
            fact_value: For single-parameter facts, an int or string.
                       For multi-parameter facts, a list of values.
        """
        if isinstance(fact_value, list):
            value_obj = {
                "tagged-type": "Instance",
                "fact-type": fact_type,
                "arguments": list(map(lambda x: _to_eflint_value(x), fact_value)),
                "textual": f"+{fact_type}({', '.join(str(v) for v in fact_value)})"
            }
        else:
            value_obj = {
                "tagged-type": "Instance",
                "fact-type": fact_type,
                "value": fact_value,
                "textual": f"+{fact_type}({fact_value})"
            }

        command = {
            "command": "create",
            "value": value_obj
        }
        return _parse_to_dict(self.send_eflint_command(command))

    def action(self, action_type: str, actor: str, recipient: str) -> dict:
        """Send execute action command to the eFLINT server"""
        command = {
            "command": "action",
            "value": {
                "tagged-type": "Action",
                "fact-type": action_type,
                "value": [
                    {
                        "tagged-type": "String",
                        "fact-type": "String",
                        "value": actor,
                        "textual": actor
                    },
                    {
                        "tagged-type": "String",
                        "fact-type": "String",
                        "value": recipient,
                        "textual": recipient
                    }
                ],
                "textual": f"{action_type}({actor}, {recipient})"
            }
        }
        return _parse_to_dict(self.send_eflint_command(command))

    def query(self, fact_type: str, fact_value: str) -> dict:
        """Send a query to the eFLINT server"""
        command = {
            "command": "test-present",
            "value": {
                "tagged-type": "Atom",
                "fact-type": fact_type,
                "value": fact_value,
                "textual": f"fact_type({fact_value})"
            }
        }
        return _parse_to_dict(self.send_eflint_command(command))

    def history(self) -> dict:
        """Get the history of actions from the eFLINT server"""
        command = {"command": "history"}
        return _parse_to_dict(self.send_eflint_command(command))

    def revert(self, value: int) -> dict:
        """Revert the eFLINT server to a previous state"""
        command = {
            "command": "revert",
            "value": value
        }
        return _parse_to_dict(self.send_eflint_command(command))
