"""Custom errors to throw
"""


class CDKVersionError(Exception):
    """Incorrect CDK version installed."""
    def __init__(self, v_installed, v_required):
        print(f"Error: Foundaws-cdk-lib {v_installed} != {v_required}")


