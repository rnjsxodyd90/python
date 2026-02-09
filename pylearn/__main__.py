"""Allow running as: python -m pylearn"""

import sys


def cli():
    """Handle CLI arguments before launching the app."""
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print("Usage: pylearn [options]")
        print()
        print("Options:")
        print("  -h, --help             Show this help message")
        print("  -v, --version          Show version")
        print("  --reset-progress       Clear all progress data")
        return

    if "--version" in args or "-v" in args:
        from pylearn.config import APP_NAME, APP_VERSION
        print(f"{APP_NAME} {APP_VERSION}")
        return

    if "--reset-progress" in args:
        from pylearn.config import PROGRESS_FILE
        import os
        if os.path.exists(PROGRESS_FILE):
            confirm = input("This will erase all progress. Are you sure? [y/N] ")
            if confirm.lower() == "y":
                os.remove(PROGRESS_FILE)
                print("Progress reset.")
            else:
                print("Cancelled.")
        else:
            print("No progress file found.")
        return

    from pylearn.app import main
    main()


cli()
