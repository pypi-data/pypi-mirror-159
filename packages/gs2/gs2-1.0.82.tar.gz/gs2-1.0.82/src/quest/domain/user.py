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
from quest import Gs2QuestRestClient, request as request_, result as result_
from quest.domain.iterator.namespaces import DescribeNamespacesIterator
from quest.domain.iterator.quest_group_model_masters import DescribeQuestGroupModelMastersIterator
from quest.domain.iterator.quest_model_masters import DescribeQuestModelMastersIterator
from quest.domain.iterator.progresses_by_user_id import DescribeProgressesByUserIdIterator
from quest.domain.iterator.completed_quest_lists import DescribeCompletedQuestListsIterator
from quest.domain.iterator.completed_quest_lists_by_user_id import DescribeCompletedQuestListsByUserIdIterator
from quest.domain.iterator.quest_group_models import DescribeQuestGroupModelsIterator
from quest.domain.iterator.quest_models import DescribeQuestModelsIterator
from quest.domain.cache.namespace import NamespaceDomainCache
from quest.domain.cache.quest_group_model_master import QuestGroupModelMasterDomainCache
from quest.domain.cache.quest_model_master import QuestModelMasterDomainCache
from quest.domain.cache.progress import ProgressDomainCache
from quest.domain.cache.completed_quest_list import CompletedQuestListDomainCache
from quest.domain.cache.quest_group_model import QuestGroupModelDomainCache
from quest.domain.cache.quest_model import QuestModelDomainCache
from quest.domain.progress import ProgressDomain
from quest.domain.progress_access_token import ProgressAccessTokenDomain
from quest.domain.progress_access_token import ProgressAccessTokenDomain
from quest.domain.completed_quest_list import CompletedQuestListDomain
from quest.domain.completed_quest_list_access_token import CompletedQuestListAccessTokenDomain
from quest.domain.completed_quest_list_access_token import CompletedQuestListAccessTokenDomain


class UserDomain:
    _session: Gs2RestSession
    _client: Gs2QuestRestClient
    _namespace_name: str
    _user_id: str
    _progress_cache: ProgressDomainCache
    _completed_quest_list_cache: CompletedQuestListDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
        namespace_name: str,
        user_id: str,
    ):
        self._session = session
        self._client = Gs2QuestRestClient(
            session,
        )
        self._namespace_name = namespace_name
        self._user_id = user_id
        self._progress_cache = ProgressDomainCache()
        self._completed_quest_list_cache = CompletedQuestListDomainCache()

    def create_progress(
        self,
        request: request_.CreateProgressByUserIdRequest,
    ) -> result_.CreateProgressByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        r = self._client.create_progress_by_user_id(
            request,
        )
        return r

    def completed_quest_lists(
        self,
    ) -> DescribeCompletedQuestListsByUserIdIterator:
        return DescribeCompletedQuestListsByUserIdIterator(
            self._completed_quest_list_cache,
            self._client,
            self._namespace_name,
            self._user_id,
        )

    def progress(
        self,
    ) -> ProgressDomain:
        return ProgressDomain(
            self._session,
            self._progress_cache,
            self._namespace_name,
            self._user_id,
        )

    def completed_quest_list(
        self,
        quest_group_name: str,
    ) -> CompletedQuestListDomain:
        return CompletedQuestListDomain(
            self._session,
            self._completed_quest_list_cache,
            self._namespace_name,
            self._user_id,
            quest_group_name,
        )
