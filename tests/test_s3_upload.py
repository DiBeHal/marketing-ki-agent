from storage import upload_file, list_files
# KEIN check_bucket() mehr!

def test_upload():
    local_file = "data/testfile.txt"
    s3_key = "tests/testfile.txt"

    # check_bucket()  # KOMMENTIERT!
    upload_file(local_file, s3_key)
    list_files()

if __name__ == "__main__":
    test_upload()
