# Automated Daily News Email using AWS EC2 and SES

## 📌 Project Overview
This project automatically fetches daily top news headlines and sends them via email using **AWS SES (Simple Email Service)** and **AWS EC2**.

## 🚀 Features
- Fetches **top news** headlines using [NewsAPI](https://newsapi.org/)
- Sends the news summary **via AWS SES**
- Runs automatically on an **AWS EC2 instance**
- Uses **Python** and **Boto3 (AWS SDK for Python)**

## 🛠 Setup Instructions

### **1️⃣ Prerequisites**
- An **AWS account**
- A verified email in **AWS SES (Sandbox Mode)**
- An **EC2 instance (Amazon Linux 2023 recommended)**
- A **GitHub repository** (to store your code)
- A **NewsAPI API Key** (Get from [NewsAPI](https://newsapi.org/))

### **2️⃣ Install Required Packages**
```sh
sudo yum update -y
sudo yum install git -y
sudo yum install python3 -y
pip3 install boto3 requests
```

### **3️⃣ Clone the Repository**
```sh
git clone https://github.com/MarriKarunyaReddy/Automated-Daily-News-Email-EC2-SES.git
cd Automated-Daily-News-Email-EC2-SES
```

### **4️⃣ Configure AWS CLI**
```
aws configure
```
Enter:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region** (e.g., `us-east-1`)

### **5️⃣ Set Up SES Permissions**
Ensure your email is verified in **AWS SES**:
```
aws ses verify-email-identity --email-address marrikarunyareddy@gmail.com
```

### **6️⃣ Run the Script**
```sh
python3 news_email.py
```

### **7️⃣ Automate with Crontab (Optional)**
To schedule the script to run daily:
```sh
crontab -e
```
Add this line at the bottom to run the script every day at 8 AM:
```sh
0 8 * * * /usr/bin/python3 /home/ec2-user/Automated-Daily-News-Email-EC2-SES/news_email.py
```

## 📌 Troubleshooting
1. **No Email Received?**
   - Check if your **SES is in Sandbox Mode** (needs verified emails)
   - Check if your **email is in spam**
   - Check **AWS SES Sending Quota**:
     ```
     aws ses get-send-quota
     ```
   - Check SES logs in AWS Console

2. **Git Push Authentication Issue?**
   - Use **GitHub PAT (Personal Access Token)** instead of a password
   - Follow [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate a token

## 📝 Future Improvements
- Support for **multiple recipients**
- Improve email formatting (HTML styling)
- Fetch news from multiple sources

## 🤝 Contributing
Feel free to fork the repo, create a new branch, and submit a **Pull Request**!

## 📄 License
This project is open-source under the **MIT License**.

