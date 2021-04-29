from mods import feature01
from mods import feature02
from mods import feature03
from mods import feature04
from mods import feature05
from mods import feature06
from mods import feature07
from mods import feature08
from mods import feature09
from mods import feature10
from mods import feature11
from mods import feature12
from mods import feature13
from mods import feature14
from mods import feature15
from mods import feature16
from mods import feature17
from mods import feature18
from mods import feature19
from mods import feature20

header = "De volgende features zijn aanwezig:\n\n"
mods = []
sep = "---------------------"

for mod in dir():
    mod_text = sep
    if 'feature' in mod:

        module = globals()[mod]
        if getattr(module, 'implemented'):
            mod_text += "\n" + mod + "\n" + sep + "\n"
            mod_text += '*** Samenvatting ***\n' + getattr(module, 'summary')
            funcs = [x for x in dir(module) if callable(getattr(module, x))]
            if len(funcs) > 0:
                mod_text += "\n*** Functies ***\n"
                for f in funcs:
                    mod_text += f +": " + getattr(module, f).__doc__ + "\n"
                mod_text += "\n"
        else:
            mod_text += "\n" + mod + " (niet geïmplementeerd)\n"
        mods.append(mod_text)

print(header + ''.join(mods))

