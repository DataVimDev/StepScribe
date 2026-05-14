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
  },
  "End": false
}
}
    """


def basic_task_test() -> None:
    get_price = Task(
        Name="Get Current Price",
        Next="Check Price",
        Resource="arn:aws:states:::lambda:invoke",
        Arguments={
            "Payload": {"product": "{% $states.context.Execution.Input.product %}"},
            "FunctionName": "arn:aws:lambda:<region>:account-id:function:priceWatcher:$LATEST",
        },
        Assign={"currentPrice": "{% $states.result.Payload.current_price %}"},
        End=False
    )

    basic_json = json.loads(BASIC)

    task_json = json.loads(get_price.to_asl_json())

    assert basic_json == task_json
