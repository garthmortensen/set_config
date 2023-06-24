import os
import subprocess
import getpass


class CondaManager:
    """
    Class to manage Conda environments.

    Provides methods to find where the directory which stores conda environments is located on filesystem, determien if an input
    conda env exists by looking therein, and finally creates it under that name if it doesn't exist.

    This is meant to run in an automatated fashion without command lines, which would merely be replicating existing
    conda env functionality. No, instead, just provide a variable name, edit script as required, and call it.
    """

    def get_conda_env_path(self) -> str:
        """
        Get path to the directory which contains already created conda envs.

        Returns:
            str: if found, returns the path to the conda envs, or "unknown" otherwise.
        """
        whoami = getpass.getuser()

        # REVIEW: works, but are there any case-sensitivity issues?
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

        all_paths = windows_paths + linux_paths

        for each_path in all_paths:
            try:
                if os.path.exists(each_path) and os.path.isdir(each_path):
                    print(f"found each_path: {each_path}")
                    return each_path
            # if no such path is found, throw error.
            except OSError as e:
                print(f"get_conda_env_path() found no windows_path or conda_path: {e}")
                pass

        # REVIEW: Not sure what conditions would lead to this return statement
        return "unknown"


    def conda_env_exists(self, env_name: str) -> bool:
        """
        Determines if provided environment name is found in environment path, given `CondaManager.get_conda_env_path()`.

        Args:
            env_name (str): environment name.

        Returns:
            bool: True if the environment exists, False otherwise.
        """

        # NOTE: method defined within a class, so it requires the self. it points to itself.
        # NOTE: self arg lets the method access attribubes and behavior
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


env_name = "rstudio"
conda_manager = CondaManager()
conda_manager.create_conda_env(env_name)

