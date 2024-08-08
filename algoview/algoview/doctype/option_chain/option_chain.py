import requests
import frappe
import json

@frappe.whitelist()
def fetch_and_post_nse_data(symbol):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'
    }

    index_url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    response = requests.get(index_url, headers=headers)
    
    # Debugging: Check response status and content
    if response.status_code != 200:
        frappe.throw(f"Failed to fetch data from NSE API: HTTP {response.status_code}")
    
    response_text = response.text
    
    # Debugging: Log the raw response text for inspection
    frappe.logger().info(f"NSE API response text: {response_text[:500]}")  # Log first 500 chars

    try:
        option_chain_data = response.json()
    except json.JSONDecodeError:
        frappe.throw("Failed to parse JSON response from NSE API")
    
    all_expiry_dates = option_chain_data['records']['expiryDates']
    filtered_data = []

    for expiry_date in all_expiry_dates:
        for item in option_chain_data['records']['data']:
            if item['expiryDate'] == expiry_date:
                underlying = item['CE']['underlying']
                strike_price = item['strikePrice']

                if 'PE' in item:
                    filtered_data.append({
                        'expiryDate': expiry_date,
                        'underlying': symbol,
                        'strikePrice': strike_price,
                        'lastPrice': item['PE']['lastPrice'],
                        'optionType': 'PUT'
                    })

                if 'CE' in item:
                    filtered_data.append({
                        'expiryDate': expiry_date,
                        'underlying': symbol,
                        'strikePrice': strike_price,
                        'lastPrice': item['CE']['lastPrice'],
                        'optionType': 'CALL'
                    })

    # Post the Transformed Data to ERPNext
    erpnext_url = "http://localhost:8000/api/resource/Option Chain"
    erpnext_headers = {
        'Authorization': 'token your_api_key:your_api_secret',  # Replace with your API token and secret
        'Content-Type': 'application/json'
    }

    for data in filtered_data:
        response = requests.post(erpnext_url, headers=erpnext_headers, json=data)
        if response.status_code == 200:
            frappe.msgprint("Data posted successfully")
        else:
            frappe.throw(f"Failed to post data: {response.json()}")
