import requests ##enables making HTTPS requests while using the python librarires to APIs and websites
import time ##tell the programme to pause or get a break for a set time
api_key = "23d008030cd2f7c444b987ee" ##from the ExchangeRate site that enables us to access updated exchange rates
base = "UGX"
target = "USD" 
def rates(base, target, api_key):
    
    link = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}"##takes us to Exchange-API where we are fetching are rates from
    try: 
        response = requests.get(link)
        list = response.json()
        if response.status_code==200:
            return list["conversion_rate"]
        else:
            print("Error:", list.get("error_type", "Unkown error"))
            return None
    except Exception as e:
        print("Network or parsing error:", e)
        return None
Rate =None
while True: 
    print("Fetching Updated Rates... Please wait.")
    Rate = rates(base, target, api_key)
    if Rate: ##checks if the Rate is popluated and not empty
        print(f"{base} = {Rate} {target}") ##prints the exchange rate
        amount= input(f"Enter the amount in {base} to change to {target} or (exit to leave.): ")
        if amount.lower() == "exit": ##changes the input to lower case if theuser enters it as uppercase
            print("Thank you for using The Currency Converter")
            break
        try:
            amount = float(amount) ##casting our amount to float
            conversion = amount * Rate
            print(f"You have changed {amount}{base} to {conversion}{target}")
        except ValueError:
            print("🙄🙄")
        else:
            print("Give us a minute. 🤞" )
    else:
        print("Left with 30seconds for next update of rates")
time.sleep(30)## tells the code to rest for 30 seconds before updating for the new rates
exit()




