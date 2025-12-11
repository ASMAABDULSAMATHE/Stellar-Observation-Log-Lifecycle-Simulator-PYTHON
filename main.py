#database list
stars_list=[]
#parent class
class stars:
  def __init__(self,name,brightness,age_million_years,obs_time,obs_date,stage):
    self.name=name
    self.brightness=brightness
    self.age_million_years=age_million_years
    self.obs_time=obs_time
    self.obs_date=obs_date
    self.stage=stage

#child class 1
class Protostar(stars):
  def __init__(self,name,brightness,age_million_years,obs_time,obs_date):
    super().__init__(name,brightness,age_million_years,obs_time,obs_date,stage="protostar")
    print("The collapsed dust and gas in space has started to heat up!")

#child class 2
class Main_sequence(stars):
  def __init__(self,name,brightness,age_million_years,obs_time,obs_date):
    super().__init__(name,brightness,age_million_years,obs_time,obs_date,stage="main_sequence")
    print("The star is fully formed!")

#child class 3
class Red_giant(stars):
  def __init__(self,name,brightness,age_million_years,obs_time,obs_date):
    super().__init__(name,brightness,age_million_years,obs_time,obs_date,stage="red_giant")
    print("The star is red huge and is running out of hydrogen ")

#method 1 to add stars to the log
def update_starlist():
    print("\n-----Add new star-----")
    name=input("Enter the name of the star: ")
    brightness=float(input("Enter the brightness: "))
    age_million_years=int(input("Enter age (million years): "))
    obs_time=input("Enter the observation time: ")
    obs_date=input("Enter the observation date(DD.MM.YY): ")
    print("Choose the star's stage:")
    print("1. Protostar")
    print("2. Main Sequence")
    print("3.Red Giant")
    while True:
      stage=input("Enter stage: ")
      if stage=="1":
        new_star=Protostar(name,brightness,age_million_years,obs_time,obs_date)
        break
      elif stage=="2":
        new_star=Main_sequence(name,brightness,age_million_years,obs_time,obs_date)
        break
      elif stage=="3":
        new_star=Red_giant(name,brightness,age_million_years,obs_time,obs_date)
        break
      else:
        print("Invalid stage.The star is not added.")
    stars_list.append(new_star)
    print(f"-----New star {name} added-----")

#method 2 to view all stars
def view():
    if (len(stars_list)!=0):
      print("\n-----Stars Observation Log-----")
      for index,star in enumerate(stars_list):
        print(f"\nStar {index+1} ___")
        print(f"Star name: {star.name.title()}")
        print(f"Brightness: {star.brightness}")
        print(f"Age: {star.age_million_years}")
        print(f"Stage: {star.stage}")
        print(f"The star was observed on {star.obs_date} at {star.obs_time}")
    else:
      print("-----No stars found-----")
      # if no stars are found the user can add the star data without returning
      # to menu
      update_starlist()

#method 3 to search for the star
def search():

    if len(stars_list)==0:
      print("-----No stars found-----")
      # if no stars are found the user can add the star data without returning
      # to menu
      update_starlist()

    else:
      print("\n-----Search for a star-----")
      name=input("Enter the name of the star to search: ")
      for star in stars_list:
        if star.name.lower()==name.lower():
          print(f"\n-----Star found-----")
          print(f"Star name: {star.name.title()}")
          print(f"Brightness: {star.brightness}")
          print(f"Age: {star.age_million_years}")
          print(f"Stage: {star.stage}")
          print(f"The star was observed on {star.obs_date} at {star.obs_time}")
          return
      print("The star is not found.")


#method 4 to simulate the lifecycle of the star
def simulate_lifecycle():
    view()
    if len(stars_list)==0:
        print("-----No stars found-----")
        update_starlist()
    else:
        name=input("\nEnter the name of the star to simulate lifecycle: ")
        for star in stars_list:
          if star.name.lower()==name.lower():
            print("-----Simulate Lifecycle-----")
            if star.stage.lower()=="protostar":
              new_star=Main_sequence(star.name,star.brightness,star.age_million_years+10,star.obs_time,star.obs_date)
              stars_list.remove(star)
              stars_list.append(new_star)
              print(f"{star.name.title()} has evolved from protostar to main sequence.")
              return
            elif star.stage.lower()=="main_sequence":
              new_star=Red_giant(star.name,star.brightness,star.age_million_years+100,star.obs_time,star.obs_date)
              stars_list.remove(star)
              stars_list.append(new_star)
              print(f"{star.name.title()} has evolved from main sequence to red giant.")
              return
            elif star.stage.lower()=="red_giant":
              print(f"{star.name.title()} is in red giant stage.")
              return
          print("The star is not found.")

#method 5 to delete the star data
def delete_star():
    view()
    if (len(stars_list)==0):
        print("-----No stars found-----")
        return
    else:
        name=input("\nEnter the name of the star to delete: ")
        for star in stars_list:
          if star.name.lower()==name.lower():
            stars_list.remove(star)
            print(f"-----Star {star.name.title()} deleted-----")
            return
          print("The star is not found. ")

#main
def menu():
  print("-----STELLAR OBSERVATION LOG & LIFECYCLE SIMULATOR-----")
  while True:
    try:
      print("\n1. Add new star")
      print("2. View list of stars")
      print("3. Search for a star ")
      print("4. Simulate Lifecycle")
      print("5. Delete a star")
      print("6. Exit")
      print("------------------------------------------------------")
      choice=input("\nEnter your choice:")
      if choice=='1':
                  update_starlist()
      elif choice=='2':
                  view()
      elif choice=='3':
                  search()
      elif choice=='4':
                  simulate_lifecycle()
      elif choice=='5':
                  delete_star()
      elif choice=='6':
                  print("\n-----Exiting the Log-----")
                  break
      else:
                  print("Invalid choice.Please try again.")
    except ValueError:
                  print("Invalid input.Please enter a number.")

menu()
