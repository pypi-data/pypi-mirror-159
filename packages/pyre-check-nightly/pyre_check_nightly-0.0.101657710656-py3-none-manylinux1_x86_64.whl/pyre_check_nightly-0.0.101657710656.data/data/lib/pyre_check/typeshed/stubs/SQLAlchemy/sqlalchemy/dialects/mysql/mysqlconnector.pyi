from typing import Any

from ...util import memoized_property
from .base import BIT, MySQLCompiler, MySQLDialect, MySQLIdentifierPreparer

class MySQLCompiler_mysqlconnector(MySQLCompiler):
    def visit_mod_binary(self, binary, operator, **kw): ...
    def post_process_text(self, text): ...
    def escape_literal_column(self, text): ...

class MySQLIdentifierPreparer_mysqlconnector(MySQLIdentifierPreparer): ...

class _myconnpyBIT(BIT):
    def result_processor(self, dialect, coltype) -> None: ...

class MySQLDialect_mysqlconnector(MySQLDialect):
    driver: str
    supports_statement_cache: bool
    supports_unicode_binds: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_native_decimal: bool
    default_paramstyle: str
    statement_compiler: Any
    preparer: Any
    colspecs: Any
    def __init__(self, *arg, **kw) -> None: ...
    @property
    def description_encoding(self): ...
    @memoized_property
    def supports_unicode_statements(self): ...
    @classmethod
    def dbapi(cls): ...
    def do_ping(self, dbapi_connection): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = MySQLDialect_mysqlconnector
