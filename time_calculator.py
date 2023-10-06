import re


def add_time(start, duration, day_of_week=""):

  hours1, minutes1, midday1 = re.split(r":| ", start)
  hours2, minutes2 = duration.split(":")
  hours3 = int(hours1) + int(hours2)
  minutes3 = int(minutes1) + int(minutes2)
  midday3 = midday1
  whatDay = ""
  days = 0

  while minutes3 >= 60:
    hours3 += 1
    minutes3 -= 60

  while hours3 >= 24:
    hours3 -= 24
    days += 1

  #if (hours3 > 12):
  #midday3 = "PM"
  #else:
  #midday3 = "AM"

  if int(hours1) < 12 and hours3 >= 12:
    if midday1 == "PM":
      midday3 = "AM"
      days += 1
    elif midday1 == "AM":
      midday3 = "PM"

  if days == 1:
    whatDay = " (next day)"
  elif days > 1:
    whatDay = " (" + str(days) + " days later)"

  if hours3 > 12:
    hours3 -= 12

  week = [
      "Monday", "tuesday", "Wednesday", "Thursday", "Friday", "saturDay",
      "Sunday"
  ]
  if day_of_week != "":
    current_day_index = week.index(day_of_week)
    added_days = days

    if (added_days >= 7):
      added_days = added_days % 7
    new_day_index = current_day_index + added_days

    if (new_day_index >= len(week)):
      new_day_index = new_day_index % 7

  if day_of_week == "":
    new_time = str(hours3) + ":" + str(minutes3).zfill(
        2) + " " + midday3 + whatDay
  elif day_of_week != "":
    new_time = str(hours3) + ":" + str(minutes3).zfill(
        2) + " " + midday3 + ", " + week[new_day_index] + whatDay

  return new_time
