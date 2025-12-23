![logo.png]
# StepScribe

A package to write AWS Step Function state machines using python and output valid AWS states language JSON or to various visualization formats.

## Installation
```pip install stescribe```

## Examples
Here's a simple task example that invokes an existing lambda function:
```python

```
This python code generates the following Amazon states language JSON for the AWS step functin state machine:

```json
"Get Current Price": {
  "Type": "Task",
  "QueryLanguage" : "JSONata",
  "Resource": "arn:aws:states:::lambda:invoke",
  "Next": "Check Price",
  "Arguments": {
    "Payload": {
    "product": "{% $states.context.Execution.Input.product %}"
    },
    "FunctionName": "arn:aws:lambda:<region>:account-id:function:priceWatcher:$LATEST"
  },
  "Assign": {
    "currentPrice": "{% $states.result.Payload.current_price %}"
  }
}
```
## Roadmap
Currently, StepScribe has python dataclasses for states and major components and assumes only JSONata is being used (not JSONPath state attributes or query language) and writes these objects to the corresponding states language JSON.

The following features are planned:
- [ ] JSONPath support
- [ ] Write state machine to mermaidJS diagram
- [ ] Read state machine
- [ ] JSONata expression validation

Usage, desired features, bug reports, bug fixes, and feature implementations are welcome.

## Contributing
For feature requests or bug reports, please submit an issue in GitHub with as much information as possible.

For bug fixes or feature implementations, fork the repo and create a PR to merge your fork branch here and request a review from me. See the contributions guide for more information.

## License
MIT

## Origin
My first use of AWS Step Functions seemed simple: a small set of parallel branches, most being short sequences of distributed map states that invoked a lambda on particular items of a large JSON data set in S3 or did partical aggregation of results from previous states. The JSON defining the state machine quickly grew to over 1000 lines when formatted, with massive amount of duplication (each branch was basically the same but invoked a different set of lambdas - so the same item reader, processor, writer and internal states inside each distributed map, just different state names and lambda arns). Furthermore, I needed to have a dev and prod version of this that would stay in sync. I also needed visual versions that could be used in documentation and presentations. 

It seemed like a better approach would be to use python to generate versions of the state machine json, allowing loops and f-strings to easily construct machine with redundant structures and to generate dev, prod, or visuals from the same base state machine definition.
