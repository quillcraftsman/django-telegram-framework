from typing import Any

def update(frozen_object: Any, **kwargs):
    frozen_object_dict = frozen_object.__dict__.copy()
    for k,v in kwargs.items():
        frozen_object_dict[k] = v
    return frozen_object.__class__(**frozen_object_dict)
