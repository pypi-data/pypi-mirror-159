"""

Calculator module does simple arithmetic operations.

Calulator module to to loaded as part of calculator package.
The calculator accepts strings, floats and ints and handles None.
One nifty feature is that it can find root of negative numbers,
if n in nth root is odd int.
For the future: a high-precision sum function will be developed.
Which will give precise floating point results, unlike naive sum function.

Usage:
------

    $ calculator.py funcName(arg)
    funcName = [add, subtract, multiply, divide, power, root]
    arg = [int, float, str, None]

Classes:
--------

    Calculator

Functions:
----------

    to_float(str) -> Optional[float]
    check_str_valid(object) -> bool

"""


from typing import Union, Optional


__all__ = ["Calculator"]


class Calculator:
    """
    This is a class that contains methods the basic math operations.

    The class Calculator contains:
    -> attributes:
        -->memory (float)
    -> methods to perform basic math operations:
        --> add(n) => adds n to memory
        --> subs(n) => subtracts n from memory
        --> mul(n) => multiplies n with memory
        --> div(n) => divides memory by n
        --> root(n) => nth root of memory
        --> reset() => (resets memory to 0)

    """

    def __init__(self) -> None:
        """
        Construct objects from the class Calculator.

        This function initializes the Calculator class setting it's
        memory to 0, and then prints the value in memory.

        Doc Test Examples:
        -----------

        >>> calc=Calculator()
        0
        """
        self.memory: float = 0
        print(self.memory)

    def add(self, num_add: Union[int, str, float]) -> float:
        """
        Add input Arg to memory, update sum in memory and print it.

        Doc Test Examples:
        -----------

        >>> calc=Calculator()
        0
        >>> calc.add(15)
        15.0
        >>> calc.add('35')
        50.0
        >>> calc.add(5.5)
        55.5
        >>> calc.add(None)
        55.5
        >>> calc.add('gre')
        Your string: 'gre' => <class 'str'> contains non-digit values
        55.5
        >>> calc.add('0.05')
        55.55
        >>> calc.add('        -0.05 ')
        55.5
        >>> calc.add(-1)
        54.5
        >>> calc.add(-1.0)
        53.5
        >>> calc.add(-0.1)
        53.4
        """
        if num_add is None:
            return self.memory
        if Calculator.to_float(num_add) is None:
            return self.memory
        num_add = Calculator.to_float(num_add)  # type: ignore # mypy bug
        self.memory += num_add  # type: ignore # mypy has no Optional type
        self.memory = round(self.memory, 10)
        return self.memory

    def subtract(self, arg_to_subtract: Union[int, str, float]) -> float:
        """
        Substract arg from memory, update memory and print it.

        Doc Test Examples:
        -----------
        >>> calc=Calculator()
        0
        >>> calc.subtract(15)
        -15.0
        >>> calc.subtract('       -35         ')
        20.0
        >>> calc.subtract(-5.5)
        25.5
        >>> calc.subtract(None)
        None type is not allowed
        25.5
        """
        if arg_to_subtract is None:
            print("None type is not allowed")
            return self.memory
        arg_to_subtract = Calculator.to_float(arg_to_subtract)  # type: ignore
        self.memory -= arg_to_subtract  # type: ignore # mypy bugs
        self.memory = round(self.memory, 10)
        return self.memory

    def multiply(self, num_mul: Union[int, str, float]) -> float:
        """
        Multiply arg with memory, update memory and print it.

        Doc Test Examples:
        -----------

        >>> calc=Calculator()
        0
        >>> calc.add(5)
        5.0
        >>> calc.multiply(6)
        30.0
        >>> calc.multiply('           -1.11        ')
        -33.3
        >>> calc.multiply(None)
        None type is not allowed
        -33.3
        """
        if num_mul is None:
            print("None type is not allowed")
            return self.memory
        self.memory *= Calculator.to_float(num_mul)  # type: ignore
        self.memory = round(self.memory, 10)
        return self.memory

    def divide(self, num_div: Union[int, str, float]) -> float:
        """
        Divide memory by arg, update memory and print it.

        Exception:
            Cannot divide by zero

        Doc Test Examples:
        -----------

        >>> calc=Calculator()
        0
        >>> calc.memory = 300
        >>> calc.divide(100)
        3.0
        >>> calc.divide('0')
        Cannot do division by zero
        3.0
        >>> calc.divide('         -1.          ')
        -3.0
        >>> calc.divide(None)
        None type is not allowed
        -3.0
        """
        if num_div is None:
            print("None type is not allowed")
            return self.memory
        num_div = Calculator.to_float(num_div)  # type: ignore # mypy bug
        if abs(num_div) > 0:  # type: ignore # mypy unable to infer type
            self.memory /= num_div  # type: ignore
            return self.memory  # type: ignore # mypy bug
        print(
            "Cannot do division by zero"
        )
        self.memory = round(self.memory, 10)
        return self.memory

    def reset(self) -> float:
        """
        Reset memory of the calculator to 0.

        Doc Test Examples:
        -----------

        >>> calc=Calculator()
        0
        >>> calc.memory = 875874
        >>> calc.memory
        875874
        >>> calc.reset()
        0
        """
        self.memory = 0
        return self.memory

    def root(self, nth_root: Union[int, str, float]) -> float:
        """
        Perform the nth root of memory, update memory and print it.

        Doc Test Examples:
        -----------

        >>> calc=Calculator()
        0
        >>> calc.memory = 100
        >>> calc.root(2)
        10.0
        >>> calc.memory = 100
        >>> calc.root("      2.0 ")
        10.0
        >>> calc.memory = 2182
        >>> calc.root(2)
        46.7118828565
        >>> calc.memory = -2182
        >>> calc.root(9)
        -2.3495455051
        >>> calc.memory = -2182
        >>> calc.root(4)
        Cannot do root of negative number with even root
        -2182
        """
        if isinstance(nth_root, int) and self.memory < 0 and nth_root % 2 != 0:
            self.memory = round(-(abs(self.memory) ** (1 / nth_root)), 10)
            return self.memory
        if isinstance(nth_root, int) and self.memory < 0 and nth_root % 2 == 0:
            print(
                "Cannot do root of negative number with even root"
            )
            return self.memory
        nth_root = Calculator.to_float(nth_root)  # type: ignore # mypy bug
        if (nth_root < 0) and (self.memory == 0):  # type: ignore
            print(
                "Cannot divide by zero"
            )
            return self.memory
        if (0 < nth_root < 0.001) and (self.memory > 1):  # type: ignore
            print(
                "for root, min float number is 0.001, try again"
            )
            return round(self.memory, 10)
        self.memory = round(self.memory ** (1 / nth_root), 10)  # type: ignore
        return self.memory

    @staticmethod
    def to_float(input_: Union[int, str, float, None]) -> Optional[float]:
        """
        Convert arg to float if can be, if not possible, handle it.

        Doc Test Examples:
        ------------

        >>> Calculator.to_float(225)
        225.0
        >>> Calculator.to_float('12136.77')
        12136.77
        >>> Calculator.to_float('24notanumber')
        Your string: '24notanumber' => <class 'str'> contains non-digit values
        >>> Calculator.to_float(5.0)
        5.0
        >>> Calculator.to_float(None)
        Type-Error. Is it None? Error input: None => <class 'NoneType'>
        """
        if isinstance(input_, str):
            input_ = input_.strip()
            sign: float = 1
            if input_[0] == '-':
                sign = -1
                input_ = input_[1:]
            if not Calculator.check_str_valid(input_):
                print(
                    f"Your string: '{input_}' => {type(input_)} "
                    "contains non-digit values"
                )
                return None  # type: ignore # mypy bug: no Optional
            return float(input_) * sign
        try:
            input_ = float(input_)  # type: ignore # mypy bug: no Optional
        except ValueError:
            print(
                f"Input numerical values. "
                f"Error input: {input_} => {type(input_)}"
            )
            return None
        except TypeError:
            print(
                f"Type-Error. Is it None? "
                f"Error input: {input_} => {type(input_)}"
            )
            return None
        except NameError:
            print(
                f"Name-Error. Is it Undefined? "
                f"Error input: {input_} => {type(input_)}"
            )
            return None
        return input_

    @staticmethod
    def check_str_valid(element: str) -> bool:
        """
        Check if the input string is a valid number.

        _description_
        To make the function complete as a complete standalone function
        We strip the string of white-spaces.
        If the string is empty, it returns False (default value)

        Args:
            element (str): The string to be checked

        Returns:
            bool: True if string can be converted to a float, False otherwise

        Doc Test Examples:
        -----------

        >>> Calculator.check_str_valid('5')
        True
        >>> Calculator.check_str_valid('5.0')
        True
        >>> Calculator.check_str_valid('5.0 ')
        True
        >>> Calculator.check_str_valid('5.0  f')
        False
        >>> Calculator.check_str_valid('')
        False
        >>> Calculator.check_str_valid(' ')
        False
        >>> Calculator.check_str_valid(None)
        False

        """
        if element is None:
            return False

        partition = element.strip().partition('.')

        if element.isdigit():
            return True

        if ((
            (partition[0].isdigit()
                and partition[1] == '.'
                and partition[2].isdigit())
        )):
            return True
        if ((
            (partition[0] == ''
                and partition[1] == '.'
                and partition[2].isdigit())
        )):
            return True
        if ((
            (partition[0].isdigit()
                and partition[1] == '.'
                and partition[2] == '')
        )):
            return True
        return False


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())


# Tested with:
#     pyflakes,  = no errors
#     flake8,    = no errors
#     pylint,    = code has been rated at 10.00/10
#     mypy*,     = Success: no issues found in 1 source file
#     pydocstyle = no errors
#     doctest    = TestResults(failed=0, attempted=55)

#     * mypy and Typing module have bugs. Typing doesn't support in-line lambda
#     * mypy !support in-line lambda, Callable and Optional across functions
#     * bugs documented in Github https://github.com/python/mypy/issues/13064
