def create_file(file_name, content=None):
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise OSError(f"File '{file_name}'already exists") from error
    except PermissionError as error: 
        raise OSError(f'You do not have permisson to create "{file_name}"')from error
    

    if content:
        file.write(content)


def update(file_name, content, overwrite=False):

    if not isinstance(content,str) or content == '':
        raise ValueError('content argument must be specified')
    
    mode = "w" if overwrite else "a"

    file = open(file_name, mode)
    file.write(content)
    file.close()


def read_file(title):
    file = open(title, "r")  # modo r
    content = file.read()
    file.close()
    return content