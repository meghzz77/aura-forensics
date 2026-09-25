import os

os.makedirs("sample_data", exist_ok=True)

# Fragment 1: The start of a critical security breach incident
chunk_1 = """[2026-09-25 10:14:02.114] CRITICAL: Unauthorized root elevation detected on SRV-DB-01.
[2026-09-25 10:14:05.420] AUTH: Token generated for user 'attacker_shadow' originating from IP 198.51.100.42.
[2026-09-25 10:14:12.890] SQL_EXEC: Accessing table 'customer_vault' with payload SELECT * FROM wire_transfers;
[2026-09-25 10:14:18.002] INITIATE_TRANSFER: Source Account: ACCT-99201, Dest IBAN: CH930000000000001, Amount: $"""

# Fragment 2: The severed continuation with transaction & exfiltration details
chunk_2 = """750,000.00 USD. Status: EXECUTED.
[2026-09-25 10:14:24.311] EXFILTRATE: Endpoint hit: sftp://exfil-node.darknet.org:2222 by operator sysadmin_leak@protonmail.com.
[2026-09-25 10:14:31.905] LOG_TAMPER: Shredding syslog audit tables to cover operational trail...
[2026-09-25 10:14:35.000] SHUTDOWN: Host forced hard reset."""

# Corrupted cluster (simulating ransomware overwrite/garbage)
corrupted_chunk = b"\x00\xff\xfe\xaa\x10\x99\x88\x77\x55\x12\x34\xde\xad\xbe\xef" * 20

with open("sample_data/cluster_01_lead.log", "w", encoding="utf-8") as f:
    f.write(chunk_1)

with open("sample_data/cluster_02_tail.log", "w", encoding="utf-8") as f:
    f.write(chunk_2)

with open("sample_data/cluster_03_ransomware.bin", "wb") as f:
    f.write(corrupted_chunk)

print("[✓] Sample evidence generated in sample_data/ directory.")