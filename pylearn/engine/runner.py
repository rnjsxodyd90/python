"""Execute user code safely and capture output."""

import io
import sys
import traceback
from contextlib import redirect_stdout, redirect_stderr


class ExecutionResult:
    """Result of running user code."""

    def __init__(self, stdout="", stderr="", error=None, namespace=None):
        self.stdout = stdout
        self.stderr = stderr
        self.error = error
        self.namespace = namespace or {}
        self.success = error is None

    def __repr__(self):
        status = "OK" if self.success else "ERROR"
        return f"ExecutionResult({status}, stdout={self.stdout!r:.50})"


def run_code(code, timeout_hint=5, pre_code="", namespace=None):
    """Execute user code and capture stdout/stderr.

    Args:
        code: The Python code string to execute.
        timeout_hint: Not enforced (stdlib has no easy timeout), but hints at expected duration.
        pre_code: Code to run before user code (setup).
        namespace: Optional namespace dict for exec().

    Returns:
        ExecutionResult with stdout, stderr, error info, and resulting namespace.
    """
    if namespace is None:
        namespace = {"__builtins__": __builtins__}

    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    full_code = pre_code + "\n" + code if pre_code else code

    try:
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(compile(full_code, "<user_code>", "exec"), namespace)

        return ExecutionResult(
            stdout=stdout_capture.getvalue(),
            stderr=stderr_capture.getvalue(),
            namespace=namespace,
        )
    except SyntaxError as e:
        return ExecutionResult(
            stdout=stdout_capture.getvalue(),
            stderr=stderr_capture.getvalue(),
            error=f"SyntaxError: {e.msg} (line {e.lineno})",
        )
    except Exception as e:
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        # Filter out internal frames
        filtered = []
        for line in tb_lines:
            if "<user_code>" in line or not line.startswith("  File"):
                filtered.append(line)
        return ExecutionResult(
            stdout=stdout_capture.getvalue(),
            stderr=stderr_capture.getvalue(),
            error="".join(filtered).strip(),
        )
