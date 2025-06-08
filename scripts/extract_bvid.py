import re
import json

with open('scripts/tmp.xml', 'r') as f:
    xml_content = f.read()

bvid_list = []
matches = re.findall(r'bvid=([A-Za-z0-9]+)', xml_content)
for match in matches:
    bvid_list.append(match)

output_list = [{"bvid": bvid} for bvid in bvid_list]
print(json.dumps({"list": output_list}))
