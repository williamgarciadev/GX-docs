---
title: "TravelAgency Transactions model"
source_id: 6477
source_url: https://wiki.genexus.com/commwiki/wiki?6477
genexus_version: "18"
---

# TravelAgency Transactions model

This project, called TravelAgency, is aimed at developing a web site that will allow customers to search for the destinations, flights and services offered, as well as to book flights and make travel reservations.

**Note:** this model corresponds to a book entitled "GeneXus Rocha Episode 1", in a version prepared especially for the 2007 International event.

It is made up of a group of interrelated transactions, which are listed below (in alphabetical order):

```
Airline
Attraction
AttractionCategory
Country
Flight
FlightInstance
Passenger
```

And it also includes the following components to complete the knowledge:

* Bachman Diagram
* TravelAgency KB Domains

### [Airline](#Airline)

The objective is to store information about the different airlines and their planes.

`[imagen omitida: wiki id 6494]`

### [Attraction](#Attraction)

The objective is to store information about all the attractions offered by each city and country.

`[imagen omitida: wiki id 6497]`

### [AttractionCategory](#AttractionCategory)

This transaction categorizes the attractions of each country's cities: "Buildings/Structures," "Nightlife," "Relaxation," "Adventure," "Gastronomy," "Safaris," "Business," etc.

`[imagen omitida: wiki id 6498]`

With the Attraction and AttractionCategory transaction structures we are implicitly saying that an attraction belongs to only one category, while a category can contain n attractions.

### [Country](#Country)

Countries have cities, which means that reality determines that there are n cities per country. Then, you can easily represent this reality with a two-level transaction.

`[imagen omitida: wiki id 6505]`

That is why the Country transaction has two levels. The first level, also known as prolog or just header, is implicit and we don't need to identify it. In this case, the header's attributes imply that there's only one instance for each country.

### [Flight](#Flight)

This transaction will contain flight information such as description, airline, departure time, and maximum number of passengers. We will also have a departure and arrival city, which is data from reality that we need to know and store.

`[imagen omitida: wiki id 6506]`

It will be a two-level transaction. Each flight has three classes (First, Business and Economy) with up to three different fares, which makes it a price list (1-n relationship). All flights have only three different fares. Keep in mind that the flight ID must not be autonumbered because this number is defined by an international standard that includes their route and time. For example, Pluna Flight 0174 from Montevideo to Buenos Aires operates on Saturday mornings. If it is moved to the afternoons, the flight number will change as well.

You will need two subtype groups to complete the transaction:

`[imagen omitida: wiki id 6507]` `[imagen omitida: wiki id 6508]`

### [FlightInstance](#FlightInstance)

The Flight transaction handles flight information; for instance, Pluna Flight 0174 from Montevideo to Buenos Aires departs daily at 11:15 AM. For each flight 0174, there will be an actual plane flying on a certain date, with a certain number of passengers on board.

The following transaction represents the actual flight, with information such as date and departure time, number of passengers, reservations, names and seat numbers. Here, the ID will be autonumbered.

`[imagen omitida: wiki id 6514]`

### [Passenger](#Passenger)

The objective is to store information about the passengers.

`[imagen omitida: wiki id 6515]`

### [Bachman diagram](#Bachman+diagram)

The following Bachman Diagram represents the relationships between the tables.

`[imagen omitida: wiki id 6518]`

### [TravelAgency KB domains](#TravelAgency+KB+domains)

Applications usually have attributes that share the same data type, size and other features. For example, the Attraction transaction has several “Id” attributes (AttractionId, AttractionCategoryId, CityId, and CountryId).

Each domain is a set of unique features that may be shared by several attributes. This allows for consistency and ease of maintenance, as changing a domain feature propagates the change to all the attributes based on that domain.

`[imagen omitida: wiki id 6517]`
