import re
sr = "This is a test text."
print(len(re.findall("is", sr)))
print(re.split(" ", sr))
print(re.sub(" ", "_", sr))
print(re.search("is", sr).span(), re.search("is", sr).start())
