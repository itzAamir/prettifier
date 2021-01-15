# Author: itzAamir
# Date : 14/01/2021

import os
import re


# Function to sort the folders present in directory
def sorted_alphanumeric(data):
    def convert(text): return int(text) if text.isdigit() else text.lower()
    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


def rename_file(arr_of_file):
    # Loop to change the name of all the folders
    try:
        for i in range(len(arr_of_file)):
            os.rename(
                f"{os.getcwd()}/{arr_of_file[i]}", f"{os.getcwd()}/{i+1} {arr_of_file[i]}")
    except WindowsError:
        pass


def prettify_folder():
    dir = sorted_alphanumeric(os.listdir())
    new_dir = []
    exclude_folder_name = []
    for folder in dir:
        if os.path.isdir(folder):
            new_dir.append(folder)

    print(
        f"\n\nThese are the files present in your directory:\n\n{new_dir}\n\n")

    exclude_folder_option = input(
        "Do you want to Exclude any folder (y or n): ")
    if exclude_folder_option.lower() == "y":
        try:
            exclude_folder_number = int(
                input("\nHow many folders you want to exclude: "))
        except BaseException:
            print("\n\nPlease enter number only!\n\n",)

        # Loop to take the folder name as exclusion
        for i in range(exclude_folder_number):
            folder_name = input(f"Enter the exact name of folder {i+1}: ")
            exclude_folder_name.append(folder_name)

        # Loop to remove the folders if exist
        for f in exclude_folder_name:
            if f in new_dir:
                new_dir.remove(f)
            else:
                print(f"\nSorry folder name {f} does not exist!\n")

        print("\nThese files will be renamed:\n", new_dir, "\n")

        confirmation = input(
            "Press [y] to continue or any key to stop the program...\n")
        if confirmation.lower() == "y":
            rename_file(new_dir)
            print(
                "\n\nThanks for using folder prettifier, your folder has been prettified successfully :)\n")
        else:
            print("\n\nProgram Stopped\n")

    else:
        confirmation = input(
            "Press [y] to continue or any key to stop the program... ")
        if confirmation.lower() == "y":
            rename_file(new_dir)
            print(
                "\n\nThanks for using folder prettifier, your folder has been prettified successfully :)\n")
        else:
            print("\n\nProgram Stopped\n")


if __name__ == "__main__":
    prettify_folder()
