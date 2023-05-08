import requests
import tkinter as ttk


# Getting the weather from Weather API
def get_weather(place):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": place}

    headers = {
        "X-RapidAPI-Key": "9354e7df27msh31eaf3e677c502bp1c7eacjsn4fa05098af96",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    # Extracting needed data from JSON
    try:
        api_response = requests.get(url, headers=headers, params=querystring)

        final_response = api_response.json()
        final_temp = final_response["current"]["temp_c"]
        final_region = final_response["location"]["region"]
        final_country = final_response["location"]["country"]
        # Concatenating data to a string for presentation
        weather_info = f"{final_region} <==> {final_country} <==> Weather <==> {final_temp} C"
        return weather_info
    # Error Implementation
    except:
        return ""


# Getting the statistics from COVID API
def get_population(place):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        "X-RapidAPI-Key": "9354e7df27msh31eaf3e677c502bp1c7eacjsn4fa05098af96",
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }
    querystring = {"country": place}
    # Extracting needed data from JSON
    try:
        response = requests.get(url, headers=headers, params=querystring)
        co_final = response.json()
        population = co_final["response"][0]["population"]
        population_info = f'Population of {place} is {population}'
        return population_info
    # Error Implementation
    except:
        return ""


# Implementing Button Press to call function by using input as a parameter
# Adding if/else statements to implement errors and aesthetics
def press():
    target = lbl_input.get()
    weather_info = get_weather(target)
    population_info = get_population(target)

    if weather_info:
        weather_label.config(text=weather_info)
    else:
        weather_label.config(text="")
        error_label.config(text="ERROR")
    if population_info:
        population_label.config(text=population_info)
    else:
        population_label.config(text="")
        error_label.config(text="ERROR")


# GUI creation
# Window and Labels
window = ttk.Tk()
window.title("Weather 4 You")
window.configure(bg="gray")
window.geometry("500x150")

lbl_greeting = ttk.Label(text="Please enter City, Country or Postcode", fg="black", bg="gray", font=("Helvetica", 10))
lbl_greeting.grid(row=0, column=0, sticky="w")
lbl_input = ttk.Entry( fg="black", bg="gray", font=("Helvetica", 10))
lbl_input.grid(row=3, column=0)
population_label = ttk.Label(text="", fg="black", bg="gray", font=("Helvetica", 10))
population_label.grid(row=10, column=0)
weather_label = ttk.Label(text="", fg="black", bg="gray", font=("Helvetica", 10))
weather_label.grid(row=6, column=0)
error_label = ttk.Label(text="", fg="black", bg="gray", font=("Helvetica", 10))
error_label.grid(row=8, column=2)

button_submit = ttk.Button(text="Submit", fg="black", bg="gray", font=("Helvetica", 10), borderwidth=0.2, command=press)
button_submit.grid(row=4, column=0)

window.mainloop()
