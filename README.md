# 🔍 Log Analyzer — Python Fundamentals Project

A simple Python-based log analyzer that parses the Linux `auth.log` file to extract:

- 🛠 Command usage by users
- 👤 New or deleted users
- 🔑 Password changes
- 🔐 Sudo/Su command usage
- ❌ Failed sudo attempts

This project was developed as part of learning Python fundamentals while applying practical cybersecurity concepts.

---

## 📂 Project Structure
log-analyzer/
├── log_analyzer.py
├── README.md


---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| **Command Tracking** | Extracts all executed commands found in `auth.log` using `sudo` or direct commands |
| **User Monitoring** | Detects and displays new users, deleted users, and password changes |
| **Privilege Use** | Parses use of `su` and `sudo`, including failed authentication attempts |
| **Interactive CLI** | Menu-driven interface with clear prompts and progress indicators |

---

## 📸 Sample Output

[] Extract command usage.
[] Processing log data... Please wait.

[1]
[] Timestamp: Jun 30 12:45:23
[] Executing user: john
[*] Command used: apt install nmap


---

## ⚙️ Requirements

- Python 3.x
- `pyfiglet` (`pip install pyfiglet`)
- Read access to `/var/log/auth.log` (typically requires sudo)

---

## 💡 How to Use

```bash
$ sudo python3 log_analyzer.py

Then, follow the on-screen options:

1) Extract command usage
2) Monitor user authentication changes
q) Quit

