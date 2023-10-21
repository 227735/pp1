facebook = True
twitter = False
instagram = True

#1
if facebook == True and twitter == True or facebook == True and instagram == True or twitter == True and instagram == True or facebook == True and twitter and instagram == True:
    print("A person can be a good influencer!")
else:
    print("A person can't be a good influencer!")

#2
social_media_count = 0

if facebook:
    social_media_count += 1

if twitter:
    social_media_count += 1

if instagram:
    social_media_count += 1

if social_media_count >= 2:
    print("A person can be a good influencer!")
else:
    print("A person cannot be a good influencer.")