from pathlib import Path
from argparse import ArgumentParser


def file_is_valid(
    path: Path, fix: bool, match: list, ignore: list, verbose: bool
) -> bool:
    """
    Processes a file and optionally fixes it.
    """
    if any(map(lambda fragment: fragment in str(path.absolute()), ignore)):
        return True
    elif (match is None) or any(
        map(lambda fragment: fragment in str(path.absolute()), match)
    ):
        with open(path, "r") as f:
            try:
                lines = f.readlines()
            except:
                if verbose:
                    print(f"Skipping {path} (couldn't read lines)")
                return True
        if len(lines) == 0:
            lines = [""]
        if lines[-1].endswith("\n"):
            return True
        else:
            if fix:
                lines[-1] += "\n"
                with open(path, "w") as f:
                    f.writelines(lines)
                if verbose:
                    print("Added newline to file {}".format(path))
                return True
            else:
                if verbose:
                    print("{} does not end with a newline".format(path))
                return False
    else:
        return True


def folder_is_valid(
    path: Path, fix: bool, match: list, ignore: bool, verbose: bool
) -> bool:
    """
    Processes a folder recursively, optionally fixing files.
    """
    if any(map(lambda fragment: str(path.absolute()) in fragment, ignore)):
        return True
    else:
        valid = True
        for p in path.iterdir():
            if p.is_dir():
                valid = (
                    folder_is_valid(p, fix, match, ignore, verbose) and valid
                )
            elif p.is_file():
                valid = file_is_valid(p, fix, match, ignore, verbose) and valid
        return valid


def path_is_valid(
    path: Path, fix: bool, match: list, ignore: list, verbose: bool
) -> bool:
    """
    Processes a path, either a folder or a file.
    """
    if path.is_dir():
        return folder_is_valid(path, fix, match, ignore, verbose)
    else:
        return file_is_valid(path, fix, match, ignore, verbose)


def cli():
    parser = ArgumentParser(description="Check if files end in newlines.")
    parser.add_argument(
        "path", help="File to check or folder to recurse into."
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Fix files that don't end in newlines.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print file names."
    )
    parser.add_argument(
        "--match",
        nargs="*",
        help="Only check files matching this pattern.",
        default=[".py", ".yaml", ".yml"],
    )
    parser.add_argument(
        "--ignore",
        nargs="*",
        help="Ignore filepaths containing these.",
        default=[
            ".pytest_cache",
            ".git",
            "_build",
            ".ipynb",
            ".pyc",
            "__pycache__",
            "node_modules",
            ".js",
        ],
    )
    args = parser.parse_args()
    if path_is_valid(
        Path(args.path), args.fix, args.match, args.ignore, args.verbose
    ):
        print("All files end in newlines.")
    else:
        print("Some files do not end in newlines.")
        exit(1)


if __name__ == "__main__":
    cli()
