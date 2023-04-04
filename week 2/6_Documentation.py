#use dir to get list of functions on type
print(dir(str))

#use ? to get description <- (?)

#use docstring to doc code
def test(var : int):
    """adds one to var

    Args:
        var (int): any integer number

    Returns:
        int: input + 1
    """
    return var + 1

test()