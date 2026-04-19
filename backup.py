import os
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, DownloadColumn
from rich.theme import Theme

# Custom Theme for Premium Look
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
})

console = Console(theme=custom_theme)

def create_backup(source: str, destination: str):
    """
    Core logic to backup files/directories.
    """
    source_path = Path(source).resolve()
    dest_base = Path(destination).resolve()

    if not source_path.exists():
        console.print(f"[error]Error:[/error] Source path '{source_path}' does not exist.")
        return

    # Create timestamped folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"backup_{timestamp}"
    final_dest = dest_base / backup_folder_name

    try:
        console.print(Panel.fit(
            f"[info]Starting Backup Operation[/info]\n"
            f"[cyan]Source:[/cyan] {source_path}\n"
            f"[cyan]Destination:[/cyan] {final_dest}",
            title="OmniBackup v1.0",
            border_style="cyan"
        ))

        # Ensure destination parent exists
        final_dest.parent.mkdir(parents=True, exist_ok=True)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            DownloadColumn(),
            transient=True,
        ) as progress:
            
            task = progress.add_task("[cyan]Copying files...", total=None)
            
            if source_path.is_dir():
                shutil.copytree(source_path, final_dest / source_path.name)
            else:
                final_dest.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, final_dest / source_path.name)
            
            progress.update(task, completed=100)

        console.print(f"\n[success]✨ Success![/success] Backup completed at {final_dest}")

    except Exception as e:
        console.print(f"[error]CRITICAL FAILURE:[/error] {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="OmniBackup: Premium CLI Backup Tool")
    parser.add_argument("source", help="Source file or directory to backup")
    parser.add_argument("destination", help="Destination directory where backups will be stored")
    
    args = parser.parse_args()
    
    create_backup(args.source, args.destination)

if __name__ == "__main__":
    main()
