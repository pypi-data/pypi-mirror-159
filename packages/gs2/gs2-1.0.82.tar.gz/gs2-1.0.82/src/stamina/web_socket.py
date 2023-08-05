# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import time
from core.web_socket import *
from core.model import Gs2Constant
from stamina.request import *
from stamina.result import *


class Gs2StaminaWebSocketClient(AbstractGs2WebSocketClient):

    def _describe_namespaces(
        self,
        request: DescribeNamespacesRequest,
        callback: Callable[[AsyncResult[DescribeNamespacesResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='namespace',
            function='describeNamespaces',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeNamespacesResult,
                callback=callback,
                body=body,
            )
        )

    def describe_namespaces(
        self,
        request: DescribeNamespacesRequest,
    ) -> DescribeNamespacesResult:
        async_result = []
        with timeout(30):
            self._describe_namespaces(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_namespaces_async(
        self,
        request: DescribeNamespacesRequest,
    ) -> DescribeNamespacesResult:
        async_result = []
        self._describe_namespaces(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_namespace(
        self,
        request: CreateNamespaceRequest,
        callback: Callable[[AsyncResult[CreateNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='namespace',
            function='createNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.overflow_trigger_script is not None:
            body["overflowTriggerScript"] = request.overflow_trigger_script.to_dict()
        if request.log_setting is not None:
            body["logSetting"] = request.log_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=CreateNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def create_namespace(
        self,
        request: CreateNamespaceRequest,
    ) -> CreateNamespaceResult:
        async_result = []
        with timeout(30):
            self._create_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_namespace_async(
        self,
        request: CreateNamespaceRequest,
    ) -> CreateNamespaceResult:
        async_result = []
        self._create_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_namespace_status(
        self,
        request: GetNamespaceStatusRequest,
        callback: Callable[[AsyncResult[GetNamespaceStatusResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='namespace',
            function='getNamespaceStatus',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetNamespaceStatusResult,
                callback=callback,
                body=body,
            )
        )

    def get_namespace_status(
        self,
        request: GetNamespaceStatusRequest,
    ) -> GetNamespaceStatusResult:
        async_result = []
        with timeout(30):
            self._get_namespace_status(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_namespace_status_async(
        self,
        request: GetNamespaceStatusRequest,
    ) -> GetNamespaceStatusResult:
        async_result = []
        self._get_namespace_status(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_namespace(
        self,
        request: GetNamespaceRequest,
        callback: Callable[[AsyncResult[GetNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='namespace',
            function='getNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def get_namespace(
        self,
        request: GetNamespaceRequest,
    ) -> GetNamespaceResult:
        async_result = []
        with timeout(30):
            self._get_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_namespace_async(
        self,
        request: GetNamespaceRequest,
    ) -> GetNamespaceResult:
        async_result = []
        self._get_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_namespace(
        self,
        request: UpdateNamespaceRequest,
        callback: Callable[[AsyncResult[UpdateNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='namespace',
            function='updateNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.description is not None:
            body["description"] = request.description
        if request.overflow_trigger_script is not None:
            body["overflowTriggerScript"] = request.overflow_trigger_script.to_dict()
        if request.log_setting is not None:
            body["logSetting"] = request.log_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def update_namespace(
        self,
        request: UpdateNamespaceRequest,
    ) -> UpdateNamespaceResult:
        async_result = []
        with timeout(30):
            self._update_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_namespace_async(
        self,
        request: UpdateNamespaceRequest,
    ) -> UpdateNamespaceResult:
        async_result = []
        self._update_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_namespace(
        self,
        request: DeleteNamespaceRequest,
        callback: Callable[[AsyncResult[DeleteNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='namespace',
            function='deleteNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DeleteNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def delete_namespace(
        self,
        request: DeleteNamespaceRequest,
    ) -> DeleteNamespaceResult:
        async_result = []
        with timeout(30):
            self._delete_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_namespace_async(
        self,
        request: DeleteNamespaceRequest,
    ) -> DeleteNamespaceResult:
        async_result = []
        self._delete_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_stamina_model_masters(
        self,
        request: DescribeStaminaModelMastersRequest,
        callback: Callable[[AsyncResult[DescribeStaminaModelMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModelMaster',
            function='describeStaminaModelMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeStaminaModelMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_stamina_model_masters(
        self,
        request: DescribeStaminaModelMastersRequest,
    ) -> DescribeStaminaModelMastersResult:
        async_result = []
        with timeout(30):
            self._describe_stamina_model_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_stamina_model_masters_async(
        self,
        request: DescribeStaminaModelMastersRequest,
    ) -> DescribeStaminaModelMastersResult:
        async_result = []
        self._describe_stamina_model_masters(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_stamina_model_master(
        self,
        request: CreateStaminaModelMasterRequest,
        callback: Callable[[AsyncResult[CreateStaminaModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModelMaster',
            function='createStaminaModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.recover_interval_minutes is not None:
            body["recoverIntervalMinutes"] = request.recover_interval_minutes
        if request.recover_value is not None:
            body["recoverValue"] = request.recover_value
        if request.initial_capacity is not None:
            body["initialCapacity"] = request.initial_capacity
        if request.is_overflow is not None:
            body["isOverflow"] = request.is_overflow
        if request.max_capacity is not None:
            body["maxCapacity"] = request.max_capacity
        if request.max_stamina_table_name is not None:
            body["maxStaminaTableName"] = request.max_stamina_table_name
        if request.recover_interval_table_name is not None:
            body["recoverIntervalTableName"] = request.recover_interval_table_name
        if request.recover_value_table_name is not None:
            body["recoverValueTableName"] = request.recover_value_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=CreateStaminaModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_stamina_model_master(
        self,
        request: CreateStaminaModelMasterRequest,
    ) -> CreateStaminaModelMasterResult:
        async_result = []
        with timeout(30):
            self._create_stamina_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_stamina_model_master_async(
        self,
        request: CreateStaminaModelMasterRequest,
    ) -> CreateStaminaModelMasterResult:
        async_result = []
        self._create_stamina_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_stamina_model_master(
        self,
        request: GetStaminaModelMasterRequest,
        callback: Callable[[AsyncResult[GetStaminaModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModelMaster',
            function='getStaminaModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetStaminaModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_stamina_model_master(
        self,
        request: GetStaminaModelMasterRequest,
    ) -> GetStaminaModelMasterResult:
        async_result = []
        with timeout(30):
            self._get_stamina_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_stamina_model_master_async(
        self,
        request: GetStaminaModelMasterRequest,
    ) -> GetStaminaModelMasterResult:
        async_result = []
        self._get_stamina_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_stamina_model_master(
        self,
        request: UpdateStaminaModelMasterRequest,
        callback: Callable[[AsyncResult[UpdateStaminaModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModelMaster',
            function='updateStaminaModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.recover_interval_minutes is not None:
            body["recoverIntervalMinutes"] = request.recover_interval_minutes
        if request.recover_value is not None:
            body["recoverValue"] = request.recover_value
        if request.initial_capacity is not None:
            body["initialCapacity"] = request.initial_capacity
        if request.is_overflow is not None:
            body["isOverflow"] = request.is_overflow
        if request.max_capacity is not None:
            body["maxCapacity"] = request.max_capacity
        if request.max_stamina_table_name is not None:
            body["maxStaminaTableName"] = request.max_stamina_table_name
        if request.recover_interval_table_name is not None:
            body["recoverIntervalTableName"] = request.recover_interval_table_name
        if request.recover_value_table_name is not None:
            body["recoverValueTableName"] = request.recover_value_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateStaminaModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_stamina_model_master(
        self,
        request: UpdateStaminaModelMasterRequest,
    ) -> UpdateStaminaModelMasterResult:
        async_result = []
        with timeout(30):
            self._update_stamina_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_stamina_model_master_async(
        self,
        request: UpdateStaminaModelMasterRequest,
    ) -> UpdateStaminaModelMasterResult:
        async_result = []
        self._update_stamina_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_stamina_model_master(
        self,
        request: DeleteStaminaModelMasterRequest,
        callback: Callable[[AsyncResult[DeleteStaminaModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModelMaster',
            function='deleteStaminaModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DeleteStaminaModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_stamina_model_master(
        self,
        request: DeleteStaminaModelMasterRequest,
    ) -> DeleteStaminaModelMasterResult:
        async_result = []
        with timeout(30):
            self._delete_stamina_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_stamina_model_master_async(
        self,
        request: DeleteStaminaModelMasterRequest,
    ) -> DeleteStaminaModelMasterResult:
        async_result = []
        self._delete_stamina_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_max_stamina_table_masters(
        self,
        request: DescribeMaxStaminaTableMastersRequest,
        callback: Callable[[AsyncResult[DescribeMaxStaminaTableMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='maxStaminaTableMaster',
            function='describeMaxStaminaTableMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeMaxStaminaTableMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_max_stamina_table_masters(
        self,
        request: DescribeMaxStaminaTableMastersRequest,
    ) -> DescribeMaxStaminaTableMastersResult:
        async_result = []
        with timeout(30):
            self._describe_max_stamina_table_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_max_stamina_table_masters_async(
        self,
        request: DescribeMaxStaminaTableMastersRequest,
    ) -> DescribeMaxStaminaTableMastersResult:
        async_result = []
        self._describe_max_stamina_table_masters(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_max_stamina_table_master(
        self,
        request: CreateMaxStaminaTableMasterRequest,
        callback: Callable[[AsyncResult[CreateMaxStaminaTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='maxStaminaTableMaster',
            function='createMaxStaminaTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.values is not None:
            body["values"] = [
                item
                for item in request.values
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=CreateMaxStaminaTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_max_stamina_table_master(
        self,
        request: CreateMaxStaminaTableMasterRequest,
    ) -> CreateMaxStaminaTableMasterResult:
        async_result = []
        with timeout(30):
            self._create_max_stamina_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_max_stamina_table_master_async(
        self,
        request: CreateMaxStaminaTableMasterRequest,
    ) -> CreateMaxStaminaTableMasterResult:
        async_result = []
        self._create_max_stamina_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_max_stamina_table_master(
        self,
        request: GetMaxStaminaTableMasterRequest,
        callback: Callable[[AsyncResult[GetMaxStaminaTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='maxStaminaTableMaster',
            function='getMaxStaminaTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.max_stamina_table_name is not None:
            body["maxStaminaTableName"] = request.max_stamina_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetMaxStaminaTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_max_stamina_table_master(
        self,
        request: GetMaxStaminaTableMasterRequest,
    ) -> GetMaxStaminaTableMasterResult:
        async_result = []
        with timeout(30):
            self._get_max_stamina_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_max_stamina_table_master_async(
        self,
        request: GetMaxStaminaTableMasterRequest,
    ) -> GetMaxStaminaTableMasterResult:
        async_result = []
        self._get_max_stamina_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_max_stamina_table_master(
        self,
        request: UpdateMaxStaminaTableMasterRequest,
        callback: Callable[[AsyncResult[UpdateMaxStaminaTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='maxStaminaTableMaster',
            function='updateMaxStaminaTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.max_stamina_table_name is not None:
            body["maxStaminaTableName"] = request.max_stamina_table_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.values is not None:
            body["values"] = [
                item
                for item in request.values
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateMaxStaminaTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_max_stamina_table_master(
        self,
        request: UpdateMaxStaminaTableMasterRequest,
    ) -> UpdateMaxStaminaTableMasterResult:
        async_result = []
        with timeout(30):
            self._update_max_stamina_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_max_stamina_table_master_async(
        self,
        request: UpdateMaxStaminaTableMasterRequest,
    ) -> UpdateMaxStaminaTableMasterResult:
        async_result = []
        self._update_max_stamina_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_max_stamina_table_master(
        self,
        request: DeleteMaxStaminaTableMasterRequest,
        callback: Callable[[AsyncResult[DeleteMaxStaminaTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='maxStaminaTableMaster',
            function='deleteMaxStaminaTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.max_stamina_table_name is not None:
            body["maxStaminaTableName"] = request.max_stamina_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DeleteMaxStaminaTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_max_stamina_table_master(
        self,
        request: DeleteMaxStaminaTableMasterRequest,
    ) -> DeleteMaxStaminaTableMasterResult:
        async_result = []
        with timeout(30):
            self._delete_max_stamina_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_max_stamina_table_master_async(
        self,
        request: DeleteMaxStaminaTableMasterRequest,
    ) -> DeleteMaxStaminaTableMasterResult:
        async_result = []
        self._delete_max_stamina_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_recover_interval_table_masters(
        self,
        request: DescribeRecoverIntervalTableMastersRequest,
        callback: Callable[[AsyncResult[DescribeRecoverIntervalTableMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverIntervalTableMaster',
            function='describeRecoverIntervalTableMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeRecoverIntervalTableMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_recover_interval_table_masters(
        self,
        request: DescribeRecoverIntervalTableMastersRequest,
    ) -> DescribeRecoverIntervalTableMastersResult:
        async_result = []
        with timeout(30):
            self._describe_recover_interval_table_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_recover_interval_table_masters_async(
        self,
        request: DescribeRecoverIntervalTableMastersRequest,
    ) -> DescribeRecoverIntervalTableMastersResult:
        async_result = []
        self._describe_recover_interval_table_masters(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_recover_interval_table_master(
        self,
        request: CreateRecoverIntervalTableMasterRequest,
        callback: Callable[[AsyncResult[CreateRecoverIntervalTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverIntervalTableMaster',
            function='createRecoverIntervalTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.values is not None:
            body["values"] = [
                item
                for item in request.values
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=CreateRecoverIntervalTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_recover_interval_table_master(
        self,
        request: CreateRecoverIntervalTableMasterRequest,
    ) -> CreateRecoverIntervalTableMasterResult:
        async_result = []
        with timeout(30):
            self._create_recover_interval_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_recover_interval_table_master_async(
        self,
        request: CreateRecoverIntervalTableMasterRequest,
    ) -> CreateRecoverIntervalTableMasterResult:
        async_result = []
        self._create_recover_interval_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_recover_interval_table_master(
        self,
        request: GetRecoverIntervalTableMasterRequest,
        callback: Callable[[AsyncResult[GetRecoverIntervalTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverIntervalTableMaster',
            function='getRecoverIntervalTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.recover_interval_table_name is not None:
            body["recoverIntervalTableName"] = request.recover_interval_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetRecoverIntervalTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_recover_interval_table_master(
        self,
        request: GetRecoverIntervalTableMasterRequest,
    ) -> GetRecoverIntervalTableMasterResult:
        async_result = []
        with timeout(30):
            self._get_recover_interval_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_recover_interval_table_master_async(
        self,
        request: GetRecoverIntervalTableMasterRequest,
    ) -> GetRecoverIntervalTableMasterResult:
        async_result = []
        self._get_recover_interval_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_recover_interval_table_master(
        self,
        request: UpdateRecoverIntervalTableMasterRequest,
        callback: Callable[[AsyncResult[UpdateRecoverIntervalTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverIntervalTableMaster',
            function='updateRecoverIntervalTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.recover_interval_table_name is not None:
            body["recoverIntervalTableName"] = request.recover_interval_table_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.values is not None:
            body["values"] = [
                item
                for item in request.values
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateRecoverIntervalTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_recover_interval_table_master(
        self,
        request: UpdateRecoverIntervalTableMasterRequest,
    ) -> UpdateRecoverIntervalTableMasterResult:
        async_result = []
        with timeout(30):
            self._update_recover_interval_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_recover_interval_table_master_async(
        self,
        request: UpdateRecoverIntervalTableMasterRequest,
    ) -> UpdateRecoverIntervalTableMasterResult:
        async_result = []
        self._update_recover_interval_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_recover_interval_table_master(
        self,
        request: DeleteRecoverIntervalTableMasterRequest,
        callback: Callable[[AsyncResult[DeleteRecoverIntervalTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverIntervalTableMaster',
            function='deleteRecoverIntervalTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.recover_interval_table_name is not None:
            body["recoverIntervalTableName"] = request.recover_interval_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DeleteRecoverIntervalTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_recover_interval_table_master(
        self,
        request: DeleteRecoverIntervalTableMasterRequest,
    ) -> DeleteRecoverIntervalTableMasterResult:
        async_result = []
        with timeout(30):
            self._delete_recover_interval_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_recover_interval_table_master_async(
        self,
        request: DeleteRecoverIntervalTableMasterRequest,
    ) -> DeleteRecoverIntervalTableMasterResult:
        async_result = []
        self._delete_recover_interval_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_recover_value_table_masters(
        self,
        request: DescribeRecoverValueTableMastersRequest,
        callback: Callable[[AsyncResult[DescribeRecoverValueTableMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverValueTableMaster',
            function='describeRecoverValueTableMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeRecoverValueTableMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_recover_value_table_masters(
        self,
        request: DescribeRecoverValueTableMastersRequest,
    ) -> DescribeRecoverValueTableMastersResult:
        async_result = []
        with timeout(30):
            self._describe_recover_value_table_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_recover_value_table_masters_async(
        self,
        request: DescribeRecoverValueTableMastersRequest,
    ) -> DescribeRecoverValueTableMastersResult:
        async_result = []
        self._describe_recover_value_table_masters(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_recover_value_table_master(
        self,
        request: CreateRecoverValueTableMasterRequest,
        callback: Callable[[AsyncResult[CreateRecoverValueTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverValueTableMaster',
            function='createRecoverValueTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.values is not None:
            body["values"] = [
                item
                for item in request.values
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=CreateRecoverValueTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_recover_value_table_master(
        self,
        request: CreateRecoverValueTableMasterRequest,
    ) -> CreateRecoverValueTableMasterResult:
        async_result = []
        with timeout(30):
            self._create_recover_value_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_recover_value_table_master_async(
        self,
        request: CreateRecoverValueTableMasterRequest,
    ) -> CreateRecoverValueTableMasterResult:
        async_result = []
        self._create_recover_value_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_recover_value_table_master(
        self,
        request: GetRecoverValueTableMasterRequest,
        callback: Callable[[AsyncResult[GetRecoverValueTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverValueTableMaster',
            function='getRecoverValueTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.recover_value_table_name is not None:
            body["recoverValueTableName"] = request.recover_value_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetRecoverValueTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_recover_value_table_master(
        self,
        request: GetRecoverValueTableMasterRequest,
    ) -> GetRecoverValueTableMasterResult:
        async_result = []
        with timeout(30):
            self._get_recover_value_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_recover_value_table_master_async(
        self,
        request: GetRecoverValueTableMasterRequest,
    ) -> GetRecoverValueTableMasterResult:
        async_result = []
        self._get_recover_value_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_recover_value_table_master(
        self,
        request: UpdateRecoverValueTableMasterRequest,
        callback: Callable[[AsyncResult[UpdateRecoverValueTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverValueTableMaster',
            function='updateRecoverValueTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.recover_value_table_name is not None:
            body["recoverValueTableName"] = request.recover_value_table_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.values is not None:
            body["values"] = [
                item
                for item in request.values
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateRecoverValueTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_recover_value_table_master(
        self,
        request: UpdateRecoverValueTableMasterRequest,
    ) -> UpdateRecoverValueTableMasterResult:
        async_result = []
        with timeout(30):
            self._update_recover_value_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_recover_value_table_master_async(
        self,
        request: UpdateRecoverValueTableMasterRequest,
    ) -> UpdateRecoverValueTableMasterResult:
        async_result = []
        self._update_recover_value_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_recover_value_table_master(
        self,
        request: DeleteRecoverValueTableMasterRequest,
        callback: Callable[[AsyncResult[DeleteRecoverValueTableMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='recoverValueTableMaster',
            function='deleteRecoverValueTableMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.recover_value_table_name is not None:
            body["recoverValueTableName"] = request.recover_value_table_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DeleteRecoverValueTableMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_recover_value_table_master(
        self,
        request: DeleteRecoverValueTableMasterRequest,
    ) -> DeleteRecoverValueTableMasterResult:
        async_result = []
        with timeout(30):
            self._delete_recover_value_table_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_recover_value_table_master_async(
        self,
        request: DeleteRecoverValueTableMasterRequest,
    ) -> DeleteRecoverValueTableMasterResult:
        async_result = []
        self._delete_recover_value_table_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _export_master(
        self,
        request: ExportMasterRequest,
        callback: Callable[[AsyncResult[ExportMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='currentStaminaMaster',
            function='exportMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=ExportMasterResult,
                callback=callback,
                body=body,
            )
        )

    def export_master(
        self,
        request: ExportMasterRequest,
    ) -> ExportMasterResult:
        async_result = []
        with timeout(30):
            self._export_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def export_master_async(
        self,
        request: ExportMasterRequest,
    ) -> ExportMasterResult:
        async_result = []
        self._export_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_current_stamina_master(
        self,
        request: GetCurrentStaminaMasterRequest,
        callback: Callable[[AsyncResult[GetCurrentStaminaMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='currentStaminaMaster',
            function='getCurrentStaminaMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetCurrentStaminaMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_current_stamina_master(
        self,
        request: GetCurrentStaminaMasterRequest,
    ) -> GetCurrentStaminaMasterResult:
        async_result = []
        with timeout(30):
            self._get_current_stamina_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_current_stamina_master_async(
        self,
        request: GetCurrentStaminaMasterRequest,
    ) -> GetCurrentStaminaMasterResult:
        async_result = []
        self._get_current_stamina_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_current_stamina_master(
        self,
        request: UpdateCurrentStaminaMasterRequest,
        callback: Callable[[AsyncResult[UpdateCurrentStaminaMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='currentStaminaMaster',
            function='updateCurrentStaminaMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.settings is not None:
            body["settings"] = request.settings

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateCurrentStaminaMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_current_stamina_master(
        self,
        request: UpdateCurrentStaminaMasterRequest,
    ) -> UpdateCurrentStaminaMasterResult:
        async_result = []
        with timeout(30):
            self._update_current_stamina_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_current_stamina_master_async(
        self,
        request: UpdateCurrentStaminaMasterRequest,
    ) -> UpdateCurrentStaminaMasterResult:
        async_result = []
        self._update_current_stamina_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_current_stamina_master_from_git_hub(
        self,
        request: UpdateCurrentStaminaMasterFromGitHubRequest,
        callback: Callable[[AsyncResult[UpdateCurrentStaminaMasterFromGitHubResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='currentStaminaMaster',
            function='updateCurrentStaminaMasterFromGitHub',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.checkout_setting is not None:
            body["checkoutSetting"] = request.checkout_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateCurrentStaminaMasterFromGitHubResult,
                callback=callback,
                body=body,
            )
        )

    def update_current_stamina_master_from_git_hub(
        self,
        request: UpdateCurrentStaminaMasterFromGitHubRequest,
    ) -> UpdateCurrentStaminaMasterFromGitHubResult:
        async_result = []
        with timeout(30):
            self._update_current_stamina_master_from_git_hub(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_current_stamina_master_from_git_hub_async(
        self,
        request: UpdateCurrentStaminaMasterFromGitHubRequest,
    ) -> UpdateCurrentStaminaMasterFromGitHubResult:
        async_result = []
        self._update_current_stamina_master_from_git_hub(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_stamina_models(
        self,
        request: DescribeStaminaModelsRequest,
        callback: Callable[[AsyncResult[DescribeStaminaModelsResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModel',
            function='describeStaminaModels',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeStaminaModelsResult,
                callback=callback,
                body=body,
            )
        )

    def describe_stamina_models(
        self,
        request: DescribeStaminaModelsRequest,
    ) -> DescribeStaminaModelsResult:
        async_result = []
        with timeout(30):
            self._describe_stamina_models(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_stamina_models_async(
        self,
        request: DescribeStaminaModelsRequest,
    ) -> DescribeStaminaModelsResult:
        async_result = []
        self._describe_stamina_models(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_stamina_model(
        self,
        request: GetStaminaModelRequest,
        callback: Callable[[AsyncResult[GetStaminaModelResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='staminaModel',
            function='getStaminaModel',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetStaminaModelResult,
                callback=callback,
                body=body,
            )
        )

    def get_stamina_model(
        self,
        request: GetStaminaModelRequest,
    ) -> GetStaminaModelResult:
        async_result = []
        with timeout(30):
            self._get_stamina_model(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_stamina_model_async(
        self,
        request: GetStaminaModelRequest,
    ) -> GetStaminaModelResult:
        async_result = []
        self._get_stamina_model(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_staminas(
        self,
        request: DescribeStaminasRequest,
        callback: Callable[[AsyncResult[DescribeStaminasResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='describeStaminas',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeStaminasResult,
                callback=callback,
                body=body,
            )
        )

    def describe_staminas(
        self,
        request: DescribeStaminasRequest,
    ) -> DescribeStaminasResult:
        async_result = []
        with timeout(30):
            self._describe_staminas(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_staminas_async(
        self,
        request: DescribeStaminasRequest,
    ) -> DescribeStaminasResult:
        async_result = []
        self._describe_staminas(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_staminas_by_user_id(
        self,
        request: DescribeStaminasByUserIdRequest,
        callback: Callable[[AsyncResult[DescribeStaminasByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='describeStaminasByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DescribeStaminasByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_staminas_by_user_id(
        self,
        request: DescribeStaminasByUserIdRequest,
    ) -> DescribeStaminasByUserIdResult:
        async_result = []
        with timeout(30):
            self._describe_staminas_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_staminas_by_user_id_async(
        self,
        request: DescribeStaminasByUserIdRequest,
    ) -> DescribeStaminasByUserIdResult:
        async_result = []
        self._describe_staminas_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_stamina(
        self,
        request: GetStaminaRequest,
        callback: Callable[[AsyncResult[GetStaminaResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='getStamina',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetStaminaResult,
                callback=callback,
                body=body,
            )
        )

    def get_stamina(
        self,
        request: GetStaminaRequest,
    ) -> GetStaminaResult:
        async_result = []
        with timeout(30):
            self._get_stamina(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_stamina_async(
        self,
        request: GetStaminaRequest,
    ) -> GetStaminaResult:
        async_result = []
        self._get_stamina(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_stamina_by_user_id(
        self,
        request: GetStaminaByUserIdRequest,
        callback: Callable[[AsyncResult[GetStaminaByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='getStaminaByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=GetStaminaByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def get_stamina_by_user_id(
        self,
        request: GetStaminaByUserIdRequest,
    ) -> GetStaminaByUserIdResult:
        async_result = []
        with timeout(30):
            self._get_stamina_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_stamina_by_user_id_async(
        self,
        request: GetStaminaByUserIdRequest,
    ) -> GetStaminaByUserIdResult:
        async_result = []
        self._get_stamina_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_stamina_by_user_id(
        self,
        request: UpdateStaminaByUserIdRequest,
        callback: Callable[[AsyncResult[UpdateStaminaByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='updateStaminaByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.value is not None:
            body["value"] = request.value
        if request.max_value is not None:
            body["maxValue"] = request.max_value
        if request.recover_interval_minutes is not None:
            body["recoverIntervalMinutes"] = request.recover_interval_minutes
        if request.recover_value is not None:
            body["recoverValue"] = request.recover_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=UpdateStaminaByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def update_stamina_by_user_id(
        self,
        request: UpdateStaminaByUserIdRequest,
    ) -> UpdateStaminaByUserIdResult:
        async_result = []
        with timeout(30):
            self._update_stamina_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_stamina_by_user_id_async(
        self,
        request: UpdateStaminaByUserIdRequest,
    ) -> UpdateStaminaByUserIdResult:
        async_result = []
        self._update_stamina_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _consume_stamina(
        self,
        request: ConsumeStaminaRequest,
        callback: Callable[[AsyncResult[ConsumeStaminaResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='consumeStamina',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.consume_value is not None:
            body["consumeValue"] = request.consume_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=ConsumeStaminaResult,
                callback=callback,
                body=body,
            )
        )

    def consume_stamina(
        self,
        request: ConsumeStaminaRequest,
    ) -> ConsumeStaminaResult:
        async_result = []
        with timeout(30):
            self._consume_stamina(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def consume_stamina_async(
        self,
        request: ConsumeStaminaRequest,
    ) -> ConsumeStaminaResult:
        async_result = []
        self._consume_stamina(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _consume_stamina_by_user_id(
        self,
        request: ConsumeStaminaByUserIdRequest,
        callback: Callable[[AsyncResult[ConsumeStaminaByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='consumeStaminaByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.consume_value is not None:
            body["consumeValue"] = request.consume_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=ConsumeStaminaByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def consume_stamina_by_user_id(
        self,
        request: ConsumeStaminaByUserIdRequest,
    ) -> ConsumeStaminaByUserIdResult:
        async_result = []
        with timeout(30):
            self._consume_stamina_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def consume_stamina_by_user_id_async(
        self,
        request: ConsumeStaminaByUserIdRequest,
    ) -> ConsumeStaminaByUserIdResult:
        async_result = []
        self._consume_stamina_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _recover_stamina_by_user_id(
        self,
        request: RecoverStaminaByUserIdRequest,
        callback: Callable[[AsyncResult[RecoverStaminaByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='recoverStaminaByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.recover_value is not None:
            body["recoverValue"] = request.recover_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=RecoverStaminaByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def recover_stamina_by_user_id(
        self,
        request: RecoverStaminaByUserIdRequest,
    ) -> RecoverStaminaByUserIdResult:
        async_result = []
        with timeout(30):
            self._recover_stamina_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def recover_stamina_by_user_id_async(
        self,
        request: RecoverStaminaByUserIdRequest,
    ) -> RecoverStaminaByUserIdResult:
        async_result = []
        self._recover_stamina_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _raise_max_value_by_user_id(
        self,
        request: RaiseMaxValueByUserIdRequest,
        callback: Callable[[AsyncResult[RaiseMaxValueByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='raiseMaxValueByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.raise_value is not None:
            body["raiseValue"] = request.raise_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=RaiseMaxValueByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def raise_max_value_by_user_id(
        self,
        request: RaiseMaxValueByUserIdRequest,
    ) -> RaiseMaxValueByUserIdResult:
        async_result = []
        with timeout(30):
            self._raise_max_value_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def raise_max_value_by_user_id_async(
        self,
        request: RaiseMaxValueByUserIdRequest,
    ) -> RaiseMaxValueByUserIdResult:
        async_result = []
        self._raise_max_value_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_max_value_by_user_id(
        self,
        request: SetMaxValueByUserIdRequest,
        callback: Callable[[AsyncResult[SetMaxValueByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setMaxValueByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.max_value is not None:
            body["maxValue"] = request.max_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetMaxValueByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def set_max_value_by_user_id(
        self,
        request: SetMaxValueByUserIdRequest,
    ) -> SetMaxValueByUserIdResult:
        async_result = []
        with timeout(30):
            self._set_max_value_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_max_value_by_user_id_async(
        self,
        request: SetMaxValueByUserIdRequest,
    ) -> SetMaxValueByUserIdResult:
        async_result = []
        self._set_max_value_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_recover_interval_by_user_id(
        self,
        request: SetRecoverIntervalByUserIdRequest,
        callback: Callable[[AsyncResult[SetRecoverIntervalByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setRecoverIntervalByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.recover_interval_minutes is not None:
            body["recoverIntervalMinutes"] = request.recover_interval_minutes

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetRecoverIntervalByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def set_recover_interval_by_user_id(
        self,
        request: SetRecoverIntervalByUserIdRequest,
    ) -> SetRecoverIntervalByUserIdResult:
        async_result = []
        with timeout(30):
            self._set_recover_interval_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_recover_interval_by_user_id_async(
        self,
        request: SetRecoverIntervalByUserIdRequest,
    ) -> SetRecoverIntervalByUserIdResult:
        async_result = []
        self._set_recover_interval_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_recover_value_by_user_id(
        self,
        request: SetRecoverValueByUserIdRequest,
        callback: Callable[[AsyncResult[SetRecoverValueByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setRecoverValueByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.recover_value is not None:
            body["recoverValue"] = request.recover_value

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetRecoverValueByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def set_recover_value_by_user_id(
        self,
        request: SetRecoverValueByUserIdRequest,
    ) -> SetRecoverValueByUserIdResult:
        async_result = []
        with timeout(30):
            self._set_recover_value_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_recover_value_by_user_id_async(
        self,
        request: SetRecoverValueByUserIdRequest,
    ) -> SetRecoverValueByUserIdResult:
        async_result = []
        self._set_recover_value_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_max_value_by_status(
        self,
        request: SetMaxValueByStatusRequest,
        callback: Callable[[AsyncResult[SetMaxValueByStatusResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setMaxValueByStatus',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.key_id is not None:
            body["keyId"] = request.key_id
        if request.signed_status_body is not None:
            body["signedStatusBody"] = request.signed_status_body
        if request.signed_status_signature is not None:
            body["signedStatusSignature"] = request.signed_status_signature

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetMaxValueByStatusResult,
                callback=callback,
                body=body,
            )
        )

    def set_max_value_by_status(
        self,
        request: SetMaxValueByStatusRequest,
    ) -> SetMaxValueByStatusResult:
        async_result = []
        with timeout(30):
            self._set_max_value_by_status(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_max_value_by_status_async(
        self,
        request: SetMaxValueByStatusRequest,
    ) -> SetMaxValueByStatusResult:
        async_result = []
        self._set_max_value_by_status(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_recover_interval_by_status(
        self,
        request: SetRecoverIntervalByStatusRequest,
        callback: Callable[[AsyncResult[SetRecoverIntervalByStatusResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setRecoverIntervalByStatus',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.key_id is not None:
            body["keyId"] = request.key_id
        if request.signed_status_body is not None:
            body["signedStatusBody"] = request.signed_status_body
        if request.signed_status_signature is not None:
            body["signedStatusSignature"] = request.signed_status_signature

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetRecoverIntervalByStatusResult,
                callback=callback,
                body=body,
            )
        )

    def set_recover_interval_by_status(
        self,
        request: SetRecoverIntervalByStatusRequest,
    ) -> SetRecoverIntervalByStatusResult:
        async_result = []
        with timeout(30):
            self._set_recover_interval_by_status(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_recover_interval_by_status_async(
        self,
        request: SetRecoverIntervalByStatusRequest,
    ) -> SetRecoverIntervalByStatusResult:
        async_result = []
        self._set_recover_interval_by_status(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_recover_value_by_status(
        self,
        request: SetRecoverValueByStatusRequest,
        callback: Callable[[AsyncResult[SetRecoverValueByStatusResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setRecoverValueByStatus',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.key_id is not None:
            body["keyId"] = request.key_id
        if request.signed_status_body is not None:
            body["signedStatusBody"] = request.signed_status_body
        if request.signed_status_signature is not None:
            body["signedStatusSignature"] = request.signed_status_signature

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetRecoverValueByStatusResult,
                callback=callback,
                body=body,
            )
        )

    def set_recover_value_by_status(
        self,
        request: SetRecoverValueByStatusRequest,
    ) -> SetRecoverValueByStatusResult:
        async_result = []
        with timeout(30):
            self._set_recover_value_by_status(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_recover_value_by_status_async(
        self,
        request: SetRecoverValueByStatusRequest,
    ) -> SetRecoverValueByStatusResult:
        async_result = []
        self._set_recover_value_by_status(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_stamina_by_user_id(
        self,
        request: DeleteStaminaByUserIdRequest,
        callback: Callable[[AsyncResult[DeleteStaminaByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='deleteStaminaByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.stamina_name is not None:
            body["staminaName"] = request.stamina_name
        if request.user_id is not None:
            body["userId"] = request.user_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=DeleteStaminaByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def delete_stamina_by_user_id(
        self,
        request: DeleteStaminaByUserIdRequest,
    ) -> DeleteStaminaByUserIdResult:
        async_result = []
        with timeout(30):
            self._delete_stamina_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_stamina_by_user_id_async(
        self,
        request: DeleteStaminaByUserIdRequest,
    ) -> DeleteStaminaByUserIdResult:
        async_result = []
        self._delete_stamina_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _recover_stamina_by_stamp_sheet(
        self,
        request: RecoverStaminaByStampSheetRequest,
        callback: Callable[[AsyncResult[RecoverStaminaByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='recoverStaminaByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=RecoverStaminaByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def recover_stamina_by_stamp_sheet(
        self,
        request: RecoverStaminaByStampSheetRequest,
    ) -> RecoverStaminaByStampSheetResult:
        async_result = []
        with timeout(30):
            self._recover_stamina_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def recover_stamina_by_stamp_sheet_async(
        self,
        request: RecoverStaminaByStampSheetRequest,
    ) -> RecoverStaminaByStampSheetResult:
        async_result = []
        self._recover_stamina_by_stamp_sheet(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _raise_max_value_by_stamp_sheet(
        self,
        request: RaiseMaxValueByStampSheetRequest,
        callback: Callable[[AsyncResult[RaiseMaxValueByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='raiseMaxValueByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=RaiseMaxValueByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def raise_max_value_by_stamp_sheet(
        self,
        request: RaiseMaxValueByStampSheetRequest,
    ) -> RaiseMaxValueByStampSheetResult:
        async_result = []
        with timeout(30):
            self._raise_max_value_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def raise_max_value_by_stamp_sheet_async(
        self,
        request: RaiseMaxValueByStampSheetRequest,
    ) -> RaiseMaxValueByStampSheetResult:
        async_result = []
        self._raise_max_value_by_stamp_sheet(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_max_value_by_stamp_sheet(
        self,
        request: SetMaxValueByStampSheetRequest,
        callback: Callable[[AsyncResult[SetMaxValueByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setMaxValueByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetMaxValueByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def set_max_value_by_stamp_sheet(
        self,
        request: SetMaxValueByStampSheetRequest,
    ) -> SetMaxValueByStampSheetResult:
        async_result = []
        with timeout(30):
            self._set_max_value_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_max_value_by_stamp_sheet_async(
        self,
        request: SetMaxValueByStampSheetRequest,
    ) -> SetMaxValueByStampSheetResult:
        async_result = []
        self._set_max_value_by_stamp_sheet(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_recover_interval_by_stamp_sheet(
        self,
        request: SetRecoverIntervalByStampSheetRequest,
        callback: Callable[[AsyncResult[SetRecoverIntervalByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setRecoverIntervalByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetRecoverIntervalByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def set_recover_interval_by_stamp_sheet(
        self,
        request: SetRecoverIntervalByStampSheetRequest,
    ) -> SetRecoverIntervalByStampSheetResult:
        async_result = []
        with timeout(30):
            self._set_recover_interval_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_recover_interval_by_stamp_sheet_async(
        self,
        request: SetRecoverIntervalByStampSheetRequest,
    ) -> SetRecoverIntervalByStampSheetResult:
        async_result = []
        self._set_recover_interval_by_stamp_sheet(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _set_recover_value_by_stamp_sheet(
        self,
        request: SetRecoverValueByStampSheetRequest,
        callback: Callable[[AsyncResult[SetRecoverValueByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='setRecoverValueByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=SetRecoverValueByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def set_recover_value_by_stamp_sheet(
        self,
        request: SetRecoverValueByStampSheetRequest,
    ) -> SetRecoverValueByStampSheetResult:
        async_result = []
        with timeout(30):
            self._set_recover_value_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def set_recover_value_by_stamp_sheet_async(
        self,
        request: SetRecoverValueByStampSheetRequest,
    ) -> SetRecoverValueByStampSheetResult:
        async_result = []
        self._set_recover_value_by_stamp_sheet(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _consume_stamina_by_stamp_task(
        self,
        request: ConsumeStaminaByStampTaskRequest,
        callback: Callable[[AsyncResult[ConsumeStaminaByStampTaskResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="stamina",
            component='stamina',
            function='consumeStaminaByStampTask',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_task is not None:
            body["stampTask"] = request.stamp_task
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=ConsumeStaminaByStampTaskResult,
                callback=callback,
                body=body,
            )
        )

    def consume_stamina_by_stamp_task(
        self,
        request: ConsumeStaminaByStampTaskRequest,
    ) -> ConsumeStaminaByStampTaskResult:
        async_result = []
        with timeout(30):
            self._consume_stamina_by_stamp_task(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def consume_stamina_by_stamp_task_async(
        self,
        request: ConsumeStaminaByStampTaskRequest,
    ) -> ConsumeStaminaByStampTaskResult:
        async_result = []
        self._consume_stamina_by_stamp_task(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result