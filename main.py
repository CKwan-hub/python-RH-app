import robin_stocks as rs
import json
import os


#  Handle login
#  Check if settings file exist
try:
    #  attempt to read from settings file
    with open("settings1.json", "r") as f:
        settings = json.load(f)
#  Set settings to variables for user & password
# rs_user = os.environ.get("rs_user")
# rs_pass = os.environ.get("rs_pass")

except FileNotFoundError:
    print("Settings file not found, please enter login information...")

    # User credentials dont exist in settings file, prompt for user input
    while True:
        try:
            print("Please enter username")
            username = input("Username:  ")
            if(username != ""):
                break
            print("Username cannot be blank")
            pass
        except Exception as e:
            print(e)

    while True:
        try:
            print("Please enter password")
            password = input("Password:  ")
            if(password != ""):
                break
            print("Password cannot be blank")
            pass
        except Exception as e:
            print(e)

    # Login to robinhood
    rs.authentication.login(username=username, password=password,
                            expiresIn=86400, scope='internal', by_sms=False, store_session=False)

    # Optional, list profile information:
    portfolioCash = rs.profiles.load_account_profile('portfolio_cash')
    cash = rs.profiles.load_account_profile('cash')
    cryptoBuyingPower = rs.profiles.load_account_profile('crypto_buying_power')
    cashBalance = rs.profiles.load_account_profile('cash_balances')
    buyingPower = rs.profiles.load_account_profile('buying_power')
    account = rs.profiles.load_portfolio_profile('account')
    equity = rs.profiles.load_portfolio_profile('equity')
    amount = rs.profiles.load_portfolio_profile('withdrawable_amount')

    name = rs.profiles.load_user_profile('first_name')
    user = rs.profiles.load_user_profile('username')
    userID = rs.profiles.load_account_profile('user_id')

    profile = rs.account.build_user_profile()

    # rs.account.download_all_documents('account_statement')
    # rs.account.download_all_documents()

    # NOTE: Get crypto info for all tradeable
    # cryptoInfoList = rs.crypto.get_crypto_currency_pairs(Filter)

    # NOTE: Get crypto info for specified
    # rs.crypto.get_crypto_info(symbol)

    # NOTE: Get crypto quote (low, high, open)
    # rs.crypto.get_crypto_quote(symbol)

    # NOTE: Will cancel all open orders
    # cancelledOrders =  rs.orders.cancel_all_crypto_orders()
    # cancelOrder = rs.orders.cancel_crypto_order(ID)
    # allCryptoOrders = rs.orders.get_all_crypto_orders()
    # allOpenCryptoOrders = rs.orders.get_all_open_crypto_orders()
    # cryptoOrder = rs.orders.get_crypto_order_info(ID)

    # NOTE: "submit a market order for crypto by specified amt of $ you want to trade"
    # rs.orders.order_buy_crypto_by_quantity(symbol, quantity, priceType='ask_price', timeInForce='gtc')

    # NOTE: "submit a market order for crypto by specifying amount of shares to buy"
    # Use this for main, since $ specified?
    # rs.orders.order_buy_crypto_limit(
    #     symbol, quantity, price, timeInForce='gtc')

    # NOTE: Sell crypto by price
    # rs.orders.order_sell_crypto_by_price(
    #     symbol, amountInDollars, priceType='bid_price', timeInForce='gtc')
    # example:
    #   rs.orders.order_buy_crypto_by_price('BTC', 500, timeInForce='gtc')

    # NOTE: Sell crypto by quanitity
    # rs.orders.order_sell_crypto_by_quantity(
    #     symbol, quantity, priceType='bid_price', timeInForce='gtc')

    # Scan for target currencies from settings - CL input "Main.py -val"
    # If no settings, (set to flag above?), ask for what currency
    # display values

    # Begin monitoring "main.py -auto"
    # If target currency is rising x times in x amount of time, buy.
    # If target continues to rise x times, sell
    # Log transactions and profit
    # Back to monitor state

    # FIXME: Revise the logic for what we want to actually do
    # Loop 1 second interval
    # Check price
    # 3 increases in a row = buy
    # 2 downticks in a row = sell
    # update all totals and history for comparison

    # Direct "buy"/"sell" functionality "main.py -buy/main.py -sell"
    # See basic functionality in robin_stocks

    # Notifications via SMTP for hourly progress updates to email
    # Backlog to file
