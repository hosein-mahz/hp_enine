car_information ={
    "bernd"         : "bmw",
    "model"         :  630,
    "engine_hp" : [
        {
            "id_engine"    : 1,
            "title_engine" : "derg",
            "hp"           : 0
        },
        {
            "id_engine"    : 2,
            "title_engine" : "Street",
            "hp"           : 0
        }
    ]
}

engine_information =[
    {
        "id_engine"     : 1 ,
        "title_engine"   : "darg",
        "base_engine_hp" : 260,
        "turbo_hp"       : 15,
        "heathers_hp"    : 0
    },
    {
        "id_engine"     : 2 ,
        "title_engine"   :"steert",
        "base_engine_hp" : 260, 
        "turbo_hp"       : 0,
        "heathers_hp"    : 0
    },
    {
        "id_engine"     : 3 ,
        "title_engine"   :"boosted",
        "base_engine_hp" : 260,
        "turbo_hp"       : 20,
        "heathers_hp"    : 10
    
    }
]

def checkEngine(id_engine,engine_information) :
    z = []
    for x in id_engine:
        for y in engine_information:
            if x["id_engine"] == y["id_engine"]:
                print(x["id_engine"])
                z.append(x)
    return z

def hp_Engine(hp,engine_information):
    total_hp = 0
    for x in hp:
        # print(x["hp"])
        for y in engine_information:
            # print(y["hp_enine"])
            if x["id_engine"] == y['id_engine']:
                total_hp =(y["base_engine_hp"]+y["turbo_hp"]+y["heathers_hp"]) 
                # print(total_hp)
    return total_hp               
hp_Engine(car_information["engine_hp"],engine_information)