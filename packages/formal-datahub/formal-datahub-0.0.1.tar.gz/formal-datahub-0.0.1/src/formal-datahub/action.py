import json
import os
from datahub_actions.action.action import Action
from datahub_actions.event.event import EventEnvelope
from datahub_actions.pipeline.pipeline_context import PipelineContext

import requests

from pydantic.fields import Field


from datahub.configuration.common import ConfigModel


class FormalSourceConfig(ConfigModel):
    client_id: str = Field(description="Client ID.")
    secret_key: str = Field(description="Secret Key.")
    mappings: object = Field(
        description="A dict mapping from Dataset URNs to Sidecar IDs.")


class FormalAction(Action):
    config: FormalSourceConfig

    @classmethod
    def create(cls, config_dict: dict, ctx: PipelineContext) -> "Action":
        config = FormalSourceConfig.parse_obj(config_dict)
        return cls(config, ctx)

    def __init__(self, config, ctx: PipelineContext):
        self.ctx = ctx
        self.config = config

    def act(self, event: EventEnvelope) -> None:
        base_url = "https://api.formalcloud.net"
        if os.getenv('PLUGIN_ENV') == "development":
            base_url = "http://localhost:4000"

        headers = {'client_id': self.config.client_id,
                   'api_key': self.config.secret_key, 'Content-Type': 'application/json', "charset": "utf-8"}

        dataset_urn = event.event.entityUrn.split(
            "urn:li:schemaField:(")[1].split("),")[0] + ")"

        if dataset_urn in self.config.mappings:
            datastore_id = self.config.mappings[dataset_urn]

            if datastore_id:
                try:
                    path = event.event.entityUrn.split(
                        ",")[1] + "." + event.event.entityUrn.split(",")[-1][:-1]
                    payload = {"datastoreId": datastore_id, "path": path,
                               "tag": event.event.modifier, "operation": event.event.operation}
                    requests.post(base_url + "/admin/inventory/datahub",
                                  data=json.dumps(payload), headers=headers)

                except BaseException as error:
                    print(error)
            else:
                print(
                    f"WARN: Datahub Dataset {dataset_urn} is not mapped to a Formal Datastore ID.")

    def close(self) -> None:
        pass
