import json
from typing import Dict, List

import pandas as pd

from archimedes.data.common import get_api_base_url_v2
from archimedes.data.types import PredictionData
from archimedes.utils.api_request import make_api_request
from archimedes.utils.threaded_executor import execute_many


def get_predictions(  # pylint:disable=too-many-arguments
    series_ids: List[str] = None,
    price_areas: List[str] = None,
    start: str = None,
    end: str = None,
    ref_dt_start: str = None,
    ref_dt_end: str = None,
    *,
    access_token: str = None,
) -> pd.DataFrame:
    """Get any number of predictions

    This function can be used to fetch predictions from the Archimedes Database.

    Unlike `archimedes.get`, this will return a list, not a dataframe.

    Example:
        >>> import archimedes
        >>> archimedes.get_predictions(
        >>>    series_ids=["PX/rk-naive"],
        >>>    price_areas=["NO1"],
        >>>    start="2020"
        >>> )
        >>> [...]

    Args:
        series_ids (List[str], optional): The series ids to get.
        price_areas (List[str], optional): The price areas to get the data for.
        start (str, optional):
            The first datetime to fetch (inclusive). Returns all if None.
            Defaults to None.
        end (str, optional):
            The last datetime to fetch (exclusive). Returns all if None.
            Defaults to None.
        ref_dt_start (pd.Timestamp, optional):
            The earliest ref_dt to fetch (inclusive). Defaults to None.
        ref_dt_end (pd.Timestamp, optional):
            The latest ref_dt to fetch (exclusive). Defaults to None.
        access_token (str, optional): None - access token for the API

    Returns:
        DataFrame with all the prediction data
    """
    if isinstance(series_ids, str):
        series_ids = [series_ids]

    if isinstance(price_areas, str):
        price_areas = [price_areas]

    query = {}

    if start is not None:
        query["start"] = pd.to_datetime(start, utc=True)

    if end is not None:
        query["end"] = pd.to_datetime(end, utc=True)

    if ref_dt_start is not None:
        query["ref_dt_start"] = pd.to_datetime(ref_dt_start, utc=True)

    if ref_dt_end is not None:
        query["ref_dt_end"] = pd.to_datetime(ref_dt_end, utc=True)

    queries = [query]
    if series_ids is not None:
        queries = [
            {"series_ids": series_id, "price_areas": price_areas, **query}
            for query in queries
            for series_id in series_ids
        ]

    def _merge_function(result, aggr):
        if aggr is None:
            aggr = []
        for item in result:
            if "json_data" in item:
                json_data = item.get("json_data")
                item.update(json_data)
                del item["json_data"]
            aggr.append(item)
        return aggr

    params_array = [
        dict(
            url=f"{get_api_base_url_v2()}/data/get_predictions",
            access_token=access_token,
            params=query,
        )
        for query in queries
    ]

    data = execute_many(make_api_request, params_array, _merge_function)

    df = pd.DataFrame.from_dict(data)

    date_fields = ["from_dt", "run_dt", "ref_dt"]

    for date_field in date_fields:
        if date_field in df:
            df[date_field] = pd.to_datetime(df[date_field], utc=True)

    df = df.fillna("")

    return df


def get_predictions_ref_dts(prediction_id: str = None, *, access_token: str = None):
    """Get which ref_dts are available.

    ref_dt == prediction_build_dt
    Users views in the database.

    Args:
        prediction_id (str): The series id to get the reference dts for. If None, get
                             ref_dts for all prediction_ids.
        access_token (str, optional): Access token for the API

    Returns:
        DataFrame with all ref_dts
    """
    query = {}

    if prediction_id:
        query["prediction_id"] = prediction_id

    data = make_api_request(
        f"{get_api_base_url_v2()}/data/get_predictions_ref_dts",
        access_token=access_token,
        params=query,
    )

    return pd.DataFrame.from_dict(data)


def store_prediction(
    prediction_id: str,
    from_dt: pd.Timestamp,
    ref_dt: pd.Timestamp,
    run_dt: pd.Timestamp,
    data: Dict,
    *,
    access_token: str = None,
):
    """Store a prediction

    Example:
        >>> import archimedes
        >>> import pandas as pd
        >>> from dateutil.tz import gettz
        >>> tz_oslo = gettz("Europe/Oslo")
        >>> d = {
        >>>     "direction": "D",
        >>>     "probability": 0.8632089971077396,
        >>>     "hours_ahead": 1,
        >>>     "price_area": "NO1"
        >>> }
        >>> archimedes.store_prediction(
        >>>     prediction_id="test-prediction-id",
        >>>     from_dt=pd.Timestamp("2021-04-11 23:47:16.854775807", tz=tz_oslo),
        >>>     ref_dt=pd.Timestamp("2021-04-10 23:00:00.000000000", tz=tz_oslo),
        >>>     run_dt=pd.Timestamp.now(tz=tz_oslo),
        >>>     data=d
        >>> )
        True
    """
    payload = {
        "prediction_id": prediction_id,
        "from_dt": from_dt.isoformat(),
        "ref_dt": ref_dt.isoformat(),
        "run_dt": run_dt.isoformat(),
        "data": data,
    }

    ret = make_api_request(
        f"{get_api_base_url_v2()}/data/store_prediction",
        method="POST",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        access_token=access_token,
    )

    return ret.get("success", False)


def store_predictions(
    prediction_id: str,
    prediction_data: List[PredictionData],
    *,
    access_token: str = None,
):
    """Store a prediction

    Example:
        >>> import archimedes
        >>> import pandas as pd
        >>> from dateutil.tz import gettz
        >>> tz_oslo = gettz("Europe/Oslo")
        >>> pid = "test-prediction-id"
        >>> from_dt = pd.Timestamp("2021-04-11 23:47:16.854775807", tz=tz_oslo)
        >>> ref_dt = pd.Timestamp("2021-04-10 23:00:00.000000000", tz=tz_oslo)
        >>> run_dt = pd.Timestamp.now(tz=tz_oslo)
        >>> data = {
        >>>     "direction": "D",
        >>>     "probability": 0.8632089971077396,
        >>>     "hours_ahead": 1,
        >>>     "price_area": "NO1"
        >>> }
        >>> p_data = [
        >>>    {'from_dt': from_dt, 'ref_dt': ref_dt, 'run_dt': run_dt, 'data': data }
        >>> ]
        >>> archimedes.store_predictions(
        >>>     prediction_id=pid,
        >>>     prediction_data=p_data
        >>> )
        True
    """

    predictions = [
        {
            "from_dt": p["from_dt"].isoformat(),
            "ref_dt": p["ref_dt"].isoformat(),
            "run_dt": p["run_dt"].isoformat(),
            "data": p["data"],
        }
        for p in prediction_data
    ]

    payload = {
        "prediction_id": prediction_id,
        "data": predictions,
    }

    ret = make_api_request(
        f"{get_api_base_url_v2()}/data/store_predictions",
        method="POST",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        access_token=access_token,
    )

    return ret.get("success", False)
