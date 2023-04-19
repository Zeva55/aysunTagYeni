import glob
from pathlib import Path
from Plugins.utils import load_edaletbalaev
import logging
from Plugins import edaletbalaev
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Plugins/edaletbalaev/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_edaletbalaev(plugin_name.replace(".py", ""))
    
print("Qoz kimi işləyirəm Ədoşş")

if __name__ == "__main__":
    edalet.run_until_disconnected()
