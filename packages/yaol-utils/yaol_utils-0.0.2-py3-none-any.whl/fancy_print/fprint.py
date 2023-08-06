from varname import argname
import inspect


def fprint(object, max_length=0, name=""):
    """ A fancier print function
    
    Args:
        name (str): Title of the printout
        object (str): The variable / object you like to print
        max_length (int): Defines the width of the print box
    """
    object = str(object)
    try:
        name = argname('object')
    except:
        if len(name) > 0:
            name = name
        else:
            name = str(object)

    # Credit: https://stackoverflow.com/a/6811020/13219555

    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    position_info = ["file: " + info.filename, "line: " + str(info.lineno)]
    length = round(max(len(object), len(name)) / 10) * 10 + 10
    if max_length < length:
        max_length = length
    hr = "#" + "="*(max_length - 2) + "#"

    def text_field(name):
        length = len(name)
        return str("#" + " "*int((max_length - length)/2 - 1) + name +
              " "*int((max_length - length)/2 + 1*(len(name)%2 - 1)) + "#")

    if len(object) > max_length - 5:
        object_split = []
        while len(object) > max_length - 5:
            object_split.append(object[:max_length-5])
            object = object[max_length-5:]
        object_split.append(object[:max_length-5])
    else:
        object_split = [object]
    
    print("")
    print(hr)
    print(text_field(name))
    print(hr)
    for obj in object_split:
        print(text_field(obj))
    print(hr)
    print("")
    print(position_info[0])
    print(position_info[1])
    print("")
    
if __name__ == "__main__":
    var_x = 555
    fprint(var_x)
    str_ = "Hello World!"
    fprint(str_, 40)
    fprint([1, 2, 3, 4, 5])
    fprint({"a": "b", "c": "d"}, name="A python dict")