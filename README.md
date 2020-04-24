# KNV Paypal™ Matcher

This project helps organizing accounting data exported from KNV's ['Shopkonfigurator'](https://shopkonfigurator.buchkatalog-reloaded.de), matching it with PayPal™ payments, so booksellers (well, KNV customers) don't have to.

## Exporting data
First of all, export payment reports from PayPal backend and invoices, orders & order info from the online shop backend (preferably in `csv` format). After that, the data needs to be loaded:

```python
import pandas as pd

df = pd.read_csv(csv_file)
data = df.to_dict('records')
```

Next, pass the data loaded from `Download.CSV` [PayPal™](https://www.paypal.com/de/home) as well as `Orders_*.csv` and `OrderInfo_*.csv` [KNV](https://shopkonfigurator.buchkatalog-reloaded.de) to the `match_data` function .. that's it!

:copyright: Fundevogel Kinder- und Jugendbuchhandlung
