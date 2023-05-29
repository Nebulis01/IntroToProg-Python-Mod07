# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Pickling and Error Handling
# ChangeLog (Who,When,What):
# Nathan Shelby,29MAY2023,Initial Commit
# ------------------------------------------------------------------------ #

# -- Import -- #
import pickle, os

# -- Processing -- #

def picklesomeitems():
    # Creating a selection of items to pickle
    firearm_manufacturer = ["Winchester", "Remington", "Springfield"]
    firearm_type = ["Pistol", "Shotgun", "Rifle"]
    firearm_action = ["Semi-Automatic", "Revolver", "Bolt", "Break", "Pump"]

    # Opening a file, using 'wb' to write binary data, creating as required, overwriting if exists
    f_db = open("firearms.db", "wb")

    # Place the items in the database
    pickle.dump(firearm_manufacturer, f_db)
    pickle.dump(firearm_type, f_db)
    pickle.dump(firearm_action, f_db)

    # ensure the file handle is closed and items are written to disk
    f_db.close()

def unpicklesomeitems():
    #globalize variables for reuse
    global firearm_manufacturer, firearm_action, firearm_type, f_db_ro
    #ensure variables are empty
    firearm_manufacturer = None
    firearm_action = None
    firearm_type = None

    # Open file to read, using 'rb' to read binary data
    f_db_ro = open("firearms.db", "rb")

    # unpickle the object and return it to variable for use
    firearm_manufacturer = pickle.load(f_db_ro)
    firearm_action = pickle.load(f_db_ro)
    firearm_type = pickle.load(f_db_ro)

# Pickle List
print("Preparing a list of items to pickle.")
picklesomeitems()
print("Unpickling the list and presenting it now.")
unpicklesomeitems()
print("\nA list of Manufacturers:")
print(firearm_manufacturer)
print("\nA list of Actions:")
print(firearm_action)
print("\nA list of Types:")
print(firearm_type)

# Error Handling
print("\nCleaning up file on disk and exiting...")
# This try fails on purpose, as the file is open and in use
try:
    os.remove("firearms.db")
except:
# Take the general exception and provide an error
    print("\nUnable to remove the file!")
finally:
# Proceed after the exception to perform another operation before removing the file
    print("\nAttempting to close the file and remove it now..")
    f_db_ro.close()
    os.remove("firearms.db")
# Check to see the file is actually deleted before printing the goodbye.
    if not os.path.exists("firearms.db"):
        print("\nFile removed successfully, goodbye.")
        exit()
