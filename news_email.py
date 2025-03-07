import boto3
import requests
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# AWS SES Configuration
AWS_REGION = "us-east-1"  # Change if your SES is in a different region
SENDER_EMAIL = "marrikarunyareddy@gmail.com"  # Your verified SES email
RECIPIENT_EMAIL = "marrikarunyareddy@gmail.com"  # Change if needed

# News API Configuration (Get API key from https://newsapi.org/)
NEWS_API_KEY = "782b826f1f754036ad16089247f92209"  # Replace with your actual NewsAPI key
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

# Initialize AWS SES Client
try:
    ses_client = boto3.client("ses", region_name=AWS_REGION)
    logging.info("✅ AWS SES client initialized successfully.")
except Exception as e:
    logging.error(f"❌ Error initializing AWS SES client: {e}")
    exit(1)

def fetch_news():
    """Fetch top 5 news headlines from NewsAPI."""
    try:
        response = requests.get(NEWS_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        news_data = response.json()

        if "articles" not in news_data:
            logging.warning("⚠️ No articles found in NewsAPI response.")
            return "No news available."

        headlines = [
            f"<li>{article['title']} - <a href='{article['url']}'>Read more</a></li>"
            for article in news_data.get("articles", [])[:5]
        ]

        return "<ul>" + "".join(headlines) + "</ul>" if headlines else "No news available."

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error fetching news: {e}")
        return "Failed to fetch news."

def send_email(news_content):
    """Send an email with the latest news using AWS SES."""
    try:
        response = ses_client.send_email(
            Source=SENDER_EMAIL,
            Destination={"ToAddresses": [RECIPIENT_EMAIL]},
            Message={
                "Subject": {"Data": "📰 Daily News Update"},
                "Body": {
                    "Html": {
                        "Data": f"""
                        <html>
                        <body>
                            <h2>📰 Daily News Update</h2>
                            <p>Here are today's top headlines:</p>
                            {news_content}
                            <hr>
                            <p>Sent via AWS SES ✅</p>
                        </body>
                        </html>
                        """
                    }
                }
            }
        )
        logging.info(f"✅ Email Sent Successfully! Message ID: {response['MessageId']}")

    except Exception as e:
        logging.error(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    logging.info("📩 Fetching news...")
    news_content = fetch_news()

    logging.info("📤 Sending email...")
    send_email(news_content)

    logging.info("✅ Daily News Email Process Completed!")

