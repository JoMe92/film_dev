import ctypes
import itertools
import os
import string
import platform
import configparser # for ini files
import win32api
import win32file

def get_available_drives():
    '''create a list of all drives connected to the pc
    Returns
    -------
    list : str
    Returns a list with all avalible drives  
    '''
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))

def get_subfolder(path: str):
    ''' get all subfodler

    Parameters
    ----------
    path : str
    The path to the folder in which you want to search for subfolders

    Returns
    -------
    list
    Returns a list with all subfolders 
    '''
    subfolder = [sub for sub in os.listdir(path) if os.path.isdir(os.path.join(path, sub))]
    if subfolder== []:
        print("no subfolders were found")
    if subfolder != []:
        print("found " + str(len(subfolder)) + " folder")

    return subfolder

def get_files(path: str):
    ''' get all files inside the folder

    Parameters
    ----------
    path : str
    The path to the folder in which you want to search for files

    Returns
    -------
    list : str
    Returns a list with all file names 
    '''
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))] 
    if files== []:
        print("no files were found")
    if files != []:
        print("found " + str(len(files)) + " files")

    return files

def check_sd_present (dir_name : str, devicelist : str):
    ''' check if a known sd card is connected 
    Parameters
    ----------
    dir_name : str
    a list with all available drives
    devicelist : str
    a list with all Sd-Cards
    Return
    ------
    card_dir : str
    a list of all sd cards that have been detected
    '''

    # --- Run through all detected drives and compare them with the drives stored in the .ini file. --- 
    for i in dir_name:

        print("found drive: " + i[0] + ", " + i[1])
        for d in devicelist:
            dict = devicelist[d]
            card_dir = dict["dir"]
            card_name = dict["name"]
            drive_dir = str(i[1])
            drive_name = str(i[0])

            if drive_dir == card_dir and drive_name == card_name:
                print("--- device found ---")
                print("drive dic: " + i[1])
                print("drive name: " + i[0])
                print("card name: " + dict["name"])
                print("card dic: " + dict["dir"])
                return card_dir  
            else:
                print("still sercing....")
                # print(card_found + "and " + drive_found)
        print("--- no device found ---")



def read_ini (ini_file):
    '''  read an ini file at a given path
    
    Parameters
    ----------
    def read_ini : str
    path to file

    Return
    ------
    devicelist : str
    a dict with all ini parameters
    '''

    cfgfile = open(ini_file,'r')
    config = configparser.ConfigParser()
    config.read(ini_file)
    # name = config.get("Section1", "name")
    devicelist =  config._sections
    cfgfile.close()
    return devicelist







def findAvailableDrives():
    '''  get all conectet drives
    Return
    ------
    devicelist : str
    a list with all drive names
    '''
    return [(d, win32file.GetDriveType(d)) for d in
            win32api.GetLogicalDriveStrings().rstrip('\0').split('\0')]

def drive_name(dir_str):

    dir_name = []
    for i in dir_str[0:-1]: # the last element is not used because the drive is not present todo find err
        # print("--- Drive Info ---")
        # print(win32api.GetVolumeInformation(i[0]))
        dir_name.append((win32api.GetVolumeInformation(i[0])[0], i[0]))

    return dir_name