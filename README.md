# autocreate_meeting_notes
Automatically create meeting notes for CILab members.

**This script is still in the development stage. We aim to automatically read the meeting schedule from a Google Sheet every week and generate notes automatically.**

## Get HackMD API Token
1. First, create a `.env` file in this directory.
2. Follow the instructions in the [HackMD API documentation](https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fhow-to-issue-an-api-token?utm_source=settings-api&utm_medium=inline-cta) to create your own API token. 
3. Then, based on the `.env.example` file, add your token information to the `.env` file.

## How to Use

1. First, install the required dependencies: `pip install -r requirements.txt`
2. Edit `script.py` to modify the title, and specify the follow-up and presentation members for that week.
3. Run `python3 script.py` to generate the meeting notes.

## Future Work
1. Integrate with Google Sheets to automatically retrieve meeting schedule information.
2. Fix the bug in `script.py` to automatically move the previous week's notes to the "Past Meeting" section.
