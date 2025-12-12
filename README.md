# Get Requester Lab

## Overview
This lab introduces basic API consumption concepts using Python.
The focus is on sending HTTP GET requests, handling raw response data,
and converting JSON responses into Python data structures.

---

## Project Structure

get-requester-lab/
get-requester-lab/GetRequester.py
get-requester-lab/testing/
get-requester-lab/testing/test_get_requester.py
get-requester-lab/README.md


- GetRequester.py contains the GetRequester class and request logic
- testing/test_get_requester.py holds automated tests for each method
- README.md provides an overview of the project and its functionality

## Application Overview
The project defines a single utility class:

GetRequester
- Accepts a URL when instantiated
- Sends an HTTP GET request to the provided URL
- Returns the raw response body as bytes
- Converts JSON responses into native Python data structures

The class is designed to be minimal and focused on core request-handling
behavior to simplify testing and reinforce API fundamentals.

## Key Features
- HTTP GET requests using the requests library
- Raw response handling using bytes
- JSON parsing into Python dictionaries and lists
- Method reuse to avoid duplicated logic
- Automated testing with pytest

## Running the Tests

From the project root use the following:
- python -m pytest

## General project notes

Project passed through ChatGPT to identify syntax issues, validate API
behavior, and assist in drafting this README.md file. The README.md was
reviewed and edited for clarity, consistency, and alignment with lab
requirements prior to submission.
