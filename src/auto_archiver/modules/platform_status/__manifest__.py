{
    # per https://github.com/bellingcat/auto-archiver/issues/340
    "name": "Platform Status",
    "version": 0.1,
    # default settings for recorder module beneath this
    "type": ["extractor", "feeder", "formatter", "storage", "enricher", "database"],
    "requires_setup": False,
    "dependencies": {
        "python": ["loguru"],
        "bin": ["bash"],
    },
    "configs": {
        "csv_file": {"default": "db.csv", "help": "CSV file name"},
        "required_field": {"required": True, "help": "required field in the CSV file"},
    },
    "description": "This is an example module",
}