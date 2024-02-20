import os

#############COULDNT REACH THE ENV PATH#############

current_file_directory = os.path.dirname(os.path.abspath(__file__))

# Now, go up two levels to the root of the project
project_root_directory = os.path.dirname(os.path.dirname(current_file_directory))

# The .env file path will be the project root directory joined with the .env filename
envFilePath = os.path.join(project_root_directory, 'app\.env')

#####################################################

def store_key_env(keyName,key):

    with open(envFilePath, "r") as file:
        lines = file.readlines()

    updatedLines = []
    keyFound = False

    for line in lines:
        if line.startswith(keyName+"="):
            updatedLines.append(f"{keyName}={key}\n")
            keyFound = True
        else:
            updatedLines.append(line)

    if not keyFound:
        updatedLines.append(f"{keyName}={key}\n")

    with open(envFilePath,"w") as file:
        file.writelines(updatedLines)