import json
import os



class ManageJson:
    def __init__(self):
        self.data = None

        self.get_file()

    def get_file(self):
        dir_path = os.path.join(os.getcwd(), "data")

        if os.path.isdir(dir_path):
            self.path = os.path.join(dir_path, "data.json")

            if os.path.isfile(self.path):
                self.load()
            else:
                print(f"File does not exist on this directory: \n   {self.path} \nPlease verify and try again")
        else:
            print(f"Directory does not exist: \n   {dir_path} \nPlease verify and try again")
        
    def load(self):
        try:
            with open(self.path) as f:
                self.data = json.load(f)
        except Exception as error:
            print(f"Exception Error: {error}")

    def save(self):
        # Save the updated data to the JSON file
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def create(self, parent_key, child_key="", child_val=None):
        if self.data:
            if parent_key:
                if parent_key not in self.data:
                    self.data[parent_key] = {}
                    self.data[parent_key]["filter_columns"] = {}
                    self.data[parent_key]["sheet_name"] = ""
                    self.data[parent_key]["skiprows"] = 0

                    self.save()
                else:
                    if child_key:
                            if child_key in self.data[parent_key]:
                                if child_val is not None:
                                    if type(child_val) == dict:
                                        
                                        for col_name, filter_col in child_val.items():
                                            if col_name not in self.data[parent_key][child_key]:
                                                self.data[parent_key][child_key][col_name] = filter_col
                                            
                                            else:
                                                for val in filter_col:
                                                    if val not in self.data[parent_key][child_key][col_name]:
                                                        self.data[parent_key][child_key][col_name].append(val)
                                    else:
                                        self.data[parent_key][child_key] = child_val

                                    self.save()
                                else:
                                    print("Child_val is required.")
                            else:
                                print(f"Please specifed your child key, 'filter_columns', 'sheet_name' or 'skiprows' ")
                    else:
                        print(f"{parent_key} already exist")
            else:
                print("Parent_key is required")
        else:
            print("Data does not exist, load your data and try again")

    def read(self, parent_key, child_key=""):
        if self.data:
            if parent_key in self.data:
                if child_key:
                    if child_key in self.data[parent_key]:
                        return self.data[parent_key][child_key]
                    else:
                        print(f"Key {child_key} does not exist.")
                        return None
                
                return self.data[parent_key]
            else:
                print(f"Key {parent_key} does not exist.")
                return None
        else:
            print("Data does not exist, load your data and try again")
            return None

    def update(self, parent_key, child_key, child_val, col_name=""):
        if self.data:
            if parent_key:
                if parent_key in self.data:
                    if child_key:
                        if child_key in self.data[parent_key]:
                            if type(child_val) == list:
                                if col_name:
                                    if col_name in self.data[parent_key][child_key]:
                                        self.data[parent_key][child_key][col_name] = child_val
                                        self.save()
                                        return True
                                    else:
                                        print(f"Column '{col_name}' does not exist") 
                                        return False
                                else:
                                    print(f"'col_name' is required")  
                                    return False     
                            else:
                                self.data[parent_key][child_key] = child_val
                                self.save()
                                return True
                        else:
                            print(f"{child_key} does not exist.")
                            return False
                    else:
                        print(f"'child_key' is required")
                        return False
                else:
                    print(f"{parent_key} does not exist.")
                    return False
            else:
                print("'parent_key' is required")
                return False

        else:
            print("Data does not exist, load your data and try again")
            return False

    def delete(self, parent_key, child_key, col_name="", col_item=""):
        if self.data:
            if parent_key:
                if parent_key in self.data:
                    if child_key:
                        if child_key in self.data[parent_key]:
                            if col_name:
                                if col_name in self.data[parent_key][child_key]:
                                    if col_item:
                                        self.data[parent_key][child_key][col_name].remove(col_item)
                                    else:
                                        del self.data[parent_key][child_key][col_name]

                                    self.save()
                                    return True
                                else:
                                    print(f"{col_name} does not exist.")
                                    return False
                            else:
                                del self.data[parent_key][child_key]
                                self.save()
                                return True
                        else:
                            print(f"{child_key} does not exist.")
                            return False
                    else:
                        del self.data[parent_key]
                        self.save()
                        return True
                else:
                    print(f"{parent_key} does not exist.")
                    return False  
            else:
                print("'parent_key' is required")
                return False
        else:
            print("Data does not exist, load your data and try again")
            return False