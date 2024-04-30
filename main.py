from manage import ManageJson

filter_columns = {
    "STATUT ECO": [
        "3 TRES RETARD",
        "2 RETARD",
        "Define Components",
        "Create",
        "CIWE/IHWE/ITD C2V JJH"
        "Wait App. RT CP",
        "Reviewed",
        "Released",
        "(vide)",
        ""
    ],
    "Retard": [
                "3 TRES RETARD", "2 RETARD"
    ],
    "METIER": [
        "CIWE/IHWE/ITD C2V JJH"
    ],
    
}

manage_json = ManageJson()

# manage_json.create("Youness Status") # done
# manage_json.create("Youness Status", "filter_columns", filter_columns) # done
# manage_json.create("Youness Status", "sheet_name", "Your Sheet name") # done
# manage_json.create("Youness Status", "skiprows", 10) # done


# print(manage_json.read("Youness Status" )) # done
# print(manage_json.read("Youness Status", 'filter_columns')) # done
# print(manage_json.read("Youness Status", 'sheet_name')) # done
# print(manage_json.read("Youness Status", 'skiprows')) # done


# upd = manage_json.update("Youness Status", "sheet_name", "New Sheet Name", None) # done
# upd = manage_json.update("Youness Status", "skiprows", 20, None) # done
# val_upd = ["3 TRES RETARD", "2 RETARD","CIWE/IHWE/ITD C2V JJH", "Wait App. RT CP"]
# upd = manage_json.update("Youness Status", "filter_columns", val_upd, "Retard") # done

# if upd:
#     print("success updating")
# else:
#     print("something is wrong")



# delete = manage_json.delete("Youness Status", "skiprows") # done
# delete = manage_json.delete("Youness Status", "sheet_name") # done
# delete = manage_json.delete("Youness Status", "filter_columns", "Retard", "3 TRES RETARD") # done
# delete = manage_json.delete("Youness Status", "filter_columns", "Retard",) # done
# delete = manage_json.delete("Youness Status", "filter_columns") # done
# delete = manage_json.delete("Youness Status", "") # done

# if delete:
#     print("success delete")
# else:
#     print("something is wrong")

def serializer(tab_name, state=False):
    data_grid = []

    for parent_key, parent_values in manage_json.data.items():

        for child_key, child_val in parent_values.items():

            if state:
                if type(child_val) == dict:
                    for col_name, col_val in child_val.items():
                        data = {}
                        data["parent"] = parent_key
                        data[tab_name] = col_name
                        data["values"] = ", ".join(col_val)
                        data_grid.append(data)
            else:

                if child_key in tab_name.replace(" ", "_").lower():
                    data = {}
                    data["Parent"] = parent_key
                    data[tab_name] = child_val
                    data_grid.append(data)

    print(data_grid)

tab_name = "Skiprows"

# serializer(tab_name)

