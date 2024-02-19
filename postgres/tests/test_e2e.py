# (C) Datadog, Inc. 2010-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

import pytest

from .common import _get_expected_tags, check_bgw_metrics, check_common_metrics


@pytest.mark.e2e
def test_e2e(dd_agent_check, pg_instance):
    aggregator = dd_agent_check(pg_instance, rate=True)

    expected_tags = _get_expected_tags(None, pg_instance)
    check_bgw_metrics(aggregator, expected_tags)
    check_common_metrics(aggregator, expected_tags=expected_tags, count=None)
