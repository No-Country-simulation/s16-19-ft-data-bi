import os

def save_uploadedfile(uploadedfile):
    if not os.path.exists("assets/tempDir"):
        os.makedirs("assets/tempDir")
    file_path = os.path.join("assets/tempDir", uploadedfile.name)
    with open(file_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    return file_path