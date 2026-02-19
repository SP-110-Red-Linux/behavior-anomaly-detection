# Log ingestion and parsing subsystem 

# This function reads raw log files and returns all lines
def read_logs(file_path: str) -> list[str]:
    # 'errors="ignore"' to prevent the program from crashing in 
    # case malformed characters are encountered. 
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.readlines()