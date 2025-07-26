# Automated Duplicate File Identification and Removal

This project automates the detection and removal of duplicate files in a specified directory. It uses cryptographic hashing to efficiently identify duplicate files, supports safe removal, and can email a log file with details of all actions performed.

## 🚀 Features

- Scans directories recursively for duplicate files
- Uses SHA-256 hashing for accurate file comparison
- Groups and lists duplicate files
- Option to safely remove redundant files
- Generates a detailed log file of detected and deleted files
- Automatically sends the log file to a specified email address

## 🛠️ How It Works

1. The script walks through the target directory and computes SHA-256 hashes for each file.
2. Files with identical hashes are considered duplicates and grouped together.
3. If the `--delete` flag is used, all but one file in each duplicate group are deleted.
4. A log of all duplicates (and deletions) is created.
5. If configured, the log file is emailed to the user using SMTP.

## 📦 Requirements

- Python 3.x
- Standard Libraries: `os`, `hashlib`, `argparse`, `logging`, `smtplib`, `email`

## 📂 Usage
python duplicate_remover.py /path/to/target/directory
