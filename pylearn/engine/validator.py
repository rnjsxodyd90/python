"""Validate user code against test cases."""

from pylearn.engine.runner import run_code, ExecutionResult


class ValidationResult:
    """Result of validating user code."""

    def __init__(self):
        self.passed = []
        self.failed = []
        self.error = None

    @property
    def success(self):
        return len(self.failed) == 0 and self.error is None

    @property
    def total(self):
        return len(self.passed) + len(self.failed)

    @property
    def summary(self):
        if self.error:
            return f"Error: {self.error}"
        return f"{len(self.passed)}/{self.total} tests passed"


def validate_output(code, expected_output, pre_code=""):
    """Validate that code produces expected stdout output.

    Args:
        code: User's code string.
        expected_output: Expected stdout (stripped for comparison).
        pre_code: Setup code to run before user code.

    Returns:
        ValidationResult
    """
    result = ValidationResult()

    exec_result = run_code(code, pre_code=pre_code)

    if not exec_result.success:
        result.error = exec_result.error
        return result

    actual = exec_result.stdout.strip()
    expected = expected_output.strip()

    if actual == expected:
        result.passed.append({
            "name": "Output matches expected",
            "expected": expected,
            "actual": actual,
        })
    else:
        result.failed.append({
            "name": "Output matches expected",
            "expected": expected,
            "actual": actual,
        })

    return result


def validate_with_tests(code, test_cases, pre_code=""):
    """Validate code against multiple test cases.

    Args:
        code: User's code string.
        test_cases: List of dicts with keys:
            - name: Test name
            - input_code: Code to run after user code (e.g., function calls)
            - expected: Expected output string
        pre_code: Setup code to run before user code.

    Returns:
        ValidationResult
    """
    result = ValidationResult()

    # First, compile and run the user code to get namespace
    exec_result = run_code(code, pre_code=pre_code)
    if not exec_result.success:
        result.error = exec_result.error
        return result

    for test in test_cases:
        test_code = test.get("input_code", "")
        expected = test.get("expected", "").strip()
        name = test.get("name", "Test")

        # Run test code in the same namespace as user code
        test_result = run_code(test_code, namespace=dict(exec_result.namespace))

        if not test_result.success:
            result.failed.append({
                "name": name,
                "expected": expected,
                "actual": f"Error: {test_result.error}",
            })
            continue

        actual = test_result.stdout.strip()
        if actual == expected:
            result.passed.append({
                "name": name,
                "expected": expected,
                "actual": actual,
            })
        else:
            result.failed.append({
                "name": name,
                "expected": expected,
                "actual": actual,
            })

    return result


def validate_with_function(code, validator_fn, pre_code=""):
    """Validate code using a custom validator function.

    Args:
        code: User's code string.
        validator_fn: Function that takes (namespace, stdout) and returns
                      (bool, message) tuple.
        pre_code: Setup code.

    Returns:
        ValidationResult
    """
    result = ValidationResult()

    exec_result = run_code(code, pre_code=pre_code)
    if not exec_result.success:
        result.error = exec_result.error
        return result

    try:
        passed, message = validator_fn(exec_result.namespace, exec_result.stdout)
        entry = {"name": "Custom validation", "expected": "Pass", "actual": message}
        if passed:
            result.passed.append(entry)
        else:
            result.failed.append(entry)
    except Exception as e:
        result.error = f"Validator error: {e}"

    return result
