There is an Apache-style access log at /app/access.log in the working directory. Read it and produce a small JSON summary report.

Write your report as a single JSON object to the absolute path /app/report.json, containing exactly these three keys:

1. total_requests — an integer: the total number of requests in the log (one per non-empty line).
2. unique_ips — an integer: the number of distinct client IP addresses (the first whitespace-separated field on each line).
3. top_path — a string: the request path (the target in the request line, e.g. the "/..." in "GET /... HTTP/1.1") that appears most often across all requests.

The file must contain only those three keys. You are graded solely on the values of total_requests, unique_ips, and top_path in /app/report.json.
