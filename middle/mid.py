import eel
from back.convert import convert_value

@eel.expose
def convert_value_py(value:float, from_cur:str, to_cur:str)->float:
    return convert_value(value, from_cur, to_cur)