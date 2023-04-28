# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/1_tec.ipynb.

# %% auto 0
__all__ = ['TECDashboard']

# %% ../nbs/1_tec.ipynb 3
import pandas as pd
from .dune import DuneWrapper

# %% ../nbs/1_tec.ipynb 4
class TECDashboard(DuneWrapper):
    "Interface to the TEC Dune Analytics dashboard."
    
    def __init__(self):
        self.market_information = self.MarketInformation()
        self.treasury_inflows_outflows = self.TreasuriesInflowsOutflows()
        self.reserves = self.Reserves()
        self.trades = self.Trades()
        self.abc_tributes = self.ABCTributes()
        self.conviction = self.Conviction()
    
    class MarketInformation(DuneWrapper):
    
        def mint_price(self, **params)->pd.DataFrame:
            """NOT WORKING"""
            df = self.refresh_into_dataframe(461108, **params)
            return df
        
        def honeyswap_tec_sales(self, **params)->pd.DataFrame:
            """Historic honeyswap tec sales."""
            df = self.refresh_into_dataframe(1898914, **params)
            return df
        
        def market_price(self, **params)->float:
            """Most recent honeyswap tec sale as market price."""
            return self.honeyswap_tec_sales().iloc[0]['price']
        
        def burn_price(self, **params)->pd.DataFrame:
            """NOT WORKING"""
            df = self.refresh_into_dataframe(421552, **params)
            return df
        
        def price_chart(self, **params)->pd.DataFrame:
            """Historic Mint, Burn, and Market Prices"""
            df = self.refresh_into_dataframe(1898885, **params)
            return df
        
        def holders_and_supply(self, **params)->pd.Series:
            """Number of TEC Holders and total supply."""
            df = self.refresh_into_dataframe(1898886, **params).iloc[0]
            return df
        
        def total_holders(self, **params)->float:
            """Number of TEC Holders."""
            return self.holders_and_supply()['total_holders']
        
        def supply(self, **params)->float:
            """TEC Supply."""
            return self.holders_and_supply()['supply']
        
        def holders_over_time(self, **params)->pd.DataFrame:
            """TEC holders over time."""
            df = self.refresh_into_dataframe(1898887, **params)
            return df
        
        def holders_distribution(self, **params)->pd.DataFrame:
            """Distribution of holders and balances."""
            df = self.refresh_into_dataframe(1898888, **params)
            return df
        

    class TreasuriesInflowsOutflows(DuneWrapper):
        
        def multisig_values_over_time(self, **params):
            """NOT WORKING"""
            df = self.refresh_into_dataframe(945136, **params)
            return df

        def multisig_treasuries(self, **params):
            """NOT WORKING"""
            df = self.refresh_into_dataframe(394403, **params)
            return df

        def multisig_distribution(self, **params):
            """NOT WORKING"""
            df = self.refresh_into_dataframe(427713, **params)
            return df

        def multisig_treasuries_movement(self, **params):
            """NOT WORKING"""
            df = self.refresh_into_dataframe(394987, **params)
            return df
        
    class Reserves(DuneWrapper):

        def reserve_pool(self, **params)->pd.Series:
            """Reserve pool information."""
            df = self.refresh_into_dataframe(1752257, **params).iloc[0]
            return df
        
        def total_pool_value(self, **params)->float:
            return self.reserve_pool()['total_pool_value']
        
        def reserve_pool_value(self, **params)->float:
            return self.reserve_pool()['reserve_pool_value']
        
        def common_pool_value(self, **params)->float:
            return self.reserve_pool()['common_pool_value']
        
        def commons_pool_balance_over_time(self, **params)->pd.DataFrame:
            """Common pool balance over time."""
            df = self.refresh_into_dataframe(1754471, **params)
            return df
        
        def reserve_balance_over_time(self, **params)->pd.DataFrame:
            """Reserve balance over time."""
            df = self.refresh_into_dataframe(1754573, **params)
            return df
        
    class Trades(DuneWrapper):
        
        def abc_top_ten_trades(self, **params):
            df = self.refresh_into_dataframe(1855820, **params)
            return df
        
        def honeyswap_top_ten_trades(self, **params):
            df = self.refresh_into_dataframe(1865657, **params)
            return df
        
        def abc_token_sales(self, **params):
            df = self.refresh_into_dataframe(1865890, **params)
            return df
        
        def honeyswap_tec_sales(self, **params):
            df = self.refresh_into_dataframe(1866227, **params)
            return df
        
    class ABCTributes(DuneWrapper):
        
        def tribute_distribution(self, **params):
            df = self.refresh_into_dataframe(1646841, **params)
            return df
        
    class Conviction(DuneWrapper):
        
        def tec_proposals(self, **params):
            df = self.refresh_into_dataframe(1849767, **params)
            return df
