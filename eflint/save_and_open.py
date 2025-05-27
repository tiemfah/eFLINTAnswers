import os
import subprocess


def save_dsl_to_file(form_dsl_string: str, form_name: str, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(form_dsl_string)

    print(f"DSL saved to {path}")


def open_liveql():
    subprocess.run(["sh", "/Users/tiemfah/Projects/LiveQL/run.sh"])
