import pypixel
import json

key = "<API key>"
test_name = "<Player Name>"
test_profile = "<Profile Name>"

api = pypixel.HypixelAPI(key)
user = api.userByName(test_name)
profiles = user["player"]["stats"]["SkyBlock"]["profiles"].values()
for profile in profiles:
    if profile["cute_name"] == test_profile:
        profile_id = profile["profile_id"]
        info = api.main("skyblock/profile",{"profile": profile_id})
        info_str = json.dumps(info,indent=2)
        print(info_str)
        with open(test_name+"_"+test_profile+".json","w") as f:
            f.write(info_str)
        ah = api.main("skyblock/auction",{"profile": profile_id})
        ah_str = json.dumps(ah,indent=2)
        print(ah_str)
        with open(test_name+"_"+test_profile+"_ah.json","w") as f:
            f.write(ah_str)
        news = api.main("skyblock/news")
        print(news)