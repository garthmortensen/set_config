import os
import subprocess


class CondaManager:

    def conda_env_dir_exists(self, env_name):
        envs_dir = os.path.expanduser("~/.conda/envs")

        env_dir = os.path.join(envs_dir, env_name)
        if os.path.exists(env_dir) and os.path.isdir(env_dir):
            return True

        return False


    def create_conda_env(self, env_name):
        if not CondaManager.conda_env_dir_exists(env_name):
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


env_name = "my_cats"
if CondaManager.conda_env_dir_exists(env_name):
    print(f"Conda env dir exists: {env_name}")
else:
    print(f"Conda env dir does not exist: {env_name}")
    print(f"Creating conda env: {env_name}")
    CondaManager.create_conda_env(env_name)
