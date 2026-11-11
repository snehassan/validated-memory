import subprocess
import sys
import tempfile
from pathlib import Path


def run_tests(code, tests, imports=(), timeout=10):
    """Run code against assert tests in a separate process.

    Returns {"passed": bool, "error": str}.
    """
    program = "\n".join(list(imports) + [code, ""] + list(tests)) + "\n"

    # Fresh temp folder per run, so model code can't touch your repo.
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "solution.py"
        path.write_text(program)
        try:
            proc = subprocess.run(
                [sys.executable, "-I", str(path)],  # -I: isolated mode
                cwd=tmp,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return {"passed": False, "error": f"Timeout after {timeout}s"}

    if proc.returncode == 0:
        return {"passed": True, "error": ""}
    # Keep only the end of the error; that's where the useful part is.
    return {"passed": False, "error": proc.stderr[-2000:]}