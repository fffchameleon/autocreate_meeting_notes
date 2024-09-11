import pygsheets
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import subprocess

def get_row_variable():
    with open('cur_row.conf', 'r') as file:
        row_variable = int(file.readline().strip())
    return row_variable

def update_row_variable(row_variable):
    with open('cur_row.conf', 'w') as file:
        file.write(str(row_variable))

# wks.export(pygsheets.ExportType.CSV)
def get_meeting_date():
    load_dotenv()
    gc = pygsheets.authorize(service_file=os.getenv("SHEET_KEY_PATH"))
    sht = gc.open_by_url(os.getenv("SHEET_URL"))

    wks = sht[0]

    df = pd.DataFrame(wks.get_all_values())
    
    row_variable = get_row_variable()
    target_month = (df[0][row_variable])
    target_day = (df[1][row_variable])
    
    meeting_date = target_month + "/" + target_day
    presentation_people = df[3][row_variable].split('、')
    follow_up = df[4][row_variable].split('、')
    update_row_variable(row_variable + 1)
    print(f"get meeting date: {meeting_date}, get presentation people: {presentation_people}, get follow up people: {follow_up}")
    print(f"new cur_row.conf updated, new row variable: {get_row_variable()}")
    return meeting_date, presentation_people, follow_up

if __name__ == "__main__":
    get_meeting_date()