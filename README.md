# dynamo/log-report — fixed Terminal-Bench 2 (Harbor) task

Parse an Apache-style access log into a small JSON summary report.

This is the corrected version of a deliberately-broken TB2 Harbor task. It is
reproducible, contains no leaked solution, and is graded on real output values.

## Layout

```
task.toml                 # TB2 Harbor task config (artifacts = ["/app/report.json"])
instruction.md            # agent prompt: exact output path, schema, numbered criteria
environment/
  Dockerfile              # approved base pinned by @sha256 digest; no solution leaked
  access.log              # input log (shipped into the agent image)
solution/
  solve.sh, solve.py      # oracle reference solution
tests/
  test.sh                 # runs pytest, writes reward.txt + ctrf.json to /logs/verifier/
  test_outputs.py         # asserts total_requests, unique_ips, top_path (1:1 with criteria)
```

## Verify

```
harbor run -p . -a oracle      # reference solution  -> reward 1
harbor run -p . --agent nop    # no-op agent         -> reward 0
```

Expected report: `{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}`
