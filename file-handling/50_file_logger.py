# Simple File Logger

log_file = "file-handling/activity.log"

message = "Python File Handling lesson completed."

with open(log_file, "a") as file:
    file.write(message + "\n")

print("Activity logged successfully!")
