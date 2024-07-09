#!/usr/bin/python3
""" Finding peak """

def find_peak(list_of_integers):
    list_l = len(list_of_integers)
    if list_l == 0:
        return None
    peak = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak]


def binary_search(a, lo, hi):
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)#!/usr/bin/python3


def find_peak(list_of_integers):
    list_l = len(list_of_integers)
    if list_l == 0:
        return None
    peak = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak]


def binary_search(a, lo, hi):
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)#!/usr/bin/python3


def find_peak(list_of_integers):
    list_l = len(list_of_integers)
    if list_l == 0:
        return None
    peak = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak]


def binary_search(a, lo, hi):
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)#!/usr/bin/python3


def find_peak(list_of_integers):
    list_l = len(list_of_integers)
    if list_l == 0:
        return None
    peak = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak]


def binary_search(a, lo, hi):
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)
