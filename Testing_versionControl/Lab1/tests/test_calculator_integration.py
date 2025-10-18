from io import StringIO
from contextlib import redirect_stdout
import builtins
from src.calculator import main


def test_simple_addition():
    user_inputs = ["1", "2", "3", "no"]
    builtins.input = lambda _: user_inputs.pop(0)

    output = StringIO()
    with redirect_stdout(output):
        main()

    result = output.getvalue()

    assert "The result is: 5" in result
    assert "Goodbye!" in result
