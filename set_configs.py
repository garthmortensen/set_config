import os

# probably carve this out into a seperate repo, bc fairly unrelated to other modules
class FileHandler:
    def __init__(self, dir_path, file_name, new_text_file):
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_path = os.path.join(self.dir_path, self.file_name)
        self.new_text_file = new_text_file
 
    def mkdir(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
    
    def create_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                pass
    
    def append_text_from_file(self):
        with open(self.new_text_file, "r") as new_text_file:
            new_text = new_text_file.read().strip()
        
        with open(self.file_path, "a+") as file:
            file.seek(0)
            content = file.read()
            if new_text and new_text not in content:
                file.write(f"{new_text}\n")

    def append_text_as_arg(self, new_text):
        with open(self.file_path, "a+") as file:
            file.seek(0)
            content = file.read()
            if new_text not in content:
                file.write(f"{new_text}\n")

    def check_directory_permissions(self):
        if not os.path.exists(self.dir_path):
            print(f"dir does not exist: {self.dir_path}")
            return

        permission_read = os.access(self.dir_path, os.R_OK)
        permission_write = os.access(self.dir_path, os.W_OK)
        permission_execute = os.access(self.dir_path, os.X_OK)

        # fancy f-strings
        print(f"Permissions for: {self.dir_path}")
        print(f"Read: {'Yes' if permission_read else 'No'}")
        print(f"Write: {'Yes' if permission_write else 'No'}")
        print(f"Execute: {'Yes' if permission_execute else 'No'}")


file_handler = FileHandler("my_dir", "my_file.txt", "new_text_file.txt")
file_handler.mkdir_file_and_append()
