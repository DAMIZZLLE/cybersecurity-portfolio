# Course 6: Automate Cybersecurity Tasks with Python

This course introduced the basics of Python programming and how to apply Python to automate cybersecurity tasks.

---

## 🧠 Key Concepts Learned

- **Python Fundamentals:** Syntax, variables, loops, functions, conditionals.
- **Working with Files:** Read, write, and process text files.
- **Use of Libraries:** `os`, `re`, `datetime`, and others for scripting and automation.
- **Regular Expressions (RegEx):** Searching, matching, and manipulating text.
- **Parsing Logs:** Analyzing security logs and filtering relevant data.
- **Data Structures:** Lists, dictionaries, and how to iterate over them for analysis.

---

## 🛠️ Tools & Skills Practiced

- Writing reusable Python functions
- Regex for pattern matching
- Log analysis automation scripts
- Scripting file operations (e.g., extracting log lines with errors)
- Creating and using Python scripts in a terminal

---

## 📁 Sample Task

> **Scenario:** Automate the extraction of suspicious IP addresses from a log file using Python and RegEx.

```python
import re

with open("server_log.txt", "r") as file:
    logs = file.readlines()

suspicious_ips = []

for line in logs:
    if "FAILED LOGIN" in line:
        match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
        if match:
            suspicious_ips.append(match.group())

print("Suspicious IPs:", suspicious_ips)
