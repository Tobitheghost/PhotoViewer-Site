import os
import random

# Setup searches the Static Folder for more folder of images.
# Make sure to name the folders someting notable, the options in the drop down menu
# will be gave the same name as the accompaning folder.
# you can replace the 'Test Folder' with a different existing folder in Static to set
# as the default
def setup(folder = 'Test Folder'):
    parentFolder = f"viewer\static"
    folderDir = os.listdir(parentFolder)
    name = folder
    return name, folderDir

# list_dir searches the selected folder in Static and gathers all images and videos and
# adds them into a list.
def list_dir(folderName = 'Test Folder'):
    folderPath = f"viewer\static\{folderName}"
    imagePath = os.listdir(folderPath)
    imageList = []
    # add or remove extentions - included extentions are included in the list created from the selected folder
    accepted_imageExtensions = ['gif', 'jfif', 'jpeg', 'jpg', 'webp', 'svg', 'png', 'pjepg', 'pjp', 'bmp', 'tif', 'tiff', 'avif']
    accepted_videoExtensions = ['3gp', 'mp4', 'avi', 'mov', 'm4v', 'webm', 'wmv']
    accepted_Extensions = accepted_videoExtensions + accepted_imageExtensions
    for file in imagePath:
        for extention in accepted_Extensions:
            if extention in file.lower():
                imageList.append(file)
    print(accepted_Extensions)
    print(imageList, len(imageList))

    listLength = len(imageList)
    # Creates a number to seperate the given list into 5 seperate list to poulate the columns
    # if you want more or less colums, chance the value for num_of_columns
    num_of_columns = 5
    listInterval = int(listLength/num_of_columns)
    randListoffiles = random.sample(imageList, listLength)
    listOFlist = []

    for x in range(num_of_columns):
        startpoint = x * listInterval
        endpoint = (startpoint + listInterval)
        if x == 4: # when checking the list for the last column, in case your total files in your
                   # selected folder is not an multiple of 'num_of_columns', we add the remainer of the files into
                   # the last column 
            templist = randListoffiles[startpoint:(listLength)]
        else:
            templist = randListoffiles[startpoint:endpoint]
        listOFlist.append(templist)
        
    return listOFlist, accepted_videoExtensions

