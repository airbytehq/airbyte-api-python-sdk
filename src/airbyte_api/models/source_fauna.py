"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class SourceFaunaDeletionMode(str, Enum):
    DELETED_FIELD = 'deleted_field'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Enabled:
    column: Optional[str] = dataclasses.field(default='deleted_at', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column'), 'exclude': lambda f: f is None }})
    r"""Name of the \\"deleted at\\" column."""
    DELETION_MODE: Final[SourceFaunaDeletionMode] = dataclasses.field(default=SourceFaunaDeletionMode.DELETED_FIELD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletion_mode') }})
    



class SourceFaunaSchemasDeletionMode(str, Enum):
    IGNORE = 'ignore'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Disabled:
    DELETION_MODE: Final[SourceFaunaSchemasDeletionMode] = dataclasses.field(default=SourceFaunaSchemasDeletionMode.IGNORE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletion_mode') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Collection:
    r"""Settings for the Fauna Collection."""
    deletions: DeletionMode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletions') }})
    r"""<b>This only applies to incremental syncs.</b> <br>
    Enabling deletion mode informs your destination of deleted documents.<br>
    Disabled - Leave this feature disabled, and ignore deleted documents.<br>
    Enabled - Enables this feature. When a document is deleted, the connector exports a record with a \"deleted at\" column containing the time that the document was deleted.
    """
    page_size: Optional[int] = dataclasses.field(default=64, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size'), 'exclude': lambda f: f is None }})
    r"""The page size used when reading documents from the database. The larger the page size, the faster the connector processes documents. However, if a page is too large, the connector may fail. <br>
    Choose your page size based on how large the documents are. <br>
    See <a href=\"https://docs.fauna.com/fauna/current/learn/understanding/types#page\">the docs</a>.
    """
    



class Fauna(str, Enum):
    FAUNA = 'fauna'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFauna:
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Fauna secret, used when authenticating with the database."""
    collection: Optional[Collection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection'), 'exclude': lambda f: f is None }})
    r"""Settings for the Fauna Collection."""
    domain: Optional[str] = dataclasses.field(default='db.fauna.com', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    r"""Domain of Fauna to query. Defaults db.fauna.com. See <a href=https://docs.fauna.com/fauna/current/learn/understanding/region_groups#how-to-use-region-groups>the docs</a>."""
    port: Optional[int] = dataclasses.field(default=443, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Endpoint port."""
    scheme: Optional[str] = dataclasses.field(default='https', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme'), 'exclude': lambda f: f is None }})
    r"""URL scheme."""
    SOURCE_TYPE: Final[Fauna] = dataclasses.field(default=Fauna.FAUNA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    


DeletionMode = Union[Disabled, Enabled]
