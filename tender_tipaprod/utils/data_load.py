import pandas as pd
def data_load():
    DATA_TYPES = {
        'undoc': 'int',
        'idlot': 'int',
        'lot_status': 'str',
        'payment_info': 'str',
        'cpv_code': 'str',
        'type_payment': 'str',
        'organizer_okpo': 'str',
        'supplier_okpo': 'str',
        'lot_title': 'str',
        'tender_title': 'str',
        'tender_description': 'str',
        'lot_amount': 'float',
        'lot_quantity': 'float',
        'guarantee': 'float',
        'price_offer_before_auction': 'float',
        'price_offer_after_auction': 'float'
    }

    DATE_COLS = ['date_publish', 'date_start_accept', 'date_end_accept',
                'date_auction', 'date_supply_from', 'date_supply_to']

    df = pd.read_csv('D:/Диплом_СмартТендер/ML_data_2021_2024.csv', dtype=DATA_TYPES, parse_dates=DATE_COLS)
    return df