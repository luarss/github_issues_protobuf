# Github Issues protobuf format

The goal of this repo is to extract dataset for Github issues easily using protobuf format.

## Requirements
- `pip install protobuf`
- Protobuf compiler, `protoc`. Refer to this [page](https://github.com/protocolbuffers/protobuf/releases/).

## Usage
```
python main.py
```

## TODO
- A lot of repeated code in utils.py for adding information.
- Add a leaner version of proto for necessary metadata (i.e. user, title+body)
- save_pb and load_pb
- save_json: use jsonl format https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset
- Comments?
- 
