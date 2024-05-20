# script.py
import sys
import os
from datetime import datetime

def main():
    who_to_greet = sys.argv[1]
    print(f"Hello {who_to_greet}")
    current_time = datetime.now().isoformat()

    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        print(f"time={current_time}", file=f)

if __name__ == "__main__":
    main()
