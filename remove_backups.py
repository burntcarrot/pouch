"""
Utility script to remove backups based on 1-week retention policy.
"""

import os
import filecmp
from datetime import datetime, timedelta

# use dumps directory for backups
os.chdir("dumps")


# retention policy = 1 week
# backups older than 1 week are removed from dumps

latest, *recent = sorted(os.listdir())[::-1]
latest_ctime = datetime.fromtimestamp(os.stat(latest).st_ctime)

previous_file_ctime = latest_ctime
for f in recent:
  ctime = datetime.fromtimestamp(os.stat(f).st_ctime)

  if latest_ctime - ctime < timedelta(days=7):
    if filecmp.cmp(latest, f):
      os.unlink(f)  # Remove similar files
  elif previous_file_ctime - ctime < timedelta(days=7):
    os.unlink(f)  # Remove less than 1 week apart
  elif latest_ctime - ctime < timedelta(days=180):
    os.unlink(f)  # Remove older than 180 days

  previous_file_ctime = ctime
