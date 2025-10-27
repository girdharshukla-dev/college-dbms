## Agricultural Produce Market :

- Farmers(farmer_id PK, farmer_name, village, phone) 
- Crops(crop_id PK, crop_name, season) 
- Markets(market_id PK, market_name, location) 
- Transactions(transaction_id PK, farmer_id FK, crop_id FK, market_id FK, quantity, price)
