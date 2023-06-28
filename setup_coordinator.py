from conda_manager import CondaManager
from git_handler import GitHandler
from ssh_creator import SSH_Creator


class SetupCoordinator:
    def __init__(self):
        # initialize instances of all utility classes
        self.ssh_creator = SSH_Creator()
        self.git_handler = GitHandler()
        self.conda_manager = CondaManager()

    def execute_ssh(self, passphrase: str) -> None:
        """
        execute ssh utility class.

        Args:
            passphrase (str): passphrase for generating ssh key.

        Returns:
            None
        """
        self.ssh_creator.create_ssh_file_ed25519(passphrase)

    def execute_git(self) -> None:
        """
        execute git utility class.

        Returns:
            None
        """
        self.git_handler.handle_git_user_settings()

    def execute_conda(self, env_name: str) -> None:
        """
        execute conda utility class.

        Args:
            env_name (str): conda environment name.

        Returns:
            None
        """
        self.conda_manager.create_conda_env(env_name)

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


passphrase = "iwantadog"
env_name = "rstudio"

setup_coordinator = SetupCoordinator()
# setup_coordinator.execute_ssh(passphrase)
# setup_coordinator.execute_git()
# setup_coordinator.execute_conda(env_name)
setup_coordinator.execute_all(passphrase, env_name)
