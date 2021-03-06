# -------------------------------------------

# Created by:               jasper
# Date:                     11/24/19

# --------------------------------------------

from os import path, mkdir


class IOHandler:

    def __init__(self, directory, fName, data_instance):
        """Save the setup of a class instance or load a class instance from a saved setup


        Parameters
        ----------
        directory : str
            path of the directory the files are saved to or read from
        fName : str
            Name of the project. File endings will be set automaticaly
        data_instance : object
            class instance to perform actions on
        """
        self.fName = fName
        self.data_instance = data_instance
        self.directory = directory

    def dump_data(self):
        """save the data contained in data_instance, checking whether the
        directories already exist and asking whether to create them if not. """
        while not path.isdir(self.directory):
            print(
                "# The directory {} does not exist. Do you want to create it (1, default) or specify another? (2) [1/2]".format(
                    self.directory))
            select = input()
            if select == "2":
                self.directory = input("Enter new directory: \n")
            else:
                mkdir(self.directory)
                print("# Directory " + self.directory + " created")

        self.fullpath = self.directory + "/" + self.fName

        self.data_instance.dump_data(self.fullpath)

    def dump_data_to_txt(self):
        while not path.isdir(self.directory):
            print(
                "# The directory {} does not exist. Do you want to create it (1, default) or specify another? (2) [1/2]".format(
                    self.directory))
            select = input()
            if select == "2":
                self.directory = input("Enter new directory: \n")
            else:
                mkdir(self.directory)
                print("# Directory " + self.directory + " created")

        self.fullpath = self.directory + "/" + self.fName

        self.data_instance.dump_to_txt(self.fullpath)

    def read_data(self):
        """Read data into the specified data_instance. If the read process
        hits a not existing file, it will be notified to you"""

        try:
            self.data_instance.read_data(self.directory + self.fName)
        except FileNotFoundError as file_error:
            print(
                "# The file {} belonging to {} do not exist.".format(
                    file_error.filename, self.fName))
