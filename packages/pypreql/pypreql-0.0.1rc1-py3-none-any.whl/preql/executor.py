from sqlalchemy.engine import create_engine, Engine

from preql.dialect.enums import Dialects
from preql.core.models import Environment
from preql.parser import parse_text
from typing import Optional


class Executor(object):
    def __init__(self, dialect: Dialects, engine: Engine, environment: Optional[Environment] = None):
        self.dialect = dialect
        self.engine = engine
        self.environment = environment or Environment({}, {})
        if self.dialect == Dialects.BIGQUERY:
            from preql.dialect.bigquery import BigqueryDialect
            self.generator = BigqueryDialect()
        else:
            raise ValueError(f"Unsupported dialect {self.dialect}")

    def execute_command(self, command: str):
        _, parsed = parse_text(command, self.environment)
        sql = self.generator.generate_queries(self.environment, parsed)
        output = None
        for statement in sql:
            sql = self.generator.compile_statement(statement)
            output = self.engine.execute(sql).fetchall()
        return output
