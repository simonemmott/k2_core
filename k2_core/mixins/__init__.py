import importlib
import logging

logger = logging.getLogger(__name__)

function_map = {}

def register(module_name, class_name):
    def wrapper(func):
        if module_name+'::'+class_name not in function_map:
            function_map[module_name+'::'+class_name] = {}
        class_map = function_map[module_name+'::'+class_name]
        class_map[func.__name__] = func
            
        return func
    return wrapper
    
def push_registry():
    logger.info('Push registry')
    for index, class_map in function_map.items():
        module_name, class_name = index.split('::')
        module = importlib.import_module(module_name)
        cls = getattr(module, class_name)
        for func_name, func in class_map.items():
            logger.info('Registering {name} on {cls}'.format(name=func_name, cls=module_name+'.'+class_name))
            setattr(cls, func_name, func)
        
    