with open("/Users/secuof/git/hide_project/insignary/automation_test_project/repos", "r") as f:
    for repo in f.readlines():
        metadata_file = repo[:-1]
        print(metadata_file)