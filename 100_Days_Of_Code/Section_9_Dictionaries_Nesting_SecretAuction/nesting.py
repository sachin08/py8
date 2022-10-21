#instead {key : value, key2 : value2,}
#we can also {key : [list], key : {dictionary},} -> notice how this is a list and dict nested inside another dict

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

 #Nesting a list in a Dict  

travel_vlog = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dict in a dict

travel_vlog_adv = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12}, #labelling what kind of data this is so cities_visited is associated now with a key/label : cities_visited
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":10},
}

#nesting a dict inside a list

#[{
#   key: [list],
#   key2: {Dict},
# } -> Index 0,
# {
#   key: value,
#   key2: value,
# } -> Index 1]

travel_vlog_dinl = [
    {
        "country": "France", #String
        "cities_visited": ["Paris", "Lille", "Dijon"], #List
        "total_visits":12, #Number
    }, #now we have entire dict having 3 pieces of data, countries and cities visited and total no of visits
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits":10,
    },
]
