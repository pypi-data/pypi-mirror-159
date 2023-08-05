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
from core.domain.access_token import AccessToken
from inventory import Gs2InventoryRestClient, request as request_, result as result_
from inventory.domain.iterator.namespaces import DescribeNamespacesIterator
from inventory.domain.iterator.inventory_model_masters import DescribeInventoryModelMastersIterator
from inventory.domain.iterator.inventory_models import DescribeInventoryModelsIterator
from inventory.domain.iterator.item_model_masters import DescribeItemModelMastersIterator
from inventory.domain.iterator.item_models import DescribeItemModelsIterator
from inventory.domain.iterator.inventories import DescribeInventoriesIterator
from inventory.domain.iterator.inventories_by_user_id import DescribeInventoriesByUserIdIterator
from inventory.domain.iterator.item_sets import DescribeItemSetsIterator
from inventory.domain.iterator.item_sets_by_user_id import DescribeItemSetsByUserIdIterator
from inventory.domain.iterator.reference_of import DescribeReferenceOfIterator
from inventory.domain.iterator.reference_of_by_user_id import DescribeReferenceOfByUserIdIterator
from inventory.domain.cache.namespace import NamespaceDomainCache
from inventory.domain.cache.inventory_model_master import InventoryModelMasterDomainCache
from inventory.domain.cache.inventory_model import InventoryModelDomainCache
from inventory.domain.cache.item_model_master import ItemModelMasterDomainCache
from inventory.domain.cache.item_model import ItemModelDomainCache
from inventory.domain.cache.inventory import InventoryDomainCache
from inventory.domain.cache.item_set import ItemSetDomainCache
from inventory.domain.reference_of import ReferenceOfDomain
from inventory.domain.reference_of_access_token import ReferenceOfAccessTokenDomain
from inventory.domain.reference_of_access_token import ReferenceOfAccessTokenDomain


class ItemSetAccessTokenDomain:
    _session: Gs2RestSession
    _client: Gs2InventoryRestClient
    _item_set_cache: ItemSetDomainCache
    _namespace_name: str
    _access_token: AccessToken
    _inventory_name: str
    _item_name: str
    _item_set_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        item_set_cache: ItemSetDomainCache,
        namespace_name: str,
        access_token: AccessToken,
        inventory_name: str,
        item_name: str,
        item_set_name: str,
    ):
        self._session = session
        self._client = Gs2InventoryRestClient(
            session,
        )
        self._item_set_cache = item_set_cache
        self._namespace_name = namespace_name
        self._access_token = access_token
        self._inventory_name = inventory_name
        self._item_name = item_name
        self._item_set_name = item_set_name

    def load(
        self,
        request: request_.GetItemSetRequest,
    ) -> result_.GetItemSetResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_inventory_name(self._inventory_name)
        request.with_item_name(self._item_name)
        request.with_item_set_name(self._item_set_name)
        r = self._client.get_item_set(
            request,
        )
        return r

    def get_item_with_signature(
        self,
        request: request_.GetItemWithSignatureRequest,
    ) -> result_.GetItemWithSignatureResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_inventory_name(self._inventory_name)
        request.with_item_name(self._item_name)
        request.with_item_set_name(self._item_set_name)
        r = self._client.get_item_with_signature(
            request,
        )
        return r

    def consume(
        self,
        request: request_.ConsumeItemSetRequest,
    ) -> result_.ConsumeItemSetResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_inventory_name(self._inventory_name)
        request.with_item_name(self._item_name)
        request.with_item_set_name(self._item_set_name)
        r = self._client.consume_item_set(
            request,
        )
        return r

    def reference_of(
        self,
    ) -> ReferenceOfAccessTokenDomain:
        return ReferenceOfAccessTokenDomain(
            self._session,
            self._namespace_name,
            self._access_token,
            self._inventory_name,
            self._item_name,
            self._item_set_name,
        )
