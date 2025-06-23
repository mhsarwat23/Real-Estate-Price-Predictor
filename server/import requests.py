import requests

def get_better_loc():
    # Step 1: Fetch city names and condition
    base = "https://quest.squadcast.tech/api/1OX21CS085/weather"
    weather_url = f"{base}/get?q="
    submit_url = "https://quest.squadcast.tech/api/1OX21CS085/submit/weather"
    
    try:
        response = requests.get(base)
        response.raise_for_status()
        data = response.json()
        city1, city2, condition = data['City1'], data['City2'], data['Condition']
        
        # Step 2: Fetch weather details for both cities
        weather1 = requests.get(weather_url + city1).json()
        weather2 = requests.get(weather_url + city2).json()
        
        # Parse necessary weather details
        temp1, temp2 = weather1['temperature'], weather2['temperature']
        wind1, wind2 = weather1['wind_speed'], weather2['wind_speed']
        rain1, rain2 = weather1.get('rain', 0), weather2.get('rain', 0)
        cloud1, cloud2 = weather1['cloud_coverage'], weather2['cloud_coverage']
        
        # Step 3: Evaluate condition
        if condition == "hot":
            better_loc = city1 if temp1 > temp2 else city2
        elif condition == "cold":
            better_loc = city1 if temp1 < temp2 else city2
        elif condition == "windy":
            better_loc = city1 if wind1 > wind2 else city2
        elif condition == "rainy":
            better_loc = city1 if rain1 > rain2 else city2
        elif condition == "sunny":
            better_loc = city1 if cloud1 < cloud2 else city2
        elif condition == "cloudy":
            better_loc = city1 if cloud1 > cloud2 else city2
        else:
            return "Invalid condition"
        
        # Step 4: Submit the result
        sub_url = f"{submit_url}?answer={better_loc}&extension=py"
        print("Submitting to:", sub_url)
        response = requests.post(sub_url, data={"code": _file_})
        response.raise_for_status()
        return response.text
    except Exception as e:
        return str(e)

# Run the function
print(get_better_loc())