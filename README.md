# OmniBackup: Precision CLI Backup Tool

OmniBackup is a lightweight yet powerful command-line interface (CLI) tool designed for seamless file and directory backups. Built with performance and user experience in mind, it provides a "premium" terminal experience while ensuring your da ta remains safe.

## ✨ Features

- **Recursive Backups**: Effortlessly backup entire directory structures. 
- **Smart Versioning**: Automatically creates timestamped backup folders to prevent overwrites.
- **Visual Feedback**: Beautiful terminal UI using `Rich` for progress tracking and status reports.
- **Flexible Targets**: Supports both single files and complex directory trees.
- **Dry Run Support**: (Upcoming) Preview backup operations before execution.
 
## Installation st
1. **Clone the repository:**
   ```bash
   git clone https://github.com/USER_NAME/OmniBackup.git
   cd OmniBackup
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Usage

### Basic Backup
Backup a file or directory to a specific destination:
```bash
python backup.py source_path destination_path
```

### Example
```bash
python backup.py ./docs ./backups
```
*This will create a folder like `./backups/backup_20260420_123045/docs`.*

## 📂 Project Structure
- `backup.py`: Core logic and CLI interface.
- `requirements.txt`: Essential dependencies.
- `README.md`: You are here!

## 🛡️ Security & Reliability
OmniBackup uses standard Python `shutil` and `pathlib` modules to ensure cross-platform compatibility and reliable file system operations.

---
*Created with precision by OmniBackup Team.*
