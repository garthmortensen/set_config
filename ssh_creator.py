import os
import getpass
import paramiko
import subprocess


class SSH_Creator:
    """Class for creating and managing ssh keys.

    It provides methods to check for the existence of ssh keys and conditionally generate them.
    """

    # static bc doesnt require instance-specific data. stateless
    # so, no need to instantiate an object
    @staticmethod
    def get_home_dir():
        """Gets users home dir (`~`)

        :return: path to users home dir
        :rtype: str or None
        """

        whoami = getpass.getuser()

        home_dir = os.path.expanduser("~" + whoami)
        if os.path.isdir(home_dir):
            return home_dir
        else:
            print(f"Home dir does not exist.")
            return None


    @staticmethod
    def check_ssh_key_exists():
        """Check if an ssh key *.pub or *.pem file exists. Pub is genearted via ssh-keygen, pem is generated via PuTTY.

        Returns True if .ssh directory exists and *.pub file found within.
        Returns False otherwise.

        :return: True if ~/.ssh/*.pub exists, False otherwise.
        :rtype: bool
        """

        home_dir = SSH_Creator.get_home_dir()
        if not home_dir:
            return None

        ssh_dir = os.path.join(home_dir, ".ssh")

        # check for ~/.ssh
        if os.path.isdir(ssh_dir):
            # directory exists, continue

            # search for .pub or .pem files, indicating ssh key already generated
            all_ssh_files = []
            for each_file in os.listdir(ssh_dir):
                if each_file.endswith((".pub", ".pem")):
                    print(f"public ssh key file already exists: {os.path.join(ssh_dir, each_file)}")
                    return True

        return False


    @staticmethod
    def create_ssh_file_ed25519_paramiko(passphrase=None):
        """Requires paramiko, which is included in recent Anaconda standard distros.
        Appears very similar blockchain wallets functions."""

        home_dir = SSH_Creator.get_home_dir()
        if not home_dir:
            return None

        if SSH_Creator.check_ssh_key_exists():
            return None

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

        print(f"ssh files created using paramiko library!")


    @staticmethod
    def create_ssh_file_ed25519_bash(passphrase=None):
        """`Paramiko.generate()` was added later than my WSL python version.
        This alternative approach which uses only bash.
        
        :param passphrase: Optional passphrase to increase private key security. This necessitates you type the password to `git push`.
        :type passphrase: str or None
        :return: None
        """

        home_dir = SSH_Creator.get_home_dir()
        if not home_dir:
            return None

        if SSH_Creator.check_ssh_key_exists():
            return None

        # ssh-keygen -t ed25519 -C "<comment>"
        command = ['ssh-keygen', '-t', 'ed25519']
        if passphrase:
            command.extend(['-N', passphrase])
        subprocess.run(command)

        print(f"ssh files created via bash subprocess command!")


SSH_Creator.get_home_dir()
# passphrase = 'iaminlovewithbeefjerky'
# SSH_Creator.create_ssh_file_ed25519_paramiko()
SSH_Creator.create_ssh_file_ed25519_bash()

