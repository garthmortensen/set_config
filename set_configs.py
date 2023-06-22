import os
import subprocess
import paramiko


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


# TODO: class CondaGitManager()

def conda_env_dir_exists(env_name):
    envs_dir = os.path.expanduser("~/.conda/envs")

    env_dir = os.path.join(envs_dir, env_name)
    if os.path.exists(env_dir) and os.path.isdir(env_dir):
        return True

    return False


def create_conda_env(env_name):
    if not conda_env_dir_exists(env_name):
        try:
            subprocess.run(['conda', 'create', '-y', '--name', env_name])
            print(f"Conda environment created: {env_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error while creating conda environment: {e}")
    else:
        print(f"Conda environment already exists: {env_name}")


env_name = "my_cats"
if conda_env_dir_exists(env_name):
    print(f"Conda env dir exists: {env_name}")
else:
    print(f"Conda env dir does not exist: {env_name}")
    print(f"Creating conda env: {env_name}")
    create_conda_env(env_name)


def set_git_config(variable, value):
    try:
        # TODO: does value need quotes?
        command = ["git", "config", "--global", f"user.{variable}", f'"{value}"']
        subprocess.run(command, check=True)
        
        print(f"Git {variable} set to: {value}")
    except subprocess.CalledProcessError as e:
        print(f"Error while setting git config --global user.{variable}: {e}")


set_git_config("email", "me@aol.com")



import getpass


class SSH_Creator():


    def get_home_dir():

        whoami = getpass.getuser()

        home_dir = os.path.expanduser("~" + whoami)
        if os.path.isdir(home_dir):
            return home_dir
        else:
            print(f"Home dir does not exist.")


    def create_ssh_file_ed25519(passphrase=None):
        """requires anaconda standard distribution. looks very much like crypto functions for blockchain wallets"""

        home_dir = get_home_dir()
        public_name = "id_ed25519.pub"
        private_name = "id_ed25519"
        filepath_public = os.path.join(home_dir, public_name)
        filepath_private = os.path.join(home_dir, private_name)

        key = paramiko.Ed25519Key.generate()

        if passphrase:
            key.write_private_key_file(filepath_private, password=passphrase)
        else:
            key.write_private_key_file(filepath_private)

        with open(filepath_public, "w") as f:
            f.write(f"{key.get_name()} {key.get_base64()}")

        print(f"ssh files created!")


SSH_Creator.create_ssh_file_ed25519()

