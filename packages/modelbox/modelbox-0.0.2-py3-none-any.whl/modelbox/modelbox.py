from datetime import datetime
from re import I, S
from time import time
from typing import Dict, List
from typing_extensions import Self
from enum import Enum

import grpc
from grpc_status import rpc_status
from numpy import float32, uint, uint64
import service_pb2
import service_pb2_grpc

DEFAULT_NAMESPACE = "default"


class MLFramework(Enum):
    UNKNOWN = 1
    PYTORCH = 2
    TENSORFLOW = 3

    def to_proto(self) -> service_pb2.MLFramework:
        if self == self.PYTORCH:
            return service_pb2.PYTORCH
        if self == self.TENSORFLOW:
            return service_pb2.KERAS
        return service_pb2.UNKNOWN


class Checkpoint:
    def __init__(self, id: str, experiment_id: str, epoch: uint64) -> None:
        self._id = id
        self._experiment_id = experiment_id
        self._epoch = epoch

    @property
    def id(self) -> str:
        return self._id

    @property
    def experiment_id(self) -> str:
        return self._experiment_id

    @property
    def epoch(self) -> uint64:
        return self._epoch


class Experiment:
    def __init__(
        self, id, name, owner, namespace, external_id, created_at, updated_at
    ) -> Self:
        self._id = id
        self._name = name
        self._owner = owner
        self._namespace = namespace
        self._external_id = external_id
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def external_id(self) -> str:
        return self._external_id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at


class Model:
    def __init__(
        self,
        id: str,
        name: str,
        owner: str,
        namespace: str,
        task: str,
        description: str,
        meta: Dict,
    ) -> Self:
        self._id = id
        self._name = name
        self._owner = owner
        self._namespace = namespace
        self._task = task
        self._description = description
        self._meta = meta

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def owner(self):
        return self._owner

    @property
    def namespace(self):
        return self._namespace

    @property
    def task(self):
        return self._task

    @property
    def description(self):
        return self._description

    @property
    def meta(self):
        return self._meta


class ModelVersion:
    def __init__(
        self,
        id: str,
        model_id: str,
        name: str,
        version: str,
        description: str,
        blobs: List,
        meta: Dict,
        framework: MLFramework,
    ) -> Self:
        self._id = id
        self._model_id = model_id
        self._name = name
        self._version = version
        self._description = description
        self._blobs = blobs
        self._meta = meta
        self._framework = framework

    @property
    def id(self):
        return self._id

    @property
    def model_id(self):
        return self._model_id

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def description(self):
        return self._description

    @property
    def blobs(self):
        return self._blobs

    @property
    def meta(self):
        return self._meta

    @property
    def framework(self):
        return self._framework


class ModelBoxClient:
    def __init__(self, addr):
        self._addr = addr
        self._channel = grpc.insecure_channel(addr)
        self._client = service_pb2_grpc.ModelStoreStub(self._channel)

    def create_model(
        self,
        name: str,
        owner: str,
        namespace: str,
        task: str,
        description: str,
        meta: Dict,
    ) -> Model:
        req = service_pb2.CreateModelRequest(
            name=name,
            owner=owner,
            namespace=namespace,
            task=task,
            description=description,
            meta=meta,
        )
        response = self._client.CreateModel(req)
        return Model(response.id, name, owner, namespace, task, description, meta)

    def create_model_version(
        self,
        model_id: str,
        name: str,
        version: str,
        description: str,
        blobs: List[service_pb2.BlobMetadata],
        meta: Dict,
        framework: MLFramework,
    ) -> ModelVersion:
        req = service_pb2.CreateModelVersionRequest(
            model=model_id,
            name=name,
            version=version,
            description=description,
            blobs=blobs,
            meta=meta,
            framework=framework,
        )
        response = self._client.CreateModelVersion(req)
        return ModelVersion(
            id=response.model_version,
            model_id=model_id,
            name=name,
            version=version,
            description=description,
            blobs=blobs,
            meta=meta,
            framework=framework,
        )

    def create_experiment(
        self,
        name: str,
        owner: str,
        namespace: str,
        external_id: str,
        framework: MLFramework,
    ) -> Experiment:
        req = service_pb2.CreateExperimentRequest(
            name=name,
            owner=owner,
            namespace=namespace,
            external_id=external_id,
            framework=framework.to_proto(),
        )
        response = self._client.CreateExperiment(req)
        return Experiment(
            response.experiment.id,
            name,
            owner,
            namespace,
            external_id,
            response.experiment.created_at,
            response.experiment.updated_at,
        )

    def create_checkpoint_meta(
        self, experiment: str, epoch: uint, path: str, metrics: Dict,
    ) -> str:
        req = service_pb2.CreateCheckpointRequest(
            experiment_id=experiment,
            epoch=epoch,
            path=path,
            checksum="",
            metrics=metrics,
        )
        response = self._client.CreateCheckpoint(req)
        return response.checkpoint_id

    def close(self):
        if self._channel is not None:
            self._channel.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self.close()
