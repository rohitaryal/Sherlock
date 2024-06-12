## 🧞 Sherlock
Find your KIIT buddy's details using his/her roll number only 🧠.
Details include 
- Name
- E-Mail
- Phone Number
- Branch/Program

## Requirements
- Python3.x
- `requests` library

> `pip install requests`

## 👓 Usage
Open up your terminal window and paste this
```bash
git clone https://github.com/rohitaryal/Sherlock
cd Sherlock
python3 sherlock.py # <-- Now continue yourself
```

🎃 **Or you can import this script.**
```python
from sherlock import Sherlock

detective=Sherlock()
print(detective.find("ROLL_NUMBER"))
```
🙀 **Outputs:**
```JSON
{
    'status': 'success',
    'student_id': '1234567890', 
    'phone_no': '1234567890', 
    'email_id': 'my_mail@gmail.com', 
    'roll_no': 'ROLL_NUMBER', 
    'name': 'ROHIT  SHARMA', 
    'is_international': True
    'program_des': 'BRANCH DESCRIPTION,  YEAR'
 }
```
---
### 🤔 TODO

- Put comments 💀

### 🤮 Issues?
Leave an issue with error logs 