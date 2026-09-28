# Timestamp Logger

from datetime import datetime

log_file = "file-handling/activity.log"

current_time = datetime.now()

message = f"Lesson completed at: {current_time}"

with open(log_file, "a") as file:
    file.write(message + "\n")

print("Timestamp added to log!")