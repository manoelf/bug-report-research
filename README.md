# bug-report-research

Research about bug reports at Federal University of Campina Grande

## Organization

- download_script
- extracting
  - Responsible for casualties extract information
    downlowad_script/data/
- get_ids
  - Folder for manual extraction of report id's

## Steps to Run

### Download

- Perform manual extraction of reports id's
- Save "id's" in "download_script/bugs_ids.txt"
- In "download_script" folder, run
  > python3 download_data.py

### Extract Information

- Create a text file with the header of the information you want to collect
- Update "extracting_info.py" variables to contain the new name
- Run the command below
  > python3 extracting_info.py
