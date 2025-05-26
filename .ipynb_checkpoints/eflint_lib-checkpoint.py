import subprocess
import json

class EF:
    def __init__(self):
        self.HOST = "localhost"
        self.PORT = 8080

    def _parse_to_dict(self, json_string: str):
        return json.loads(json_string)

    def _parse_response(method):
        def wrapper(self, *args, **kwargs):
            response = method(self, *args, **kwargs)
            return self.__parse_to_dict(response)
        return wrapper

    def send_eflint_command(self, command_obj: dict) -> str:
        """Send a command to the eFLINT server and return the response"""
        command_json = json.dumps(command_obj)
        full_cmd = f"echo '{command_json}' | nc {self.HOST} {self.PORT}"
        return subprocess.check_output(full_cmd, shell=True, text=True)

    @_parse_response
    def status(self) -> dict:
        """Send a status command to the eFLINT server"""
        command = { "command": "status" }
        return self.send_eflint_command(command)

    @_parse_response
    def phrase(self, phrase_text: str) -> dict:
        """Send a phrase to the eFLINT server"""
        command = {
            "command": "phrase",
            "text": phrase_text
        }
        return self.send_eflint_command(command)

    @_parse_response
    def types(self) -> dict:
        """Get all types from the eFLINT server"""
        command = { "command": "types" }
        return self.send_eflint_command(command)
