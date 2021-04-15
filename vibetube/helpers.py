from django.contrib.auth import authenticate, login

import random

def auth_user(request, data):
        if '@' in data['username']:
            user = authenticate(request, email=data['username'], password=data["password"])
        else: 
            user = authenticate(request, username=data['username'], password=data["password"])

        if user:
            login(request, user)
            return True
        return False

def check_for_name(name):
    if not name:
        display_name = f"User{random.randint(101010101, 999999999)}"
    else:
        display_name = name
    return display_name

def check_for_username(name, display_name):
    if not name: return display_name
    else: return name

def user_vid_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.creator.username}/video/{instance.uuid}.{ext}"

def user_sound_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.creator.username}/sound/{instance.original_video.uuid}.{ext}"

def user_photo_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.username}/profile-photos/{random.randint(101010101, 999999999)}.{ext}"

def gen_uuid():
    return random.randint(690000000, 699999999)

def generate_html(email, token):
    return f""" <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <meta name="viewport"
                        content="width-device-width,initial-scale=1.0,maximum-scale=1.0, minimum-scale=1.0,user-scalable=no, minimal-ui">
                    <style>
                        * {{
                        margin: 0;
                        font-family: Helvetica;
                        box-sizing: border-box;
                        }}

                        a {{
                        text-decoration: none;
                        background-color: transparent;
                        outline: none;
                        cursor: pointer;
                        }}

                        html.ar {{
                        direction: rtl;
                        }}

                        html.ar input {{
                        text-align: right;
                        }}
                    </style>
                </head>
                <body style="display: flex; justify-content: center;">
                    <div style="width:100%;max-width: 440px; padding: 0 20px;">
                        <div style="width: 100%; padding: 40px 7px;">
                            <img style="width: 35px;"
                                src="https://i.ibb.co/GVYGFCF/vibe-icon.png"
                                style="margin: 40px 12px 40px 12px; width: 35px; height: 40px;">
                            <img style="width: 150px;"
                                src="https://i.ibb.co/N6D8RGC/vibe-text.png"
                                style="margin: 40px 12px 40px 12px; width: 150px; height: 40px;">
                        </div>
                        <div
                        style="max-width:100%;background-color: #f1f1f1; padding: 20px 16px; font-weight: bold;font-size: 20px;color: rgb(22,24, 35)">
                            Verification Code
                        </div>
                        <div
                        style="max-width:100%;background-color: #f8f8f8; padding: 24px 16px;font-size: 17px;color: rgba(22,24, 35, 0.75);line-height: 20px;">
                            <p style="margin-bottom:20px;">To verify your account, enter this code in VibeTube:</p>
                            <p style="margin-bottom:20px;color: rgb(22,24,35);font-weight: bold;">{token}</p>
                            <p style="margin-bottom:20px;">Verification codes expire after 48 hours.</p>
                            <p style="margin-bottom:20px;">If you didn&#39;t request this code, you can ignore this message.</p>

                            <p>VibeTube Support Team</p>
                            <p style="word-break: break-all;">
                                VibeTube Help Center: <br>
                                <a style="color: rgb(0, 91, 158);" href="https://trollface.dk/">https://thegreatestandtotallylegalsupport.com</a>
                            </p>
                        </div>
                        
                        <div style="max-width:100%;padding: 40px 16px 20px;font-size: 15px;color: rgba(22, 24, 35, 0.5);line-height:18px;">
                            <div>Have a question?</div>
                            <div style="margin-bottom:20px;">Check out our help center or contact us in the app using
                                <span style="color: rgb(0, 91, 158);font-weight: bold;">Settings &gt; Report a Problem.</span></div>
                            <div>This is an automatically generated email. Replies to this email address aren&#39;t monitored.</div>
                        </div>
                        <div style="border: 0; background-color: rgba(0, 0, 0, 0.12); height: 1px;margin-bottom:16px;"></div>
                            <div style="color: rgba(22, 24, 35, 0.5); margin: 20px 16px 40px 16px;font-size: 12px;line-height:18px;">
                            <div>
                                This email was generated for {email.split("@")[0]}.
                            </div>
                            <div style="word-break: break-all;">
                                <a style="color: rgba(22, 24, 35, 0.5);text-decoration:underline;"
                                href="https://www.youtube.com/watch?v=989-7xsRLR4">Privacy Policy (you have no privacy, privacy is a myth)
                            </a>
                        </div>
                            <div>VibeTube, 42 North Vibe Avenue Cloud 9, Andromeda Galaxy 424242</div>
                        </div>
                        </div>
                    </div>
                </body>
                """