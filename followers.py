import instaloader
from tqdm import tqdm

L = instaloader.Instaloader()

username = input("Username: ")
password = input("Password: ")

try:
    L.login(username, password)
except instaloader.exceptions.TwoFactorAuthRequiredException:
    two_factor_code = input("Enter the 2FA code: ")
    L.two_factor_login(two_factor_code)

profile = instaloader.Profile.from_username(L.context, username)
followers = profile.get_followers()

print("Getting followers...")

followers = profile.get_followers()
followers_list = []
for follower in tqdm(followers):
  followers_list += [follower]

print("Getting following...")
followings = profile.get_followees()
following_list = []
for following in tqdm(followings):
  following_list += [following]

print("Checking who is not following you back...")
not_following_me_back = [user for user in following_list if user not in followers_list]

profiles = []
for profile in tqdm(not_following_me_back):
   profiles += [profile]

print(profiles)

with open("newfile.txt", "w") as file:
    file.write("/n".join(profiles))
    file.close()