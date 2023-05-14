import json

f = open('response.json')

idempotencyKeys = set()
data = json.load(f)
hits = data["hits"]["hits"]

customerCount = dict()
count3DS = set()
non3Ds = set()
approved = 0
non3DsApproved = 0
count3DsAutoExpired = 0
uniqueIds = set()
for hit in hits:
    source = hit["_source"]
    sig = source["processor_request_signature"]
    uniqueIds.add(sig)
    if sig.startswith("NXl"):
        if sig not in count3DS:
            count3DS.add(sig)
            latestPro = source["latestProcessorResponseStatus"]
            if latestPro == "OKAY/APPROVED/APPROVED_AS_REQUESTED":
                approved += 1
            elif latestPro == "REJECTED/AUTO_EXPIRED":
                count3DsAutoExpired += 1
    else:
        if sig not in non3Ds:
            non3Ds.add(sig)
            latestPro = source["latestProcessorResponseStatus"]
            if latestPro == "OKAY/APPROVED/APPROVED_AS_REQUESTED":
                non3DsApproved += 1
print("Unique 3DS count:", len(count3DS))
print("Approved:", approved)
print("AutoExpired:", count3DsAutoExpired)

print()

print("Unique Non3Ds count:", len(non3Ds))
print("Approved:", non3DsApproved)

print(len(uniqueIds))