from datetime import datetime
from aws_cdk import (
    aws_iam as iam,
    custom_resources as cr,
)

from constructs import Construct


class SsmParameterReader(cr.AwsCustomResource):
    def __init__(self, scope: Construct, construct_id: str, parameter_name: str, region: str) -> None:
        ssm_aws_sdk_call = cr.AwsSdkCall(
            service="SSM",
            action="getParameter",
            parameters={
                "Name": parameter_name
            },
            region=region,
            physical_resource_id=cr.PhysicalResourceId.of(str(datetime.now()))
        )

        super().__init__(
            scope,
            construct_id,
            on_update=ssm_aws_sdk_call,
            policy=cr.AwsCustomResourcePolicy.from_statements([
                iam.PolicyStatement(
                    resources=["*"],
                    actions=["ssm:GetParameter"],
                    effect=iam.Effect.ALLOW
                )
            ])
        )

    def get_parameter_value(self):
        return self.get_response_field('Parameter.Value')