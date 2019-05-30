# GEM Analytics

Suite of helper tools for viewing logs.

- [GEM Analytics](#gem-analytics)
  - [Getting Started](#getting-started)
  - [Scripts](#scripts)
    - [Reduce Logs](#reduce-logs)
    - [Count Logs](#count-logs)

## Getting Started

To use these you need to copy the google logs via gsutil.
Follow the guide at https://cloud.google.com/storage/docs/gsutil to set up gsutil. 

Make sure your account uses the GEM credentials, and run the following to copy the logs to this directory: 

`gsutil cp gs://gem-log-export ./`

*note: this might take a while -- the logs are about 3GB*

## Scripts
List of currently available analytic scripts

### Reduce Logs
A sanity helper to be able to reduce over the log files in chronological order with useful date meta data.

See [Count Logs](#count-logs) for a simple example of how to use Reduce Logs.

### Count Logs
Simple script to count and print the number of logs in each log file, and then print the total number of logs.