# a.voss@fh-aachen.de


def version(n: int) -> str:
    return f"1.2.3-{n}"  # same as in pyproject.toml


if __name__ == "__main__":
    print(f"Version 23: {version(23)}")


"""

https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://choosealicense.com/licenses/mit/
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps cbl_test_package   

"""
