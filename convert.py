import os
import json


def create(file_name:str, content: list | dict =None)-> None:
    """Create a new json file

    Args:
        file_name (str): file name or path
        content (list | dict, optional): Text file content or list or dict. Defaults to None.
    """
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise OSError(f"JSON'{file_name}'already exists") from error
    except PermissionError as error: 
        raise OSError(f'You do not have permisson to create "{file_name}"')from error
    
    if content:
        cre_list= [content]
        json_cre_list = json.dumps(cre_list)
        file.write(json_cre_list)
        

def update(file_name :str, content : list | dict , overwrite:bool=False):

    """Create or overwrite a JSON File
    args:
        file_name: str
        content: list | dict 
        overwrite: you will update the file with another JSON info. 
    
    Raises:
        ValueError: only will see this error when not is a list | dict or this is void
    """

    if not isinstance(content,list | dict) or content == '':
    
        raise ValueError('content argument must be specified')
    
    mode = "w" if overwrite else "a"

    file = open(file_name, mode)
    if mode == 'w':
        cre_list= [overwrite]
        json_cre_list = json.dumps(cre_list)
        file.write(json_cre_list)
    else:
        cre_list= [content]
        json_cre_list = json.dumps(cre_list)
        file.write(json_cre_list)
    file.close()


def read(file_name:list | dict) -> list | dict:
    """
    Returns the content of a JSON text file

    args: 
        file_name(list | dict) : File name or path 
        Returns(list | dict ): File content
    
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f'File {file_name} was not found')

    file = open(file_name, "r")  # modo r
    file_name = file.read()
    python_user_list = json.loads(file_name)
    file.close()
    return python_user_list

