import numpy as np

def price(df):
    price = np.round(
        np.random.normal(
            loc=np.mean(df.iloc[1,1:]),
            scale=np.std(df.iloc[1,1:]),
            size=1),
        0)
    price = int(np.mean(price))
    return price

def fixed_costs(df):
    fc = int(np.round(np.random.uniform(low=df.iloc[6,1], high=df.iloc[6,5]),0))
    return fc

def quantity(df):
    q = np.round(
        np.random.normal(
            loc=np.mean(df.iloc[0,1:]),
            scale=np.std(df.iloc[0,1:]),
            size=1),
        0)
    q = int(np.mean(q))
    return q

def mgmt_costs(df):
    mc = int(np.round(np.random.uniform(low=df.iloc[7,1], high=df.iloc[7,5]),0))
    return mc


def revenue(df):
    revenue = quantity(df) * price(df)
    return revenue



def sales_costs(df, sales_commission: float):
    sc = int(revenue(df) * sales_commission)
    return sc

def income(df):
    inc = revenue(df) - sales_costs(df, 0.07)
    return inc

def interest(df):
    interest = int(np.round(np.random.uniform(low=df.iloc[8,1], high=df.iloc[8,5]),0))
    return interest

def Earns_Bef_Tax(df):
    ebt = income(df) - ( interest(df) + am_depr_inst(df)[0] + am_depr_inst(df)[2] + mgmt_costs(df))
    return ebt

def taxes(df):
    if (int(Earns_Bef_Tax(df) * 0.27)) < 0:
        return 0
    else:
        return (int(Earns_Bef_Tax(df) * 0.27))

def Earns_Af_Tax(df):
    eat = Earns_Bef_Tax(df) - taxes(df)
    return eat

def am_depr_inst(df):
    amortization = df.iloc[9,1]
    depreciation = df.iloc[10,1]
    installment = df.iloc[15,1]
    return [amortization, depreciation, installment]

def net_income(df):
    ni = (Earns_Af_Tax(df) + interest(df) + am_depr_inst(df)[1]) - am_depr_inst(df)[2]
    return ni

