def is_valid_command(cmd):
    return isinstance(cmd, str) and len(cmd.strip()) > 0
