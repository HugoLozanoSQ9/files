def create(file_name:str, content: bool=None):
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise OSError(f"File '{file_name}'already exists") from error
    except PermissionError as error: 
        raise OSError(f'You do not have permisson to create "{file_name}"')from error
    

    if content:
        file.write(content)


def update(file_name :str, content : str, overwrite:bool=False):

    if not isinstance(content,str) or content == '':
        raise ValueError('content argument must be specified')
    
    mode = "w" if overwrite else "a"

    file = open(file_name, mode)
    file.write(content)
    file.close()


def read(file_name:str) -> str:
    """
    Returns the content of a text file 

    args: 
        file_name(str) : File name or path 
    Returns(str): File content
    
    """
    file = open(file_name, "r")  # modo r
    content = file.read()
    file.close()
    return content

