import instaloader

insta = instaloader.Instaloader()

account = input('Enter the public account name: ' )

insta.download_profile(account)