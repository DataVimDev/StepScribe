import json

from stepscribe import Pass, StateMachine

BASIC = """{
  "Comment": "A Hello World example of the Amazon States Language using a Pass state",
  "StartAt": "HelloWorld",
  "States": {
    "HelloWorld": {
      "Type": "Pass",
      "Output": "Hello World!",
      "QueryLanguage": "JSONata",
      "End": true
    }
  },
  "QueryLanguage": "JSONata"
}
    """


def basic_state_machine_test() -> None:
    hello_world = Pass(
        Name="HelloWorld",
        Output="Hello World!",
        End=True,
    )
    hello = StateMachine(
        Comment="A Hello World example of the Amazon States Language using a Pass state",
        StartAt="HelloWorld",
        States=[hello_world],
    )

    basic_json = json.loads(BASIC)

    state_machine_json = json.loads(hello.to_asl_json())

    assert basic_json == state_machine_json
