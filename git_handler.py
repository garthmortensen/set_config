import subprocess


class GitHandler:
    """
    Utility class for handling Git configuration.

    It provides methods to get and set Git `user.name` and `user.email`.

    If values are not set, then it prompts user for input and sets accordingly.

    To use it, simply call `GitHandler.handle_git_user_settings()`.

    Why are all of these staticmethods? Because you don't need to instantiate the class, and
    there's no instance variables or values. `list.sort()` is a staticmethod.

    Use staticmethod when methods need to access/modify instance data.
    
    If I didn't use @staticmethod, I would have to __init__, e.g.
    def __init__(self):
        self.user_name = None
        self.user_email = None
    """

    @staticmethod
    def get_git_config(variable: str):
        """
        The getter. Checks if git global configuration for `user.name` and `user.email` is set. That is, has the user `git config --global user.name "Hancock, John" yet?

        Inspiration: https://stackoverflow.com/questions/71397719/how-to-get-a-git-user-with-python
        
        Args:
            variable: The setting to retrieve ("name" or "email").

        Returns:
            current value of the git config variable. If it hasn't been set, then None. Pretty neat that you can do that, actually.
        """
        try:
            # git config --global user.email
            output = subprocess.check_output(['git', 'config', '--global', f"user.{variable}"]).decode().strip()
            # print(f"Current value of `git user.{variable}`: {output}")
            return output

        except subprocess.CalledProcessError as e:
            # print(f"Error while running `get_git_config()` for user.{variable}: {e}")
            return None


    @staticmethod
    def set_git_config(variable: str, value: str) -> None:
        """
        The setter. Sets git config variable to the specified value.

        Args:
            variable: The config variable to set ("name" or "email").
            value: The value (e.g. "alf@aol.com").
        """
        try:
            command = ["git", "config", "--global", f"user.{variable}", value]
            subprocess.run(command, check=True)
            
            print(f"Git user.{variable} set to: {value}")
        except subprocess.CalledProcessError as e:
            print(f"Error while setting git config --global user.{variable}: {e}")


    @staticmethod
    def handle_git_user_settings():
        """
        Check if git global configuration for `user.name` and `user.email` is set. That is, has the user `git config --global user.name "Hancock, John" yet?

        It checks if both user.name and user.email are set.
        If both values are not set, it prompts user for input.

        Inspiration: https://stackoverflow.com/questions/71397719/how-to-get-a-git-user-with-python
        
        Returns:
            True if both `user.name` and `user.email` are set, False otherwise.
        """
        user_name = GitHandler.get_git_config("name")
        if not user_name:
            print("git config --global user.name has not been set")
            user_name_input = input("Enter user.name (e.g. Monster, Alf): ")
            GitHandler.set_git_config("name", user_name_input)

        user_email = GitHandler.get_git_config("email")
        # say not to regex hierglyphs for validating email
        if not user_email:
            print("git config --global user.email has not been set")
            user_email_input = input("Input user.email (e.g. alf.monster@aol.com): ")
            GitHandler.set_git_config("email", user_email_input)

        # if name or email above were blank, theyre now populated and variables need re-assignment
        user_name = GitHandler.get_git_config("name")
        user_email = GitHandler.get_git_config("email")

        if user_name and user_email:
            print("Both git user.name and user.email are set.")
            return True
        else:
            print("Both git user.name and user.email are NOT set!")
            return False


GitHandler.handle_git_user_settings()
