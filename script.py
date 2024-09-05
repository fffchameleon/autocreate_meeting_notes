import requests
import json
import os
from dotenv import load_dotenv
import pygsheets
import re
from create_template import create_template
load_dotenv()

## TODO: link to google sheet to get meeting detailed information
meeting_time = "9/12 meeting"
presentation_people = ["敬淇", "宥成"]
followup_people = ['志翔', '昭融']

new_note_content = create_template(meeting_time, presentation_people, followup_people)

API_TOKEN = os.getenv("HACKMD_TOKEN")
to_be_modified_notes_id = os.getenv("HACKMD_NOTEID")

create_note_url = "https://api.hackmd.io/v1/notes"
update_note_url = f"https://api.hackmd.io/v1/notes/{to_be_modified_notes_id}"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

new_note_data = {
    "title": "New note from Python",
    "content": new_note_content,
    "readPermission": "guest",  # Options: 'owner', 'signed_in', 'guest'
    "writePermission": "signed_in",  # Options: 'owner', 'signed_in', 'guest'
    "commentPermission": "everyone"  # Options: 'disabled', 'forbidden', 'owners', 'signed_in_users', 'everyone'
}

response = requests.post(create_note_url, headers=headers, data=json.dumps(new_note_data))

if response.status_code == 201:
    print("Note created successfully!")
    note_info = response.json()
    print("Note ID:", note_info['id'])
    print("Note Title:", note_info['title'])
    print("Note Content:", note_info['content'])
    print("Note URL:", note_info['publishLink'])
    
    existing_note_response = requests.get(update_note_url, headers=headers)
    
    if existing_note_response.status_code == 200:
        existing_note_content = existing_note_response.json()["content"]
        
        ## TODO: remove last week note to past meeting section
        new_note_link = f"- [{meeting_time}](/{note_info['id']})"
        updated_content = existing_note_content.replace("## Current meeting", f"## Current meeting\n{new_note_link}")

        update_data = {
            "content": updated_content,
            "readPermission": "guest",
            "writePermission": "signed_in"
        }

        patch_response = requests.patch(update_note_url, headers=headers, data=json.dumps(update_data))

        if patch_response.status_code == 202:
            print("Existing note updated successfully with the new link!")
        else:
            print(f"Failed to update the existing note: {patch_response.status_code}")
            print(patch_response.text)
    
    else:
        print("Failed to get existing note")
        print(existing_note_response.status_code)
else:
    print("Failed to create note:", response.status_code)
    print(response.text)
