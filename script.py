import requests
import json
import os
from dotenv import load_dotenv
import re
from create_template import create_template
from sheets import get_meeting_date

load_dotenv()
API_TOKEN = os.getenv("HACKMD_TOKEN")

def get_note_details():
    meeting_time, presentation_people, followup_people = get_meeting_date()
    return meeting_time, presentation_people, followup_people

def create_hackmd_note(meeting_time, new_note_content):
    create_note_url = "https://api.hackmd.io/v1/notes"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    new_note_data = {
        "title": f"New note for {meeting_time}",
        "content": new_note_content,
        "readPermission": "guest",
        "writePermission": "signed_in",
        "commentPermission": "everyone"
    }

    response = requests.post(create_note_url, headers=headers, data=json.dumps(new_note_data))
    
    if response.status_code == 201:
        print("Note created successfully!")
        return response.json()
    else:
        print(f"Failed to create note: {response.status_code}")
        print(response.text)
        return None

def get_existing_note_content(note_id):
    update_note_url = f"https://api.hackmd.io/v1/notes/{note_id}"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(update_note_url, headers=headers)

    if response.status_code == 200:
        return response.json()["content"]
    else:
        print(f"Failed to get existing note: {response.status_code}")
        return None

def update_existing_note(note_id, updated_content):
    update_note_url = f"https://api.hackmd.io/v1/notes/{note_id}"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    update_data = {
        "content": updated_content,
        "readPermission": "guest",
        "writePermission": "signed_in"
    }

    response = requests.patch(update_note_url, headers=headers, data=json.dumps(update_data))

    if response.status_code == 202:
        print("Existing note updated successfully with the new link!")
    else:
        print(f"Failed to update the existing note: {response.status_code}")
        print(response.text)

def process_meeting_notes():
    meeting_time, presentation_people, followup_people = get_note_details()

    new_note_content = create_template(meeting_time, presentation_people, followup_people)

    new_note_info = create_hackmd_note(meeting_time, new_note_content)

    if new_note_info:
        to_be_modified_notes_id = os.getenv("HACKMD_NOTEID")
        existing_note_content = get_existing_note_content(to_be_modified_notes_id)

        if existing_note_content:
            new_note_link = f"- [{meeting_time} meeting](/{new_note_info['id']})"
            updated_content = existing_note_content.replace("## Current meeting", f"## Current meeting\n{new_note_link}")
            
            update_existing_note(to_be_modified_notes_id, updated_content)

if __name__ == "__main__":
    process_meeting_notes()
