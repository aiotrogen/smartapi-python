# package import statement
from smartapi.smartConnect import SmartConnect #from smartapi import SmartConnect

# obj=SmartConnect()
obj=SmartConnect(api_key="9MsNuOkg")

#login api call

data = obj.generateSession('aiotrogen@gmail.com','Abcd#1234')
refreshToken= data['data']['refreshToken']

#fetch User Profile
userProfile= obj.getProfile(refreshToken)

#place order
try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "SBIN-EQ",
        "symboltoken": "3045",
        "transactiontype": "BUY",
        "exchange": "NSE",
        "ordertype": "LIMIT",
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": "19500",
        "squareoff": "0",
        "stoploss": "0",
        "quantity": "1"
        }
    orderId=obj.placeOrder(orderparams)
    print("The order id is: {}".format(orderId))
except Exception as e:
    print("Order placement failed: {}".format(e.message))

#logout
try:
    logout=obj.terminateSession('Your Client Id')
    print("Logout Successfull")
except Exception as e:
    print("Logout failed: {}".format(e.message))