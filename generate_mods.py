import json
import glob

influence_affix_names = ["Crusader's", "of the Crusade", "Redeemer's", "of Redemption", "Hunter's", "of the Hunt", "Warlord's", "of the Conquest"]

def load_mods(file_path, stats_dict):
    with open(file_path) as stats:
        all_stats = json.loads(stats.read())
        for stat in all_stats:
            for id in stat["ids"]:
                stats_dict.update({id: stat["English"][0]["string"]})

with open("mods.json") as mods:
    all_mods = json.loads(mods.read())

stats_with_name = {}
for file_name in glob.glob("./stat_translations/*"):
    print("loading %s" % file_name)
    load_mods(file_name, stats_with_name)

influence_mods = dict(filter(lambda x: x[1]["name"] in influence_affix_names, all_mods.items()))

influence_mods_with_stat = { mod[1]["stats"][0]["id"]:stats_with_name[mod[1]["stats"][0]["id"]] for mod in influence_mods.items()}

with open("./generated/influence_mods.json", "w+") as mods_file:
    mods_file.write(json.dumps(influence_mods_with_stat))