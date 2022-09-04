from data import people, basic_plants_list, plants_list, plants_dict

if bool(people) and all([person[1] for person in people]):
    print("Sending email")  # if no emails are blank
else:
    print("User must edit the list of recipients")  # email is blank


if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")  # contains at least on grass
else:
    print("No grass in this pack")

if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This dict contains grass")
else:
    print("No grass in the dict")
