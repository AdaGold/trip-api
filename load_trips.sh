#!/bin/bash

# Define the trips as a JSON array
trips='[
  {
    "name": "Safari Adventure in Kenya",
    "cost": 4500,
    "weeks": 2,
    "continent": "Africa",
    "category": "Adventure",
    "about": "Embark on a thrilling safari through Kenya'"'"'s iconic national parks, encountering elephants, lions, and breathtaking savannah landscapes."
  },
  {
    "name": "Backpacking the Alps",
    "cost": 3200,
    "weeks": 3,
    "continent": "Europe",
    "category": "Adventure",
    "about": "Hike through stunning alpine trails across Switzerland, France, and Austria while enjoying scenic mountain villages and crisp, fresh air."
  },
  {
    "name": "Island Hopping in the Philippines",
    "cost": 2800,
    "weeks": 2,
    "continent": "Asia",
    "category": "Sight-Seeing",
    "about": "Discover the natural beauty of the Philippines by hopping between white-sand islands, turquoise lagoons, and vibrant coral reefs."
  },
  {
    "name": "Road Trip through Patagonia",
    "cost": 5000,
    "weeks": 4,
    "continent": "South America",
    "category": "Adventure",
    "about": "Journey through the wild terrain of Patagonia, exploring glaciers, mountain peaks, and remote villages along one of the world'"'"'s most scenic drives."
  },
  {
    "name": "Surfing and Sunsets in Australia",
    "cost": 4200,
    "weeks": 3,
    "continent": "Australasia",
    "category": "Adventure",
    "about": "Catch waves on Australia'"'"'s famous Gold Coast, soak in beach culture, and enjoy unforgettable sunsets and laid-back vibes."
  },
  {
    "name": "Northern Lights in Iceland",
    "cost": 3500,
    "weeks": 2,
    "continent": "Europe",
    "category": "Sight-Seeing",
    "about": "Experience the magical northern lights, explore ice caves, and relax in geothermal lagoons on this unforgettable Icelandic journey."
  },
  {
    "name": "Wildlife Wonders of the Amazon",
    "cost": 4700,
    "weeks": 3,
    "continent": "South America",
    "category": "Adventure",
    "about": "Venture deep into the Amazon rainforest, encountering exotic wildlife, indigenous cultures, and the unparalleled biodiversity of the jungle."
  },
  {
    "name": "Historical Treasures of Egypt",
    "cost": 3100,
    "weeks": 2,
    "continent": "Africa",
    "category": "Sight-Seeing",
    "about": "Explore the ancient wonders of Egypt—from the Great Pyramids to the Valley of the Kings—while cruising the historic Nile River."
  },
  {
    "name": "Cultural Escape to Japan",
    "cost": 4300,
    "weeks": 3,
    "continent": "Asia",
    "category": "Culture",
    "about": "Immerse yourself in Japan'"'"'s rich traditions, futuristic cities, serene temples, and delectable cuisine in a trip blending old and new."
  },
  {
    "name": "National Parks Extravaganza in the USA",
    "cost": 3900,
    "weeks": 3,
    "continent": "North America",
    "category": "Adventure",
    "about": "Visit America'"'"'s top national parks, from Yellowstone to Yosemite, for hiking, wildlife spotting, and awe-inspiring natural beauty."
  }
]'

# Convert JSON array into individual JSON objects and POST each
echo "$trips" | jq -c '.[]' | while read trip; do
  echo "Posting: $trip"
  curl -X POST https://trektravel.onrender.com/trips \
    -H "Content-Type: application/json" \
    -d "$trip"
  echo -e "\n"
done

