import json

from stepscribe import Task

BASIC = """{
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
    """


def basic_task_test() -> None:
    get_price = Task(
        name="Get Current Price",
        next_="Check Price",
        resource="arn:aws:states:::lambda:invoke",
        arguments={
            "Payload": {"product": "{% $states.context.Execution.Input.product %}"},
            "FunctionName": "arn:aws:lambda:<region>:account-id:function:priceWatcher:$LATEST",
        },
        assign={"currentPrice": "{% $states.result.Payload.current_price %}"},
    )

    basic_json = json.loads(BASIC)

    task_json = json.loads(get_price.to_json())

    assert basic_json == task_json
