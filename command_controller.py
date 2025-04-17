from os import path, listdir
from importlib import import_module

def load_commands():
    command_folder = "commands"
    if not path.isdir(command_folder):
        print(f"⚠️ Command folder '{command_folder}' not found.")
        return

    print(f"📦 Loading commands from '{command_folder}/'")
    for filename in sorted(listdir(command_folder)):
        if filename.endswith(".py"):
            module_name = f"{command_folder}.{filename[:-3]}"
            import_module(module_name)
            print(f"   🔹 Loaded: {filename}")
