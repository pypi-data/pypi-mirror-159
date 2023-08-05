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
from schedule import Gs2ScheduleRestClient, request as request_, result as result_
from schedule.domain.iterator.namespaces import DescribeNamespacesIterator
from schedule.domain.iterator.event_masters import DescribeEventMastersIterator
from schedule.domain.iterator.triggers import DescribeTriggersIterator
from schedule.domain.iterator.triggers_by_user_id import DescribeTriggersByUserIdIterator
from schedule.domain.iterator.events import DescribeEventsIterator
from schedule.domain.iterator.events_by_user_id import DescribeEventsByUserIdIterator
from schedule.domain.iterator.raw_events import DescribeRawEventsIterator
from schedule.domain.cache.namespace import NamespaceDomainCache
from schedule.domain.cache.event_master import EventMasterDomainCache
from schedule.domain.cache.trigger import TriggerDomainCache
from schedule.domain.cache.event import EventDomainCache


class EventDomain:
    _session: Gs2RestSession
    _client: Gs2ScheduleRestClient
    _event_cache: EventDomainCache
    _namespace_name: str
    _user_id: str
    _event_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        event_cache: EventDomainCache,
        namespace_name: str,
        user_id: str,
        event_name: str,
    ):
        self._session = session
        self._client = Gs2ScheduleRestClient(
            session,
        )
        self._event_cache = event_cache
        self._namespace_name = namespace_name
        self._user_id = user_id
        self._event_name = event_name

    def load(
        self,
        request: request_.GetEventByUserIdRequest,
    ) -> result_.GetEventByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        request.with_event_name(self._event_name)
        r = self._client.get_event_by_user_id(
            request,
        )
        self._event_cache.update(r.item)
        return r

    def get_raw(
        self,
        request: request_.GetRawEventRequest,
    ) -> result_.GetRawEventResult:
        request.with_namespace_name(self._namespace_name)
        request.with_event_name(self._event_name)
        r = self._client.get_raw_event(
            request,
        )
        self._event_cache.update(r.item)
        return r
