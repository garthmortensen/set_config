# file handler

<img src="./mrclippy.png" alt="universal_paperclip" style="zoom:25%;" />

Thanks to the advanced state which Mr Clippy has evolved into, he can now auto configs a new system for AWS.

## Instructions

To check if an ssh key exists and create if not, run `ssh_creator.py` which (at the time of writing) contains:

``` python
SSH_Creator.create_ssh_file_ed25519(passphrase=None)
```

or execute from bash:

``` bash
alias sshoop='python /pathy/ssh_creator.py'
```

To check if `git config --global` `user.name` and `user.email` have been set, and if not set them:

``` python
GitHandler.handle_git_user_settings()
```

or execute from bash:

``` bash
alias git_set_go='python /pathy/git_handler.py'
```

### setup_coordinator.py

If you just want the script to handle everything for you, use the `setup_coordinator.py` module with `argparse` options:

``` bash
python script.py --passphrase ilovemydog --env_name rstudio
```

