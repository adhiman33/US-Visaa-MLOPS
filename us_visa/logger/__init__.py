# import logging
# import os
# from from_root import from_root
# from datetime import datetime

# import os

# log_dir = os.path.join(from_root(), 'logs')
# if not os.path.exists(log_dir):
#     print(f"Log directory {log_dir} does not exist. Creating it.")
#     os.makedirs(log_dir, exist_ok=True)
# else:
#     print(f"Log directory {log_dir} already exists.")

# # print(from_root)
# # Create the log file name based on the current date and time
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# # Define the logs directory
# log_dir = os.path.join(from_root(), 'logs')

# # Ensure the directory exists or create it
# os.makedirs(log_dir, exist_ok=True)

# # Full path to the log file
# logs_path = os.path.join(log_dir, LOG_FILE)

# # Configure logging
# logging.basicConfig(
#     filename=logs_path,
#     format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG,
# )

# logging.info("Logging has started!")


import logging
import os
from datetime import datetime

# Use raw string for the directory path to avoid escape characters issues
log_directory = r"C:\Users\Admin\Desktop\MAJOR_PROJECT\US-Visaa-MLOPS\logs"

# Check if directory exists, create if not
if not os.path.exists(log_directory):
    os.makedirs(log_directory)  # Create the logs directory if it doesn't exist

# Log file path with timestamp
log_file = os.path.join(log_directory, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# # Test logging
# logging.info("Logging is configured properly.")
# print(f"Log directory path: {log_directory}")
# print(f"Log file path: {log_file}")

