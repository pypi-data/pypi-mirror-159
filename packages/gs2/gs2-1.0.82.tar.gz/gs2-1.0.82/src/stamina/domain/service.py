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
from __future__ import annotations

from core import Gs2RestSession
from stamina import Gs2StaminaRestClient, request as request_, result as result_
from stamina.domain.iterator.namespaces import DescribeNamespacesIterator
from stamina.domain.cache.namespace import NamespaceDomainCache
from stamina.domain.namespace import NamespaceDomain

class Gs2Stamina:
    _session: Gs2RestSession
    _client: Gs2StaminaRestClient
    _namespace_cache: NamespaceDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
    ):
        self._session = session
        self._client = Gs2StaminaRestClient (
            session,
        )
        self._namespace_cache = NamespaceDomainCache()

    def create_namespace(
        self,
        request: request_.CreateNamespaceRequest,
    ) -> result_.CreateNamespaceResult:
        r = self._client.create_namespace(
            request,
        )
        self._namespace_cache.update(r.item)
        return r

    def recover_stamina_by_stamp_sheet(
        self,
        request: request_.RecoverStaminaByStampSheetRequest,
    ) -> result_.RecoverStaminaByStampSheetResult:
        r = self._client.recover_stamina_by_stamp_sheet(
            request,
        )
        return r

    def raise_max_value_by_stamp_sheet(
        self,
        request: request_.RaiseMaxValueByStampSheetRequest,
    ) -> result_.RaiseMaxValueByStampSheetResult:
        r = self._client.raise_max_value_by_stamp_sheet(
            request,
        )
        return r

    def set_max_value_by_stamp_sheet(
        self,
        request: request_.SetMaxValueByStampSheetRequest,
    ) -> result_.SetMaxValueByStampSheetResult:
        r = self._client.set_max_value_by_stamp_sheet(
            request,
        )
        return r

    def set_recover_interval_by_stamp_sheet(
        self,
        request: request_.SetRecoverIntervalByStampSheetRequest,
    ) -> result_.SetRecoverIntervalByStampSheetResult:
        r = self._client.set_recover_interval_by_stamp_sheet(
            request,
        )
        return r

    def set_recover_value_by_stamp_sheet(
        self,
        request: request_.SetRecoverValueByStampSheetRequest,
    ) -> result_.SetRecoverValueByStampSheetResult:
        r = self._client.set_recover_value_by_stamp_sheet(
            request,
        )
        return r

    def consume_stamina_by_stamp_task(
        self,
        request: request_.ConsumeStaminaByStampTaskRequest,
    ) -> result_.ConsumeStaminaByStampTaskResult:
        r = self._client.consume_stamina_by_stamp_task(
            request,
        )
        return r

    def namespaces(
        self,
    ) -> DescribeNamespacesIterator:
        return DescribeNamespacesIterator(
            self._namespace_cache,
            self._client,
        )

    def namespace(
        self,
        namespace_name: str,
    ) -> NamespaceDomain:
        return NamespaceDomain(
            self._session,
            self._namespace_cache,
            namespace_name,
        )
