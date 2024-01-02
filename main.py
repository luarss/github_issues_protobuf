
import requests
import subprocess
import os
import json
from utils import get_request, add_to_collection, add_to_comments

# compile proto definitions
os.remove("issues_pb2.py")
command = "./protoc/bin/protoc --python_out=. ./issues.proto"
subprocess.run(command, shell=True)


import issues_pb2
print(dir(issues_pb2))

if __name__ == "__main__":
    #collection = issues_pb2.ApiResponses()
    #url = "https://api.github.com/repos/The-OpenROAD-Project/OpenROAD/issues/126"
    #text = get_request(url)
    #add_to_collection(text, collection)
    #print(collection)

    comments = issues_pb2.CommentList()
    url = "https://api.github.com/repos/The-OpenROAD-Project/OpenROAD/issues/126/comments"
    text = get_request(url)
    add_to_comments(text, comments)
    print([x.body for x in comments.comment])