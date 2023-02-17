def add_time(start, duration, startweek= False): 

#splitting the time string into hours and minutes and casting them to int for calculations 
  hour_minute, PM_AM = start.split()
  hour, minute = hour_minute.split(":")
  hour = int(hour)
  minute = int(minute)
  week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  
 #Splitting the duration into hours and minutes to add to the start time 
  hour_added, min_added = duration.split(":")
  hour_added = int(hour_added)
  min_added = int(min_added)
    
  #Adding the start minutes to duration minutes
  new_min = minute + min_added

# if added minutes is more than 60, then iterate and add an hour until less than 60
  
  while new_min >= 60:
    new_min -= 60
    hour_added+=1

#Formatting the new minute to correct time format 
  final_min = str(new_min).rjust(2, "0")
  
# figuring out how many days are added to the start time and how many hours remain 
  new_days = hour_added//24
  extra_hours = hour_added % 24

#final hour is a measure of the number of hours that we started with and how many hours were added. 
  final_hour = hour + extra_hours
  
  PM_AM_A = ""

#Flipping the AM/PM to PM/AM when necessary 
  if (PM_AM == "PM") and  (final_hour >=12):
    PM_AM_A = "AM"
    new_days+=1
    if final_hour !=12:
      final_hour-=12 
    else: 
      final_hour
    
  elif (PM_AM =="PM") and (final_hour <12):
    PM_AM_A ="PM"
    final_hour = final_hour

  elif (PM_AM =="AM") and (final_hour >= 12):
    PM_AM_A = "PM"
    new_days = new_days
    if final_hour !=12:
      final_hour-=12 
    else: 
      final_hour

  elif (PM_AM =="AM") and (final_hour < 12):
    PM_AM_A = "AM"
    final_hour = final_hour
    new_days = new_days


#Concatinating the return strings 
  if startweek:
    startweek = startweek.strip().lower()
    selected_day = int((week_days.index(startweek) + new_days) % 7)
    current_day = week_days[selected_day]
    if new_days ==0:
      new_time = f"{final_hour}:{final_min} {PM_AM_A}, {current_day.title()}"
    elif new_days ==1: 
      new_time = f"{final_hour}:{final_min} {PM_AM_A}, {current_day.title()} (next day)"
    else:
      new_time = f"{final_hour}:{final_min} {PM_AM_A}, {current_day.title()} ({new_days} days later)"

  else: 
    if new_days ==0:
      new_time = f"{final_hour}:{final_min} {PM_AM_A}"
    elif new_days ==1: 
      new_time = f"{final_hour}:{final_min} {PM_AM_A} (next day)"
    else:
      new_time = f"{final_hour}:{final_min} {PM_AM_A} ({new_days} days later)"
  
  return new_time