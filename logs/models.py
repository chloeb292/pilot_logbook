

from django.db import models

# Models

class Pilot(models.Model):
    
    # Pilot Base Info
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200)



    date_of_birth = models.DateField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Contact
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    # Address

    STATE_CHOICES = (("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming"))

    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
    def __str__(self): 
        return "%s %s" % (self.first_name , self.last_name)


class LogbookEntry(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    departure_apt = models.CharField(max_length=4)
    arrival_apt = models.CharField(max_length=4)
    departure_date = models.DateField(null=True)

    # Time in Aircraft Cat and Class 
    single_engine_time = models.FloatField(default=0, blank=True)
    multi_engine_time = models.FloatField(default=0, blank=True)
    rotorcraft_time = models.FloatField(default=0, blank=True)

    # Type of Piloting Time
    dual_recieved = models.FloatField(default=0, blank=True)
    pilot_in_command = models.FloatField(default=0, blank=True)
    second_in_command = models.FloatField(default=0, blank=True)
    as_flight_instructor = models.FloatField(default=0, blank=True)

    # Conditions of Flight
    day_time = models.FloatField(default=0.0, blank=True)
    night_time = models.FloatField(default=0.0, blank=True)
    x_country_time = models.FloatField(default=0.0, blank=True)
    actual_instrument_time = models.FloatField(default=0.0, blank=True)
    simulated_instrument_time = models.FloatField(default=0.0, blank=True)
    total_duration_of_flight = models.FloatField(default=0.0, blank=True)

    # Approaches/Landings
    number_instrument_approaches = models.IntegerField(default=0, blank=True)
    number_landings = models.IntegerField(default=0)

    notes_on_flight = models.CharField(max_length=200)

    def __str__(self): 
        return "%s to %s, Date: %s " % (self.departure_apt, self.arrival_apt, self.departure_date)
