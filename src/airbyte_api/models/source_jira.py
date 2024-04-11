"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, List, Optional

class IssuesStreamExpandWith(str, Enum):
    RENDERED_FIELDS = 'renderedFields'
    TRANSITIONS = 'transitions'
    CHANGELOG = 'changelog'

class Jira(str, Enum):
    JIRA = 'jira'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceJira:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Jira API Token. See the <a href=\\"https://docs.airbyte.com/integrations/sources/jira\\">docs</a> for more information on how to generate this key. API Token is used for Authorization to your account by BasicAuth."""
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    r"""The Domain for your Jira account, e.g. airbyteio.atlassian.net, airbyteio.jira.com, jira.your-domain.com"""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The user email for your Jira account which you used to generate the API token. This field is used for Authorization to your account by BasicAuth."""
    enable_experimental_streams: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_experimental_streams'), 'exclude': lambda f: f is None }})
    r"""Allow the use of experimental streams which rely on undocumented Jira API endpoints. See https://docs.airbyte.com/integrations/sources/jira#experimental-tables for more info."""
    expand_issue_changelog: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expand_issue_changelog'), 'exclude': lambda f: f is None }})
    r"""(DEPRECATED) Expand the changelog when replicating issues."""
    expand_issue_transition: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expand_issue_transition'), 'exclude': lambda f: f is None }})
    r"""(DEPRECATED) Expand the transitions when replicating issues."""
    issues_stream_expand_with: Optional[List[IssuesStreamExpandWith]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issues_stream_expand_with'), 'exclude': lambda f: f is None }})
    r"""Select fields to Expand the `Issues` stream when replicating with:"""
    lookback_window_minutes: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_minutes'), 'exclude': lambda f: f is None }})
    r"""When set to N, the connector will always refresh resources created within the past N minutes. By default, updated objects that are not newly created are not incrementally synced."""
    projects: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects'), 'exclude': lambda f: f is None }})
    r"""List of Jira project keys to replicate data for, or leave it empty if you want to replicate data for all projects."""
    render_fields: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('render_fields'), 'exclude': lambda f: f is None }})
    r"""(DEPRECATED) Render issue fields in HTML format in addition to Jira JSON-like format."""
    SOURCE_TYPE: Final[Jira] = dataclasses.field(default=Jira.JIRA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date from which you want to replicate data from Jira, use the format YYYY-MM-DDT00:00:00Z. Note that this field only applies to certain streams, and only data generated on or after the start date will be replicated. Or leave it empty if you want to replicate all data. For more information, refer to the <a href=\\"https://docs.airbyte.com/integrations/sources/jira/\\">documentation</a>."""
    

