import csv
import re

input_file = "60000.txt"
progress_csv = "progress_data.csv"
summary_csv = "summary_data.csv"

progress_rows = []
summary_rows = []

# Regex patterns
progress_pattern = re.compile(
    r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}:\d+)\s+"
    r"(?P<seconds>\d+)\s+sec:\s+"
    r"(?P<operations>\d+)\s+operations;\s+"
    r"(?P<ops_per_sec>[\d.]+)\s+current ops/sec"
)

summary_pattern = re.compile(
    r"\[(?P<section>[A-Z_]+)\],\s*(?P<metric>[^,]+),\s*(?P<value>.+)"
)

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()

        # Match progress lines
        progress_match = progress_pattern.search(line)
        if progress_match:
            progress_rows.append(progress_match.groupdict())
            continue

        # Match summary lines
        summary_match = summary_pattern.search(line)
        if summary_match:
            summary_rows.append(summary_match.groupdict())

# Write progress CSV
if progress_rows:
    with open(progress_csv, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["datetime", "seconds", "operations", "ops_per_sec"]
        )
        writer.writeheader()
        writer.writerows(progress_rows)

# Write summary CSV
if summary_rows:
    with open(summary_csv, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["section", "metric", "value"]
        )
        writer.writeheader()
        writer.writerows(summary_rows)

print("Conversion complete:")
print(f"- Progress data → {progress_csv}")
print(f"- Summary data  → {summary_csv}")

