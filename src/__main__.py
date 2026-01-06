"""
Main entry point for the Python Todo application.
"""
from src.services.todo_service import TodoService
from src.cli.todo_cli import TodoCLI


def main():
    """Main entry point for the application."""
    # Initialize the service and CLI
    service = TodoService()
    cli = TodoCLI(service)

    # Check if any arguments were provided (excluding the script name)
    import sys
    
    if len(sys.argv) > 1:
        # Arguments provided, run in one-off logic mode
        cli.handle_command()
    else:
        # No arguments, run in interactive loop mode
        cli.run_interactive()


if __name__ == "__main__":
    main()