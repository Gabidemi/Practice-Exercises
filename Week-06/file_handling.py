import os
FILENAME = 'interactions.txt'
# ── 1. Create the log file (write mode) ─────────────────────────────
def create_log():
    with open(FILENAME, 'w') as f:
        f.write('=== Customer Interaction Log ===\n')
        f.write('Date | Customer | Issue | Rep\n')
        f.write('-' * 60 + '\n')
    print(f'Log created: {FILENAME}')

# ── 2. Append new records (append mode + writelines) ─────────────────
def append_records(entries):
    records = [f'{date} | {cust:<15} | {issue:<15} | {rep}\n'
for date, cust, issue, rep in entries]
    with open(FILENAME, 'a') as f:
        f.writelines(records)
    print(f'{len(records)} record(s) appended.')

# ── 3. Read entire log (read mode + .read()) ─────────────────────────
def display_log():
    try:
        with open(FILENAME, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('Log not found. Run option 1 to create it.')

# ── 4. Search by customer name (readlines + filter) ──────────────────
def search_customer(name):
    try:
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
        matches = [l for l in lines if name.lower() in l.lower()]
        if matches:
            print(f'Found {len(matches)} record(s) for "{name}":')
            print(''.join(matches))
        else:
            print(f'No records found for "{name}".')
    except FileNotFoundError:
        print('Log not found. Run option 1 to create it.')

# ── 5. Count entries + update header (r+ mode) ───────────────────────
def update_entry_count():
    try:
        with open(FILENAME, 'r+') as f:
            lines = f.readlines()
            count = sum(1 for l in lines[1:] if l.strip() and not l.startswith('-'))
            lines[0] = f'=== Customer Interaction Log | Entries: {count} ===\n'
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        print(f'Header updated. Total entries: {count}')
    except FileNotFoundError:
        print('Log not found. Run option 1 to create it.')


# ── 6. Read header only (readline) ───────────────────────────────────
def show_header():
    try:
        with open(FILENAME, 'r') as f:
            header = f.readline()
            print('Header:', header.strip())
    except FileNotFoundError:
        print('Log not found.')

# ── Main menu ────────────────────────────────────────────────────────
SAMPLE = [
('2025-05-01', 'Alice Nguyen', 'Billing query', 'J. Park'),
('2025-05-01', 'Bob Carter', 'Login issue', 'S. Diaz'),
('2025-05-02', 'Carol Singh', 'Refund request', 'J. Park'),
('2025-05-02', 'Alice Nguyen', 'Follow-up', 'M. Lee' ),
]
def main():
    while True:
        print('\n=== Customer Log Manager ===')
        print('1 Create / reset log')