import glob
import importlib
from modules.exception import *
from os.path import basename, splitext

PLUGINS_DIR = "./plugins"

def get_plugins(plugins_dir = PLUGINS_DIR):
    plugins = {}
    plugin_files = glob.glob("{}/*.py".format(plugins_dir))
    for plugin_file in plugin_files:
        if plugin_file.endswith("__init__.py"):
            continue
        name, ext = splitext(basename(plugin_file))
        module_name = "plugins.{}".format(name)
        module = importlib.import_module(module_name)
        try:
            plugin = module.__plugin__()
        except AttributeError:
            raise Failed("Module '{}' has no attribute '__plugin__'".format(name))
        try:
            plugins[module.__cname__] = plugin
        except AttributeError:
            raise Failed("Module '{}' has no attribute '__cname__'".format(name))
    return plugins

def dispatch(plugin, fields):
    try:
        if not plugin.VerifyFields(fields):
            raise Failed('Invalid Fields')
    except (AttributeError, TypeError):
        raise Failed("'VerifyFields' function not defined")

    try:
        if not plugin.VerifyCredentials():
            try:
                plugin.Authorize()
            except (AttributeError, TypeError):
                raise Failed("'Authorize' function not defined")
            except (AuthorizationError, NetworkError), e:
                raise Failed(e.message)
    except (AttributeError, TypeError):
        raise Failed("'VerifyCredentials' function not defined")
    except NetworkError, e:
        raise Failed(e.message)

    req_fields_list = plugin.__fields__
    req_fields = {}
    for field in fields:
        if field in req_fields_list:
            req_fields[field] = fields[field]
    try:
        plugin.SendMsg(req_fields)
    except (AttributeError, TypeError):
        raise Failed("'SendMsg' function not defined")
    except NetworkError, e:
        raise Failed(e.message)
