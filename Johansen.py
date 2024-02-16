import numpy as np
import pandas as pd
import statsmodels.api as sm
import yfinance as yf
from statsmodels.tsa.vector_ar.vecm import coint_johansen


def johansen(assets):
    """
    determine cointegration of asset pairs
    assets - array of data frames containing time series data
    """
    # delete this later I just wanna see how the data is formatted
    stock_list = ["AAPL", "AMZN", "NFLX", "BUD"]
    start_date = "2010-01-01"
    end_date = "2022-10-26"
    data = yf.download(stock_list, start=start_date, end=end_date)["Adj Close"]
    data.to_excel("output.xlsx")
    # specified_number = 0  # testing for zero cointegrating relationships
    # coint_test_result = coint_johansen(data, specified_number, 1)

    # # extract the trace and eigen stats
    # trace_stats = coint_test_result.lr2
    # eigen_stats = coint_test_result.lr1

    # print(coint_test_result.eig)

    # # output the results
    # print(
    #     "Johansen Cointegration Test Results (Testing for Zero Cointegrating Relationships):"
    # )
    # print(f"Trace Statistics: {coint_test_result.lr1}")
    # print(f"Critical Values: {coint_test_result.cvt}")

    # # Define stock pairs
    # stock_pairs = [("AAPL", "AMZN"), ("NFLX", "AAPL"), ("AMZN", "NFLX")]

    # # Separate the output sections
    # print("\n" + "-" * 50 + "\n")

    # Interpret the results for each pair
    # for i, (stock1, stock2) in enumerate(stock_pairs):
    #     trace_statistic = trace_stats[i]
    #     eigen_statistic = eigen_stats[i]
    #     print(f"Pair {i + 1} ({stock1} and {stock2}):")
    #     print(f"Trace Statistic: {trace_statistic}")
    #     print(f"Eigen Statistic: {eigen_statistic}")
    #     print("\n" + "-" * 50 + "\n")

    # Determine cointegration based on critical values or other criteria
    # Add your cointegration assessment logic here
    print(
        "Cointegration Assessment: Testing for Zero Cointegrating Relationships (Null Hypothesis)\n"
    )


johansen("snip")
