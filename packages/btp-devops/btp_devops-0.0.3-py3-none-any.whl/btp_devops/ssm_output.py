from aws_cdk import (
    aws_ssm as ssm
)

from constructs import Construct


class SsmOutput(Construct):
    def __init__(self, scope: Construct, construct_id: str,
                 parameter_name: str, value: str, description: str = None) -> None:
        super().__init__(scope, construct_id)

        ssm.StringParameter(
            self,
            f"Parameter-{construct_id}",
            parameter_name=parameter_name,
            string_value=value,
            description=description,
            tier=ssm.ParameterTier.STANDARD,
        )
