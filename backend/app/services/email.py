import os

import resend


def send_password_reset_email(
    recipient: str,
    reset_link: str,
) -> None:
    resend.api_key = os.environ["RESEND_API_KEY"]

    params = {
        "from": os.environ["EMAIL_FROM"],
        "to": [recipient],
        "subject": "Reset your IntelliPrep password",
        "html": f"""
        <h2>Reset your IntelliPrep password</h2>

        <p>Hello,</p>

        <p>We received a request to reset your IntelliPrep password.</p>

        <p>Use the following link to choose a new password.
        This link expires in 30 minutes.</p>

        <p><a href="{reset_link}">Reset Password</a></p>

        <p>If you did not request this, you can ignore this email.</p>

        <p>IntelliPrep Team</p>
        """,
    }

    response = resend.Emails.send(params)
    print("Password reset email sent successfully:", response)
