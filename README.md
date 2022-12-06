# Trip API™

Welcome to the Trip API™™™, that services the Ada Trip Reserving Service!

The Ada Trip Reserving Service does two things very well:
  1. helps tour guides create Trip packages catered to global travelers
  2. helps travelers find Trip packages that fit their needs, and make a reservation for that trip

Read the API documentation for more details.

## Actions

### Retrieve list of all Trip packages
`get` `https://trektravel.herokuapp.com/trips`

### Retrieve list of all Trips by continent
`get` `https://trektravel.herokuapp.com/trips/continent?query={continent}`

Accepted query params:
- `query` (string), represents the continent of the trip results to filter by
    - Required
    - Must be one of the following values: `"Africa"`, `"Antarctica"`, `"Asia"`, `"Australasia"`, `"Europe"`, `"North America"`, `"South America"`

### Retrieve list of all Trips by max amount of weeks
`get` `https://trektravel.herokuapp.com/trips/weeks?query={weeks}`

Accepted query params:
- `query` (string), represents the max duration of the trips to filter by, in weeks
    - Required
    - Must be a number

### Retrieve list of all Trips by max budget
`get` `https://trektravel.herokuapp.com/trips/budget?query={budget}`

Accepted query params:
- `query` (string), represents the max budget of the trips to filter by, in whole dollar amount
    - Required
    - Must be a number
    - budget is in dollar amount, above represents $5,000

### Retrieve Data on Single Trip From ID
`get` `https://trektravel.herokuapp.com/trips/{id}`

### Retrieve all reservations of a Trip
`get` `https://trektravel.herokuapp.com/trips/{id}/reservations`

### Add a New Trip package to be listed
`post` `https://trektravel.herokuapp.com/trips`

Accepted query params:
- `name` (string), represents the name of your trip
  - Required
- `continent` (string), represents the continent that the trip takes place in
  - Required
  - Must be one of the following values: `"Africa"`, `"Antarctica"`, `"Asia"`, `"Australasia"`, `"Europe"`, `"North America"`, `"South America"`
- `about` (string), represents a description of this trip and why someone would join this trip
  - Optional
- `category` (string), represents a broad category or tag of this trip
  - Required
- `weeks` (integer), represents the duration of this trip in number of weeks
  - Required
  - Must be a number
- `cost` (float), represents the cost of this trip in USD
  - Required
  - Must be a number

### Reserve a Ticket on a Trip package
`post` `https://trektravel.herokuapp.com/trips/{trip id}/reservations`

Accepted query params:
- `name` (string), represents the name of the primary traveler on the trip reservation
  - Required
- `age` (integer), represents the age of the primary traveler on the trip reservation
  - Optional
- `email` (string), represents the contact email of the primary traveler on the trip reservation
  - Required

## Note: Feel free to dive into the source code

If this API documentation seems lacking, feel free to dive into the source code to find out what's going on. It's an API built in Ruby on Rails!
