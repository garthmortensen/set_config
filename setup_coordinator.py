import argparse
from conda_manager import CondaManager
from git_handler import GitHandler
from ssh_creator import SSH_Creator


class SetupCoordinator:
    def __init__(self):
        # initialize instances of all utility classes
        self.ssh_creator = SSH_Creator()
        self.git_handler = GitHandler()
        self.conda_manager = CondaManager()

    def execute_all(self, passphrase: str, env_name: str) -> None:
        """
        execute all utility classes to configure computer environment.

        Args:
            passphrase (str): passphrase for generating ssh key.
            env_name (str): conda environment name.

        Returns:
            None
        """

        # call each utility class method
        self.ssh_creator.create_ssh_file_ed25519(passphrase)
        self.git_handler.handle_git_user_settings()
        self.conda_manager.create_conda_env(env_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Configure git, ssh, and conda env.')
    parser.add_argument('--passphrase', type=str, nargs='?', help='passphrase to generate SSH key')
    parser.add_argument('--env_name', type=str, nargs='?', help='conda env name')
    args = parser.parse_args()

    setup_coordinator = SetupCoordinator()
    passphrase = args.passphrase
    env_name = args.env_name
    setup_coordinator.execute_all(passphrase, env_name)
