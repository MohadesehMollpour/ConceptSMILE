# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Small installation check for ``python -m conceptsmile``."""

from conceptsmile import __version__


def main() -> None:
    """Print the installed package version."""
    print(f"ConceptSMILE {__version__}")


if __name__ == "__main__":
    main()

