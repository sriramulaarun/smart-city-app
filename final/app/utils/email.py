import smtplib
from email.message import EmailMessage
from flask import current_app
import logging

logger = logging.getLogger(__name__)

def send_confirmation_email(to_address, tracking_id):
    if not to_address:
        return
        
    smtp_email = current_app.config.get("SMTP_EMAIL")
    smtp_pass = current_app.config.get("SMTP_PASSWORD")
    
    msg = EmailMessage()
    msg['Subject'] = f'Problem Report Received - Tracking ID: {tracking_id}'
    msg['From'] = smtp_email if smtp_email else "no-reply@reportapp.local"
    msg['To'] = to_address
    msg.set_content(f"Hello,\n\nYour problem report has been successfully received.\n\nTracking ID: {tracking_id}\n\nYou can track its status using the tracking ID on our Track page.\n\nThank you!")

    if smtp_email and smtp_pass:
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(smtp_email, smtp_pass)
                server.send_message(msg)
            logger.info(f"Email sent to {to_address} for ID {tracking_id}")
        except Exception as e:
            logger.error(f"Failed to send email to {to_address}: {e}")
    else:
        logger.warning("MOCK EMAIL (No SMTP credentials set)")
        logger.info(f"To: {msg['To']}")
        logger.info(f"Subject: {msg['Subject']}")
