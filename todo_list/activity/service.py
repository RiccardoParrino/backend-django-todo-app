from .models import Activity

def findAll ():
    return Activity.objects.all()

def create (author, name, date, description, city):
    activity = Activity(
        author=author, 
        name=name, 
        date=date, 
        description=description, 
        city=city
    )
    activity.save()
    return True

def update (name, new_name, new_date, new_description, new_city):
    old_activity = Activity.objects.get(name=name)
    old_activity.name = new_name if new_name is not None else old_activity.name
    old_activity.date = new_date if new_date is not None else old_activity.date
    old_activity.description = new_description if new_description is not None else old_activity.description
    old_activity.city = new_city if new_city is not None else old_activity.city
    old_activity.save()
    return True

def delete (name):
    Activity.objects.get(name=name).delete()
    return True