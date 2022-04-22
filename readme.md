# Overview

Since the current version of Hold'em Manager 3 cannot import WPN tournament summaries properly, I've written
this simple script to import them manually from SharkScope.

After results have posted to SharkScope, one can download a CSV of all of their results.

This script currently requires you to install Python 3 on your system. This is written as I have used it, and only provieded here in case anyone else is interested. Future versions may be a standalone executable if
there is enough interest.

# Useage

** BACK UP YOUR HM3 DATABASE BEFORE ATTEMPTING THIS. While this operation should generally be pretty safe, I cannot be
held responsible for any data loss resulting from the use of this script. **

Ensure HM3 is closed during this operation.

1. Download your tournament results from SharkScope in CSV format (this costs 25 'searches' and is available to premium members).

2. Move it to the same directory as the script and rename it 'tourneys.csv'.

3. Open the python script, and edit lines 5 and 6 to reflect your WPN username and the location of your HM3 database (the default location is provided).
```python
    db_file = 'C:\HM3 Files\Databases\MyHM3Database.hmdb'
    player_name = 'yourWPNname'
```
4. Open a terminal in the run the script (e.g. ```py3 hm3fix.py```). The script will parse the CSV file and start writing your SharkScope results into HM3.

If all goes well, your HM3 results should now be totally congruent with SharkScope.
