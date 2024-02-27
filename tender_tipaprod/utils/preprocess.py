import pandas as pd
import re
def process_dataframe(df):
    df.type_payment = df.type_payment.fillna('-')
    df['days_to_get_paid'] = df['payment_info'].str.extract('(\d+)')
    # Create columns for prepayment, postpayment, prepayment_percentage, postpayment_percentage, and amount_of_splits
    df['prepayment'] = 0.0
    df['postpayment'] = 0.0
    df['prepayment_percentage'] = 0.0
    df['postpayment_percentage'] = 0.0
    df['amount_of_splits'] = 0

    # Iterate through the DataFrame
    for index, row in df.iterrows():
        input_string = row['type_payment']  # Replace 'your_column_name' with the actual column name containing the strings
        # Use regex to find all pay types and percentages
        matches = re.findall(r'(\b\w+\b)\s+(\d+\.\d+%)', input_string)

        # Create dictionaries to store the sum of percentages and count of splits for each pay type
        pay_types_sums = {'prepayment': 0.0, 'postpayment': 0.0}
        pay_types_counts = {'prepayment': 0, 'postpayment': 0}
        prepayment = False
        postpayment = False
        # Accumulate percentages and count of splits for each pay type
        for pay_type, percentage in matches:
            if 'аванс' in pay_type.lower():
                prepayment = True
                pay_types_sums['prepayment'] += float(percentage[:-1])
                pay_types_counts['prepayment'] += 1
            elif 'пiсляоплата' in pay_type.lower():
                postpayment = True
                pay_types_sums['postpayment'] += float(percentage[:-1])
                pay_types_counts['postpayment'] += 1

        # Update the DataFrame with the calculated values
        df.at[index, 'prepayment'] = int(prepayment)
        df.at[index, 'postpayment'] = int(postpayment)
        df.at[index, 'prepayment_percentage'] = pay_types_sums['prepayment']  if prepayment else 0.0
        df.at[index, 'postpayment_percentage'] = pay_types_sums['postpayment']  if postpayment else 0.0
        df.at[index, 'amount_of_splits'] = pay_types_counts['prepayment'] + pay_types_counts['postpayment']

    return df