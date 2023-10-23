from bot import InternetSpeedTwitterBot

internetspeedbot = InternetSpeedTwitterBot()
download_speed = internetspeedbot.get_internet_speed()

if download_speed < 5:
    internetspeedbot.tweet_at_provider()
else:
    print("Internet Speed is Perfect.")