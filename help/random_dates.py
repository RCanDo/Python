"""
generating random dates between start and end;
vectorised version;
"""
# %%
import numpy as np
import pandas as pd

from quantup_utils.config import pandas_options
pandas_options()

# %%
dd0 = pd.Series(['2025-01-01', '2025-01-11', '2025-01-07', '2025-02-01', '2025-02-21'])
dd1 = pd.Series(['2025-01-21', '2025-01-19', '2025-02-17', '2025-02-02', '2025-03-11'])


# %%
def sample_date(start_date: pd.Series, end_date: pd.Series | pd.Timestamp) -> pd.Series:
    """
    Randomly sample a date from the interval between start_date and end_date.

    Args:
        start_date: Start date in the given date_format.
        end_date: End date in the given date_format.

    Returns:
        str: Randomly sampled date as a string in the same date_format.
    """
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)
    intervals: pd.Series = (end_dt - start_dt)  # type: ignore # [operator]
    deltas = np.random.randint(0, intervals.dt.days)
    random_date: pd.Series = start_dt + pd.to_timedelta(deltas, unit="D")
    return random_date

# %%
df0 = pd.concat([dd0, sample_date(dd0, dd1), dd1], axis=1)
df0.dtypes

df1 = pd.concat([dd0, sample_date(dd0, '2025-03-03')], axis=1)
df1

# %%
start_dt = pd.to_datetime(dd0)
end_dt = pd.to_datetime(dd1)

delta: pd.Series = (end_dt - start_dt)  # type: ignore # [operator]
delta
random_days = np.array([np.random.uniform(0, upper) for upper in delta.dt.days])
random_days

random_deltas = pd.Series([pd.Timedelta(days=d) for d in random_days])
random_deltas

random_date: pd.Series = start_dt + random_deltas

# %%
help(np.random.randint)
ds = np.random.randint(0, delta.dt.days)
ds
help(pd.to_timedelta)
pd.to_timedelta(ds, unit="D")
start_dt + pd.to_timedelta(ds, unit="D")


# %%
# %% random date-time
# https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates

# mamba install radar
from faker import Faker
fake = Faker()

fake.date_between(start_date='today', end_date='+30y')
# datetime.date(2025, 3, 12)

fake.date_time_between(start_date='-30y', end_date='now')
# datetime.datetime(2007, 2, 28, 11, 28, 16)

# Or if you need a more specific date boundaries, provide the start
# and end dates explicitly.
import datetime
start_date = datetime.date(year=2015, month=1, day=1)
fake.date_between(start_date=start_date, end_date='+30y')

dir(fake)

import pandas as pd
fake.date_time_between_dates(pd.Timestamp('2021-09-30 12:00:00'), pd.Timestamp('2022-08-10 12:00:00'))
help(fake.date_time_between_dates)

# %%
# pip install radar
import radar

# Generate random datetime (parsing dates from str values)
radar.random_datetime(start='2000-05-24', stop='2013-05-24T23:59:59')

# Generate random datetime from datetime.datetime values
radar.random_datetime(
    start = datetime.datetime(year=2000, month=5, day=24),
    stop = datetime.datetime(year=2013, month=5, day=24)
)

# Just render some random datetime. If no range is given, start defaults to
# 1970-01-01 and stop defaults to datetime.datetime.now()
radar.random_datetime()
