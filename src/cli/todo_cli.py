"""
CLI interface for the Todo application.
"""
import argparse
from typing import Optional
from src.services.todo_service import TodoService


class TodoCLI:
    """
    Command-line interface for the Todo application.
    """
    def __init__(self, service: TodoService):
        """
        Initialize the CLI with a TodoService.

        Args:
            service: The TodoService instance to use
        """
        self.service = service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the argument parser with all commands."""
        parser = argparse.ArgumentParser(
            description="A Python in-memory console Todo application",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('--title', required=True, help='Task title')
        add_parser.add_argument('--description', help='Task description')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update a task')
        update_parser.add_argument('--id', type=int, required=True, help='Task ID')
        update_parser.add_argument('--title', help='New task title')
        update_parser.add_argument('--description', help='New task description')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('--id', type=int, required=True, help='Task ID')

        # Mark command
        mark_parser = subparsers.add_parser('mark', help='Mark a task as complete/incomplete')
        mark_parser.add_argument('--id', type=int, required=True, help='Task ID')
        mark_parser.add_argument(
            '--status',
            required=True,
            choices=['complete', 'incomplete'],
            help='Mark task as complete or incomplete'
        )

        return parser

    def handle_command(self, args: Optional[argparse.Namespace] = None) -> bool:
        """
        Handle the parsed command arguments.

        Args:
            args: Parsed arguments (if None, will parse from sys.argv)

        Returns:
            True if command executed successfully, False otherwise
        """
        if args is None:
            args = self.parser.parse_args()

        if args.command == 'add':
            return self._handle_add(args.title, args.description)
        elif args.command == 'list':
            return self._handle_list()
        elif args.command == 'update':
            return self._handle_update(args.id, args.title, args.description)
        elif args.command == 'delete':
            return self._handle_delete(args.id)
        elif args.command == 'mark':
            return self._handle_mark(args.id, args.status)
        else:
            self.parser.print_help()
            return False

    def run_interactive(self):
        """Run the CLI in interactive mode."""
        while True:
            self._clear_screen()
            self._print_header()
            self._print_menu()
            
            choice = input("\nSelect an option: ").strip()
            
            if choice == '1':
                self._interactive_add()
            elif choice == '2':
                self._interactive_list()
            elif choice == '3':
                self._interactive_update()
            elif choice == '4':
                self._interactive_mark()
            elif choice == '5':
                self._interactive_delete()
            elif choice == '6':
                print("\nGoodbye!")
                break
            else:
                input("\nInvalid option. Press Enter to continue...")

    def _clear_screen(self):
        """Clear the console screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def _print_header(self):
        print("=========================================")
        print("          PYTHON TODO APP")
        print("=========================================")

    def _print_menu(self):
        print("1. [Add]    Add a new task")
        print("2. [List]   List all tasks")
        print("3. [Update] Update a task")
        print("4. [Mark]   Mark task status")
        print("5. [Delete] Delete a task")
        print("6. [Exit]   Exit application")
        print("=========================================")

    def _interactive_add(self):
        print("\n--- Add New Task ---")
        title = input("Title: ").strip()
        if not title:
            input("Title is required. Press Enter...")
            return
        
        description = input("Description (optional): ").strip()
        self._handle_add(title, description)
        input("\nPress Enter to continue...")

    def _interactive_list(self):
        print("\n--- Task List ---")
        self._handle_list()
        input("\nPress Enter to continue...")

    def _interactive_update(self):
        print("\n--- Update Task ---")
        try:
            task_id_str = input("Task ID: ").strip()
            if not task_id_str: 
                return
            task_id = int(task_id_str)
            
            title = input("New Title (press Enter to keep current): ").strip()
            description = input("New Description (press Enter to keep current): ").strip()
            
            self._handle_update(task_id, title if title else None, description if description else None)
        except ValueError:
            print("Invalid ID format.")
        input("\nPress Enter to continue...")

    def _interactive_mark(self):
        print("\n--- Mark Task ---")
        try:
            task_id_str = input("Task ID: ").strip()
            if not task_id_str:
                return
            task_id = int(task_id_str)
            
            status_input = input("Status (c=complete, i=incomplete): ").strip().lower()
            if status_input in ['c', 'complete']:
                status = 'complete'
            elif status_input in ['i', 'incomplete']:
                status = 'incomplete'
            else:
                print("Invalid status.")
                input("\nPress Enter to continue...")
                return

            self._handle_mark(task_id, status)
        except ValueError:
            print("Invalid ID format.")
        input("\nPress Enter to continue...")

    def _interactive_delete(self):
        print("\n--- Delete Task ---")
        try:
            task_id_str = input("Task ID: ").strip()
            if not task_id_str:
                return
            task_id = int(task_id_str)
            
            confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").lower()
            if confirm == 'y':
                self._handle_delete(task_id)
        except ValueError:
            print("Invalid ID format.")
        input("\nPress Enter to continue...")

    # Shared logic handlers

    def _handle_add(self, title: str, description: Optional[str]) -> bool:
        """Handle adding a task."""
        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def _handle_list(self) -> bool:
        """Handle listing tasks."""
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return True

        print(f"{'ID':<4} {'Status':<10} {'Title':<30} {'Description'}")
        print("-" * 70)

        for task in tasks:
            status = "✓" if task.completed else "○"
            desc = task.description if task.description else ""
            print(f"{task.id:<4} {status:<10} {task.title:<30} {desc}")

        return True

    def _handle_update(self, task_id: int, title: Optional[str], description: Optional[str]) -> bool:
        """Handle updating a task."""
        task = self.service.update_task(task_id, title, description)

        if task is None:
            print(f"Error: Task with ID {task_id} not found")
            return False

        print(f"Task {task_id} updated successfully")
        return True

    def _handle_delete(self, task_id: int) -> bool:
        """Handle deleting a task."""
        success = self.service.delete_task(task_id)

        if not success:
            print(f"Error: Task with ID {task_id} not found")
            return False

        print(f"Task {task_id} deleted successfully")
        return True

    def _handle_mark(self, task_id: int, status_str: str) -> bool:
        """Handle marking a task."""
        completed = status_str == 'complete'
        task = self.service.mark_task(task_id, completed)

        if task is None:
            print(f"Error: Task with ID {task_id} not found")
            return False

        print(f"Task {task_id} marked as {status_str} successfully")
        return True