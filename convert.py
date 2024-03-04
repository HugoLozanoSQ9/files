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
    
    if content and isinstance(content,(list,dict)):
        content = json.dumps(content)
    file.write(content)
         

def update(file_name :str, content : list | dict)-> None:

    """Create or update a JSON File
    args:
        file_name: str
        content: list | dict 
        overwrite: Bool -> False you will update the file with another JSON info. 
    
    Raises:
        ValueError: only will see this error when not is a list | dict or this is void
    """

    if not isinstance(content, (dict, list)) or content == '':
        raise ValueError('content argument must be specified or not is the rigth value')
    
    file = open(file_name,'r')
    file_content = json.loads(file.read())
    file.close()

    if isinstance(file_content, list):
        if isinstance(content, dict):
            file_content.append(content)

        elif isinstance(content,list):
            file_content += content

    elif isinstance(file_content, dict):
        if isinstance(content,dict):
            file_content = [file_content,content]

        elif isinstance(content, list):
            file_content = [file_content] + content 
    file = open(file_name,'w')
    file.write(json.dumps(file_content))
    file.close()


def read(file_name:list | dict) -> list | dict:
    """
    Returns the content of a JSON text file

    args: 
        file_name(list | dict) : File name or path 
        Returns(list | dict ): File content
    
    Raises:
        FileNotFoundError: This error will appear when the file not exist
    
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f'File {file_name} was not found')

    file = open(file_name, "r")  # modo r, se puede quitar la r pq es el argumento por defecto
    file_name = file.read()
    python_user_list = json.loads(file_name)
    file.close()
    return python_user_list

