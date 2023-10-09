def flattenJsonFunc(data, result, prefixKey=""):
    if type(data) is dict:
        for key in data:
            flattenJsonFunc(data[key], result, prefixKey + key + "__")
    elif type(data) is list:
        index = 0
        for item in data:
            flattenJsonFunc(item, result, prefixKey + str(index) + "__")
            index += 1
    else:
        result[prefixKey[:-2]] = data

# jsonData = {
#     "name": {
#         "first": "somit",
#         "last": "sri"
#     },
#     "place": "bangalore",
#     "value": [1, 2, 4]
# }
# output = {}
# flattenJsonFunc(jsonData, output)
# print(output)
