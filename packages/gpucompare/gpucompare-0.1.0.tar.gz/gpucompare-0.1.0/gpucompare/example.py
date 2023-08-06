"""Example of code."""


def gpu_name(name: str) -> str:
    """Print GPU name.

    Args:
        name (str): Name to print.

    Returns:
        str: message

    Examples:
        .. code:: python

            >>> gpu_name("Tesla T4")
            'GPU: Tesla T4!'
    """
    return f"GPU: {name}!"
