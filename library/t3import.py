from lxml import objectify
from collections import defaultdict
import sys
import yaml
import csv

xml = open(sys.argv[1], 'rb').read()

objects = defaultdict(dict)
tree = objectify.fromstring(xml)
for row in tree.xpath('//tablerow'):
    #if row.attrib.get('index', '').startswith('tx_tkthemen_list:'):
    for i in  row.fieldlist.field:
        objects[row.attrib['index']][i.attrib['index']] = i.text


ret = []
for idx, obj  in list(objects.items()):
    if not idx.startswith('tx_tkthemen_list'):
        #print(idx)
        continue

    data = {}
    for (v,n) in sorted([('titel', 'title'), ('autor', 'author'), ('anmerkunga', 'type'),
                         ('teaser', 'description'), ('beschreibung', 'summary'),
                         ('eventid', 'ID'), ('veranstalter', 'year')]):
        if v in obj and obj[v]:
            data[str(n)] = obj[v]

    for kat,x in [('a','category'), ('f', 'topic'), ('g', 'location')]:
        if obj['kategorie'+kat]:
            key = 'tx_tkthemen_kategorie%s:%s'%(kat, obj['kategorie'+kat])
            other = objects[key]
            if not other:
                continue
            data[x] = other['kategorie' + kat]
    try:
        data['year'] = int(data['year'])
    except:
        if 'year' in data:
            del data['year']

    if not data:
        continue

    #fd.writerow(
    #    [data['ID'], data['title'], data['author'], data['type'],
    #     data['description'], data['summary'], data.get('topic'),
    #     data['category']])
    ret.append(data)

yaml.dump_all(sorted(ret, key=lambda x: x.get('ID','')), sys.stdout, allow_unicode=True,default_flow_style = False)
