# Main file for integration  

from src.parser import read_logs

# Main execution function 
def main():
    print("SP-110-TESTING")

    # Define the filepath for the parser to access authentication logs
    log_path = "data/raw/auth.log"

    # Using the parser subsystem, read all lines in auth.log
    lines = read_logs(log_path)

    # Print statement for confirmation 
    print(f"Successfully loaded {len(lines)} lines from {log_path}")

    # For verification of accurate file reading, print the first 5 lines (temporary)
    print("\nVerifying first 5 lines: ")
    for line in lines[:5]:
        print(line.rstrip())



if __name__ == "__main__":
    main()
