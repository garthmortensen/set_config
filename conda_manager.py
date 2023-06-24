import os
import subprocess
import getpass


class CondaManager:


    def get_conda_env_path(self) -> str:
        """
        Get path to the directory which contains already created conda envs.

        Returns:
            str: if found, returns the path to the conda envs, or "unknown" otherwise.
        """
        whoami = getpass.getuser()

        # TODO: works, but are there any case-sensitivity issues?
        # windows paths
        windows_paths = [
            os.path.join("C:", "Users", whoami, "Anaconda3", "envs"),
            os.path.join("C:", "Users", whoami, "AppData", "Local", "Continuum", "Anaconda3", "envs"),
        ]

        # linux paths
        linux_paths = [
            os.path.expanduser(f"~{whoami}/anaconda3/envs"),
            os.path.expanduser(f"~{whoami}/.conda/envs"),
        ]

        # TODO: add try except to better handle "unknown" unhappy path
        for conda_path in windows_paths:
            if os.path.exists(conda_path) and os.path.isdir(conda_path):
                print(f"found conda_path: {conda_path}")
                return conda_path

        for conda_path in linux_paths:
            if os.path.exists(conda_path) and os.path.isdir(conda_path):
                print(f"found conda_path: {conda_path}")
                return conda_path

        return "unknown"


    def conda_env_exists(self, env_name: str) -> bool:
        """
        Determines if provided environment name is found in environment path, given `CondaManager.get_conda_env_path()`.

        Args:
            env_name (str): environment name.

        Returns:
            bool: True if the environment exists, False otherwise.
        """

        # method defined within a class, so it requires the self. it points to itself.
        # self arg lets the method access attribubes and behavior
        conda_path = self.get_conda_env_path()  # "method invocation", i.e. calling a method

        # if conda_path found, proceed
        if conda_path != "unknown":
            env_dir = os.path.join(conda_path, env_name)
            if os.path.exists(env_dir) and os.path.isdir(env_dir):
                print(f"env_dir found: {env_dir}")
                return True

        return False


    def create_conda_env(self, env_name: str) -> None:
        """
        Uses input name to create a new conda environment.

        Args:
            env_name (str): environment name.
        """

        # if the provided environment name is not found as a directory
        if not self.conda_env_exists(env_name):

            try:
                # command = ['conda', 'create', '-y', '--name', env_name, 'python=3.7']
                # command = ['conda', 'create', '-y', '--name', env_name, '--file', 'environment.yml']
                command = ['conda', 'create', '-y', '--name', env_name]
                subprocess.run(command)
                print(f"Conda environment created: {env_name}")
            except subprocess.CalledProcessError as e:
                print(f"Error while running create_conda_env(): {e}")
        else:
            print(f"Conda environment already exists: {env_name}")


env_name = "cats"
conda_manager = CondaManager()
conda_manager.create_conda_env(env_name)

