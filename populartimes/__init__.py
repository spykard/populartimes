#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .crawler import run
from .crawler import get_populartimes
from .crawler import get_populartimes_from_search
from .crawler import get_populartimes_from_search_format_output

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

"""

ENTRY POINT

"""


def get(api_key, types, p1, p2, n_threads=20, radius=180, all_places=False):
    """
    :param api_key: str; api key from google places web service
    :param types: [str]; placetypes
    :param p1: (float, float); lat/lng of the south-west delimiting point
    :param p2: (float, float); lat/lng of the north-east delimiting point
    :param n_threads: int; number of threads to use
    :param radius: int; meters;
    :param all_places: bool; include/exclude places without populartimes
    :return: see readme
    """
    params = {
        "API_key": api_key,
        "radius": radius,
        "type": types,
        "n_threads": n_threads,
        "all_places": all_places,
        "bounds": {
            "lower": {
                "lat": min(p1[0], p2[0]),
                "lng": min(p1[1], p2[1])
            },
            "upper": {
                "lat": max(p1[0], p2[0]),
                "lng": max(p1[1], p2[1])
            }
        }
    }

    return run(params)


def get_id(api_key, place_id):
    """
    retrieves the current popularity for a given place
    :param api_key:
    :param place_id:
    :return: see readme
    """
    return get_populartimes(api_key, place_id)

def get_popular_times_by_crawl(name, address):
    """
    the raw crawler implementation which
    retrieves the current popularity for a given place
    from the Google Maps page
    the parameters are concatenated in order to perform the search
    :param name:
    :param address:
    :return: a tuple in the form of (place_address, latitude, longtitude, place_name, types, place_id, rating, rating_n, popular_times, current_popularity, time_spent) which is then formatted into a dict
    """
    return get_populartimes_from_search_format_output(* get_populartimes_from_search(name, address))
