# python_for_Networking

A small collection of Python exercises for network engineers: built-in
functions, nested lists, JSON manipulation, and sample device inventory data.

These are practice scripts written while learning Python for network
automation. Each file is self-contained and small enough to read end to end.

## Layout

| Path | Purpose |
| --- | --- |
| `builtin_functions.py` | Explores built-in list functions with a list of device models (`dir`, `help`, `count`). |
| `nested_lists.py` | Recursively finds the position paths of given values inside a deeply nested list. |
| `working_with_json.py` | Loads a device description from JSON, reads individual fields, appends an interface, and writes the result back out. |
| `switch_device.json` | Sample switch description (name, version, vendor, interfaces) used by `working_with_json.py`. |
| `inventory.yml` | Sample YAML device inventory (device facts and SNMP settings). Illustrative data; not loaded by any script yet. |
| `restfulAPI.js` | Placeholder for a future REST API example. Contains no code yet. |

## Requirements

- Python 3.8 or newer
- No third-party packages

## Running the examples

Run each script from the repository root so relative file paths resolve:

```sh
python3 builtin_functions.py
python3 nested_lists.py
python3 working_with_json.py
```

`working_with_json.py` reads `switch_device.json` from the current directory
and writes the modified copy to `data_modified.json`, which is generated output
and therefore ignored by Git.

## Notes

- `inventory.yml` and `restfulAPI.js` are supporting material rather than
  runnable examples. Wiring the YAML sample into a script would be a natural
  next step.
- No license file is included in this repository.
