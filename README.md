<div align="center"> <img src="https://raw.githubusercontent.com/DataVimDev/StepScribe/main/logo.png" alt="Step Scribe logo" width="200"> </div>

A package to write AWS Step Function state machines using python and output valid AWS states language JSON or to various visualization formats (eventually).

## Installation
```pip install stepscribe```

## Examples
Here's a simple task example that invokes an existing lambda function:
```python
from stepscribe import Task

if __name__ == "__main__":
    get_price = Task(
                    Name="Get Current Price",
                    Next='Check Price',
                    Resource="arn:aws:states:::lambda:invoke",
                    Arguments={'Payload': {"product": "{% $states.context.Execution.Input.product %}"},
                        'FunctionName': "arn:aws:lambda:<region>:account-id:function:priceWatcher:$LATEST",
                    },
                    Assign={'currentPrice': "{% $states.result.Payload.current_price %}"}
    )
    print(get_price.to_asl_json(indent=2))               
```

This python code generates the following Amazon states language JSON:

```json
{
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
}
```

The value of StepScribe comes from leveraging python to create or compose objects and then generate the corresponding JSON. For example, what if we wanted to get the current price of a product, check if it's on sale, and check our inventory. If each of these actions is a lambda, we now need 3 tasks like above, but with different names and lambda functions, and each of these to be a branch of a parallel state.

```python
from stepscribe import Task, Parallel

def product_task(name: str, lambda_name: str) -> Task:
    output=name.lower().replace(' ', '_').replace('get_', '')

    return Task(
                Name=name,
                Next='Check Price',
                Resource="arn:aws:states:::lambda:invoke",
                Arguments={'Payload': {"product": "{% $states.context.Execution.Input.product %}"},
                        'FunctionName': f"arn:aws:lambda:<region>:account-id:function:{lambda_name}:$LATEST",
                },
                Assign={'currentPrice': f"{{% $states.result.Payload.{output} %}}"}
    )


if __name__ == "__main__":

    tasks = [("Get Current Price", "priceWatcher"), ("Check Sale", "isOnSale"), ("Get Current Inventory", "inventoryWatcher")]
    step_function = Parallel(
                        Name="Product Check",
                        Branches=[product_task(task[0], task[1]) for task in tasks)]
                        )
    print(step_function.to_asl_json())
```
This allows for considerable consolidation of the boilerplate and becomes more valuable if custom retry, catcher, item readers, or other components are reused across large state machines or for maintaining identical versions of state machines in multiple environments where resource arns can be provided via infrastructure as code without requiring multiple large messy JSON files to be kept in sync.

## Roadmap
Currently, StepScribe uses pydantic models for state machine, states and major components and assumes only JSONata is being used (not JSONPath state attributes or query language) and writes these objects to the corresponding states language JSON. StepScribe also provides a `load_from_asl_json` that can take a JSON string or a filename for the JSON file and returns a state machine pydantic model. 

The following features are planned:
- [ ] Test coverage and documentation
- [ ] JSONPath support
- [ ] Write state machine to mermaidJS diagram
- [ ] JSONata expression validation

Usage, desired features, bug reports, bug fixes, and feature implementations are welcome.

## Contributing
For feature requests or bug reports, please submit an issue in GitHub with as much information as possible.

For bug fixes or feature implementations, fork the repo and create a PR to merge your fork branch here and request a review from me. See the contributions guide for more information.

## License
MIT

