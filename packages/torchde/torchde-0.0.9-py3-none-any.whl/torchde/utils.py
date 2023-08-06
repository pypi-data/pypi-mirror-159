import importlib
import typing as th
import types
import inspect
import os

# for eval context
import torch
import torchde

# types
CallableFunctionDescriptorStr = th.Union[str, th.Dict[str, th.Any]]
FunctionDescriptor = th.Union[th.Callable, CallableFunctionDescriptorStr]


def safe_function_call_wrapper(function: th.Callable):
    signature = inspect.signature(function)
    params = signature.parameters

    def wrapper(*args, **kwargs):
        call_kwargs = {name: kwargs[name] for name in params if name in kwargs}
        return function(*args, **call_kwargs)

    return wrapper


def generate_function(code_block, function: str) -> th.Callable[[th.Any], th.Any]:
    context = dict()
    exec(code_block, dict(), context)
    return types.FunctionType(
        code=context[function].__code__,
        globals=context,
        name=function,
        argdefs=context[function].__defaults__,
    )


def process_function_description(
    function: th.Union[th.Callable, str, th.Dict[str, str]], entry_function
) -> th.Callable:
    if callable(function) or not isinstance(function, (str, dict)):
        return function
    try:
        return eval(function if isinstance(function, str) else function["code"])
    except SyntaxError:
        return generate_function(
            code_block=function if isinstance(function, str) else function["code"],
            function=function.get("entry", entry_function) if isinstance(function, dict) else entry_function,
        )


def is_module(name):
    route_steps = name.split(".")
    route_steps = route_steps[1:] if not route_steps[0] else route_steps  # .modulename.<...>
    return os.path.exists(os.path.join(*route_steps[:-1], f"{route_steps[-1]}.py"))


def is_package(name):
    route_steps = name.split(".")
    route_steps = route_steps[1:] if not route_steps[0] else route_steps  # .modulename.<...>
    return os.path.exists(os.path.join(*route_steps, "__init__.py"))


def importer(name):
    try:
        return __import__(name, globals=globals(), locals=locals())
    except:
        route_steps = name.split(".")
        route_steps = route_steps[1:] if not route_steps[0] else route_steps
        is_name_module, is_name_package = is_module(name), is_package(name)
        assert is_name_module or is_name_package
        file_path = os.path.join(*route_steps)
        if is_name_module:
            file_path = f"{file_path}.py"
        else:  # name is definitely a package (because of the assertion)
            file_path = os.path.join(file_path, "__init__.py")
        spec = importlib.util.spec_from_file_location(name, file_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        return foo


def greedy_import_context(name, upwards: bool = False, level: int = 0):
    module_hierarchy = name.split(".")
    imported_module = None
    for trial_index in range(
        1 if upwards else len(module_hierarchy) - level,
        (len(module_hierarchy) + 1 - level) if upwards else -1,
        1 if upwards else -1,
    ):
        try:
            imported_module = importer(".".join(module_hierarchy[:trial_index]))
            break
        except:
            pass
    return imported_module, ".".join(module_hierarchy[trial_index:])


def __get_value(name: str, strict: bool = True, upwards=True, context=None):
    var, name = greedy_import_context(name, upwards=upwards) if context is None else (context, name)
    for split in name.split(".") if name else []:
        if isinstance(var, dict):
            if split not in var:
                if strict:
                    raise KeyError('Invalid key "%s"' % name)
                else:
                    return None
            var = var[split]
        else:
            if not hasattr(var, split):
                if strict:
                    raise AttributeError("Invalid attribute %s" % name)
                else:
                    return None
            var = getattr(var, split)
    return var


def get_value(name, prefer_modules: bool = False, strict: bool = True, context=None, num_trys=3):
    for _ in range(num_trys):
        try:
            return _get_value(name, strict=strict, prefer_modules=prefer_modules, context=context)
        except KeyError:
            pass
        except AttributeError:
            pass
        except ImportError:
            pass


def _get_value(name, prefer_modules: bool = False, strict: bool = True, context=None):
    results = []
    try:
        results.append(__get_value(name, upwards=True, strict=strict, context=context))
    except:
        pass
    try:
        results.append(__get_value(name, upwards=False, strict=strict, context=context))
    except:
        pass
    if not results:
        raise ImportError(name)
    if len(results) == 1:
        return results[0]

    # checking for successful lookup in non-strict config
    if not strict and results[0] is None and results[1] is not None:
        return results[1]
    elif not strict and results[0] is not None and results[1] is None:
        return results[0]

    # looking for modules
    if prefer_modules:
        return results[1] if inspect.ismodule(results[1]) else results[0]
    else:
        return results[0]


def set_value(name, value, context=None):
    var, name = greedy_import_context(name, upwards=True, level=1) if context is None else (context, name)
    for split in name.split(".")[:-1] if name else []:
        if isinstance(var, dict):
            var = var[split]
        elif isinstance(var, list):
            var = var[int(split)]
        else:
            var = getattr(var, split)
    if isinstance(var, dict):
        var[name.split(".")[-1]] = value
    else:
        setattr(var, name.split(".")[-1], value)


def args_list_len(*args):
    return max(len(arg) if isinstance(arg, (tuple, list)) else (1 if arg is not None else 0) for arg in args)


def list_args(*args, length: th.Optional[int] = None, return_length: bool = False):
    length = args_list_len(*args) if length is None else length
    if not length:
        results = args if len(args) > 1 else args[0]
        return results if not return_length else (results, length)
    results = [([arg] * length if not isinstance(arg, (tuple, list)) else arg) for arg in args]
    results = results if len(args) > 1 else results[0]
    return results if not return_length else (results, length)
