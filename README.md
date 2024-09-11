# autocreate_meeting_notes
Automatically create meeting notes for CILab members.

**We aim to automatically read the meeting schedule from a Google Sheet every week and generate notes automatically.**

## Get HackMD API Token
1. First, create a `.env` file in this directory.
2. Follow the instructions in the [HackMD API documentation](https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fhow-to-issue-an-api-token?utm_source=settings-api&utm_medium=inline-cta) to create your own API token. 
3. Then, based on the `.env.example` file, add your token information to the `.env` file.

## pygsheet
1. Based on [this article](https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/), get your google sheet API.
2. Add your sheet url and sheet_key.json path to `.env`

## How to Use

1. First, install the required dependencies: `pip install -r requirements.txt`
2. Run `python3 script.py` to generate the meeting notes.
3. You can use `crontab` to let system routinely execute `script.py`.

## Future Work
1. Integrate with Google Sheets to automatically retrieve meeting schedule information. (finished)
2. Fix the bug in `script.py` to automatically move the previous week's notes to the "Past Meeting" section. (finished)
