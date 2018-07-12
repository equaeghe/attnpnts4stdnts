#!/usr/bin/env python

import yaml
import os


labels = {}
points = {}

with open('../labels.yaml', 'r') as f:
    labels = yaml.load(f)

for root, dirs, files in os.walk('../attention_points'):
    for filename in files:
        if not filename.endswith('.yaml'):
            continue
        with open(root + '/' + filename, 'r') as f:
            points[filename[:-5]] = yaml.load(f)

output = ""
for point, content in points.items():
    output += "# " + point + "\n\n"
    output += "_" + content['summary'] + "_\n\n"
    output += "**Labels**: " + ', '.join(content['labels']) + "\n\n"
    output += content['description'] + "\n---\n\n"

print(output)
