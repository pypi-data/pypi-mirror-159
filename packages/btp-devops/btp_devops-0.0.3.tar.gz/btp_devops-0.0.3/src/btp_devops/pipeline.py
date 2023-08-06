from abc import abstractmethod, ABC
from aws_cdk import (
    Stack,
    pipelines,
    Environment,
    aws_iam as iam,
    aws_codebuild as codebuild
)
from constructs import Construct


class BasicPipelineStack(ABC, Stack):
    @staticmethod
    def get_python_build_commands():
        return [
            "cd ${CODEBUILD_SRC_DIR}/${SRC_RELATIVE_APP_DIR}",
            "pip install -r requirements.txt -t .",
        ]

    @staticmethod
    def get_synth_commands_for(config):
        return [
            "cd ${CODEBUILD_SRC_DIR}/${SRC_RELATIVE_CDK_DIR}",
            "pip install -r requirements.txt",
            "npm install -g aws-cdk",
            f"cdk synth -c config={config}"
        ]

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        raw_config = self.get_config()

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            pipeline_name=raw_config.get("PipelineName"),
            self_mutation=True,
            cross_account_keys=True,
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection(
                    raw_config.get("Repo"),
                    raw_config.get("Branch"),
                    connection_arn=raw_config.get("ConnectionARN"),
                    trigger_on_push=raw_config.get("TriggerOnPush")
                ),
                env={
                    "SRC_RELATIVE_CDK_DIR": self.get_path_to_cdk(),
                    "SRC_RELATIVE_APP_DIR": self.get_path_to_app()
                },
                install_commands=self.get_install_commands(),
                commands=self.get_synth_commands(),
                primary_output_directory=f"{self.get_path_to_cdk()}/cdk.out"
            ),
            code_build_defaults=pipelines.CodeBuildOptions(
                build_environment=codebuild.BuildEnvironment(
                    compute_type=codebuild.ComputeType.SMALL
                ),
                role_policy=[
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        actions=["sts:AssumeRole"],
                        resources=["*"],
                        conditions={
                            "StringEquals": {
                                "iam:ResourceTag/aws-cdk:bootstrap-role": "lookup",
                            },
                        }
                    )
                ]
            )
        )

        app_account = raw_config.get("AccountID")
        app_region = raw_config.get("Region")

        stage_cls = self.get_stage_cls()
        stage = stage_cls(
            self,
            "Deploy",
            app_config=raw_config,
            env=Environment(account=app_account, region=app_region)
        )

        change_set_steps = []
        requires_approve = raw_config.get("ApproveDeploy")
        if requires_approve:
            change_set_steps.append(
                pipelines.ManualApprovalStep(
                    id="Approve",
                    comment=f"Switch to {app_account} AWS Account and review the Change Set before approving.")
            )

        pipeline.add_stage(
            stage,
            stack_steps=[pipelines.StackSteps(stack=stage.stage_stack, change_set=change_set_steps)]
        )

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod
    def get_stage_cls(self):
        pass

    @abstractmethod
    def get_path_to_cdk(self):
        pass

    @abstractmethod
    def get_path_to_app(self):
        pass

    def get_install_commands(self):
        return []

    @abstractmethod
    def get_synth_commands(self):
        pass
