import lasair, json, sys
token     = '5aadfe361ef8db70d83baea53527d13b4778630f'
endpoint  = 'http://192.41.108.37:8080/api/'

objectIds = ['ZTF22aacisjd']

L = lasair.lasair_client(token, endpoint=endpoint)

for objectId in objectIds:
    print(objectId)
    lcs = L.lightcurves([objectId])
#    for lc in lcs:
#        for cand in lc:
#             print(cand['isdiffpos'])
#
    print(json.dumps(lcs, indent=2))
