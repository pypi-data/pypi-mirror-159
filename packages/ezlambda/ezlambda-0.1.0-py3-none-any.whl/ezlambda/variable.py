from __future__ import annotations
from typing import Any, Callable

class VariableOperationMarker:
    pass

class _VariableSuper(object):
    def getFunc(self):
        return super().__getattribute__("func")
    
    def setFunc(self, func):
        super().__setattr__("func", func)
    
    def getParams(self):
        return super().__getattribute__("params")
    
    def setParams(self, params):
        super().__setattr__("params", params)
    
    def getChild(self):
        return super().__getattribute__("child")
    
    def setChild(self, child):
        super().__setattr__("child", child)
    
    def _execute(self, *args, **kwargs):
        func = super(Variable, self).getFunc()
        params = super(Variable, self).getParams()
        # print("func:", func, sep="\n")
        # print("params:", params, sep="\n")
        # print("args:", args, sep="\n")
        # print("kwargs:", kwargs, sep="\n")
        if func is None:
            return None if len(args) == 0 else args[0] if len(args) == 1 else args
        return func(*args, **kwargs)

class Variable(_VariableSuper):
    def __init__(self, func: Callable | None = None, params: tuple = tuple(), child: Variable | None = None) -> None:
        super().setFunc(func)
        super().setParams(params)
        super().setChild(child)
    
    def __repr__(self) -> str:
        func = super().getFunc()
        if func is None:
            return "_(None)"
        return f"_(f = {repr(func).split('.')[1]}, p = {repr(super().getParams())}, c = {repr(super().getChild())})"

    def __call__(self, *args, **kwargs) -> Variable | Any:
        func = super().getFunc()
        if len(args) == 0 or not isinstance(args[0], VariableOperationMarker):
            return super()._execute(*args)
        if isinstance(args[0], VariableOperationMarker):
            args = args[1:]
        if func is None:
            return Variable(lambda f: f(*args, **kwargs), args, self)
        return Variable(lambda *largs: super(Variable, self).getFunc()(*largs)(), args, self)
    
    def __getattribute__(self, __name: str) -> Variable:
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: getattr(x, __name), (__name,), self)
        return Variable(lambda *largs: getattr(super(Variable, self).getFunc()(*largs), __name), (__name,), self)
    
    def __setattr__(self, __name: str, __value: Any) -> Variable:  # type: ignore # __setattr__ usually returns None, but here it is used to return an action that will set an object's attribute when called
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: setattr(x, __name, __value), (__name, __value), self)
        return Variable(lambda *largs: setattr(super(Variable, self).getFunc()(*largs), __name, __value), (__name, __value), self)
    
    def __add__(self, other: Any) -> Any:
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: x + other, (other,), self)
        return Variable(lambda *largs: super(Variable, self).getFunc()(*largs) + other, (other,), self)
    
    def __sub__(self, other: Any) -> Any:
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: x - other, (other,), self)
        return Variable(lambda *largs: super(Variable, self).getFunc()(*largs) - other, (other,), self)
    
    def __mul__(self, other: Any) -> Any:
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: x * other, (other,), self)
        return Variable(lambda *largs: super(Variable, self).getFunc()(*largs) * other, (other,), self)
    
    def __truediv__(self, other: Any) -> Any:
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: x / other, (other,), self)
        return Variable(lambda *largs: super(Variable, self).getFunc()(*largs) / other, (other,), self)
    
    def __floordiv__(self, other: Any) -> Any:
        func = super().getFunc()
        if func is None:
            return Variable(lambda x: x // other, (other,), self)
        return Variable(lambda *largs: super(Variable, self).getFunc()(*largs) // other, (other,), self)
