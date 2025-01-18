class Constant:
    service = "datastore-management-service"

    datastore_root_dir = "/Users/bubz/Developer/master-project/tests/test-datastore-root"

    base_url = "http://localhost:"
    dao_port = "5010"

    dao = {
        "create": "/api/create",
        "read": "/api/read",
        "list": "/api/read_list",
        "update": "/api/update",
        "delete": "/api/delete",
        "read_all": "/api/read_all",
        "query": "/api/query"
    }

    table = {
        "DATASTORE": "datastore",
        "DATASTORE_ROLES": "datastore_roles",
        "DATASET": "dataset",
        "DATASET_ROLES": "dataset_roles",
        "FILES": "files",
        "DATASTORE_CONFIG": "datastore_config",
        "DATASET_FILES": "dataset_files",
    }

    delimeter = {
        "DATASTORE": "__",
        "DATASET": "__"
    }

    datastore = {
        "directories": [
            "raw_data/videos",
            "raw_data/images",
            "raw_data/audio",
            "raw_data/other",
            "datasets",
            "logs",
            "reports",
        ],
    }

    dataset = {
        "directories": [
            "ground_truth",
            "preprocessed_data/videos",
            "preprocessed_data/images",
            "preprocessed_data/audio",
            "models",
            "predictions",
            "annotations",
            "misc"
        ],

    }
    files = {
        "metadata": "-metadata.json"
    }

    file_dir = {
        "datastore": {
            "audio": "raw_data/audio",
            "image": "raw_data/images",
            "video": "raw_data/videos",
            "other": "raw_data/other"
        },
        "dataset": {
            "ground_truth": "ground_truth",
            "preprocessed_data": "preprocessed_data",
            "model": "models",
            "prediction": "predictions",
            "annotation": "annotations",
        }

    }
